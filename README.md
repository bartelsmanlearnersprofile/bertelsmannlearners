# bartelsmannlearners

## Flask API Project

### Notes: The included database file app.db should be deleted before being used.

- purpose: Side project for the bartelsmann udacity scholarship program 2020
- requirements: 
  - sqlite3
  - requirements.txt file contents 
- Use:
  
  > To be used to store and retrieve learners information from other projects
  > 
  > Use as a backend service
  
- Usage:
   - API endpoints list:
     ```
     - GET: # return: json, format: {'status': 'success|failure, 'status_code': code, 'data': '[]|[{students_info}]}
      - /api/v1.0/learners/students/all
      - /api/v1.0/learners/student/slackname/<string:slackname>
      - /api/v1.0/learners/student?firstname=[string] # Not implemented 
      - /api/v1.0/learners/student?lastname=[string]  # Not implemented
     - POST: # return: json, format: {'status': 'success|failure, 'status_code': code, 'data': '[]|[{students_info}]}
      - /api/v1.0/learners/students # payload is json
     - DELETE: # return: json, format: {'status': 'success|failure, 'status_code': code, 'data': '[]|[{students_info}]}
      - /api/v1.0/learners/student/delete/<string:slackname>
     - PUT: # return: json, format: {'status': 'success|failure, 'status_code': code, 'data': '[]|[{students_info}]}
       - /api/v1.0/learners/student/update/<string:slackname> # payload is json
     
     ``` 
     
   - Basic usage (Base Url, /api/v1.0/learners:
        - Get all learners:
          > GET :: /students/all
          > 
          > Response: Json
          
        - Get specific learners:
          > GET :: /student/slackname/<string:slackname>
          > 
          > Response: Json          

       - Add users to the database
         
           > POST :: /students
           > 
           > Body sent in json format:
         
          ```
           {
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

 
          ```
          > Response: Entered data in json format
    
       - Update a learners's information
         
          > PUT :: /student/update/<string:slackname>
          > Body sent in json format
         
            ```
            {
                'data': [
                    {
                        'firstname': 'Joseph',
                        'lastname': 'Udosen'
                    }
                ]
            }

            ```
          >
          > Response: Json
         
       - Delete a learner from the database
         
          > DELETE :: /student/delete/<string:slackname>
          >  
          > Response: Json