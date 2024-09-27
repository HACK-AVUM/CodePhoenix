from app import app
from app.config.config_services import get_port, get_debug_mode

if __name__ == '__main__':
    app.run(debug=get_debug_mode(), port=get_port())
