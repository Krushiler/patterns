import connexion
from flasgger import Swagger

app = connexion.FlaskApp(__name__)

from .reports.routing import *  # noqa
from .filter.filter import *  # noqa
from .store.routing import *  # noqa
from .settings.routing import *  # noqa
from .nomenclature.routing import *  # noqa

swagger = Swagger(app.app)
