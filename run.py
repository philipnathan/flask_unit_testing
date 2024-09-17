from app import philip_app

if __name__ == "__main__":
    philip_app.run()
else:
    gunicorn_app = philip_app
