import flask
from flask import Flask

import models
from models import ScrapeWell_Les_1

app = Flask(__name__)

@app.route("/")
def index():
    sale_listings = ScrapeWell_Les_1.go()
    return str(sale_listings)