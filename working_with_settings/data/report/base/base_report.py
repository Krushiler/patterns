from abc import ABC, abstractmethod

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat


class BaseReport(ABC):
    def create(self, obj: list[BaseModel]) -> str:
        serialized_data = [AbsoluteMapper.to_dict(item) for item in obj]
        return self.create_from_serialized(serialized_data, obj)

    @abstractmethod
    def create_from_serialized(self, obj: list[dict], original_obj: list[BaseModel]) -> str:
        pass

    @property
    @abstractmethod
    def format(self) -> ReportFormat:
        pass

    def _flatten_dict(self, d: dict, parent_key: str = '', sep: str = '.') -> dict:
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
