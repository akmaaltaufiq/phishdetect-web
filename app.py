import string
import pickle
from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd

nltk.download('stopwords')
nltk.download('wordnet')

# Load model & vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return ' '.join(words)

app = Flask(__name__)
history = []

# Static values for accuracy and classification report
accuracy = "95.47"
report = """
Laporan Klasifikasi:
                   precision    recall  f1-score   support

       Safe Email       0.93      0.98      0.95      7935
   Phishing Email       0.98      0.93      0.96      8563

         accuracy                           0.95     16498
        macro avg       0.96      0.96      0.95     16498
     weighted avg       0.95      0.95      0.95     16498
""".strip()

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    email_text = ""

    if request.method == "POST":
        email_text = request.form["email"]
        cleaned = clean_text(email_text)
        vector = vectorizer.transform([cleaned])
        result = model.predict(vector)[0]
        prediction = "✅ Safe Email" if result == 0 else "❌ Phishing Email"
        history.insert(0, {"time": pd.Timestamp.now().strftime("%H:%M:%S"), "label": prediction})
        if len(history) > 5:
            history.pop()

    return render_template(
        "index.html",
        prediction=prediction,
        email=email_text,
        history=history,
        accuracy=accuracy,
        report=report
    )

if __name__ == "__main__":
    app.run(debug=True)
