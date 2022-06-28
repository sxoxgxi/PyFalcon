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

Open http://127.0.0.1:8000/images

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

 ====== 1 passed in some seconds ======
```
