from flask.cli import FlaskGroup
from flask import app 
import unittest

cli = FlaskGroup(app)

@cli.command("test")
def test():
    """Runs the unit tests without test coverage."""
    test = unittest.TestLoader().discover("test")
    result = unittest.TextTestRunner(verbosity=2).run(test)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    cli()
