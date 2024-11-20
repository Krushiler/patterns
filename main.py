from working_with_settings.di.di import Di
from working_with_settings.routing.routing import app
from working_with_settings.util.logging.logger import Logger


def _init_managers():
    Di.instance().get_dao().load()

    settings_manager = Di.instance().get_settings_manager()
    Di.instance().get_log_writer().setup()

    settings = settings_manager.state.settings

    Di.instance().get_start_manager().init(settings)
    Di.instance().get_store_manager().init()
    Di.instance().get_recipe_manager().init()
    settings_manager.mark_as_loaded()


if __name__ == '__main__':
    _init_managers()
    app.run(host='0.0.0.0', port=8080)

    Logger.info('main', 'Application started')
