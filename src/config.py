import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "Africa_towers_sample.csv")

OUTPUT_CHARTS = os.path.join(BASE_DIR, "output", "charts")
OUTPUT_REPORTS = os.path.join(BASE_DIR, "output", "reports")

os.makedirs(OUTPUT_CHARTS, exist_ok=True)
os.makedirs(OUTPUT_REPORTS, exist_ok=True)