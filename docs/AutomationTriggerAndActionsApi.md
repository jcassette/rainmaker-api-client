# rainmaker_api_client.AutomationTriggerAndActionsApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_automation_trigger_action**](AutomationTriggerAndActionsApi.md#add_automation_trigger_action) | **POST** /{version}/user/node_automation | This API adds new automation trigger
[**get_automation_trigger_action**](AutomationTriggerAndActionsApi.md#get_automation_trigger_action) | **GET** /{version}/user/node_automation | Get Automation trigger.
[**remove_automation_trigger_action**](AutomationTriggerAndActionsApi.md#remove_automation_trigger_action) | **DELETE** /{version}/user/node_automation | This API removes the automation trigger.
[**update_automation_trigger_action**](AutomationTriggerAndActionsApi.md#update_automation_trigger_action) | **PUT** /{version}/user/node_automation | This API updates existing automation trigger.

# **add_automation_trigger_action**
> AutomationTriggerAPISuccessResponse add_automation_trigger_action(body, version)

This API adds new automation trigger

This API adds new automation trigger

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
api_instance = rainmaker_api_client.AutomationTriggerAndActionsApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.AddAutomationTriggerRequest() # AddAutomationTriggerRequest | Request body for creating new automation trigger.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API adds new automation trigger
    api_response = api_instance.add_automation_trigger_action(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationTriggerAndActionsApi->add_automation_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAutomationTriggerRequest**](AddAutomationTriggerRequest.md)| Request body for creating new automation trigger. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**AutomationTriggerAPISuccessResponse**](AutomationTriggerAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automation_trigger_action**
> GetAutomationTriggerResponse get_automation_trigger_action(version, automation_id=automation_id, node_id=node_id, start_id=start_id, num_records=num_records)

Get Automation trigger.

This API will fetch automation trigger

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
api_instance = rainmaker_api_client.AutomationTriggerAndActionsApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
automation_id = 'automation_id_example' # str |  (optional)
node_id = 'node_id_example' # str |  (optional)
start_id = 'start_id_example' # str | use next_id from the response as start_id to fetch the next set of records (optional)
num_records = 'num_records_example' # str | number of records to fetch (optional)

try:
    # Get Automation trigger.
    api_response = api_instance.get_automation_trigger_action(version, automation_id=automation_id, node_id=node_id, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationTriggerAndActionsApi->get_automation_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **automation_id** | **str**|  | [optional] 
 **node_id** | **str**|  | [optional] 
 **start_id** | **str**| use next_id from the response as start_id to fetch the next set of records | [optional] 
 **num_records** | **str**| number of records to fetch | [optional] 

### Return type

[**GetAutomationTriggerResponse**](GetAutomationTriggerResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_automation_trigger_action**
> APISuccessResponse remove_automation_trigger_action(version, automation_id)

This API removes the automation trigger.

This API allows user to remove created automation trigger

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
api_instance = rainmaker_api_client.AutomationTriggerAndActionsApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
automation_id = 'automation_id_example' # str | 

try:
    # This API removes the automation trigger.
    api_response = api_instance.remove_automation_trigger_action(version, automation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationTriggerAndActionsApi->remove_automation_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **automation_id** | **str**|  | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_automation_trigger_action**
> APISuccessResponse update_automation_trigger_action(body, automation_id, version)

This API updates existing automation trigger.

This API updates existing automation trigger

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
api_instance = rainmaker_api_client.AutomationTriggerAndActionsApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdateAutomationTriggerRequest() # UpdateAutomationTriggerRequest | Request body for updating existing automation trigger.
automation_id = 'automation_id_example' # str | automation_id
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API updates existing automation trigger.
    api_response = api_instance.update_automation_trigger_action(body, automation_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationTriggerAndActionsApi->update_automation_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAutomationTriggerRequest**](UpdateAutomationTriggerRequest.md)| Request body for updating existing automation trigger. | 
 **automation_id** | **str**| automation_id | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

