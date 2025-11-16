def wrap_responses_in_base_format(result, generator, request, public):
    components = result.get("components", {})

    for path, methods in result.get("paths", {}).items():
        for method, operation in methods.items():
            responses = operation.get("responses", {})
            for status_code, response in responses.items():
                content = response.get("content")
                if not content:
                    continue

                for media_type, media_obj in content.items():
                    schema = media_obj.get("schema", {})

                    # Skip if it's already wrapped
                    if (
                        isinstance(schema, dict)
                        and schema.get("properties", {}).get("success") is not None
                    ):
                        continue

                    wrapped = {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "success": {"type": "boolean"},
                                    "data": schema,
                                    "error": {"type": "string", "nullable": True},
                                    "user_error": {"type": "string", "nullable": True},
                                },
                                "required": ["success", "data", "error", "user_error"],
                            }
                        ]
                    }

                    content[media_type]["schema"] = wrapped

    return result
