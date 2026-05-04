from httpx import HTTPTransport, Request


class ResponseHandler(HTTPTransport):

    def handle_request(self, request: Request):
        response = super().handle_request(request)

        return response
