import pandas as pd
import sqlite3

class ETIPipeline:
    def __init__(self, input_path, db_path):
        self.input_path = input_path
        self.db_path = db_path

    def extract(self):
        """ Read the CSV file """
        # TODO: Implement reading logic
        pass

    def transform(self, df):
        """ Clean and Aggregate Data """
        # TODO:
        # 1. Fix dates
        # 2. Convert amount to float
        # 3. Drop invalid rows
        # 4. Group by country -> sum(amount)
        pass

    def load(self, df):
        """ Save to SQLite """
        # TODO: Save to table 'revenue_by_country'
        pass

    def run(self):
        df = self.extract()
        clean_df = self.transform(df)
        self.load(clean_df)
        print("Pipeline Completed Successfully.")

if __name__ == "__main__":
    pipeline = ETIPipeline('data/sales_raw.csv', 'sales.db')
    pipeline.run()
