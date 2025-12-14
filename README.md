# 🛢️ PureStack Data Engineering Challenge: The ETL Pipeline

**PureStack.es - Engineering Validation Protocol.**
> *"Data is never clean. We audit your ability to turn chaos into reliable KPIs."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Data Engineering.
In the real world, "Happy Paths" don't exist. We audit your ability to handle **Missing Values**, **Inconsistent Formats**, and **Schema Drift**.

**The Mission:** The sales team has provided a dump of raw data (`data/sales_raw.csv`). It contains errors, duplicates, and mixed formats. Your job is to build a resilient **ETL Pipeline** to clean it and store high-level KPIs into a SQL database.

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by the robustness and reproducibility of your pipeline. State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Functional ETL & Pandas/Polars usage.
* **Requirement:** Complete the pipeline to pass the provided tests.
* **Tasks:**
    1.  **Extract:** Read the `data/sales_raw.csv`.
    2.  **Transform:**
        * **Sanitization:** Standardize dates to `YYYY-MM-DD`. Handle nulls (drop rows with missing `order_id` or `amount`).
        * **Type Casting:** Ensure `amount` is a float (strip symbols like `$`).
        * **Aggregation:** Group by `country` and calculate `total_revenue`.
    3.  **Load:** Save the aggregated data into a SQLite database (`sales.db`) in a table named `revenue_by_country`.
* **Deliverable:** A functional `src/pipeline.py` that generates correct numbers.

#### 🥈 Level 2: Pro / Senior
* **Focus:** Data Quality (DQ) & Observability.
* **Requirement:** Everything in Level 3 + **Schema Validation & Logging**.
* **Extra Tasks:**
    1.  **Schema Validation:** Before loading, validate the transformed data using a library like **Pandera** or simple assertions. Ensure no negative values in revenue and that country codes are valid (e.g., length 2-3 chars).
    2.  **Structured Logging:** Replace `print()` with Python's `logging` module. The pipeline should log info (rows processed) and errors (rows rejected) to a file or stdout with timestamps.
    3.  **Error Isolation:** Instead of dropping bad rows silently, save them to a `data/rejected.csv` for audit purposes.
* **Deliverable:** A pipeline that tells you *what* happened and *why* data was rejected.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Idempotency, Containerization & Scalability.
* **Requirement:** Everything above + **Docker & Idempotency**.
* **Extra Tasks:**
    1.  **Idempotency:** Ensure the pipeline can run multiple times without duplicating data in the Database. Implement an "Upsert" logic or a clean-replace strategy for the specific batch.
    2.  **Dockerization:** Create a `Dockerfile`. The entire pipeline should run with a single command (e.g., `docker run purestack-etl`) without requiring the user to manually install Python dependencies.
    3.  **Architecture Decision:** Include a `ARCHITECTURE.md` explaining why you chose Pandas vs Polars vs SQL for the transformation, discussing memory trade-offs.
* **Deliverable:** A production-ready, reproducible artifact.

---

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+.
* **Libraries:** Pandas (Standard) or Polars (High Performance).
* **Database:** SQLite (Standard library `sqlite3`).
* **Testing:** Pytest.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Analyze `data/sales_raw.csv` to identify the anomalies.
4.  Implement your logic in `src/pipeline.py`.
5.  Run validation tests: `pytest`.
6.  Submit via **Pull Request** stating your target Level.

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Data Integrity** | 35% | Are the final numbers correct? Did you clean the `$` and dates properly? |
| **Robustness** | 25% | Does the script crash on bad data? (Level 2/1 check). |
| **Code Structure** | 25% | Modular functions (`extract`, `transform`, `load`) vs Monolithic script. |
| **Best Practices** | 15% | Dependency management, Logging, and Idempotency logic. |

---

### 🚨 Project Structure (Standard)
To ensure our **Automated Auditor** works, keep the core structure:

```text
/
├── .github/workflows/   # PureStack Audit System (DO NOT TOUCH)
├── data/
│   └── sales_raw.csv    # <--- DIRTY DATA (Input)
├── src/
│   ├── __init__.py
│   └── pipeline.py      # <--- YOUR CODE HERE
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py # <--- VALIDATION TESTS
├── requirements.txt
├── Dockerfile           # <--- (Optional) Level 1
└── README.md
