"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import requests


def extract(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/goose/goose_rawdata.csv",
    file_path="data/goose_rawdata.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
