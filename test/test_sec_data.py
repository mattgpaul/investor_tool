import pytest
from unittest.mock import Mock
from src.sec_data import SecData

def mock_get(*args, **kwargs):
    mock_response = Mock()
    mock_response.content = b'PK\x03\x04\x14\x00\x00\x00\x08\x00n\xaeGP'
    return mock_response

def test_download_data(monkeypatch):
    monkeypatch.setattr("requests.get", mock_get)

    sec_data = SecData()
    data = sec_data.download_data()
    assert data[:4] == b'PK\x03\x04'