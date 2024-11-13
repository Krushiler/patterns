from working_with_settings.di.di import Di
from working_with_settings.routing.routing import app


def _init_managers():
    Di.instance().get_start_manager().init()
    Di.instance().get_store_manager().init()
    Di.instance().get_recipe_manager().init()


if __name__ == '__main__':
    _init_managers()
    app.run(port=8080)
