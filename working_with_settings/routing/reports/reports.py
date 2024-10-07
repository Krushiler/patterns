import flask

from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.di.di import Di
from working_with_settings.domain.exceptions.base.either import Either
from working_with_settings.domain.model.report.report_format import ReportFormat
from working_with_settings.routing.routing import app
from working_with_settings.routing.util.response_factory import ResponseFactory


def _get_report() -> Either[object, BaseReport]:
    report_name = flask.request.args.get('format').upper()
    if report_name not in ReportFormat:
        return Either.with_left(ResponseFactory.error('Unknown report format: {}'.format(report_name)))

    report_format = ReportFormat[report_name]

    settings = Di.instance().get_settings_manager().state.settings
    return Either.with_right(Di.instance().get_report_factory().create(report_format, settings))


@app.route('/api/reports/formats', methods=['GET'])
def formats():
    """
    Retrieve available report formats.
    ---
    responses:
      200:
        description: A list of report formats
        schema:
          type: array
          items:
            type: string
    """
    return [e.name for e in ReportFormat]


@app.route('/api/reports/nomenclature', methods=['GET'])
def nomenclature():
    """
    Retrieve nomenclature report in the specified format.
    ---
    parameters:
      - name: format
        in: query
        type: string
        required: true
        description: ReportFormat key name
    responses:
      200:
        description: Nomenclature report
      400:
        description: Invalid report format
    """
    res = _get_report()
    if res.is_left:
        return res.left
    report = res.right
    nomenclature = Di.instance().get_nomenclature_repository().get_nomenclatures()

    return report.create(nomenclature)


@app.route('/api/reports/nomenclature-groups', methods=['GET'])
def nomenclature_groups():
    """
    Retrieve nomenclature groups report in the specified format.
    ---
    parameters:
      - name: format
        in: query
        type: string
        required: true
        description: ReportFormat key name
    responses:
      200:
        description: Nomenclature Groups report
      400:
        description: Invalid report format
    """
    res = _get_report()
    if res.is_left:
        return res.left
    report = res.right
    nomenclature = Di.instance().get_nomenclature_repository().get_nomenclature_groups()

    return report.create(nomenclature)


@app.route('/api/reports/units', methods=['GET'])
def units():
    """
    Retrieve units report in the specified format.
    ---
    parameters:
      - name: format
        in: query
        type: string
        required: true
        description: ReportFormat key name
    responses:
      200:
        description: Units report
      400:
        description: Invalid report format
    """
    res = _get_report()
    if res.is_left:
        return res.left
    report = res.right
    units = Di.instance().get_measurement_units_factory().get_units()

    return report.create(units)


@app.route('/api/reports/recipes', methods=['GET'])
def recipes():
    """
       Retrieve recipes report in the specified format.
       ---
       parameters:
         - name: format
           in: query
           type: string
           required: true
           description: ReportFormat key name
       responses:
         200:
           description: Recipes report
         400:
           description: Invalid report format
       """
    res = _get_report()
    if res.is_left:
        return res.left
    report = res.right
    recipes = Di.instance().get_recipe_repository().get_recipes()

    return report.create(recipes)
