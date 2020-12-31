class SampleData:
    """
    Class to pass mock data
    """

    single_return_success_data = {
        "status": "success",
        "status_code": 200,
        "data": [{
            "firstname": "George",
            "lastname": "Udosen",
            "slackname": "udoyen"
        }]
    }
    multiple_return_success_data = {
        "status": "success",
        "status_code": 200,
        "total": 4,
        "data": [
            {
                "firstname": "George",
                "lastname": "Udosen",
                "slackname": "udoyen24"
            },
            {
                "firstname": "Kenneth",
                "lastname": "Udosen",
                "slackname": "nicce2"
            },
            {
                "firstname": "Koo",
                "lastname": "Udosen",
                "slackname": "udoyen11"
            },
            {
                "firstname": "David",
                "lastname": "Ekanem",
                "slackname": "mowa2"
            },
        ]
    }

    database_initialization_success_return = {
        "status": "success",
        "status_code": 200,
        "data": [
            {
                "id": 1,
                "firstname": "George",
                "lastname": "Udosen",
                "slackname": "udoyen"
            },
            {
                "id": 2,
                "firstname": "Kenneth",
                "lastname": "Udosen",
                "slackname": "nicce"
            },
            {
                "id": 3,
                "firstname": "Koo",
                "lastname": "Udosen",
                "slackname": "udoyen1"
            },
            {
                "id": 4,
                "firstname": "David",
                "lastname": "Ekanem",
                "slackname": "mowa"
            },
        ]
    }

    slacknames = [
        'udoyen',
        'nicce',
        'udoyen1',
        'mowa'
    ]

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
        "status": "failure",
        "status_code": 404,
        "data": []
    }

    user_data = {
        "data": [
            {
                "firstname": "George",
                "lastname": "Udosen",
                "slackname": "udoyen24"
            },
            {
                "firstname": "Kenneth",
                "lastname": "Udosen",
                "slackname": "nicce2"
            },
            {
                "firstname": "Koo",
                "lastname": "Udosen",
                "slackname": "udoyen11"
            },
            {
                "firstname": "David",
                "lastname": "Ekanem",
                "slackname": "mowa2"
            },
        ]
    }

    user_update_data = {
        'data': [
            {
                'firstname': 'Joseph',
                'lastname': 'Udosen'
            }
        ]
    }

    invalid_user_data_update_failure = {
        'slackname': 'udoyen',
        'data': [
            {
                'firstname': 'Joseph',
                'lastname': 'Udosen',
                'set': 'erw'
            }
        ]
    }

    multiple_user_update_data = {
        'slackname': 'udoyen',
        'data': [
            {
                'firstname': 'Joseph',
                'lastname': 'Udosen'
            },
            {
                'firstname': 'Joseph',
                'lastname': 'Udosen'
            }
        ]
    }

