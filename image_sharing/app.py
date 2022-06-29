import falcon
from .images import Resource

app = application = falcon.App()
images = Resource(storage_path='.')
app.add_route('/images', images)
