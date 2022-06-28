# Falcon webframework

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
 $ waitress-serve --port=8000 image_sharing.app:app
```
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
### Open http://127.0.0.1:8000/images
