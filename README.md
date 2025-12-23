# 🛢️ PureStack Data Engineering Challenge: The ETL Pipeline

**PureStack.es - Engineering Validation Protocol.**
> *"Data is never clean. We audit your ability to turn chaos into reliable KPIs."*

> [!TIP]
> **HOW TO START THIS CHALLENGE**
> 1. Click the green **"Use this template"** button (top right) -> **"Create a new repository"**.
> 2. Select **"Private"** visibility (Crucial to prevent spoilers).
> 3. Clone your new private repository to your machine.
> 4. Once finished, invite user **[JLMoraCastilla](https://github.com/JLMoraCastilla)** as a collaborator to review.
>
> ⚠️ **DO NOT FORK** this repository directly, as it will force your solution to be public.

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Data Engineering.
In the real world, "Happy Paths" don't exist. We audit your ability to handle **Missing Values**, **Inconsistent Formats**, and **Schema Drift**.

**The Mission:** The sales team has provided a dump of raw data (`data/sales_raw.csv`). It contains errors, duplicates, and mixed formats. Your job is to build a resilient **ETL Pipeline** to clean it and store high-level KPIs into a SQL database.

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by the robustness and reproducibility of your pipeline. State your target level in your Pull Request (or commit message).

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Functional ETL & Pandas/Polars usage.
* **Requirement:** Complete the pipeline to pass the provided tests.
* **Tasks:**
    1.  **Extract:** Read the `data/sales_raw.csv`.
    2.  **Transform:**
        * **Sanitization:** Standardize dates to `YYYY-MM-DD`. Handle nulls (drop rows with missing `order_id` or `amount`).
        * **Type Casting:** Ensure `amount` is a float (strip symbols like `$`, handle `"USD"`).
        * **Aggregation:** Group by `country` and calculate `total_revenue`.
    3.  **Load:** Save the aggregated data into a SQLite database (`sales.db`) in a table named `revenue_by_country`.
* **Deliverable:** A functional `src/pipeline.py` that generates correct numbers (Turns the tests Green).

#### 🥈 Level 2: Pro / Senior
* **Focus:** Data Quality (DQ) & Observability.
* **Requirement:** Everything in Level 3 + **Schema Validation & Logging**.
* **Extra Tasks:**
    1.  **Schema Validation:** Before loading, validate the transformed data (e.g., ensure no negative revenue).
    2.  **Structured Logging:** Replace `print()` with Python's `logging` module. Log processed row counts and errors.
    3.  **Error Isolation:** Instead of dropping bad rows silently, save them to a `data/rejected.csv` for audit purposes.
* **Deliverable:** A pipeline that tells you *what* happened and *why* data was rejected.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Idempotency, Containerization & Scalability.
* **Requirement:** Everything above + **Docker & Idempotency**.
* **Extra Tasks:**
    1.  **Idempotency:** Ensure the pipeline can run multiple times without duplicating data in the Database (Use `DROP TABLE IF EXISTS` or `INSERT OR REPLACE`).
    2.  **Dockerization:** Create a `Dockerfile`. The pipeline should run with a single command (e.g., `docker run purestack-etl`).
    3.  **Architecture Decision:** Include a `ARCHITECTURE.md` explaining why you chose Pandas vs Polars vs SQL.
* **Deliverable:** A production-ready, reproducible artifact.

---

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+.
* **Libraries:** Pandas (Standard) or Polars (High Performance).
* **Database:** SQLite (Standard library `sqlite3`).
* **Testing:** Pytest.

---

### 🚀 Execution Instructions

1.  **Use the Template:** Create your **Private Repository** using the instructions at the top of this file.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Analyze `data/sales_raw.csv` to identify the anomalies.
4.  Implement your logic in `src/pipeline.py`.
    * **IMPORTANT:** Your main logic must be encapsulated in a function named `run_pipeline()` so the tests can call it.
5.  Run validation tests:
    ```bash
    pytest tests/
    ```
6.  **Submit:** Push your changes to your private repo and invite the reviewer.

> **Note:** You will see a ❌ (**Red Cross**) initially because the database doesn't exist yet. Your goal is to turn it ✅ (**Green**).

---

### 📝 Audit & Validation Rules (Strict)

> **⚠️ The "Production-Ready" Policy**
>
> Our automated auditor (`audit.yml`) enforces strict quality rules. Your PR will be automatically rejected if:
>
> 1.  **Use of `print()`:** We are building a production pipeline. `print()` statements are **forbidden** in `src/`. You **must** use the Python `logging` module.
> 2.  **Hardcoded Paths:** Do not use absolute paths (e.g., `C:/Users/...` or `/home/runner/...`). Use relative paths (e.g., `data/sales_raw.csv`) to ensure portability.
> 3.  **Structure Integrity:** Do not rename `src/pipeline.py` or the `run_pipeline()` function, as the test suite depends on them.

---

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Data Integrity** | 35% | Are the final numbers correct? Did you clean the `$` and dates properly? |
| **Robustness** | 25% | Does the script crash on bad data? |
| **Code Structure** | 25% | Modular functions (`extract`, `transform`, `load`) vs Monolithic script. |
| **Best Practices** | 15% | Dependency management, Proper Logging (No prints), and Idempotency logic. |

---

### 🚨 Project Structure (Standard)
To ensure our **Automated Auditor** works, keep the core structure:

```text
/
├── .github/
│   └── workflows/
│       └── audit.yml            # PureStack Audit System
├── data/
│   └── sales_raw.csv            # Input Data (Dirty CSV with errors)
├── src/
│   ├── __init__.py
│   └── pipeline.py              # <--- YOUR CODE HERE (Must contain 'run_pipeline')
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py         # Validation Logic
├── .gitignore
├── requirements.txt             # Dependencies
└── README.md
```
---
## ⚖️ License & Legal Notice

**© 2025 PureStack.es. All Rights Reserved.**

This repository is "Source Available" for **evaluation purposes only**.

* **Public viewing:** Allowed.
* **Commercial use:** ❌ Strictly Prohibited.
* **Redistribution:** ❌ Strictly Prohibited.

By accessing this material, you agree to the terms in `LICENSE.md`.

> **🚫 Publishing solutions to public repositories is a violation of these terms.**
