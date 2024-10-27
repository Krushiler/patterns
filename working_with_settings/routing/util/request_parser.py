from working_with_settings.di.di import Di
from working_with_settings.domain.exceptions.base.either import Either
from working_with_settings.routing.util.response_factory import ResponseFactory


class RequestParser:
    @staticmethod
    def parse_body(json: dict, json_type: type) -> Either:
        serializer = Di.instance().get_json_serializer()
        try:
            return Either.with_right(serializer.deserialize(json, json_type))
        except Exception as e:
            return Either.with_left(ResponseFactory.error(str(e), 400))
