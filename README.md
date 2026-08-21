# Airline Passenger Satisfaction

## Team

### Member 1 — Data

* EDA
* Clean data
* Preprocessing

### Member 2 — Modeling

* Train models
* Evaluate models
* Chọn best model

### Member 3 — Demo

* Làm Streamlit
* Prediction
* Report / README

## Project Structure

```text
airline-satisfaction/
│
├── data/
│   ├── raw/              # Dataset gốc
│   └── processed/        # Data đã xử lý
│
├── notebooks/
│   ├── 01_eda.ipynb      # EDA
│   └── 02_modeling.ipynb # Thử nghiệm model
│
├── src/
│   ├── preprocessing.py  # Xử lý dữ liệu
│   ├── train.py          # Train model
│   ├── evaluate.py       # Đánh giá model
│   └── predict.py        # Predict
│
├── models/               # Model đã lưu
│
├── app/
│   └── app.py            # Streamlit
│
├── reports/
│   └── figures/          # Biểu đồ / ảnh report
│
├── requirements.txt      # Thư viện
├── .gitignore
└── README.md
```

## Setup

```bash
git clone <repo-url>
cd airline-satisfaction

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

## Branch

```text
feature/data-eda
feature/modeling
feature/demo
```

Không push trực tiếp lên `main`.
