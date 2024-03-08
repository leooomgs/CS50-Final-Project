# Fake News Detection

#### Video Demo: [https://www.youtube.com/watch?v=ivdCwbtLisM](https://www.youtube.com/watch?v=ivdCwbtLisM)

#### Kaggle Dataset and Source Code:
Find the dataset used for training the machine learning models and part of the source code on Kaggle at [https://www.kaggle.com/code/therealsampat/fake-news-detection/input](https://www.kaggle.com/code/therealsampat/fake-news-detection/input).

#### Description:
The "Fake News Detection" project utilizes Python and machine learning to discern real news from fake, addressing the challenge of misinformation proliferation online. This Python-based tool leverages a user-friendly interface developed with PyQt5, allowing users to input and verify news articles. Initiated with Jupyter Notebooks for model prototyping, the project features a blend of technology aimed at combating the spread of fake news.

### Local Execution Requirement:
Due to the GUI dependencies on PyQt5, this application is designed to run locally. Ensure all dependencies are installed by executing `pip install -r requirements.txt` in your project directory before launching the application with `python app.py`. The tool is optimized for English-language text, in line with the training dataset.

### Files:
- `app.py`: The main application script that invokes the user interface and processes the news text.
- `ui.py`: Defines the application's GUI layout and behavior.
- `test_app.py`: Contains pytest tests to verify the application's processing functions.
- `FakeNewsDetection.ipynb`: The Jupyter Notebook where initial model development and training occurred.
- `dt_model.joblib`, `gb_model.joblib`, `lr_model.joblib`, `vectorizer.joblib`: Serialized versions of the trained machine learning models and text vectorization tool.
- `Fake (1).csv` and `True.csv`: Datasets containing the labeled news articles used for training the models.
- `requirements.txt`: A list of Python packages required to run the application.

### Functionality:
Users input news text, which is then processed and classified as fake or real news, with results displayed instantaneously.

### Design Choices:
- **Jupyter Notebook**: Facilitated rapid model development and testing.
- **Machine Learning Models**: Logistic Regression, Decision Tree, and Gradient Boosting selected for text classification efficiency.
- **PyQt5**: Chosen for crafting a responsive user interface.
- **Minimum Text Length**: Ensures accuracy in predictions.

### Usage:
Run the application locally after installing dependencies with `pip install -r requirements.txt`. Launch via `python app.py` and input English-language news text for verification.

### Development:
Demonstrates practical application of Python, PyQt5, and machine learning in addressing real-world issues like misinformation.

#### Dependencies:
Install required packages from `requirements.txt` for a seamless setup.


