import uuid

from working_with_settings.application.organization.nomenclature_manager import NomenclatureManager
from working_with_settings.application.start.start_manager import StartManager
from working_with_settings.di.di import Di


def test_nomenclature_added(inject: Di):
    start_manager: StartManager = inject.get_start_manager()
    start_manager.init()
    manager: NomenclatureManager = inject.get_nomenclature_manager()
    nomenclature = inject.get_start_nomenclature_factory().wheat_flour()
    nomenclature.id = str(uuid.uuid4())

    assert manager.delete_nomenclature( str(uuid.uuid4())) is True


def test_nomenclature_not_added_with_existing_references(inject: Di):
    start_manager: StartManager = inject.get_start_manager()
    start_manager.init()
    manager: NomenclatureManager = inject.get_nomenclature_manager()
    nomenclature = inject.get_start_nomenclature_factory().wheat_flour()

    assert manager.delete_nomenclature(nomenclature.id) is False
