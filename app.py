from core import create_app


app = create_app()


@app.route("/")
def welcome():
    return "<p>Welcome</p>"
