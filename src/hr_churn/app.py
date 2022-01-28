import logging

from pandas import json_normalize
from flask import Flask
from flask_restx import Resource, Api

from hr_churn.swagger_doc import reqFields
from hr_churn.prediction_server import PredictionServer

logger = logging.getLogger(__name__)

prediction_server = PredictionServer()

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True

api = Api(app)
data = api.model('Chance for employee churn', reqFields)

employee_churn_ns = api.namespace(
    'Employee churn predictor',
    description='Here we have a post method to predict whether a employee is likely to leave from json data')


class EmployeeChurnPrediction(Resource):
    """Calculate employee churn probability"""
    # error codes
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    # expect the certain kind of data specified above, this is just a form and not binding
    @api.expect(data)
    # if request.method == 'POST'
    def post(self):
        # read in data. Error handling is done in the parser itself
        args = prediction_server.parser.parse_args(strict=True)
        try:
            df = json_normalize(args)
        except Exception as e:
            employee_churn_ns.abort(400, e.__doc__, status="Could not convert json to dataframe", statusCode="400")

        try:
            prediction = prediction_server.model.predict_proba(df)
        except Exception as e:
            employee_churn_ns.abort(500, e.__doc__, status="Model prediction failed", statusCode="500")

        return {'leave probability': prediction_server.model.predict_proba(df)[0][1],
                'stay probability': prediction_server.model.predict_proba(df)[0][0]}

    @api.doc(responses={200: 'OK', 400: "Only post method available", 500: 'Mapping Key Error'})
    def get(self):
        employee_churn_ns.abort(400, status="Only post method available", statusCode="400")


employee_churn_ns.add_resource(EmployeeChurnPrediction, '/employee-churn/')

if __name__ == '__main__':
    app.run(debug=True)
