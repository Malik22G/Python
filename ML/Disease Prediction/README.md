Disease Prediction using Machine Learning
This project implements a disease prediction system using machine learning algorithms trained on symptom data.

Dataset
Training Data: dataset/Training.csv
Testing Data: dataset/Testing.csv
Each record represents symptoms (as binary features) and the corresponding disease.

Installation
Ensure you have Python 3.x installed. Install the required libraries:

bash
Copy code
pip install numpy pandas scikit-learn scipy
Usage
Run the Script:

bash
Copy code
python disease_prediction.py
This will:

Load and preprocess the data.
Train classifiers: Support Vector Machine (SVM), Gaussian Naive Bayes (GNB), and Random Forest (RF).
Evaluate models and print accuracy scores.
Predict Disease:

Use the predictDisease function by providing symptoms as a comma-separated string.

python
Copy code
predictions = predictDisease("Headache,Cough,Loss Of Appetite")
print(predictions)
Sample Output:

python
Copy code
{
  'rf_model_prediction': 'Jaundice',
  'naive_bayes_prediction': 'Jaundice',
  'svm_model_prediction': 'Jaundice',
  'final_prediction': 'Jaundice'
}
