import io
from wsgiref.validate import InputWrapper

from unittest.mock import call, MagicMock, mock_open

import falcon
from falcon import testing
import msgpack
import pytest

import image_sharing.app
import image_sharing.images


@pytest.fixture
def mock_store():
    return MagicMock()


@pytest.fixture
def client(mock_store):
    app = image_sharing.app.create_app(mock_store)
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


def test_post_image(client, mock_store):
    file_name = 'fake-image-name.xyz'
    mock_store.save.return_value = file_name
    image_content_type = 'image/xyz'

    response = client.simulate_post(
        '/images',
        body=b'some-fake-bytes',
        headers={'content-type': image_content_type}
    )

    assert response.status == falcon.HTTP_CREATED
    assert response.headers['location'] == f'/images/{file_name}'
    saver_call = mock_store.save.call_args
    assert isinstance(saver_call[0][0], InputWrapper)
    assert saver_call[0][1] == image_content_type
