# Falcon Web Framework

- https://falcon.readthedocs.io/en/stable/

# Installation

Clone the project:

```bash
 $ git clone https://github.com/sxoxgxi/PyFalcon
 $ cd PyFalcon
```

## Deployment

To deploy this project run:

```bash
 $ pip install -r requirements.txt
 $ waitress-serve --port=8000 image_sharing.app:get_app  ❌
```

#### In app.py

```py
app = get_app()
```

```bash
$ waitress-serve --port=8000 image_sharing.app:app  ✅
```

Note: You shouldn't pass wsgi the create_app function, instead should make the function return app and give the wsgi returned app.

* Open http://127.0.0.1:8000/images

## Checking routes

To chect the available routes for the app run:

```bash
 $ falcon-inspect-app image_sharing.app:app
```

It should look like this:

```bash
 • Routes:
    ⇒ /images - Resource:
       └── GET - on_get
```

## Testing the application

Let’s start by installing the pytest package if not installed:

```bash
 $ pip install pytest
```

Next, run the following from the main directory:

```bash
 $ pytest tests
```

It should look like this:

```bash
 ====== test session starts ======

            some messages

 ====== number of tests passed in some seconds ======
```

## POST request

Now les try sending a POST request to the server by using httpie:

```bash
 $ http POST localhost:8000/images Content-Type:image/png < images/kaguyachaa.png
```

**Note: (images/kaguyachaa.png) can be any image of your choice**

After sending the POST request to the server you should have a copy of the original image in your storage path
