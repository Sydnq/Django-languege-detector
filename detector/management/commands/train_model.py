from django.core.management.base import BaseCommand
from django.utils import timezone

from detector.model.model import Model


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('-m', '--model_folder', type=str, help='Path to save the model to')
        parser.add_argument('-p', '--data_path', type=str, help='Data set path', )

    def handle(self, *args, **kwargs):
        """Basic commandline mathod to train model.

        This is basic as checks for proper path assigment
        for both model and dataset is missing.
        #TODO: ADD PROPER CHECKS FOR PATH
        """
        # load model
        dataset_path = kwargs['data_path']
        if dataset_path:
            model = Model(languages_data_folder=dataset_path)
        else:
            model = Model()
        try:
            model.train()
        except Exception as e:
            print(e)
