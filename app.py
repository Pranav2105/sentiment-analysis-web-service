# app.py
from flask import Flask, request, jsonify
from model import SentimentAnalysisModel
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)
model = SentimentAnalysisModel()

class PredictionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    prediction = db.Column(db.Float)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    result = model.predict(data)
    log_prediction(data, result)
    return jsonify({'prediction': result.tolist()})

def log_prediction(text, prediction):
    new_prediction = PredictionLog(text=text, prediction=float(prediction))
    db.session.add(new_prediction)
    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)
