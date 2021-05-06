# -*- coding: utf-8 -*-
"""
This is the module where you can get the status code of
the API response & you can also modify the API response format.
"""

from rest_framework import status

# -----------------------------------------------------------------------------


def get_status(code):
    """Get the human readable SNAKE_CASE version of a status code."""
    for name, val in status.__dict__.items():
        if not callable(val) and code is val:
            return name.replace("HTTP_%s_" % code, "")
    return "UNKNOWN"


def modify_api_response(response):
    """
    Modify API response format.
    Example success:
    {
        "code": 200,
        "status": "OK",
        "data": {
            "username": "username"
        }
    }

    Example error:
    {
        "code": 404,
        "status": "NOT_FOUND",
        "errors": [
            {
                "title": "detail",
                "detail": "Not found."
            }
        ]
    }
    """
    modified_data = {}
    modified_data["code"] = response.status_code

    if response.data.get("errors"):
        modified_data["status"] = "FAIL"
        modified_data["message"] = response.data.get("errors")[0].get("detail")
        modified_data["data"] = []

    else:
        if response.data.get("status") is None:
            modified_data["status"] = "OK"
        else:
            modified_data["status"] = response.data.get("status")
        modified_data["message"] = response.data.get("message")
        modified_data["data"] = response.data.get("data")

    response.data = modified_data
    return response
