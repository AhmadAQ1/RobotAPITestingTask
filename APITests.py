import requests

BASE_URL = "https://reqres.in/"  # This is the base URL used for all requests
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


def get_all_users():
    """
          Documentation: This function uses the provided url to send an API request
          using python's requests library (GET method). It should return the json data that contains
          the specific data you are hoping to find. This function only returns the data with
          the given path you provide (in tuple format).

          returns:
            response_status_code: The response status of the request
            number_of_users: total number of users in the database
    """
    relative_url = "api/users"
    url = BASE_URL + relative_url
    response = requests.request("GET", url, headers=HEADERS)  # Stores the response
    number_of_users = response.json()['total']  # returns total number of users in the database
    response_status_code = response.status_code
    return response_status_code, number_of_users


def get_single_user(user_id):
    """
          Documentation: This function uses the provided user_id to send an API request
          using python's requests library (GET method). It should return the json data
          that contains the specific data you are hoping to find. This function only returns the data with
          the given path you provide (in tuple format).

          parameters:
            user_id: The id of the user to use as an endpoint.

          returns:
            received_id: The received id from the response.
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users/" + str(user_id)
    url = BASE_URL + relative_url
    response = requests.request("GET", url, headers=HEADERS)
    received_id = (response.json()['data'])['id']
    response_status_code = response.status_code
    return response_status_code, received_id


def single_user_not_found(user_id):
    """
          Documentation: This function uses the provided user_id to send an API request
          using python's requests library (GET method). It should return the json data
          that contains the specific data you are hoping to find. This function only returns
          the data with the given path you provide (in tuple format).

          parameters:
            user_id: The id of the user to use as an endpoint.

          returns:
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users/" + str(user_id)
    url = BASE_URL + relative_url
    response = requests.request("GET", url, headers=HEADERS)
    print(response.status_code)
    return response.status_code


def create_user(user_name, user_job):
    """
          Documentation: This function uses the provided user_name and user_job post a request
          using python's requests library (POST request). It Creates a new user with the given
          parameters.This function only returns the data in tuple format.

          parameters:
            user_name:  The new user name to create for a user
            user_job:   The new job to create for a user

          returns:
            created_name: The received name from the response after posting the request.
            created_job: The received job from the response after posting the request.
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users"
    url = BASE_URL + relative_url
    data = {'name': user_name, 'job': user_job}
    response = requests.request("POST", url, json=data, headers=HEADERS)
    created_name = response.json()['name']
    created_job = response.json()['job']
    response_status = response.status_code
    return created_name, created_job, response_status


def update_user(ID, user_name, user_job):
    """
          Documentation: This function uses the provided user ID to update the specific user
          using python's requests library (PUT method). It updates the specific user with the given parameters.
          This function returns the response data (name, job) from the request in tuple format.

          parameters:
            ID:  The specific user id to updates his data
            user_name:  The new user name to create for a user
            user_job:   The new job to create for a user

          returns:
            updated_name: The updated name from the response after posting the request.
            updated_job: The updated job from the response after posting the request.
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users/"
    url = BASE_URL + relative_url + str(ID)
    data = {'name': user_name, 'job': user_job}
    response = requests.request("PUT", url, headers=HEADERS, json=data)
    updated_name = response.json()['name']
    updated_job = response.json()['job']
    response_status = response.status_code
    return updated_name, updated_job, response_status


def delete_user(Id):
    """
          Documentation: This function uses the provided user ID to delete a specific user
          using python's requests library (DELETE method). This function returns the response
          status data.

          parameters:
            ID:  The specific user id to delete.

          returns:
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users/"
    url = BASE_URL + relative_url + str(Id)
    response = requests.request("DELETE", url, headers=HEADERS)
    return response.status_code


def successful_registration(user_email, user_password):
    """
          Documentation: This function uses the provided user user_email and user_password to register
          using python's requests library (POST method). It sends email, password details.This function
          returns the response data (registration id,registration token, response status code) from the
          request in tuple format.

          parameters:
            user_email: The user email for registration
            user_password: The user password for registration

          returns:
            created_id: The response id created from registration request.
            created_token: The response token created from registration request.
            response_status_code: Response status code from registration request.
    """
    relative_url = "api/register"
    url = BASE_URL + relative_url
    data = {'email': user_email, 'password': user_password}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    created_id = response.json()['id']
    created_token = response.json()['token']
    return created_id, created_token, response.status_code


def unsuccessful_registration(user_email, user_password):
    """
          Documentation: This function uses the provided user user_email and user_password to register
          using python's requests library (POST method). It sends email, password details.This function
          returns the response data (response status code) from the request.

          parameters:
            user_email: The user email for registration
            user_password: The user password for registration

          returns:
            response_status_code: Response status code from registration request.
    """
    relative_url = "api/register"
    url = BASE_URL + relative_url
    data = {'email': user_email, 'password': user_password}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    return response.status_code


def successful_login(user_email, user_password):
    """
          Documentation: This function uses the provided user user_email and user_password to login
          using python's requests library (POST method). It sends email, password details.This function
          returns the response data (login token, response status code) from the request in tuple format.

          parameters:
            user_email: The user email for login
            user_password: The user password for login

          returns:
            response_token: The response token from login request.
            response_status_code: Response status code from registration request.
    """
    relative_url = "api/login"
    url = BASE_URL + relative_url
    data = {'email': user_email, 'password': user_password}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    response_token = response.json()['token']
    return response_token, response.status_code


def unsuccessful_login(Email, Passsword):
    """
          Documentation: This function uses the provided user user_email and user_password to login
          using python's requests library (POST method). It sends email, password details.This function
          returns the response data (response status code) from the reques.

          parameters:
            user_email: The user email for login
            user_password: The user password for login

          returns:
            response_status_code: Response status code from registration request.
    """
    relative_url = "api/login"
    url = BASE_URL + relative_url
    data = {'email': Email, 'password': Passsword}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    return response.status_code


def delayed_response():
    """
          Documentation: This function uses the url to send an API request
          using python's requests library (GET request). It should return the json data
          that contains the specific data you are hoping to find. This
          function only returns the data with the given path you provide (in tuple format).

          returns:
            response_status_code: The response status of the request
            number_of_users: total number of users in the database
    """
    url = BASE_URL + "api/users?delay=3"
    response = requests.get(url, headers=HEADERS)
    number_of_users = response.json()['total']
    response_status_code = response.status_code
    return response_status_code, number_of_users
