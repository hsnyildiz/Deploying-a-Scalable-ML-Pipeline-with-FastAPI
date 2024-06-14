def test_data_loading():
    from data import load_data

    data = load_data("data/census.csv")
    assert data is not None


def test_model_training():
    from model import train_model
    from data import load_data

    data = load_data("data/census.csv")
    model = train_model(data)
    assert model is not None
