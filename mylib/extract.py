"""
Extract a dataset from a URL to a file path

food dataset
"""

# import requests

# def extract(
#     url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/"
#     "goose/goose_rawdata.csv",
#     file_path="data/goose_rawdata.csv",
# ):
#     """ "Extract a url to a file path"""
#     with requests.get(url) as r:
#         with open(file_path, "wb") as f:
#             f.write(r.content)
#     return file_path

import os
import requests


def extract(
    url=(
        "https://github.com/fivethirtyeight/data/raw/refs/heads/master/"
        "goose/goose_rawdata.csv"
    ),
    file_path="data/goose_rawdata.csv",
):
    """Extract a URL to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return os.path.abspath(file_path)
