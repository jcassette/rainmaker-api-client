# rainmaker_api_client.APIInfoApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_paths_methods**](APIInfoApi.md#get_api_paths_methods) | **GET** /{version}/admin/api_paths_methods | This api fetches available API endpoints and methods.

# **get_api_paths_methods**
> get_api_paths_methods(version, all_paths=all_paths)

This api fetches available API endpoints and methods.

This api fetches available API endpoints and methods.

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
api_instance = rainmaker_api_client.APIInfoApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
all_paths = false # bool | When true, the response will contain all available endpoints and methods. When false, the response will contain only admin API endpoints and methods. (optional) (default to false)

try:
    # This api fetches available API endpoints and methods.
    api_instance.get_api_paths_methods(version, all_paths=all_paths)
except ApiException as e:
    print("Exception when calling APIInfoApi->get_api_paths_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **all_paths** | **bool**| When true, the response will contain all available endpoints and methods. When false, the response will contain only admin API endpoints and methods. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

