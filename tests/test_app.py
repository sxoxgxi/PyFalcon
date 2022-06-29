from email import header
from wsgiref import headers
import falcon
from falcon import testing
import msgpack
import pytest
from unittest.mock import mock_open, call
from image_sharing.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_list_images(client):
    doc = {
        'images': [
            {
                'href': '/images/kaguyachaa.png'
            }
        ]
    }
    response = client.simulate_get('/images')
    result_doc = msgpack.unpackb(response.content, raw=False)
    assert result_doc == doc
    assert response.status == falcon.HTTP_OK


def test_posted_image_gets_saved(client, monkeypatch):
    mock_file_open = mock_open()
    monkeypatch.setattr('io.open', mock_file_open)

    fake_uuid = '123e4567-e89b-12d3-a456-426655440000'
    monkeypatch.setattr('uuid.uuid4', lambda: fake_uuid)

    fake_image_bytes = b'fake-image-bytes'
    response = client.simulate_post(
        '/images',
        body=fake_image_bytes,
        headers={'Content-Type': 'image/png'}
    )

    assert response.status_code == falcon.HTTP_CREATED
    assert call().write(fake_image_bytes) in mock_file_open.mock_calls
    assert response.headers['location'] == f'image/{fake_uuid}.png'
