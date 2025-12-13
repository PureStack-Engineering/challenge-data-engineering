import os
import sqlite3
import pytest
from src.pipeline import ETIPipeline

DB_PATH = "test_sales.db"
CSV_PATH = "data/sales_raw.csv"

@pytest.fixture
def run_pipeline():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    pipeline = ETIPipeline(CSV_PATH, DB_PATH)
    pipeline.run()
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

def test_database_creation(run_pipeline):
    assert os.path.exists(DB_PATH)

def test_usa_revenue_calculation(run_pipeline):
    """
    USA Calculation Logic:
    - 100.50 (Valid)
    - $200.00 (Valid if cleaned)
    - ERROR (Should be dropped)
    Total Expected: 300.50
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT total_revenue FROM revenue_by_country WHERE country='USA'")
    result = cursor.fetchone()
    conn.close()
    
    assert result is not None, "USA data missing in DB"
    assert result[0] == 300.50, f"Expected 300.50 for USA, got {result[0]}"

def test_spain_revenue_calculation(run_pipeline):
    """
    Spain Calculation Logic:
    - 300.00 (Valid)
    - 50.50 (Valid)
    Total Expected: 350.50
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT total_revenue FROM revenue_by_country WHERE country='Spain'")
    result = cursor.fetchone()
    conn.close()
    
    assert result[0] == 350.50
