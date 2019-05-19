import logging
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn import metrics
import joblib

from django.core.cache import cache
from django.conf import settings

from .utils import target_names


logging.basicConfig(level=logging.DEBUG)


class Model:
    """Main class for training or load the language detctor model."""

    def __init__(self):
        """Init the Model."""
        self.languages_data_folder = settings.DATASET_PATH
        self.model_path = settings.MODEL_PATH
        self.logger = logging.getLogger(self.__class__.__name__)
        self.clf = None

    def load(self, model_path=None):
        """Load model and return instace of classifier."""
        if model_path:
            self.defaul_model_path = model_path

        # Load the model
        try:
            clf = joblib.load(self.model_path)
        except Exception as e:
            self.logger.exception(e)
        else:
            return clf

    def train(self, languages_data_folder=None, model_path=None):
        """Train language detector model."""
        if languages_data_folder:
            self.languages_data_folder = languages_data_folder
        try:

            self.logger.debug("Loading data...")
            dataset = load_files(self.languages_data_folder)

            # read the data, Capital X is used as is convention
            # for machine learning models
            X = [open(f).read() for f in dataset.filenames]
            y = dataset.target

            self.logger.debug("Spliting data...")
            # split the dataset in training and test set:
            x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            # Build a classifier pipeline
            self.clf = Pipeline([
                ('vec', CountVectorizer(lowercase=True, ngram_range=(1, 3))),
                ('tfidf', TfidfTransformer(use_idf=False)),
                ('clf', LogisticRegression(
                    random_state=0,
                    multi_class='multinomial',
                    solver='newton-cg')),
            ])

            self.logger.debug("Training data...")
            # Fit the pipeline on the training set
            self.clf.fit(x_train, y_train)

            # Predict the outcome on the testing set
            y_predicted = self.clf.predict(x_test)

            # Plot the confusion matrix
            cm = metrics.confusion_matrix(y_test, y_predicted)

            self.logger.debug("Model  score: {}".format(cm))

            if model_path:
                self.model_path = model_path

            # Save model to model_path directory
            s = joblib.dump(self.clf, self.model_path)
            if s:
                self.logger.debug("Classifier has been saved to {}".format(s[0]))
        except Exception as e:
            self.logger.exception(e)


def detect_language(text):
    """Interface for detecting language in order to make it easier to use."""
    model_cache_key = 'language_model_cache'
    target_names_key = 'target_names_cache'
    clf = cache.get(model_cache_key)
    target_names_ls = cache.get(target_names_key)

    if clf is None:
        # load model
        model = Model()
        clf = model.load()
        # save in django memory cache
        cache.set(model_cache_key, clf, None)
    # load the target names
    if target_names_ls is None:
        target_names_ls = target_names(settings.DATASET_PATH)
        # cach the target names
        cache.set(target_names_key, target_names_ls, None)

    # predict the langauge
    prediction = clf.predict([text])
    # Get language
    detected_language = target_names_ls[prediction[0]]

    return detected_language
