import flask

from working_with_settings.di.di import Di
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.routing.routing import app
from working_with_settings.routing.storage_factory.storage_factory import StorageFactory


@app.route('/api/filter/<entity>', methods=['POST'])
def filter(entity):
    """
    Fetch entities filtered by the specified filters.
    ---
    parameters:
      - in: body
        name: filter
        required: true
      - name: entity
        in: path
        type: string
        enum: ['nomenclature', 'nomenclature-group', 'unit', 'recipe', 'store', 'store-transaction']
        required: true
        default: nomenclature
    responses:
      200:
        description: A list of entities
        schema:
          type: array
    """

    storage = StorageFactory.get_storage(entity)

    if storage.is_left:
        return storage.left

    serializer = Di.instance().get_json_serializer()
    filters = serializer.deserialize(flask.request.json, Filter)
    return serializer.serialize(storage.right.get_filtered(filters))
