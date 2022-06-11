# rainmaker_api_client.UserApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forgotpassword**](UserApi.md#forgotpassword) | **PUT** /{version}/forgotpassword | Handle forgot password request from the user
[**forgotpassword_mobile**](UserApi.md#forgotpassword_mobile) | **PUT** /{version}/forgotpassword2 | Handle forgot password request from the user
[**get_user**](UserApi.md#get_user) | **GET** /{version}/user | Fetches the details of current user
[**get_user_mobile**](UserApi.md#get_user_mobile) | **GET** /{version}/user2 | Fetches the details of current user
[**login**](UserApi.md#login) | **POST** /{version}/login | Handle login or extend session request from the user
[**login2**](UserApi.md#login2) | **POST** /{version}/login2 | Handle login or extend session request from the user
[**logout**](UserApi.md#logout) | **POST** /{version}/logout | Log out user from the session
[**password**](UserApi.md#password) | **PUT** /{version}/password | Handle password change request from the user
[**password_mobile**](UserApi.md#password_mobile) | **PUT** /{version}/password2 | Handle password change request from the user
[**userattributeupdate**](UserApi.md#userattributeupdate) | **PUT** /{version}/user2 | Updates Name and Phone number of the user
[**usercreation**](UserApi.md#usercreation) | **POST** /{version}/user | Creates the new user or confirms the user
[**usercreation_mobile**](UserApi.md#usercreation_mobile) | **POST** /{version}/user2 | Creates the new user or confirms the user. The user can specify his email address or the mobile number with country code for creating his account.
[**userdeletion**](UserApi.md#userdeletion) | **DELETE** /{version}/user | Deletes user account
[**userdeletion_mobile**](UserApi.md#userdeletion_mobile) | **DELETE** /{version}/user2 | Deletes user account
[**usernameupdate**](UserApi.md#usernameupdate) | **PUT** /{version}/user | Updates Name of the user

# **forgotpassword**
> APISuccessResponse forgotpassword(body, version)

Handle forgot password request from the user

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
body = rainmaker_api_client.VersionForgotpasswordBody() # VersionForgotpasswordBody | password change request parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Handle forgot password request from the user
    api_response = api_instance.forgotpassword(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->forgotpassword: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionForgotpasswordBody**](VersionForgotpasswordBody.md)| password change request parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgotpassword_mobile**
> APISuccessResponse forgotpassword_mobile(body, version)

Handle forgot password request from the user

This api handles forgot password request from the user

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
body = rainmaker_api_client.VersionForgotpassword2Body() # VersionForgotpassword2Body | password change request parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Handle forgot password request from the user
    api_response = api_instance.forgotpassword_mobile(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->forgotpassword_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionForgotpassword2Body**](VersionForgotpassword2Body.md)| password change request parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserResponse get_user(version, custom_data=custom_data)

Fetches the details of current user

This API fetches user_id, user_name, super_admin flag, URL of profile picture and name of current user. <br><br>The <b>super_admin</b> flag is returned only when the user is a super admin, in other cases, it will not be returned in the output. <br>Also the <b>picture_url</b> and <b>name</b> are not returned in the output, if it is not set by the user.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
custom_data = false # bool | When true, will fetch the custom data of the logged in user (optional) (default to false)

try:
    # Fetches the details of current user
    api_response = api_instance.get_user(version, custom_data=custom_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **custom_data** | **bool**| When true, will fetch the custom data of the logged in user | [optional] [default to false]

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_mobile**
> GetUserResponse get_user_mobile(version, custom_data=custom_data)

Fetches the details of current user

This API fetches user_id, user_name, super_admin flag, URL of profile picture and name of current user. <br><br>The <b>super_admin</b> flag is returned only when the user is a super admin, in other cases, it will not be returned in the output. <br>Also the <b>picture_url</b> and <b>name</b> are not returned in the output, if it is not set by the user.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
custom_data = false # bool | When true, will fetch the custom data of the logged in user containing</b>. (optional) (default to false)

try:
    # Fetches the details of current user
    api_response = api_instance.get_user_mobile(version, custom_data=custom_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **custom_data** | **bool**| When true, will fetch the custom data of the logged in user containing&lt;/b&gt;. | [optional] [default to false]

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> InlineResponse200 login(body, version)

Handle login or extend session request from the user

This API will be used by the users to Login to RainMaker or to extend an existing session

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
body = rainmaker_api_client.VersionLoginBody() # VersionLoginBody | username and password for Login
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Handle login or extend session request from the user
    api_response = api_instance.login(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionLoginBody**](VersionLoginBody.md)| username and password for Login | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login2**
> InlineResponse2001 login2(body, version)

Handle login or extend session request from the user

This API will be used by the users to Login to RainMaker or to extend an existing session <br>If MFA is enabled, then an SMS will be sent to the phone number after authentication with password. Then, verifying the code and session will lead to successful login of the user.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
body = rainmaker_api_client.VersionLogin2Body() # VersionLogin2Body | username and password for Login
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Handle login or extend session request from the user
    api_response = api_instance.login2(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionLogin2Body**](VersionLogin2Body.md)| username and password for Login | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> APISuccessResponse logout(version, logout_all=logout_all)

Log out user from the session

This API will be used by the users to Logout from Rainmaker session

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
logout_all = 'false' # str | Using this flag the user can be logged out from all sessions or only current session. The possible values are true and false. (optional) (default to false)

try:
    # Log out user from the session
    api_response = api_instance.logout(version, logout_all=logout_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **logout_all** | **str**| Using this flag the user can be logged out from all sessions or only current session. The possible values are true and false. | [optional] [default to false]

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password**
> APISuccessResponse password(body, version)

Handle password change request from the user

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.PasswordChangeRequest() # PasswordChangeRequest | Password change request parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Handle password change request from the user
    api_response = api_instance.password(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)| Password change request parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_mobile**
> APISuccessResponse password_mobile(body, version)

Handle password change request from the user

This api handles password change request from the user

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.PasswordChangeRequest() # PasswordChangeRequest | Password change request parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Handle password change request from the user
    api_response = api_instance.password_mobile(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->password_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)| Password change request parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userattributeupdate**
> APISuccessResponse userattributeupdate(body, version)

Updates Name and Phone number of the user

This API sets or updates the name or phone number of the user. <br><br> MFA can also be enabled / disabled for superadmins. If MFA is enabled, an SMS with verification code is sent to the superadmin's phone number after initial authentication for successful login. <br><br><b>Note:</b> <ul><li>The verification_code will confirm the current phone_number.<li>At any point there can be just one phone number associated with the user. Adding a new phone number will replace the existing one and require reverification. <li>The MFA settings will reflect from the next login onwards.</ul>

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.VersionUser2Body() # VersionUser2Body | Request body for updating name / phone number of the user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Updates Name and Phone number of the user
    api_response = api_instance.userattributeupdate(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->userattributeupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionUser2Body**](VersionUser2Body.md)| Request body for updating name / phone number of the user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usercreation**
> APISuccessResponse usercreation(body, version)

Creates the new user or confirms the user

This API creates a new user or confirms the user. If the password is specified in the request body, a new user is created and a verification code is sent to user's mail address. If the verification code is sent in the request body, the user is confirmed.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
body = rainmaker_api_client.VersionUserBody() # VersionUserBody | Request body for creating new user or confirming the user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Creates the new user or confirms the user
    api_response = api_instance.usercreation(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->usercreation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionUserBody**](VersionUserBody.md)| Request body for creating new user or confirming the user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usercreation_mobile**
> APISuccessResponse usercreation_mobile(body, version)

Creates the new user or confirms the user. The user can specify his email address or the mobile number with country code for creating his account.

This API creates a new user or confirms the user. If the password is specified in the request body, a new user is created and a verification code is sent to user's mail address/phone number. If the verification code is sent in the request body, the user is confirmed.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi()
body = rainmaker_api_client.VersionUser2Body1() # VersionUser2Body1 | Request body for creating new user or confirming the user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Creates the new user or confirms the user. The user can specify his email address or the mobile number with country code for creating his account.
    api_response = api_instance.usercreation_mobile(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->usercreation_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionUser2Body1**](VersionUser2Body1.md)| Request body for creating new user or confirming the user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userdeletion**
> APISuccessResponse userdeletion(version, request=request, verification_code=verification_code)

Deletes user account

This API can be used by end-users to delete his/her account. Here are the details- <ul> <li> If the 'request' query param is true, user delete request is initiated and verification code is sent to user using email or phone number. <li>If 'verification_code' query param is specified, user account is deleted.</ul>

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request = false # bool | if delete user request is to be initiated, value of request param should be true. (optional) (default to false)
verification_code = 1.2 # float | if delete user request is to be verified and user account is to be deleted, the verification code received by user should be entered as value of verification_code query param. (optional)

try:
    # Deletes user account
    api_response = api_instance.userdeletion(version, request=request, verification_code=verification_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->userdeletion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request** | **bool**| if delete user request is to be initiated, value of request param should be true. | [optional] [default to false]
 **verification_code** | **float**| if delete user request is to be verified and user account is to be deleted, the verification code received by user should be entered as value of verification_code query param. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userdeletion_mobile**
> APISuccessResponse userdeletion_mobile(version, request=request, verification_code=verification_code)

Deletes user account

This API can be used by end-users to delete his/her account. Here are the details- <ul> <li> If the 'request' query param is true, user delete request is initiated and verification code is sent to user using email or phone number. <li>If 'verification_code' query param is specified, user account is deleted.</ul>

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request = false # bool | if delete user request is to be initiated, value of request param should be true. (optional) (default to false)
verification_code = 1.2 # float | if delete user request is to be verified and user account is to be deleted, the verification code received by user should be entered as value of verification_code query param. (optional)

try:
    # Deletes user account
    api_response = api_instance.userdeletion_mobile(version, request=request, verification_code=verification_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->userdeletion_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request** | **bool**| if delete user request is to be initiated, value of request param should be true. | [optional] [default to false]
 **verification_code** | **float**| if delete user request is to be verified and user account is to be deleted, the verification code received by user should be entered as value of verification_code query param. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usernameupdate**
> APISuccessResponse usernameupdate(body, version)

Updates Name of the user

This API Sets or updates the name of the user.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = rainmaker_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rainmaker_api_client.UserApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdateNameRequest() # UpdateNameRequest | Request body for updating name of the user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Updates Name of the user
    api_response = api_instance.usernameupdate(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->usernameupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateNameRequest**](UpdateNameRequest.md)| Request body for updating name of the user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

