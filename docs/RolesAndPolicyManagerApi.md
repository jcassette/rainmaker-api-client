# rainmaker_api_client.RolesAndPolicyManagerApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy**](RolesAndPolicyManagerApi.md#add_policy) | **POST** /{version}/admin/policy | This API adds policy
[**add_roles_policy**](RolesAndPolicyManagerApi.md#add_roles_policy) | **POST** /{version}/admin/role | This API adds new roles
[**get_policy**](RolesAndPolicyManagerApi.md#get_policy) | **GET** /{version}/admin/policy | This api fetches policies.
[**get_roles**](RolesAndPolicyManagerApi.md#get_roles) | **GET** /{version}/admin/role | This api fetches roles.
[**remove_policy**](RolesAndPolicyManagerApi.md#remove_policy) | **DELETE** /{version}/admin/policy | This API removes the policy.
[**remove_roles**](RolesAndPolicyManagerApi.md#remove_roles) | **DELETE** /{version}/admin/role | This API removes the roles.
[**update_policy**](RolesAndPolicyManagerApi.md#update_policy) | **PUT** /{version}/admin/policy | This API updates existing policy.
[**update_role**](RolesAndPolicyManagerApi.md#update_role) | **PUT** /{version}/admin/role | This API updates existing role.

# **add_policy**
> APISuccessResponse add_policy(body, version)

This API adds policy

This API adds new policy

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.Policy() # Policy | Request body for creating new policy.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API adds policy
    api_response = api_instance.add_policy(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->add_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)| Request body for creating new policy. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_roles_policy**
> APISuccessResponse add_roles_policy(body, version)

This API adds new roles

This API adds new role

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.Role() # Role | Request body for creating new role.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API adds new roles
    api_response = api_instance.add_roles_policy(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->add_roles_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)| Request body for creating new role. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> GetPolicyResponse get_policy(version, policy_name=policy_name)

This api fetches policies.

This API will fetch policies

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
policy_name = 'policy_name_example' # str |  (optional)

try:
    # This api fetches policies.
    api_response = api_instance.get_policy(version, policy_name=policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **policy_name** | **str**|  | [optional] 

### Return type

[**GetPolicyResponse**](GetPolicyResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> GetRoleResponse get_roles(version, role_name=role_name)

This api fetches roles.

This API will fetch roles

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
role_name = 'role_name_example' # str |  (optional)

try:
    # This api fetches roles.
    api_response = api_instance.get_roles(version, role_name=role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->get_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **role_name** | **str**|  | [optional] 

### Return type

[**GetRoleResponse**](GetRoleResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_policy**
> APISuccessResponse remove_policy(version, policy_name)

This API removes the policy.

This API allow to remove policy

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
policy_name = 'policy_name_example' # str | 

try:
    # This API removes the policy.
    api_response = api_instance.remove_policy(version, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->remove_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **policy_name** | **str**|  | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_roles**
> APISuccessResponse remove_roles(version, role_name)

This API removes the roles.

This API allow to remove role

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
role_name = 'role_name_example' # str | 

try:
    # This API removes the roles.
    api_response = api_instance.remove_roles(version, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->remove_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **role_name** | **str**|  | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> APISuccessResponse update_policy(body, policy_name, version)

This API updates existing policy.

This API updates existing policy.

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdatePolicy() # UpdatePolicy | Request body for updating existing policy.
policy_name = 'policy_name_example' # str | policy_name
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API updates existing policy.
    api_response = api_instance.update_policy(body, policy_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePolicy**](UpdatePolicy.md)| Request body for updating existing policy. | 
 **policy_name** | **str**| policy_name | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> APISuccessResponse update_role(body, role_name, operation, version)

This API updates existing role.

This API updates existing role.

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
api_instance = rainmaker_api_client.RolesAndPolicyManagerApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdateRole() # UpdateRole | Request body for updating existing role.
role_name = 'role_name_example' # str | role_name
operation = 'operation_example' # str | operation can be add or remove
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API updates existing role.
    api_response = api_instance.update_role(body, role_name, operation, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesAndPolicyManagerApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRole**](UpdateRole.md)| Request body for updating existing role. | 
 **role_name** | **str**| role_name | 
 **operation** | **str**| operation can be add or remove | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

