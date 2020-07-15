from app.app import application
import os


@application.route('/', methods=['GET'])
def index():
    return "Welcome to Huxy Travel API"


if __name__ == '__main__':
    application.run(host=os.environ['APPLICATION_HOST'], port=os.environ['APPLICATION_PORT'],
                    debug=os.environ['APPLICATION_DEBUG'])
