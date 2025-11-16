from rest_framework.response import Response
from rest_framework.views import exception_handler
from core.base.renderers import base_response

def base_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = base_response(
            success=False,
            status=exc.status_code,
            error=str(exc),
            user_error=getattr(exc, "detail", "Something went wrong"),
            data=None,
        )
        response.status_code = 200
        return response

    return Response(
        base_response(
            success=False,
            status=exc.status_code,
            error=str(exc),
            user_error="Unexpected server error",
            data=None,
        ),
        status=200
    )
