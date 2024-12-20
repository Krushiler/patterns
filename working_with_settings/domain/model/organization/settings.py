import datetime

from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException, \
    InvalidFormatException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat
from working_with_settings.data.report.csv_report import CsvReport
from working_with_settings.data.report.json_report import JsonReport
from working_with_settings.data.report.markdown_report import MarkdownReport
from working_with_settings.data.report.rtf_report import RtfReport
from working_with_settings.data.report.xml_report import XmlReport


class Settings(BaseModel):
    _inn: str = None
    _bic: str = None
    _account: str = None
    _ownership_form: str = None
    _default_report_format: ReportFormat = None
    _report_map: dict[ReportFormat, type] = {
        ReportFormat.CSV: CsvReport,
        ReportFormat.MARKDOWN: MarkdownReport,
        ReportFormat.JSON: JsonReport,
        ReportFormat.XML: XmlReport,
        ReportFormat.RTF: RtfReport
    }
    _blocking_date: datetime.datetime = None
    _first_start: bool = False

    def __init__(self, inn: str = None, bic: str = None, account: str = None, ownership_form: str = None,
                 default_report_format: ReportFormat = ReportFormat.JSON, blocking_date: datetime.datetime = None,
                 first_start: bool = False):
        super().__init__()

        self.inn = inn
        self.bic = bic
        self.account = account
        self.ownership_form = ownership_form
        self.default_report_format = default_report_format
        self.blocking_date = blocking_date
        self.first_start = first_start

    @property
    def inn(self) -> str:
        return self._inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException('str', type(value))
        if not value.isdigit():
            raise InvalidFormatException('digits', value)
        if len(value) != 12:
            raise InvalidLengthException(12, len(value))
        self._inn = value

    @property
    def bic(self) -> str:
        return self._bic

    @bic.setter
    def bic(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._bic = value

    @property
    def account(self) -> str:
        return self._account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._account = value

    @property
    def ownership_form(self) -> str:
        return self._ownership_form

    @ownership_form.setter
    def ownership_form(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._ownership_form = value

    @property
    def default_report_format(self) -> ReportFormat:
        return self._default_report_format

    @default_report_format.setter
    def default_report_format(self, value: ReportFormat):
        if not isinstance(value, ReportFormat):
            raise InvalidTypeException(ReportFormat, type(value))
        self._default_report_format = value

    @property
    def report_map(self) -> dict:
        return self._report_map

    @report_map.setter
    def report_map(self, value: dict):
        if not isinstance(value, dict):
            raise InvalidTypeException(dict, type(value))
        for v in value.values():
            if not issubclass(v, BaseReport):
                raise InvalidTypeException(BaseReport, type(v))
        self._report_map = value

    @property
    def blocking_date(self) -> datetime.datetime:
        return self._blocking_date

    @blocking_date.setter
    def blocking_date(self, value: datetime.datetime):
        if not isinstance(value, datetime.datetime):
            raise InvalidTypeException(datetime.datetime, type(value))
        self._blocking_date = value

    @property
    def first_start(self) -> bool:
        return self._first_start

    @first_start.setter
    def first_start(self, value: bool):
        if not isinstance(value, bool):
            raise InvalidTypeException(bool, type(value))
        self._first_start = value
