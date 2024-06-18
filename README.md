# Deploying a Scalable ML Pipeline with FastAPI

This repository contains a scalable machine learning pipeline developed using FastAPI. The pipeline handles data preprocessing, model training, and serving a trained model via a RESTful API.

## Table of Contents

- [Deploying a Scalable ML Pipeline with FastAPI](#deploying-a-scalable-ml-pipeline-with-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [API Endpoints](#api-endpoints)
  - [Contributing](#contributing)


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hsnyildiz/Deploying-a-Scalable-ML-Pipeline-with-FastAPI.git
   cd Deploying-a-Scalable-ML-Pipeline-with-FastAPI
    ```


2. **Create and activate a conda environment:**
    ```bash
    conda env create -f environment.yml
    conda activate ml-pipeline-env
    ```

3. **or Install the required packages with pip:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Model Training:**
Run the train_model.py script to train the machine learning model.
   ```bash
   python train_model.py
   ```
2. **Start the FastAPI Server:**
Run the main.py script to start the FastAPI server.
   ```bash
   uvicorn main:app --reload
   ```
3. **Test the API Locally:**
Use the local_api.py script to send a test request to the API.
   ```bash
   python local_api.py
   ```
4. **Test PyTest:**
Use the test_ml.py script to test with PyTest.
   ```bash
   python test_ml.py
   ```

## API Endpoints

POST /inference: Takes in input data and returns the model prediction.

**Example request:**
```bash
curl -X POST "http://127.0.0.1:8000/inference" -H "Content-Type: application/json" -d '{
    "data": {
        "age": 30,
        "workclass": "Private",
        "education": "Bachelors",
        ...
    }
}'
```

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

1. Fork the Project
2. Create your Feature Branch 
   ```git checkout -b feature/AmazingFeature```
3. Commit your Changes
   ```git commit -m 'Add some AmazingFeature'```
4. Push to the Branch
   ```git push origin feature/AmazingFeature```
5. Open a Pull Request