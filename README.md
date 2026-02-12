📦 Installation

Clone the repository

git clone https://github.com/your-username/alarm-detection-pipeline.git

cd alarm-detection-pipeline


Create a virtual environment (optional but recommended)

python -m venv venv

source venv/bin/activate   # Linux / Mac

venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

▶️ How to Run

Run main pipeline

python main.py

Run application (API / service)

python app.py

📊 Dataset

File: Historical Alarm Cases.xlsx

Contains historical alarm records used for training and evaluation

Features may include:

Alarm type

Timestamp

Severity

System metadata

Target label (if supervised)

🧪 Model Pipeline

Saved as alarm_pipeline.pkl

Includes:

Data preprocessing

Feature engineering

Trained ML model

Loaded during runtime for inference

🔍 Use Cases

False alarm detection

Alarm prioritization

Operational efficiency improvement

Predictive maintenance systems
