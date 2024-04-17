import pytest
from src.sec_data import SecData

def test_download_data(mocker):
    mock_response = mocker.Mock()
    mock_response.content = b'PK\x03\x04\x14\x00\x00\x00\x08\x00n\xaeGP'
    mocker.patch('requests.get', return_value=mock_response)

    sec_data = SecData()
    data = sec_data.download_data()
    assert data[:4] == b'PK\x03\x04'