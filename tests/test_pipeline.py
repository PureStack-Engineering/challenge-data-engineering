import os
import sqlite3
import pytest
import pandas as pd
from src.pipeline import run_pipeline

DB_PATH = "sales.db"

@pytest.fixture(autouse=True)
def clean_db():
    """Ensure a clean state before running tests"""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    yield
    # Optional: cleanup after test

def test_pipeline_execution():
    """Test if the pipeline runs and creates the database"""
    try:
        run_pipeline()
    except NotImplementedError:
        pytest.fail("❌ Pipeline is not implemented yet.")
    
    assert os.path.exists(DB_PATH), "❌ Database file 'sales.db' was not created."

def test_data_integrity():
    """Test if the logic cleaned the data correctly"""
    run_pipeline()
    
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM revenue_by_country", conn)
    conn.close()
    
    # 1. Check Schema
    assert "country" in df.columns, "❌ Column 'country' missing."
    assert "total_revenue" in df.columns, "❌ Column 'total_revenue' missing."
    
    # 2. Check Data Cleaning Logic
  
    usa_revenue = df.loc[df["country"] == "USA", "total_revenue"].values[0]
    assert usa_revenue == 501.0, f"❌ Incorrect Revenue for USA. Expected 501.0, got {usa_revenue}"
    
   
    france_revenue = df.loc[df["country"] == "France", "total_revenue"].values[0]
    assert france_revenue == 150.0, "❌ Incorrect Revenue for France."

  
