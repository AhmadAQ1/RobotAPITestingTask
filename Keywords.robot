*** Settings ***
Library  APITests.py

*** Variables ***
${STATUS_CODE_OK}  200
${STATUS_CODE_CREATED}  201
${STATUS_CODE_NO_CONTENT}  204
${STATUS_CODE_BAD_REQUEST}  400
${STATUS_CODE_NOT_FOUND}  404
${TOTAL_NUMBER_OF_USERS}  12
*** Keywords ***
Get All Users Test
    ${response_code}  ${users_total}  get all users
    should be equal as integers  ${response_code}  ${STATUS_CODE_OK}
    should be equal as integers  ${users_total}  ${TOTAL_NUMBER_OF_USERS}

Get A Specific User Test
    ${id}=  Evaluate  random.randint(1, 12)  modules=random
    ${recived_response}  ${sent_id}   get single user  ${id}
    should be equal as integers  ${recived_response}  ${STATUS_CODE_OK}
    should be equal as integers  ${id}  ${sent_id}

single user not found Test
    ${id}=  Evaluate  random.randint(13, 100)  modules=random
    ${recived_response}  single user not found  ${id}
    should be equal as integers  ${recived_response}  ${STATUS_CODE_NOT_FOUND}

Create a New User and Verify it was created
    ${created_name}  set variable  ahmad
    ${created_job}  set variable  Actor
    ${new_user_name}  ${new_user_job}  ${response_status}  create user  ${created_name}  ${created_job}
    should be equal as integers  ${response_status}  ${STATUS_CODE_CREATED}
    should be equal as strings  ${created_name}   ${new_user_name}
    should be equal as strings  ${created_job}   ${new_user_job}

Update User and Verify it has been updated
    ${user_ID}  Evaluate  random.randint(1, 12)  modules=random
    ${new_name}  set variable  ahmad
    ${new_job}  set variable  Actor
    ${updated_user_name}  ${updated_user_job}   update user  ${user_ID}  ${new_name}  ${new_job}
    should be equal as strings  ${new_name}   ${updated_user_name}
    should be equal as strings  ${new_job}   ${updated_user_job}


Delete User and Verify it Has been Deleted
     ${User_ID}=  Evaluate  random.randint(1, 12)  modules=random
     ${received_response}  delete user  ${User_ID}
     should be equal as integers  ${received_response}  ${STATUS_CODE_NO_CONTENT}

Successfull Registration Test
    ${user_email}=  set variable  eve.holt@reqres.in
    ${password}=  set variable  qwerty
    ${verify_successful_registration}  successful registration  ${user_email}  ${password}
    should be equal as integers  ${verify_successful_registration}  ${STATUS_CODE_OK}

UnSuccessfull Registration Test
    ${user_email}  set variable  ahmad@reqers.in
    ${password}  set variable  qwerty
    ${verify_unSuccessful_registration}  unsuccessful registration  ${user_email}  ${password}
    should be equal as integers  ${verify_unSuccessful_registration}  ${STATUS_CODE_BAD_REQUEST}

Successfull Login Test
    ${user_email}  set variable  eve.holt@reqres.in
    ${password}  set variable  qwerty
    ${verify_Successful_Login}  successful login  ${user_Email}  ${password}
    should be equal as integers  ${verify_successful_login}  ${STATUS_CODE_OK}

UnSuccessfull login Test
    ${user_Email}  set variable  ahmad@reqers.in
    ${password}  set variable  qwerty
    ${verify_unSuccessful_Login}  unsuccessful login  ${user_Email}  ${password}
    should be equal as integers  ${verify_unSuccessful_login}  ${STATUS_CODE_BAD_REQUEST}

delayed response test
    ${recived_response}  ${users_total}  delayed response
    should be equal as integers  ${recived_response}  ${STATUS_CODE_OK}
    should be equal as integers  ${users_total}  ${TOTAL_NUMBER_OF_USERS}
