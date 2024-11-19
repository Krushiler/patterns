import datetime

from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.repository.store_repository import StoreRepository
from working_with_settings.data.storage_finder.nomenclature.nomenclature_storage_finder import NomenclatureStorageFinder
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType
from working_with_settings.domain.model.filter.range_model import RangeModel
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.store.osv_nomenclature_report import OsvNomenclatureReport
from working_with_settings.util.stream.base.base_observable import StreamSubscription


class StoreManager(BaseManager[BaseState]):
    _nomenclature_repository: NomenclatureRepository
    _store_repository: StoreRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder

    _nomenclature_updates_subscription: StreamSubscription

    def __init__(self, nomenclature_repository, store_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._store_repository = store_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder

    def init(self):
        self._nomenclature_updates_subscription = self._nomenclature_repository.watch_nomenclature_updates() \
            .subscribe(self._on_nomenclature_updated)

    def _on_nomenclature_updated(self, nomenclature: Nomenclature):
        transactions = self._nomenclature_storage_finder.find_dependant_transactions(nomenclature.id)

        for transaction in transactions:
            transaction.nomenclature = nomenclature
            self._store_repository.update_transaction(transaction.id, transaction)

    def close(self):
        self._nomenclature_updates_subscription.close()

    def get_osv_nomenclature_reports(
            self,
            start_date: datetime.datetime,
            end_date: datetime.datetime,
            store_id: str,
            blocking_date: datetime.datetime
    ) -> list[OsvNomenclatureReport]:

        store_filter = Filter('store.id', store_id, FilterType.EQUALS)

        start_turnovers = self._store_repository.get_turnovers(
            filters=[
                Filter(
                    'time',
                    RangeModel(datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc), start_date),
                    FilterType.BETWEEN
                ),
                store_filter
            ],
            grouping=['nomenclature'],
            blocking_date=blocking_date
        )

        end_turnovers = self._store_repository.get_turnovers(
            filters=[
                Filter('time', RangeModel(start_date, end_date), FilterType.BETWEEN),
                store_filter
            ],
            grouping=['nomenclature'],
            blocking_date=blocking_date
        )

        reports = {}

        def get_report(turnover):
            nomenclature = AbsoluteMapper.from_dict(turnover.group['nomenclature'], Nomenclature)
            if nomenclature.id not in reports:
                reports[nomenclature.id] = OsvNomenclatureReport(nomenclature)
            return reports[nomenclature.id]

        for turnover in start_turnovers:
            get_report(turnover).start_amount = turnover.turnover

        for turnover in end_turnovers:
            get_report(turnover).end_amount = turnover.turnover

        return list(reports.values())
