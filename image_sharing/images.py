import io
import os
import uuid
import mimetypes
# import json
import msgpack
import falcon


class Resource:
    _CHUNK_SIZE_BYTES = 4096

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/kaguyachaa.png'
                }
            ]
        }
        resp.data = msgpack.packb(doc, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        ext = mimetypes.guess_extension(req.content_type)
        name = f'{uuid.uuid4()}{ext}'
        image_path = os.path.join(self.storage_path, name)

        with io.open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break
                image_file.write(chunk)
            resp.status = falcon.HTTP_201
            resp.location = f'/images/{name}'