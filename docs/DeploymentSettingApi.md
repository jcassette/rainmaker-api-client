# rainmaker_api_client.DeploymentSettingApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_service_configuration**](DeploymentSettingApi.md#backup_service_configuration) | **PUT** /{version}/admin/deployment_settings/backup/{service} | API for the super admin user to backup service&#x27;s configuration
[**cofigure_service_configuration**](DeploymentSettingApi.md#cofigure_service_configuration) | **PUT** /{version}/admin/deployment_settings/config/{service} | API for the super admin user to configure service&#x27;s configuration
[**get_service_configuration**](DeploymentSettingApi.md#get_service_configuration) | **GET** /{version}/admin/deployment_settings/{service} | API for the super admin user to get service&#x27;s stored configuration details.
[**restore_service_configuration**](DeploymentSettingApi.md#restore_service_configuration) | **PUT** /{version}/admin/deployment_settings/restore/{service} | API for the super admin user to restore service&#x27;s configuration

# **backup_service_configuration**
> APISuccessResponse backup_service_configuration(version, service)

API for the super admin user to backup service's configuration

This API is used by customer's super admin users to backup service's configuration.

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
api_instance = rainmaker_api_client.DeploymentSettingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
service = 'service_example' # str | Service

try:
    # API for the super admin user to backup service's configuration
    api_response = api_instance.backup_service_configuration(version, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentSettingApi->backup_service_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **service** | **str**| Service | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cofigure_service_configuration**
> APISuccessResponse cofigure_service_configuration(version, service, body=body)

API for the super admin user to configure service's configuration

This API is used by customer's super admin users to configure service's configuration.

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
api_instance = rainmaker_api_client.DeploymentSettingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
service = 'service_example' # str | Service
body = rainmaker_api_client.ConfigureRBAC() # ConfigureRBAC | Request body for configuring rbac (optional)

try:
    # API for the super admin user to configure service's configuration
    api_response = api_instance.cofigure_service_configuration(version, service, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentSettingApi->cofigure_service_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **service** | **str**| Service | 
 **body** | [**ConfigureRBAC**](ConfigureRBAC.md)| Request body for configuring rbac | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_configuration**
> InlineResponse20011 get_service_configuration(version, service, platform=platform, package_name=package_name, is_email_user_pool=is_email_user_pool)

API for the super admin user to get service's stored configuration details.

This API is used by customer's super admin users to get service's stored configuration details. Can be used to get configurations for building mobile apps.

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
api_instance = rainmaker_api_client.DeploymentSettingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
service = 'service_example' # str | Service
platform = 'platform_example' # str | If service is mobile_app, App platform(ios or android) is Mandatory (optional)
package_name = 'package_name_example' # str | If service is mobile_app, package name of the Application is Mandatory (optional)
is_email_user_pool = 'false' # str | If service is mobile_app, use true for older/email-only userPool or false for newer/email-and-phone userPool. Default is Newer userpool. (optional) (default to false)

try:
    # API for the super admin user to get service's stored configuration details.
    api_response = api_instance.get_service_configuration(version, service, platform=platform, package_name=package_name, is_email_user_pool=is_email_user_pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentSettingApi->get_service_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **service** | **str**| Service | 
 **platform** | **str**| If service is mobile_app, App platform(ios or android) is Mandatory | [optional] 
 **package_name** | **str**| If service is mobile_app, package name of the Application is Mandatory | [optional] 
 **is_email_user_pool** | **str**| If service is mobile_app, use true for older/email-only userPool or false for newer/email-and-phone userPool. Default is Newer userpool. | [optional] [default to false]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_service_configuration**
> APISuccessResponse restore_service_configuration(version, service)

API for the super admin user to restore service's configuration

This API is used by customer's super admin users to restore service's configuration.

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
api_instance = rainmaker_api_client.DeploymentSettingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
service = 'service_example' # str | Service

try:
    # API for the super admin user to restore service's configuration
    api_response = api_instance.restore_service_configuration(version, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentSettingApi->restore_service_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **service** | **str**| Service | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

