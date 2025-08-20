from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentiment(review):
    review_tfidf = vectorizer.transform([review])
    prediction = model.predict(review_tfidf)[0]
    return "Positive" if prediction == 1 else "Negative"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form.get('user_input', '')  # Get input from form data
        if not review:
            return jsonify({'error': 'No review provided'}), 400
        
        sentiment = predict_sentiment(review)
        return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
