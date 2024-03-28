import unittest
from flask.cli import AppGroup
from web import create_app

# Create an instance of your Flask application
app = create_app()

# Create a new Flask AppGroup for custom commands
custom_commands = AppGroup('custom')

@custom_commands.command('runserver')
def run_server():
    """Runs the Flask server."""
    app.run()

@custom_commands.command('test')
def run_tests():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('web/test', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

# Register the AppGroup with the Flask CLI
app.cli.add_command(custom_commands)

if __name__ == '__main__':
    app.run()
