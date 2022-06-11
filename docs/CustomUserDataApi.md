# rainmaker_api_client.CustomUserDataApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_data**](CustomUserDataApi.md#get_user_data) | **GET** /{version}/user/custom_data | Get the Custom user data
[**store_user_data**](CustomUserDataApi.md#store_user_data) | **PUT** /{version}/user/custom_data | Store the custom User data

# **get_user_data**
> InlineResponse2002 get_user_data(version)

Get the Custom user data

Fetches the custom user data of the logged-in user.

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
api_instance = rainmaker_api_client.CustomUserDataApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Get the Custom user data
    api_response = api_instance.get_user_data(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserDataApi->get_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_user_data**
> InlineResponse2002 store_user_data(version, body=body)

Store the custom User data

To store or update the custom user data of the logged-in user. <b>Operations on Data:</b> <ul> <li>The data can be deleted by putting data: <b>null</b>. <li>If the key is already present, then the value will be replaced. Arrays will also be replaced entirely. <li>If the key is not present, then the value will be added. <li>If the value is <b>null</b>, then the key-value will be deleted. </ul><b>Note</b>: The JSON size should not exceed 399 KB.

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
api_instance = rainmaker_api_client.CustomUserDataApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = {
  "$ref" : "#/components/examples/SetCustomData"
} # dict(str, MapItem) |  (optional)

try:
    # Store the custom User data
    api_response = api_instance.store_user_data(version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserDataApi->store_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**dict(str, MapItem)**](dict.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

