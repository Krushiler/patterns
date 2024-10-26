import flask

from working_with_settings.di.di import Di
from working_with_settings.routing.routing import app
from working_with_settings.routing.store.dto import TransactionsRequestDto
from working_with_settings.routing.util.request_parser import RequestParser


@app.route('/api/store-turnovers', methods=['POST'])
def turnovers():
    """
    Calculate turnovers for the specified period.
    ---
    parameters:
      - in: body
        name: request
        required: true
    responses:
      200:
        description: A list of turnovers
        schema:
            type: array
            items:
                type: string
    """
    serializer = Di.instance().get_json_serializer()
    request = RequestParser.parse_body(flask.request.json, TransactionsRequestDto)

    if request.is_left:
        return request.left

    request = request.right

    turnovers = Di.instance().get_store_repository().get_turnovers(request.filters, request.date_from, request.date_to)

    return serializer.serialize(turnovers)
