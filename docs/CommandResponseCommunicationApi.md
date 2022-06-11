# rainmaker_api_client.CommandResponseCommunicationApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cmd_response_requests**](CommandResponseCommunicationApi.md#get_cmd_response_requests) | **GET** /{version}/user/nodes/cmd | Get the Command Response Requests
[**get_cmd_response_requests2**](CommandResponseCommunicationApi.md#get_cmd_response_requests2) | **GET** /{version}/admin/nodes/cmd | Get the Command Response Requests
[**post_cmd_response_requests**](CommandResponseCommunicationApi.md#post_cmd_response_requests) | **POST** /{version}/user/nodes/cmd | Add a Command Response Request
[**post_cmd_response_requests_admin**](CommandResponseCommunicationApi.md#post_cmd_response_requests_admin) | **POST** /{version}/admin/nodes/cmd | Add a Command Response Request

# **get_cmd_response_requests**
> CmdResponseGetRequest get_cmd_response_requests(version, request_id, node_id=node_id, start_id=start_id, num_records=num_records)

Get the Command Response Requests

Get the Command Response Requests for a given request id. If node id is provided then request corresponding to the request id and node id is returned.

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
api_instance = rainmaker_api_client.CommandResponseCommunicationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | ID of the command response request.
node_id = 'node_id_example' # str | ID of the node (optional)
start_id = 'start_id_example' # str | Used for pagination. (optional)
num_records = 10 # float | Used for pagination, number of records to be fetched. (optional) (default to 10)

try:
    # Get the Command Response Requests
    api_response = api_instance.get_cmd_response_requests(version, request_id, node_id=node_id, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandResponseCommunicationApi->get_cmd_response_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request_id** | **str**| ID of the command response request. | 
 **node_id** | **str**| ID of the node | [optional] 
 **start_id** | **str**| Used for pagination. | [optional] 
 **num_records** | **float**| Used for pagination, number of records to be fetched. | [optional] [default to 10]

### Return type

[**CmdResponseGetRequest**](CmdResponseGetRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cmd_response_requests2**
> CmdResponseGetRequest get_cmd_response_requests2(version, request_id, node_id=node_id, start_id=start_id, num_records=num_records)

Get the Command Response Requests

Get the Command Response Requests for a given request id. If node id is provided then request corresponding to the request id and node id is returned.

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
api_instance = rainmaker_api_client.CommandResponseCommunicationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | ID of the command response request.
node_id = 'node_id_example' # str | ID of the node (optional)
start_id = 'start_id_example' # str | Used for pagination. (optional)
num_records = 10 # float | Used for pagination, number of records to be fetched. (optional) (default to 10)

try:
    # Get the Command Response Requests
    api_response = api_instance.get_cmd_response_requests2(version, request_id, node_id=node_id, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandResponseCommunicationApi->get_cmd_response_requests2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request_id** | **str**| ID of the command response request. | 
 **node_id** | **str**| ID of the node | [optional] 
 **start_id** | **str**| Used for pagination. | [optional] 
 **num_records** | **float**| Used for pagination, number of records to be fetched. | [optional] [default to 10]

### Return type

[**CmdResponseGetRequest**](CmdResponseGetRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cmd_response_requests**
> CmdResponsePostResponse post_cmd_response_requests(body, version)

Add a Command Response Request

Used to add a Command Response Request. There can be maximum of 25 nodes in a single request.

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
api_instance = rainmaker_api_client.CommandResponseCommunicationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CmdResponsePostRequest() # CmdResponsePostRequest | Add a request to Command Response
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Add a Command Response Request
    api_response = api_instance.post_cmd_response_requests(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandResponseCommunicationApi->post_cmd_response_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CmdResponsePostRequest**](CmdResponsePostRequest.md)| Add a request to Command Response | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**CmdResponsePostResponse**](CmdResponsePostResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cmd_response_requests_admin**
> CmdResponsePostResponse post_cmd_response_requests_admin(body, version)

Add a Command Response Request

Used to add a Command Response Request. There can be maximum of 25 nodes in a single request.

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
api_instance = rainmaker_api_client.CommandResponseCommunicationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CmdResponsePostRequest() # CmdResponsePostRequest | Add a request to Command Response
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Add a Command Response Request
    api_response = api_instance.post_cmd_response_requests_admin(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandResponseCommunicationApi->post_cmd_response_requests_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CmdResponsePostRequest**](CmdResponsePostRequest.md)| Add a request to Command Response | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**CmdResponsePostResponse**](CmdResponsePostResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

