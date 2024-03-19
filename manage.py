from flask.cli import FlaskGroup
from web import app, db  # Assuming `db` is your SQLAlchemy instance
from flask_migrate import Migrate
from decouple import config
import unittest

# Initialize Migrate
#migrate = Migrate(app, db)

cli = FlaskGroup(app)

@cli.command("test")
def test():
    """Runs the unit tests without test coverage."""
    app.config.from_object(config("APP_SETTINGS", default="config.DevelopmentConfig"))

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)  # Adjusted verbosity for readability

    if result.wasSuccessful():
        return 0
    else:
        return 1

if __name__ == "__main__":
    cli()
