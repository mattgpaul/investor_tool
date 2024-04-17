# Python

import requests
from bs4 import BeautifulSoup
import pandas as pd

class SecData:
    HEADERS = {'User-Agent': "email@address.com"}
    ZIP_FILE_URL = 'https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip'

    def download_data(self):
        response = requests.get(self.ZIP_FILE_URL, headers=self.HEADERS)
        return response.content

    def parse_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Parse data here
        return soup

    def create_dataframe(self, data):
        df = pd.DataFrame(data)
        # Organize data by quarter here
        return df

    def get_quarterly_data(self):
        html = self.download_data(self.SEC_URL)
        data = self.parse_data(html)
        df = self.create_dataframe(data)
        return df