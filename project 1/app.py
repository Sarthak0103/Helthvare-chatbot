venv\Scripts\activate
pip install Flask
from flask import Flask, render_template, request
import chatbot_model as model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_suggestion', methods=['POST'])
def get_suggestion():
    symptoms = request.form.get('symptoms')
    prediction = model.predict_symptoms(symptoms)
    return render_template('index.html', suggestion=prediction)

if __name__ == "__main__":
    app.run(debug=True)
