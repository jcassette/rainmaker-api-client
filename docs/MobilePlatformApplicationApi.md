# rainmaker_api_client.MobilePlatformApplicationApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteplatformapplication**](MobilePlatformApplicationApi.md#deleteplatformapplication) | **DELETE** /{version}/admin/push_notification/mobile_platform | This API removes the configured platform application.
[**getplatformapplication**](MobilePlatformApplicationApi.md#getplatformapplication) | **GET** /{version}/admin/push_notification/mobile_platform | This API fetches the list of configured platform applications
[**platformapplicationcreation**](MobilePlatformApplicationApi.md#platformapplicationcreation) | **POST** /{version}/admin/push_notification/mobile_platform | Creates the new platform application

# **deleteplatformapplication**
> InlineResponse2005 deleteplatformapplication(version, platform_application_arn)

This API removes the configured platform application.

This API removes the configured platform application.

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
api_instance = rainmaker_api_client.MobilePlatformApplicationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
platform_application_arn = 'platform_application_arn_example' # str | platform application arn

try:
    # This API removes the configured platform application.
    api_response = api_instance.deleteplatformapplication(version, platform_application_arn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobilePlatformApplicationApi->deleteplatformapplication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **platform_application_arn** | **str**| platform application arn | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getplatformapplication**
> GetPlatformApplicationResponse getplatformapplication(version)

This API fetches the list of configured platform applications

This API fetches configured platform application

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
api_instance = rainmaker_api_client.MobilePlatformApplicationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API fetches the list of configured platform applications
    api_response = api_instance.getplatformapplication(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobilePlatformApplicationApi->getplatformapplication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**GetPlatformApplicationResponse**](GetPlatformApplicationResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platformapplicationcreation**
> PlatformApplicationAPISuccessResponse platformapplicationcreation(body, version)

Creates the new platform application

This API creates a new mobile platform application <p>&nbsp; &nbsp; &nbsp;<strong>Platform</strong> : Represents a push notification service from a provider like Google, Amazon or Microsoft.</p>

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
api_instance = rainmaker_api_client.MobilePlatformApplicationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.PushNotificationMobilePlatformBody() # PushNotificationMobilePlatformBody | Request body for creating new platform application, Valid platform to be specified are ADM,APNS,APNS_SANDBOX or GCM.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Creates the new platform application
    api_response = api_instance.platformapplicationcreation(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobilePlatformApplicationApi->platformapplicationcreation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PushNotificationMobilePlatformBody**](PushNotificationMobilePlatformBody.md)| Request body for creating new platform application, Valid platform to be specified are ADM,APNS,APNS_SANDBOX or GCM. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**PlatformApplicationAPISuccessResponse**](PlatformApplicationAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

