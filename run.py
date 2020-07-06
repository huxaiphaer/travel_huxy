from app.app import application, db


@application.route('/', methods=['GET'])
def index():
    return "Welcome to Huxy Travel API"


@application.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    application.run(port=5001, debug=True)
