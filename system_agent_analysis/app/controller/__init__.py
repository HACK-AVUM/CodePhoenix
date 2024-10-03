from flask import Flask

app = Flask(__name__)

from app.controller.analysis_controller import analyze_code_endpoint