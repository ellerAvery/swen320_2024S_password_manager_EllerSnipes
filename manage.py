import sys
from flask.cli import FlaskGroup
from web.create_app import create_app  

app = create_app()
cli = FlaskGroup(create_app=lambda: app)

@cli.command('test')
def run_tests():
    """Runs the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('web/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)

if __name__ == '__main__':
    cli()
