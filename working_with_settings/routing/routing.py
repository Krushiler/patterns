import connexion
from flasgger import Swagger

app = connexion.FlaskApp(__name__)

from .reports.reports import *  # noqa

swagger = Swagger(app.app)
