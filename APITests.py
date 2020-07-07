import requests

BASE_URL = "https://reqres.in/"
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


def get_all_users():
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/users"
    url = BASE_URL + relative_url
    response = requests.request("GET", url, headers=HEADERS)
    number_of_users = response.json()['total']
    response_status_code = response.status_code
    return response_status_code, number_of_users


def get_single_user(user_id):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/users/" + str(user_id)
    url = BASE_URL + relative_url
    response = requests.request("GET", url, headers=HEADERS)
    received_id = (response.json()['data'])['id']
    return response.status_code, received_id


def single_user_not_found(user_id):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/users/" + str(user_id)
    url = BASE_URL + relative_url
    response = requests.request("GET", url, headers=HEADERS)
    print(response.status_code)
    return response.status_code


def create_user(Name, Job):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/users"
    url = BASE_URL + relative_url
    data = {'name': Name, 'job': Job}
    response = requests.request("POST", url, json=data, headers=HEADERS)
    created_name = response.json()['name']
    created_job = response.json()['job']
    response_status = response.status_code
    return created_name, created_job, response_status


def update_user(ID, Name, Job):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/users/"
    url = BASE_URL + relative_url + str(ID)
    data = {'name': Name, 'job': Job}
    response = requests.request("PUT", url, headers=HEADERS, json=data)
    updated_name = response.json()['name']
    updated_job = response.json()['job']
    return updated_name, updated_job


def delete_user(Id):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/users/"
    url = BASE_URL + relative_url + str(Id)
    response = requests.request("DELETE", url, headers=HEADERS)
    return response.status_code


def successful_registration(Email, Passsword):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/register"
    url = BASE_URL + relative_url
    data = {'email': Email, 'password': Passsword}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    return response.status_code


def unsuccessful_registration(Email, Passsword):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/register"
    url = BASE_URL + relative_url
    data = {'email': Email, 'password': Passsword}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    return response.status_code


def successful_login(Email, Passsword):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/login"
    url = BASE_URL + relative_url
    data = {'email': Email, 'password': Passsword}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    return response.status_code


def unsuccessful_login(Email, Passsword):
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    relative_url = "api/login"
    url = BASE_URL + relative_url
    data = {'email': Email, 'password': Passsword}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    return response.status_code


def delayed_response():
    """
          Documentation: Takes a value such as a string to search against a regular expression.
          To search for a specific regex value input into exp_value, set "escape_regex_chars" to False:
          escape_regex_chars=False.
    """
    url = BASE_URL + "api/users?delay=3"
    response = requests.get(url, headers=HEADERS)
    number_of_users = response.json()['total']
    response_status_code = response.status_code
    return response_status_code, number_of_users
