# rainmaker_api_client.AdminUserManagementApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_with_privileges**](AdminUserManagementApi.md#create_user_with_privileges) | **POST** /{version}/admin/user | Creates the new user
[**create_user_with_privileges2**](AdminUserManagementApi.md#create_user_with_privileges2) | **POST** /{version}/admin/user2 | Creates the new user in user email mobile user pool
[**delete_user**](AdminUserManagementApi.md#delete_user) | **DELETE** /{version}/admin/user | Deletes user account
[**delete_user2**](AdminUserManagementApi.md#delete_user2) | **DELETE** /{version}/admin/user2 | Deletes user account
[**get_users**](AdminUserManagementApi.md#get_users) | **GET** /{version}/admin/user | Fetches the details of a user
[**get_users2**](AdminUserManagementApi.md#get_users2) | **GET** /{version}/admin/user2 | Fetches the details of a user
[**update_user_privileges**](AdminUserManagementApi.md#update_user_privileges) | **PUT** /{version}/admin/user | Updates the user
[**update_user_privileges2**](AdminUserManagementApi.md#update_user_privileges2) | **PUT** /{version}/admin/user2 | Updates the user in user email mobile user pool

# **create_user_with_privileges**
> APISuccessResponse create_user_with_privileges(body, version)

Creates the new user

This API creates a new user. Only Email is supported as user name. Here the role is disjoint of the flags the user need to explicitly assign the required role.

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CreateUserAdminRequest() # CreateUserAdminRequest | Request body for creating new user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Creates the new user
    api_response = api_instance.create_user_with_privileges(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->create_user_with_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserAdminRequest**](CreateUserAdminRequest.md)| Request body for creating new user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_with_privileges2**
> APISuccessResponse create_user_with_privileges2(body, version)

Creates the new user in user email mobile user pool

This API creates a new user in user email mobile user pool. Only Email is supported as user name. Here the role is disjoint of the flags the user need to explicitly assign the required role.

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CreateUserAdminRequest() # CreateUserAdminRequest | Request body for creating new user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Creates the new user in user email mobile user pool
    api_response = api_instance.create_user_with_privileges2(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->create_user_with_privileges2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserAdminRequest**](CreateUserAdminRequest.md)| Request body for creating new user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> APISuccessResponse delete_user(version, user_name, request=request, verification_code=verification_code)

Deletes user account

This API can be used by admin-users to delete other users account. Here are the details- <ul> <li>If the 'request' query param is true, user delete request is initiated and verification code is sent to the invoking user email. <li>If 'verification_code' query param is specified, user account is deleted. <li>The 'super_admin' flag has higher priority over 'admin' flag.</ul>

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_name = 'user_name_example' # str | user_name of the user who needs to be deleted
request = false # bool | if delete user request is to be initiated, value of request param should be true. (optional) (default to false)
verification_code = 1.2 # float | if delete user request is to be verified and user account is to be deleted, the verification code received by user should be entered as value of verification_code query param. (optional)

try:
    # Deletes user account
    api_response = api_instance.delete_user(version, user_name, request=request, verification_code=verification_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_name** | **str**| user_name of the user who needs to be deleted | 
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

# **delete_user2**
> APISuccessResponse delete_user2(version, user_name, request=request, verification_code=verification_code)

Deletes user account

This API can be used by admin-users to delete other users account. Here are the details- <ul> <li>If the 'request' query param is true, user delete request is initiated and verification code is sent to the invoking user email. <li>If 'verification_code' query param is specified, user account is deleted. <li>The 'super_admin' flag has higher priority over 'admin' flag.</ul>

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_name = 'user_name_example' # str | user_name of the user who needs to be deleted
request = false # bool | if delete user request is to be initiated, value of request param should be true. (optional) (default to false)
verification_code = 1.2 # float | if delete user request is to be verified and user account is to be deleted, the verification code received by user should be entered as value of verification_code query param. (optional)

try:
    # Deletes user account
    api_response = api_instance.delete_user2(version, user_name, request=request, verification_code=verification_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->delete_user2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_name** | **str**| user_name of the user who needs to be deleted | 
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

# **get_users**
> GetInternalUsers get_users(version, user_name=user_name, start_id=start_id, num_records=num_records)

Fetches the details of a user

This API fetches all the internal users by default. If user name is provided then user_id, user_name, super_admin flag, quota, user roles, URL of profile picture and name of that user is returned. <br><br>The <b>super_admin</b> flag is returned only when the user is a super admin, in other cases, it will not be returned in the output. <br>Also the <b>picture_url</b> and <b>name</b> are not returned in the output, if it is not set by the user.

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_name = 'user_name_example' # str | user_name of the user whose details are to be fetched. (optional)
start_id = 'start_id_example' # str | use next_id from the response as start_id to fetch the next set of records. A combination of userID and user name. (optional)
num_records = '25' # str | number of users to fetch (optional) (default to 25)

try:
    # Fetches the details of a user
    api_response = api_instance.get_users(version, user_name=user_name, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_name** | **str**| user_name of the user whose details are to be fetched. | [optional] 
 **start_id** | **str**| use next_id from the response as start_id to fetch the next set of records. A combination of userID and user name. | [optional] 
 **num_records** | **str**| number of users to fetch | [optional] [default to 25]

### Return type

[**GetInternalUsers**](GetInternalUsers.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users2**
> GetInternalUsers get_users2(version, user_name=user_name, start_id=start_id, num_records=num_records)

Fetches the details of a user

This API fetches all the internal users by default. If user name is provided then user_id, user_name, super_admin flag, quota, user roles, URL of profile picture and name of that user is returned. <br><br>The <b>super_admin</b> flag is returned only when the user is a super admin, in other cases, it will not be returned in the output. <br>Also the <b>picture_url</b> and <b>name</b> are not returned in the output, if it is not set by the user.

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_name = 'user_name_example' # str | user_name of the user whose details are to be fetched. (optional)
start_id = 'start_id_example' # str | use next_id from the response as start_id to fetch the next set of records. A combination of userID and user name. (optional)
num_records = '25' # str | number of users to fetch (optional) (default to 25)

try:
    # Fetches the details of a user
    api_response = api_instance.get_users2(version, user_name=user_name, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->get_users2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_name** | **str**| user_name of the user whose details are to be fetched. | [optional] 
 **start_id** | **str**| use next_id from the response as start_id to fetch the next set of records. A combination of userID and user name. | [optional] 
 **num_records** | **str**| number of users to fetch | [optional] [default to 25]

### Return type

[**GetInternalUsers**](GetInternalUsers.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_privileges**
> APISuccessResponse update_user_privileges(body, version)

Updates the user

This API updates the permissions and quota of the user.

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CreateUserAdminRequest() # CreateUserAdminRequest | Request body for updating name of the user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Updates the user
    api_response = api_instance.update_user_privileges(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->update_user_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserAdminRequest**](CreateUserAdminRequest.md)| Request body for updating name of the user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_privileges2**
> APISuccessResponse update_user_privileges2(body, version)

Updates the user in user email mobile user pool

This API updates the permissions and quota of the user in user email mobile user pool.

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
api_instance = rainmaker_api_client.AdminUserManagementApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CreateUserAdminRequest() # CreateUserAdminRequest | Request body for updating name of the user
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Updates the user in user email mobile user pool
    api_response = api_instance.update_user_privileges2(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUserManagementApi->update_user_privileges2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserAdminRequest**](CreateUserAdminRequest.md)| Request body for updating name of the user | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

