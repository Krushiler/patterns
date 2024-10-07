from working_with_settings.di.di import Di
from working_with_settings.routing.routing import app

if __name__ == '__main__':
    Di.instance().get_start_manager().init()

    app.run(port=8080)
