*** Settings ***
Library  APITests.py

*** Variables ***
${STATUS_CODE_OK}  200
${STATUS_CODE_CREATED}  201
${STATUS_CODE_NO_CONTENT}  204
${STATUS_CODE_BAD_REQUEST}  400
${STATUS_CODE_NOT_FOUND}  404
${TOTAL_NUMBER_OF_USERS}  6    # total number of users in a page
*** Keywords ***
Get All Users In A Page
    [Tags]    GET
    [Documentation]
    ...    Calls the API to return the response status code and total number of users.
    ...    Expected result is the API returns a code 200 success and 6 total users.
    ${page_number}  Evaluate  random.randint(1, 2)  modules=random
    ${response_code}  ${total_users_in_page}  get users in page  ${page_number}
    should be equal as integers  ${response_code}  ${STATUS_CODE_OK}
    should be equal as integers  ${total_users_in_page}  ${TOTAL_NUMBER_OF_USERS}

Get A Specific User Test
    [Tags]    GET
    [Documentation]
    ...    Calls the API to return the response status code and reponse user id.
    ...    Expected result is the API returns 200 status code success and the user id from the response.
    ${id}  Evaluate  random.randint(1, 12)  modules=random     #generates a random ID between 1 - 12
    ${recived_response}  ${sent_id}   get single user  ${id}
    should be equal as integers  ${recived_response}  ${STATUS_CODE_OK}
    should be equal as integers  ${id}  ${sent_id}

Single User Not Found Test
    [Tags]    GET
    [Documentation]
    ...    Calls the API to return the response status code.
    ...    Expected result is the API returns 404 status code not found.
    ${id}  Evaluate  random.randint(13, 100)  modules=random   #generates a random ID between 13 - 100
    ${recived_response}  single user not found  ${id}
    should be equal as integers  ${recived_response}  ${STATUS_CODE_NOT_FOUND}

Create A New User And Verify It Was Created
    [Tags]    POST
    [Documentation]
    ...    Calls the API to return the response status code (CREATED) name and job from the response body.
    ...    Expected result is the API returns 201 status code (CREATED) . name, job of the sent request should
    ...    be the same from the response data.
    ${created_name}  set variable  ahmad
    ${created_job}  set variable  Actor
    ${new_user_name}  ${new_user_job}  ${response_status}  create user  ${created_name}  ${created_job}
    should be equal as integers  ${response_status}  ${STATUS_CODE_CREATED}
    should be equal as strings  ${created_name}   ${new_user_name}
    should be equal as strings  ${created_job}   ${new_user_job}

Update User And Verify It Has Been Updated
    [Tags]    PUT
    [Documentation]
    ...    Calls the API to return the response status code, updated name and job from the response body.
    ...    Expected result is the API returns 200 status code OK. name, job of the sent request should be
    ...    the same from the response data.
    ${user_ID}  Evaluate  random.randint(1, 12)  modules=random     #generates a random ID between 1 - 12
    ${new_name}  set variable  ahmad
    ${new_job}  set variable  Actor
    ${updated_user_name}  ${updated_user_job}   ${received_status}   update user  ${user_ID}  ${new_name}  ${new_job}
    should be equal as integers  ${received_status}  ${STATUS_CODE_OK}
    should be equal as strings  ${new_name}   ${updated_user_name}
    should be equal as strings  ${new_job}   ${updated_user_job}


Delete User And Verify It Has been Deleted
    [Tags]    POST
    [Documentation]
    ...    Calls the API to return the response status code NO CONTENT.
    ...    Expected result is the API returns 204 status code NO CONTENT.
     ${User_ID}=  Evaluate  random.randint(1, 12)  modules=random
     ${received_response}  delete user  ${User_ID}
     should be equal as integers  ${received_response}  ${STATUS_CODE_NO_CONTENT}

Successfull Registration Test
    [Tags]    POST
    [Documentation]
    ...    Calls the API to return the response status code (OK) , created id and token.
    ...    Expected result is the API returns 200 status code (OK) , an id and token for successfull registration.
    ${user_email}  set variable  eve.holt@reqres.in
    ${password}  set variable  qwerty
    ${created_id}   ${created_token}   ${verify_successful_registration}  successful registration  ${user_email}  ${password}
    variable should exist  ${created_id}
    should not be empty  ${created_token}
    should be equal as integers  ${verify_successful_registration}  ${STATUS_CODE_OK}

UnSuccessfull Registration Test
    [Tags]    POST
    [Documentation]
    ...    Calls the API to return the response status code (BAD REQUEST).
    ...    Expected result is the API returns 400 status code (BAD REQUEST).
    ${user_email}  set variable  ahmad@reqers.in
    ${password}  set variable  qwerty
    ${verify_unSuccessful_registration}  unsuccessful registration  ${user_email}  ${password}
    should be equal as integers  ${verify_unSuccessful_registration}  ${STATUS_CODE_BAD_REQUEST}

Successfull Login Test
    [Tags]    POST
    [Documentation]
    ...    Calls the API to return the response status code (OK) and token.
    ...    Expected result is the API returns 200 status code (OK) and token for successfull login.
    ${user_email}  set variable  eve.holt@reqres.in
    ${password}  set variable  qwerty
    ${response_token}   ${verify_Successful_Login}  successful login  ${user_Email}  ${password}
    should not be empty  ${response_token}
    should be equal as integers  ${verify_successful_login}  ${STATUS_CODE_OK}

UnSuccessfull login Test
    [Tags]    POST
    [Documentation]
    ...    Calls the API to return the response status code (BAD REQUEST).
    ...    Expected result is the API returns 400 status code (BAD REQUEST).
    ${user_Email}  set variable  ahmad@reqers.in
    ${password}  set variable  qwerty
    ${verify_unSuccessful_Login}  unsuccessful login  ${user_Email}  ${password}
    should be equal as integers  ${verify_unSuccessful_login}  ${STATUS_CODE_BAD_REQUEST}

Delayed Response Test
    [Tags]    GET
    [Documentation]
    ...    Calls the API to return the response status code (OK) and total number of users in a page.
    ...    Expected result is the API returns a code 200 success (OK) and 6 total users.
    ${recived_response}  ${users_total}  delayed response
    should be equal as integers  ${recived_response}  ${STATUS_CODE_OK}
    should be equal as integers  ${users_total}  ${TOTAL_NUMBER_OF_USERS}
