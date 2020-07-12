from app.app import application


@application.route('/', methods=['GET'])
def index():
    return "Welcome to Huxy Travel API"


if __name__ == '__main__':
    application.run(port=5001, debug=True)
