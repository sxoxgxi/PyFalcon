from email.mime import image
import io
import mimetypes
import os
import uuid
import falcon
import msgpack


class Resource:

    def __init__(self, store):
        self._store = store

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
        name = self._store.save(req.stream,  req.content_type)
        resp.status = falcon.HTTP_201
        resp.location = f'/images/{name}'


class ImageStore:

    _CHUNK_SIZE_BYTES = 4096

    def __init__(self, storage_path, uuidgen=uuid.uuid4, fopen=io.open) -> None:
        self._storage_path = storage_path
        self._uuidgen = uuidgen
        self._fopen = fopen

    def save(self, image_stream, image_content_type):
        ext = mimetypes.guess_extension(image_content_type)
        name = f'{self._uuidgen}{ext}'
        image_path = os.path.join(self._storage_path, name)
        with self._fopen(image_path, 'wb') as image_file:
            while True:
                chunk = image_stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break
                image_file.write(chunk)
        return name
