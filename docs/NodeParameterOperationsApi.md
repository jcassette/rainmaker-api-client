# rainmaker_api_client.NodeParameterOperationsApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getnodestate**](NodeParameterOperationsApi.md#getnodestate) | **GET** /{version}/user/nodes/params | Get the Node parameter
[**updatenodestate**](NodeParameterOperationsApi.md#updatenodestate) | **PUT** /{version}/user/nodes/params | Update the Node Parameter

# **getnodestate**
> SetParamsRequestBody getnodestate(version, node_id)

Get the Node parameter

This API will Get the state of the device

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
api_instance = rainmaker_api_client.NodeParameterOperationsApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node id

try:
    # Get the Node parameter
    api_response = api_instance.getnodestate(version, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeParameterOperationsApi->getnodestate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node id | 

### Return type

[**SetParamsRequestBody**](SetParamsRequestBody.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatenodestate**
> APISuccessResponse updatenodestate(body, version, node_id=node_id)

Update the Node Parameter

This API will update the state of the device

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
api_instance = rainmaker_api_client.NodeParameterOperationsApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.NodesParamsBody() # NodesParamsBody | Request body for updating Node Parameter
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node id (optional)

try:
    # Update the Node Parameter
    api_response = api_instance.updatenodestate(body, version, node_id=node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeParameterOperationsApi->updatenodestate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodesParamsBody**](NodesParamsBody.md)| Request body for updating Node Parameter | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node id | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

