# Model Card

For additional information, see the Model Card paper: [Model Cards for Model Reporting](https://arxiv.org/pdf/1810.03993.pdf)

## Model Details
The task of this model is to predict whether an individual earns over 50K annually. We have employed a GradientBoostingClassifier with optimized hyperparameters using scikit-learn 1.2.0. Hyperparameter tuning was accomplished via GridSearchCV, and the best parameters found are:
- **learning_rate**: 1.0
- **max_depth**: 5
- **min_samples_split**: 100
- **n_estimators**: 10

The model is stored as a pickle file in the model directory. All training steps and metrics are logged in the file "journal.log".

## Intended Use
This model is intended for predicting an individual's salary level based on a set of features. Its primary usage is for educational, academic, or research purposes.

## Training Data
The training dataset, the Census Income Dataset, was sourced from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income). The dataset contains 32,561 rows and 15 columns, including the target label "salary," 8 categorical features, and 6 numerical features. For detailed descriptions of each feature, refer to the UCI link provided.

The target label "salary" has two classes ('<=50K', '>50K') and exhibits a class imbalance with approximately a 75% / 25% split. Basic data cleaning was performed to remove leading and trailing whitespaces. The data exploration and cleaning steps are documented in the data_cleaning.ipynb notebook.

The dataset was divided into training and testing sets using an 80-20 split, with stratification on the target label "salary." For training, a One Hot Encoder was applied to the categorical features, and a label binarizer was used on the target label.

## Evaluation Data
20% of the dataset was reserved for model evaluation. The same transformations applied to the training set (One Hot Encoding for categorical features and label binarization for the target label) were applied to the evaluation data.

## Metrics
The model's classification performance was assessed using precision, recall, and F-beta score metrics. Additionally, the confusion matrix was calculated. The model's performance on the test set is as follows:
- **Precision**: 0.759
- **Recall**: 0.643
- **F-beta**: 0.696
- **Confusion Matrix**:
[[4625 320]
[ 560 1008]]


## Ethical Considerations
The dataset should not be viewed as a fair representation of salary distribution across different demographics. Consequently, this model should not be used to infer salary levels for specific population segments.

## Caveats and Recommendations
This dataset was extracted from the 1994 Census database and, as such, represents an outdated sample. It should not be used as a statistically accurate representation of the current population. It is recommended to use this dataset primarily for educational purposes, such as training on machine learning classification tasks or related problems.