from flask.cli import FlaskGroup
from web import app  # Ensure 'web' is your Flask app's package
import unittest

cli = FlaskGroup(app)

@cli.command("test")
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    cli()
