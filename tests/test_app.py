import falcon
from falcon import testing
import msgpack
import pytest

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
