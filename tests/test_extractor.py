import pytest
import pandas as pd
from unittest.mock import patch, mock_open
from etl.extractor import extract_and_select_file

def test_extract_and_select_file_success():
    with patch('os.listdir') as mock_listdir, \
         patch('builtins.open', new_callable=mock_open, read_data='data') as mock_file:
        mock_listdir.return_value = ['test.csv']
        path = r'data\input\example\customers-100.csv'
        with patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame({'data': [1, 2, 3]})
            file_path, df = extract_and_select_file('data/input')
            assert file_path == path
            assert not df.empty

def test_extract_and_select_file_no_files():
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = []  
        file_path, data = extract_and_select_file('data/input')
        assert file_path is None
        assert data is None