import connexion
from flasgger import Swagger

app = connexion.FlaskApp(__name__)

from .reports.reports import *  # noqa
from .filter.filter import *  # noqa
from .store.store import *  # noqa
from .settings.settings import *  # noqa

swagger = Swagger(app.app)
