from app import app
from app.config.config_services import get_port, get_debug_mode

if __name__ == '__main__':
    
    port = get_port()
    debug_mode = get_debug_mode()

    app.run(debug=debug_mode, port=port)
