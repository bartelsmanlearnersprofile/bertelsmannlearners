"""
- Common error HTTP status codes include:
    - 400 Bad Request – This means that client-side input fails validation.
    - 401 Unauthorized – This means the user isn’t not authorized to access a resource. It usually returns when the user isn’t authenticated.
    - 403 Forbidden – This means the user is authenticated,
    but it’s not allowed to access a resource.
    - 404 Not Found – This indicates that a resource is not found.
    - 500 Internal server error – This is a generic server error.
    It probably shouldn’t be thrown explicitly.
    - 502 Bad Gateway – This indicates an invalid response from an upstream server.
    - 503 Service Unavailable – This indicates that something unexpected happened on server side
    (It can be anything like server overload, some parts of the system failed, etc.).

"""
from flask import json
from werkzeug.exceptions import InternalServerError, NotFound, Forbidden, \
    BadRequest, BadGateway, Unauthorized, ServiceUnavailable

from FlaskAPI import app


@app.errorhandler(Forbidden)
def forbidden_error_403(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(Unauthorized)
def unauthorized_error_401(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(InternalServerError)
def internal_server_error_500(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(NotFound)
def not_found_error_404(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(BadGateway)
def bad_gateway_error_502(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(ServiceUnavailable)
def service_unavailable_error_503(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(BadRequest)
def bad_request_error_400(e):
    response = e.get_response()
    response.data = json.dumps({
        "status_code": e.code,
        "status": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
