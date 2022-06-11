# rainmaker_api_client.MobilePlatformEndpointApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteplatformendpoint**](MobilePlatformEndpointApi.md#deleteplatformendpoint) | **DELETE** /{version}/user/push_notification/mobile_platform_endpoint | This API removes the configured platform endpoint.
[**getplatformendpoint**](MobilePlatformEndpointApi.md#getplatformendpoint) | **GET** /{version}/user/push_notification/mobile_platform_endpoint | This API fetches configured platform endpoints
[**platformendpointcreation**](MobilePlatformEndpointApi.md#platformendpointcreation) | **POST** /{version}/user/push_notification/mobile_platform_endpoint | Creates the new platform endpoint for the user&#x27;s Mobile device

# **deleteplatformendpoint**
> InlineResponse2005 deleteplatformendpoint(version, mobile_device_token=mobile_device_token, endpoint=endpoint)

This API removes the configured platform endpoint.

This API removes the configured platform endpoint. Either mobile_device_token or endpoint must be specified in query params.

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
api_instance = rainmaker_api_client.MobilePlatformEndpointApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
mobile_device_token = 'mobile_device_token_example' # str | mobile device token (optional)
endpoint = 'endpoint_example' # str | platform endpoint ARN (optional)

try:
    # This API removes the configured platform endpoint.
    api_response = api_instance.deleteplatformendpoint(version, mobile_device_token=mobile_device_token, endpoint=endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobilePlatformEndpointApi->deleteplatformendpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **mobile_device_token** | **str**| mobile device token | [optional] 
 **endpoint** | **str**| platform endpoint ARN | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getplatformendpoint**
> GetPlatformEndpointResponse getplatformendpoint(version)

This API fetches configured platform endpoints

This API fetches configured platform endpoints

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
api_instance = rainmaker_api_client.MobilePlatformEndpointApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API fetches configured platform endpoints
    api_response = api_instance.getplatformendpoint(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobilePlatformEndpointApi->getplatformendpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**GetPlatformEndpointResponse**](GetPlatformEndpointResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platformendpointcreation**
> PlatformEndpointAPISuccessResponse platformendpointcreation(body, version)

Creates the new platform endpoint for the user's Mobile device

This API will be called from the Mobile App by the end user, to subscribe to Push Notification.

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
api_instance = rainmaker_api_client.MobilePlatformEndpointApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.PlatformEndpointCreateRequest() # PlatformEndpointCreateRequest | Request body for creating new platform application, Valid values for platform are GCM, APNS or APNS_SANDBOX.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Creates the new platform endpoint for the user's Mobile device
    api_response = api_instance.platformendpointcreation(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobilePlatformEndpointApi->platformendpointcreation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlatformEndpointCreateRequest**](PlatformEndpointCreateRequest.md)| Request body for creating new platform application, Valid values for platform are GCM, APNS or APNS_SANDBOX. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**PlatformEndpointAPISuccessResponse**](PlatformEndpointAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

