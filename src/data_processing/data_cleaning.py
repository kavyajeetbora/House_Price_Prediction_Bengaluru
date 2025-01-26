import pandas as pd
from src.logger import logging
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataCleanerConfig:
    raw_data_path: str = os.path.join("data", "Bengaluru_House_Data.csv")


class DataCleaner:
    def __init__(self):
        self.config = DataCleanerConfig()

    def splitData(self):

        try:

            ## Read the data
            df_raw = pd.read_csv(self.config.raw_data_path)
            df = df_raw.copy()

            logging.info(f"The raw loaded as dataframe with shape: {df.shape}")

            ## Start cleaning the data

            ## 1. Dropping unncessary columns
            drop_columns = ["area_type", "availability", "balcony", "society"]
            df = df.drop(drop_columns, axis="columns")

            logging.info("Dropping unnecessary columns: {drop_columns}")
            logging.info("Shape of the new dataframe: {df.shape}")

            ## 2. Remove nulls
            logging.info("Dropping null rows")
            df = df.dropna()
            logging.info(f"Number of null rows dropped: {df.isna().sum()}")
            logging.info(f"Number of non null rows: {df.notna().sum()}")

            ## 3. Standardize room size column
            logging.info("Extracting and transforming the room size to integers")
            df["bhk"] = df["size"].apply(lambda x: int(x.split(" ")[0]))
            logging.info(f"New column bhk created")

            ## 4. Convert the square foot column to float
            logging.info("Converting all the 'Square foot' column to float")
            logging.info("Dropping invalid sqft values")
            df = df[df["total_sqft"].str.contains("-")].copy()
            logging.info(
                "Splitting the sqft value -> averaging the range -> converting it to floats"
            )
            df["total_sqft"] = df["total_sqft"].apply(self.avg_sqft)
            logging.info(
                "Sucessfully cleaned and converted the total square foot values to float"
            )

        except Exception as e:
            logging.info(f"Error has occured\n.{e}")

    def avg_sqft(self, x: str):
        """
        This functions transforms the given string value:
        1. Splits the given column into two values by using '-' delimiter.
        2.
        """

        tokens = x.split("-")
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2

        try:
            return float(x)
        except:
            return None
