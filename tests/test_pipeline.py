import os
import sqlite3
import pytest
from src.pipeline import run_pipeline

# --- CRITICAL CONFIGURATION ---
# The filename must match exactly what we ask the candidate to create.
DB_PATH = "sales.db" 
# ------------------------------

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # 1. Pre-cleanup: If an old DB exists, remove it to start fresh.
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    # 2. Run the Candidate's Pipeline (This is where the DB should be created)
    run_pipeline()
    
    yield
    
    # 3. Teardown: We do NOT remove the DB at the end so you can inspect it if it fails.
    # if os.path.exists(DB_PATH):
    #     os.remove(DB_PATH)

def test_database_creation():
    """Mission 1: Validate that the script generates the .db file."""
    assert os.path.exists(DB_PATH), f"❌ The file '{DB_PATH}' was not generated. Check your code."

def test_data_integrity():
    """Mission 2: Validate that the table exists and contains data."""
    if not os.path.exists(DB_PATH):
        pytest.fail("The database file does not exist.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Check if the table 'revenue_by_country' exists
        cursor.execute("SELECT country, total_revenue FROM revenue_by_country")
        rows = cursor.fetchall()
        assert len(rows) > 0, "❌ The table 'revenue_by_country' was created, but it is empty."
    except sqlite3.OperationalError:
        pytest.fail("❌ The table 'revenue_by_country' does NOT exist in the database.")
    finally:
        conn.close()

def test_usa_revenue_calculation():
    """Mission 3: Validate the data cleaning logic for USA."""
    if not os.path.exists(DB_PATH):
        pytest.skip("DB does not exist")

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT total_revenue FROM revenue_by_country WHERE country='USA'")
        result = cursor.fetchone()
        
        assert result is not None, "❌ No data found for 'USA'"
        revenue = result[0]
        
        # Expected value based on logic: 100.50 + 150.00 + 200.00 = 450.50
        # (This depends on how strict your cleaning logic is regarding the null ID row)
        assert revenue == 450.50, f"❌ Incorrect calculation for USA. Got: {revenue}, Expected: 450.50"
        
    except sqlite3.OperationalError:
        pytest.fail("❌ SQL Error: The table probably does not exist.")
    finally:
        conn.close()
