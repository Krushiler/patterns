import flask

from working_with_settings.di.di import Di
from working_with_settings.routing.routing import app
from working_with_settings.routing.settings.dto import UpdateBlockingDateRequestDto
from working_with_settings.routing.util.request_parser import RequestParser


@app.route('/api/settings/blocking-date', methods=['GET'])
def settings():
    """
    Get settings
    ---
    responses:
      200:
        description: A list of turnovers
        schema:
            type: array
            items:
                type: string
    """
    serializer = Di.instance().get_json_serializer()
    settings = Di.instance().get_settings_manager().state.settings
    return serializer.serialize(settings.blocking_date)


@app.route('/api/settings/blocking-date', methods=['PATCH'])
def blocking_date():
    """
    Update blocking date
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
    request = RequestParser.parse_body(flask.request.json, UpdateBlockingDateRequestDto)

    if request.is_left:
        return request.left

    request = request.right
    settings = Di.instance().get_settings_manager().change_blocking_date(request.date)

    return serializer.serialize(settings)
