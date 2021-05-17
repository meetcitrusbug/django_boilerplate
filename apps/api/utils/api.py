def modify_api_response(response):
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
