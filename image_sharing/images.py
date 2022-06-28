import falcon
# import json
import msgpack


class Resource:
    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': 'https://pbs.twimg.com/profile_images/1527968318153338880/8PX5U9u3_400x400.jpg'
                }
            ]
        }
        resp.data = msgpack.packb(doc, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200
