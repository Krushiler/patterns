from flask import make_response


class ResponseFactory:

    @staticmethod
    def error(error: str, status_code: int = 400) -> str:
        response = make_response({'error': error})
        response.status_code = status_code
        return response

    @staticmethod
    def success_no_data() -> str:
        response = make_response()
        response.status_code = 204
        return response
