import datetime

from working_with_settings.application.settings.settings_manager import SettingsManager
from working_with_settings.util.logging.log import Log
from working_with_settings.util.logging.logger import Logger


class LogWriter:
    _settings_manager: SettingsManager

    def __init__(self, settings_manager: SettingsManager):
        self._settings_manager = settings_manager

    def setup(self):
        Logger.watch_logs().subscribe(self.write)

    def write(self, log: Log):
        if self._settings_manager.state.settings.log_level.value >= log.level.value:
            log_str = f"{log.level} [{datetime.datetime.now().isoformat()}] {log.tag}: {log.message}"
            with open('logs.txt', 'a') as log_file:
                log_file.write(log_str + '\n')
                log_file.flush()
            print(log_str)
