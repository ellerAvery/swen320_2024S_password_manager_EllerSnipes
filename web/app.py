import sys
import os
import time
from flask import Flask, render_template, request, send_from_directory, flash, url_for, redirect


app = Flask(__name__, 
			static_url_path='', 
			static_folder='static',
			template_folder='templates')


# We do not have to use app.run. Use of flask run is a newer preferred method
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5000)