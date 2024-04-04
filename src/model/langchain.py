"""
Helper for loading files from S3
"""

import os
from langchain_community.document_loaders import S3DirectoryLoader
from src.config import AppConfig


class DataLoader:
    def __init__(self) -> None:
        self.config = AppConfig()
        

    def load(self):
        loader = S3DirectoryLoader(self.config.file_bucket, prefix=self.config.file_prefix)
        docs = loader.load()
        return docs



# if __name__ == "__main__":
#     data_loader = DataLoader(
#         bucket="bedrock-test-example", 
#         prefix="_data/"
#     )
#     data_loader.load()