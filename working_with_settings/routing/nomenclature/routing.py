import flask

from working_with_settings.application.organization.nomenclature_manager import NomenclatureManager
from working_with_settings.data.serialization.json_serializer import JsonSerializer
from working_with_settings.di.di import Di
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.routing.routing import app
from working_with_settings.routing.util.request_parser import RequestParser
from working_with_settings.routing.util.response_factory import ResponseFactory


@app.route('/api/nomenclature/<id>', methods=['PATCH'])
def update_nomenclature():
    nomenclature_id = flask.request.args['id']
    request = RequestParser.parse_body(flask.request.json, Nomenclature)

    if request.is_left:
        return request.left

    nomenclature = request.right
    nomenclature_manager: NomenclatureManager = Di.instance().get_nomenclature_manager()
    nomenclature_manager.update_nomenclature(nomenclature_id, nomenclature)

    return ResponseFactory.success_no_data()


@app.route('/api/nomenclature/<id>', methods=['DELETE'])
def delete_update_nomenclature():
    nomenclature_id = flask.request.args['id']

    nomenclature_manager: NomenclatureManager = Di.instance().get_nomenclature_manager()
    result = nomenclature_manager.delete_nomenclature(nomenclature_id)
    if result:
        return ResponseFactory.success_no_data()
    return ResponseFactory.error('Cannot delete this nomenclature', 400)


@app.route('/api/nomenclature/<id>', methods=['GET'])
def get_nomenclature():
    nomenclature_id = flask.request.args['id']
    json_serializer: JsonSerializer = Di.instance().get_json_serializer()

    nomenclature_manager: NomenclatureManager = Di.instance().get_nomenclature_manager()
    nomenclature = nomenclature_manager.get_nomenclature(nomenclature_id)

    if nomenclature is not None:
        return json_serializer.serialize(nomenclature)

    return ResponseFactory.error('No such nomenclature', 404)


@app.route('/api/nomenclature', methods=['PUT'])
def put_nomenclature():
    request = RequestParser.parse_body(flask.request.json, Nomenclature)

    if request.is_left:
        return request.left

    nomenclature = request.right

    nomenclature_manager: NomenclatureManager = Di.instance().get_nomenclature_manager()
    nomenclature_manager.create_nomenclature(nomenclature)

    return ResponseFactory.success_no_data()
