from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np
import os

BASE = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE, '..', 'Frontend'),
            static_folder=os.path.join(BASE, '..', 'Frontend'))

with open(os.path.join(BASE, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        df = pd.read_csv(file)

        features = ['Attendance', 'Internal_Marks', 'Semester_Result',
                    'Fee_Pending', 'LMS_Usage', 'Scholarship', 'Backlogs']

        missing = [f for f in features if f not in df.columns]
        if missing:
            return jsonify({'error': f'Missing columns: {missing}'}), 400

        X = df[features]

        proba       = model.predict_proba(X)[:, 1]
        predictions = model.predict(X)

        df['Drop_Probability'] = (proba * 100).round(2)
        df['Risk'] = df['Drop_Probability'].apply(
            lambda x: 'High Risk' if x >= 60 else ('Medium Risk' if x >= 40 else 'Low Risk')
        )
        df['Predicted_Dropout'] = predictions

        total       = len(df)
        high_risk   = int((df['Risk'] == 'High Risk').sum())
        medium_risk = int((df['Risk'] == 'Medium Risk').sum())
        low_risk    = int((df['Risk'] == 'Low Risk').sum())

        imp      = model.get_feature_importance()
        feat_imp = pd.DataFrame({'Feature': features, 'Importance': imp})
        feat_imp = feat_imp.sort_values('Importance', ascending=False)

        students = df[['Student_ID', 'Attendance', 'Internal_Marks', 'Backlogs',
                        'Fee_Pending', 'LMS_Usage', 'Scholarship',
                        'Drop_Probability', 'Risk']].to_dict(orient='records')

        return jsonify({
            'total': total,
            'high_risk': high_risk,
            'medium_risk': medium_risk,
            'low_risk': low_risk,
            'students': students,
            'feature_importance': feat_imp.to_dict(orient='records')
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)