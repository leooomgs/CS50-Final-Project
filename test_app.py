import pytest
from app import wordopt, manual_testing

@pytest.mark.parametrize("test_input,expected", [
    ("This is a [test] string with https://example.com and some punctuation!?", "this is a   string with   and some punctuation  "),
    ("TEST with CAPITALS", "test with capitals"),
    ("Zahlen 12345 sind auch Text!", "zahlen      sind auch text "),
    ("", ""),  
    ("No special characters here", "no special characters here"),
])
def test_wordopt(test_input, expected):
    assert wordopt(test_input) == expected

def test_manual_testing():
   
    fake_news = "This is clearly fake news."
    real_news = "Official sources reported today."
   
    
    prediction_fake = manual_testing(fake_news)
    prediction_real = manual_testing(real_news)
    
    assert "Fake News" in prediction_fake, "The prediction for a fake news example did not match expected output."
    assert "Not A Fake News" in prediction_real, "The prediction for a real news example did not match expected output."
