import joblib
import logging
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


def preprocessing(df):
    """Clean up data, select features and split into train and test"""
    # df['salary'] = label_encoder.fit_transform(df['salary'])
    # df['departments'] = label_encoder.fit_transform(df['departments'])

    df_short = df[["satisfaction_level", "time_spend_company", "number_project"]]
    return train_test_split(df_short, df.left)


def fit(X_train, y_train):
    """Fit model opbject using training set"""
    random_forest_model = RandomForestClassifier(n_estimators=100)
    random_forest_model.fit(X_train, y_train)
    return random_forest_model


def evaluate_model(model, X_test, y_test):
    """Evaluate model"""
    y_predicted = model.predict(X_test)
    logger.info(f"Accuracy: {metrics.accuracy_score(y_test, y_predicted)}")

    confusion_matrix = pd.crosstab(y_test, y_predicted, rownames=['Actual'], colnames=['Predicted'])
    logger.info(f"Confusion Matrix: \n{confusion_matrix}")


def predict(model, X):
    return model.predict(X)


def save(model, filename):
    joblib.dump(model, filename)


def load(filename):
    return joblib.load(filename)