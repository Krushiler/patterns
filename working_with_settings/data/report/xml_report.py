from xml.etree.ElementTree import Element, tostring, SubElement

from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat


class XmlReport(BaseReport):

    def create_from_serialized(self, obj: list[dict], original_obj: list[BaseModel]) -> str:
        root = Element("root")

        class_name = original_obj[0].__class__.__name__

        for i, item in enumerate(obj, 1):
            object_element = SubElement(root, f"{class_name}_{i}")
            self._dict_to_xml(item, object_element)

        return tostring(root, encoding='unicode', xml_declaration=True)

    def _dict_to_xml(self, d: dict, parent: Element):
        for key, value in d.items():
            child = SubElement(parent, key)
            if isinstance(value, dict):
                self._dict_to_xml(value, child)
            else:
                child.text = str(value)

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.XML
