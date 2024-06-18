import pytest
import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.exceptions import NotFittedError
from ml.model import train_model, inference, compute_model_metrics
from ml.data import process_data


@pytest.fixture(scope="module")
def data():
    return pd.read_csv("./data/census.csv")


@pytest.fixture(scope="module")
def cat_features():
    return [
        "workclass", "education", "marital-status",
        "occupation", "relationship", "race",
        "sex", "native-country"
    ]


@pytest.fixture(scope="module")
def train_dataset(data, cat_features):
    train, _ = train_test_split(
        data, test_size=0.20, random_state=10, stratify=data['salary']
    )
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )
    return X_train, y_train, encoder, lb


def test_apply_labels(data):
    assert not data.empty, "Dataframe is empty"
    assert data.shape[1] > 0, "Dataframe has no columns"


def test_train_model(train_dataset):
    X_train, y_train, _, _ = train_dataset
    model = train_model(X_train, y_train)
    savepath = "./model/model.pkl"
    with open(savepath, 'wb') as f:
        pickle.dump(model, f)
    assert os.path.isfile(savepath), "Model file was not saved"
    with open(savepath, 'rb') as f:
        loaded_model = pickle.load(f)
    try:
        loaded_model.predict(X_train)
    except NotFittedError:
        assert False, "Model is not fitted"
    except Exception as e:
        assert False, f"Error during prediction: {e}"


def test_compute_model_metrics(train_dataset):
    X_train, y_train, _, _ = train_dataset
    savepath = "./model/model.pkl"
    assert os.path.isfile(savepath), "Model file does not exist"
    with open(savepath, 'rb') as f:
        model = pickle.load(f)
    preds = inference(model, X_train)
    try:
        precision, recall, fbeta = compute_model_metrics(y_train, preds)
        assert precision is not None, "Precision is None"
        assert recall is not None, "Recall is None"
        assert fbeta is not None, "F-beta score is None"
    except Exception:
        assert False, "Performance metrics cannot be calculated on train data"
