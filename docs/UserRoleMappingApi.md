# rainmaker_api_client.UserRoleMappingApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_role_mapping**](UserRoleMappingApi.md#get_user_role_mapping) | **GET** /{version}/admin/user_role | This api fetches roles for a user.
[**update_user_role_mapping**](UserRoleMappingApi.md#update_user_role_mapping) | **PUT** /{version}/admin/user_role | This API assigns or removes role from or to user.

# **get_user_role_mapping**
> InlineResponse20010 get_user_role_mapping(version, user_name=user_name, user_id=user_id, role_name=role_name)

This api fetches roles for a user.

This API will fetches roles for a user.

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
api_instance = rainmaker_api_client.UserRoleMappingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_name = 'user_name_example' # str | user_name (optional)
user_id = 'user_id_example' # str | user_id (optional)
role_name = 'role_name_example' # str | role_name (optional)

try:
    # This api fetches roles for a user.
    api_response = api_instance.get_user_role_mapping(version, user_name=user_name, user_id=user_id, role_name=role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRoleMappingApi->get_user_role_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_name** | **str**| user_name | [optional] 
 **user_id** | **str**| user_id | [optional] 
 **role_name** | **str**| role_name | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_role_mapping**
> APISuccessResponse update_user_role_mapping(body, user_name, operation, version, user_id=user_id)

This API assigns or removes role from or to user.

This API assigns or removes role from or to user.

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
api_instance = rainmaker_api_client.UserRoleMappingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UserRoleMapping() # UserRoleMapping | Request body for updating user role mapping.
user_name = 'user_name_example' # str | user_name
operation = 'operation_example' # str | operation can be add or remove
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_id = 'user_id_example' # str | user_id (optional)

try:
    # This API assigns or removes role from or to user.
    api_response = api_instance.update_user_role_mapping(body, user_name, operation, version, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRoleMappingApi->update_user_role_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRoleMapping**](UserRoleMapping.md)| Request body for updating user role mapping. | 
 **user_name** | **str**| user_name | 
 **operation** | **str**| operation can be add or remove | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_id** | **str**| user_id | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

