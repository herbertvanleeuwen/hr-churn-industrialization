import logging
from hr_churn.model import load
from flask_restx import reqparse

logger = logging.getLogger(__name__)


class PredictionServer:
    def __init__(self, *args, ** kwargs):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self._setup_parser()

        self.model = load('model.pkl')

    def _setup_parser(self):
        """Set up json parser"""
        logger.info('Setting up parser')
        self.parser.add_argument('satisfaction_level', type=float, required=True, location='json',
                                 help='Satisfaction level not provided')
        self.parser.add_argument('time_spend_company', type=int, required=True, location='json',
                                 help='Time spend at the company not provided')
        self.parser.add_argument('number_project', type=int, required=True, location='json',
                                 help='Number of projects not provided')