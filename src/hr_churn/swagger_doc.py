"""File contains swagger documentation"""
from flask_restx import fields

reqFields = {
    'satisfaction_level': fields.Float(required=True, description='Satisfaction Level',
                                       min=0.0, max=1.0, example=0.95),
    'time_spend_company': fields.Integer(required=True, description="Time spend at the company",
                                         min=0, max=11, example=2),
    'number_project': fields.Integer(required=True, description="Number of projects",
                                     min=0, max=11, example=2)
}
