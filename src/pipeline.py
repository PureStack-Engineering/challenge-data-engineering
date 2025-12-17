import logging
import sqlite3
import pandas as pd

# Configure logging (Minimal setup)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    """
    Orchestrates the ETL process.
    Reads data, transforms it, and loads it into SQLite.
    """
    logger.info("Starting ETL Pipeline...")
    
    # TODO: Implement Extraction
    # TODO: Implement Transformation (Cleaning, Aggregation)
    # TODO: Implement Loading (SQLite)
    
    raise NotImplementedError("Pipeline logic not implemented yet!")

if __name__ == "__main__":
    run_pipeline()
