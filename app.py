from flask_sqlalchemy import SQLAlchemy
from website import create_app
from website.models import db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
