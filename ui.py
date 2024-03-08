from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QProgressBar, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class FakeNewsDetectionUI(QWidget):
    def __init__(self, manual_testing_func, calculate_progress_func):
        super().__init__()
        self.manual_testing_func = manual_testing_func
        self.calculate_progress_func = calculate_progress_func
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Überschrift
        title_label = QLabel("Check if news is real or fake!")
        title_font = QFont("Arial", 18, QFont.Bold)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)

        # Textfeld für Nachrichtentext
        self.news_input = QTextEdit()
        self.news_input.setPlaceholderText("Enter the news here...")
        main_layout.addWidget(self.news_input)

        # Schaltflächen und Fortschrittsbalken
        button_layout = QHBoxLayout()
        detect_button = QPushButton("Predict")
        detect_button.clicked.connect(self.detect_fake_news)
        button_layout.addWidget(detect_button)

        self.progress_bar = QProgressBar()
        button_layout.addWidget(self.progress_bar)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_inputs)
        button_layout.addWidget(clear_button)

        main_layout.addLayout(button_layout)

        # Label für die Vorhersage
        self.prediction_label = QLabel()
        self.prediction_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.prediction_label)

        # Darkmode-Checkbox
        self.dark_mode_checkbox = QCheckBox("Dark Mode")
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)
        main_layout.addWidget(self.dark_mode_checkbox)

        self.setLayout(main_layout)

    def detect_fake_news(self):
        news_text = self.news_input.toPlainText()
        if news_text:
            if len(news_text) < 100:
                self.prediction_label.setText("Text is too short. Please enter at least 100 characters.")
                self.progress_bar.setValue(0)
                return

            prediction = self.manual_testing_func(news_text)
            progress_value = self.calculate_progress_func(prediction)
            self.prediction_label.setText(f"Prediction: {'Fake News' if progress_value > 50 else 'Real News'}")
            self.progress_bar.setValue(progress_value)
        else:
            self.prediction_label.setText("Please enter a news text.")
            self.progress_bar.setValue(0)

    # Restliche Methoden bleiben unverändert

    def clear_inputs(self):
        self.news_input.clear()
        self.prediction_label.clear()
        self.progress_bar.setValue(0)

    def toggle_dark_mode(self, state):
        if state == Qt.Checked:
            # Aktiviere den Dunkelmodus
            self.setStyleSheet("QWidget { background-color: #333333; color: #FFFFFF; }")
        else:
            # Deaktiviere den Dunkelmodus
            self.setStyleSheet("")