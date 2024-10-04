<!DOCTYPE html>
<html>
<head>

</head>
<body>

<h1>Disease Prediction using Machine Learning</h1>

<p>This project implements a disease prediction system using machine learning algorithms trained on symptom data.</p>

<h2>Dataset</h2>

<ul>
    <li><strong>Training Data:</strong> <code>dataset/Training.csv</code></li>
    <li><strong>Testing Data:</strong> <code>dataset/Testing.csv</code></li>
</ul>

<p>Each record represents symptoms (as binary features) and the corresponding disease.</p>

<h2>Installation</h2>

<p>Ensure you have Python 3.x installed. Install the required libraries:</p>

<pre><code>pip install numpy pandas scikit-learn scipy
</code></pre>

<h2>Usage</h2>

<ol>
    <li>
        <p><strong>Run the Script:</strong></p>
        <pre><code>python disease_prediction.py
</code></pre>
        <p>This will:</p>
        <ul>
            <li>Load and preprocess the data.</li>
            <li>Train classifiers: Support Vector Machine (SVM), Gaussian Naive Bayes (GNB), and Random Forest (RF).</li>
            <li>Evaluate models and print accuracy scores.</li>
        </ul>
    </li>
    <li>
        <p><strong>Predict Disease:</strong></p>
        <p>Use the <code>predictDisease</code> function by providing symptoms as a comma-separated string.</p>
        <pre><code>predictions = predictDisease("Headache,Cough,Loss Of Appetite")
print(predictions)
</code></pre>
        <p><strong>Sample Output:</strong></p>
        <pre><code>{
  'rf_model_prediction': 'Jaundice',
  'naive_bayes_prediction': 'Jaundice',
  'svm_model_prediction': 'Jaundice',
  'final_prediction': 'Jaundice'
}
</code></pre>
    </li>
</ol>


<hr>

</body>
</html>
