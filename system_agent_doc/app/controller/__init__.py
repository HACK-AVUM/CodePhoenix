from flask import Flask

app = Flask(__name__)

from system_agent_doc.app.controller import docs_controller