# 🛢️ PureStack Data Engineering Challenge: The ETL Pipeline

### Context
Welcome to the **PureStack Technical Validation Protocol** for Data Engineering.
In the real world, data is never clean. We audit your ability to handle **Missing Values**, **Inconsistent Formats**, and **Data Aggregation**.

**⚠️ The Scenario:** The sales team has sent us a dump of raw data (`data/sales_raw.csv`). It's a mess. Your job is to clean it and store high-level KPIs into a SQL database.

---

### 🎯 The Objective
Build a Python ETL Pipeline that performs the following steps:

1.  **Extract:** Read the `data/sales_raw.csv` file.
2.  **Transform:**
    * **Clean Dates:** Standardize all dates to `YYYY-MM-DD`.
    * **Handle Nulls:** Drop rows where `order_id` or `amount` is missing.
    * **Fix Formats:** Ensure `amount` is a float (remove symbols like `$`).
    * **Calculate KPI:** Group by `country` and calculate `total_revenue`.
3.  **Load:** Save the cleaned aggregate data into a SQLite database named `sales.db` in a table called `revenue_by_country`.

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+.
* **Libraries:** Pandas (preferred) or Polars.
* **Database:** SQLite (Standard library `sqlite3`).
* **Testing:** Pytest.

## 🧪 Evaluation Criteria (How we audit you)

We will clone your repo and run `pytest`. We look for:

- **Green Lights:** Your code must generate the `sales.db` with the correct numbers.
- **Robustness:** Did you handle the row with the corrupt date correctly?
- **Code Quality:** Modular functions (`extract`, `transform`, `load`) vs a single script block.

## 🚀 Getting Started

1. Use this template.
2. Install dependencies: `pip install -r requirements.txt`.
3. Analyze `data/sales_raw.csv` to spot the errors.
4. Implement `src/pipeline.py`.
5. Run tests: `pytest`.

---

### 🚨 CRITICAL: Project Structure
To ensure our **Automated Auditor** works, keep this structure:

```text
/
├── .github/workflows/   # PureStack Audit System
├── data/
│   └── sales_raw.csv    # <--- DIRTY DATA (Do not modify manually)
├── src/
│   ├── __init__.py
│   └── pipeline.py      # <--- YOUR CODE HERE
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py # <--- VALIDATION TESTS
├── requirements.txt
└── README.md
