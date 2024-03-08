import sys
from PyQt5.QtWidgets import QApplication
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import langdetect

LR = joblib.load('lr_model.joblib')
DT = joblib.load('dt_model.joblib')
GB = joblib.load('gb_model.joblib')
vectorization = joblib.load('vectorizer.joblib')

MIN_TEXT_LENGTH = 100  

def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', ' ', text)
    text = re.sub(r'\\W', ' ', text)
    text = re.sub(r'https?://\S+', ' ', text)
    text = re.sub(r'<.*?>+', ' ', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', ' ', text)
    return text

def output_label(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)

    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GB = GB.predict(new_xv_test)

    return (output_label(pred_LR[0]),
            output_label(pred_DT[0]),
            output_label(pred_GB[0]))

def calculate_progress(predictions):
    fake_news_count = predictions.count("Fake News")
    total_count = len(predictions)
    progress_value = int(fake_news_count / total_count * 100)
    return progress_value

if __name__ == "__main__":
    from ui import FakeNewsDetectionUI
    app = QApplication(sys.argv)
    window = FakeNewsDetectionUI(manual_testing, calculate_progress)
    window.show()
    sys.exit(app.exec())