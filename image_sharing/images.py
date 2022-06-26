import falcon
import json


class Resource:
    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': 'https://pbs.twimg.com/profile_images/1527968318153338880/8PX5U9u3_400x400.jpg'
                }
            ]
        }
        resp.text = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
