from flask import Flask

app = Flask(__name__)

from app.controller import scanning_vuln_controller