from typing import Any

from rest_framework.renderers import JSONRenderer


def base_response(status:int, data: Any = None, success: bool = True, error: Any = "", user_error: Any=""):
    return {
        "success": success,
        "status": status,
        "error": error,
        "user_error": user_error,
        "data": data
    }


class BaseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get("response", None)

        if data is None:
            data = {}

        if isinstance(data, dict) and "success" in data and "data" in data:
            final_data = data
        else:
            success = True
            status = 200
            if response is not None and response.status_code >= 400:
                success = False
            if response is not None:
                status = response.status_code
                response.status_code = 200
            final_data = base_response(
                success=success,
                status=status,
                error=None if success else str(data),
                user_error=None if success else str(data),
                data=data if success else None,
                )

        return super().render(final_data, accepted_media_type, renderer_context)