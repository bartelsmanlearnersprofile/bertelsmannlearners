class SampleData:
    """
    Class to pass mock data
    """

    single_return_success_data = {
        "status": "success",
        "status_code": 200,
        "data": {
            "firstname": "George",
            "lastname": "Udosen",
            "slackname": "udoyen"
        }
    }
    multiple_return_success_data = {
        "status": "success",
        "status_code": 200,
        "data": [
            {
                "firstname": "George",
                "lastname": "Udosen",
                "slackname": "udoyen"
            },
            {
                "firstname": "Kenneth",
                "lastname": "Udosen",
                "slackname": "nicce"
            },
            {
                "firstname": "Koo",
                "lastname": "Udosen",
                "slackname": "udoyen1"
            },
            {
                "firstname": "David",
                "lastname": "Ekanem",
                "slackname": "mowa"
            },
        ]
    }

    unauthorized = {
        "status": "failure",
        "status_code": 401,
    }

    internal_server_error = {
        "status": "failure",
        "status_code": 500
    }
    bad_gateway = {
        "status": "failure",
        "status_code": 502
    }
    service_unavailable = {
        "status": "failure",
        "status_code": 503
    }

    bad_request = {
        "status": "failure",
        "status_code": 400
    }
    not_found = {
        "status": "success",
        "status_code": 404,
        "data": []
    }

    user_data = [
        {
            "firstname": "George",
            "lastname": "Udosen",
            "slackname": "udoyen"
        },
        {
            "firstname": "Kenneth",
            "lastname": "Udosen",
            "slackname": "nicce"
        },
        {
            "firstname": "Koo",
            "lastname": "Udosen",
            "slackname": "udoyen1"
        },
        {
            "firstname": "David",
            "lastname": "Ekanem",
            "slackname": "mowa"
        },
    ]
