# rainmaker_api_client.WebhookIntegrationApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook_integration**](WebhookIntegrationApi.md#add_webhook_integration) | **POST** /{version}/admin/webhook_integration | This API adds new webhook for specified integration.
[**add_webhook_user_node_integration**](WebhookIntegrationApi.md#add_webhook_user_node_integration) | **POST** /{version}/admin/webhook_user_node_integration | This API adds webhook user node integration
[**delete_webhook_event_mapping**](WebhookIntegrationApi.md#delete_webhook_event_mapping) | **DELETE** /{version}/admin/webhook_event_mapping | This API removes webhook event mapping
[**delete_webhook_user_node_integration**](WebhookIntegrationApi.md#delete_webhook_user_node_integration) | **DELETE** /{version}/admin/webhook_user_node_integration | This API deletes webhook user node integration
[**get_webhook_event_mapping**](WebhookIntegrationApi.md#get_webhook_event_mapping) | **GET** /{version}/admin/webhook_event_mapping | Get webhook event mapping information.
[**get_webhook_integration**](WebhookIntegrationApi.md#get_webhook_integration) | **GET** /{version}/admin/webhook_integration | Get webhook information.
[**get_webhook_user_node_integration**](WebhookIntegrationApi.md#get_webhook_user_node_integration) | **GET** /{version}/admin/webhook_user_node_integration | Get user node webhook integration information.
[**remove_webhook_integration**](WebhookIntegrationApi.md#remove_webhook_integration) | **DELETE** /{version}/admin/webhook_integration | This API removes the webhooks configured for integration.
[**update_webhook_event_mapping**](WebhookIntegrationApi.md#update_webhook_event_mapping) | **PUT** /{version}/admin/webhook_event_mapping | This API adds webhook event mapping
[**update_webhook_integration**](WebhookIntegrationApi.md#update_webhook_integration) | **PUT** /{version}/admin/webhook_integration | This API updates existing webhook configuration.
[**update_webhook_user_node_integration**](WebhookIntegrationApi.md#update_webhook_user_node_integration) | **PUT** /{version}/admin/webhook_user_node_integration | This API updates webhook user node integration.

# **add_webhook_integration**
> WebhookAPISuccessResponse add_webhook_integration(body, version)

This API adds new webhook for specified integration.

This API adds new webhook for specified service name, endpoint and whether its enabled or not. <p>&nbsp; &nbsp; <strong>&nbsp;Service Name </strong> : Name of external service to be integrated</p> <p>&nbsp; &nbsp; &nbsp;<strong>Endpoint Name</strong> : A Service may have more than Webhook Endpoints. Endpoint Name of Service which we are integrating to&nbsp;</p> <p>&nbsp; &nbsp; &nbsp;<strong>Enabled</strong> : This flag tells whether this integration is enabled</p> <p>&nbsp;</p></p>

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.AddWebhookIntegrationRequest() # AddWebhookIntegrationRequest | request body for creating new Webhook Integration.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API adds new webhook for specified integration.
    api_response = api_instance.add_webhook_integration(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->add_webhook_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddWebhookIntegrationRequest**](AddWebhookIntegrationRequest.md)| request body for creating new Webhook Integration. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**WebhookAPISuccessResponse**](WebhookAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_webhook_user_node_integration**
> APISuccessResponse add_webhook_user_node_integration(version, body=body)

This API adds webhook user node integration

This API adds the webhook for user node integration 

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.WebhookUserNodeIntegration() # WebhookUserNodeIntegration | request body for adding a webhook for user node integration. (optional)

try:
    # This API adds webhook user node integration
    api_response = api_instance.add_webhook_user_node_integration(version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->add_webhook_user_node_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**WebhookUserNodeIntegration**](WebhookUserNodeIntegration.md)| request body for adding a webhook for user node integration. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_event_mapping**
> APISuccessResponse delete_webhook_event_mapping(version, webhook_name, event_name)

This API removes webhook event mapping

This API removes the webhook event mapping 

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
webhook_name = 'webhook_name_example' # str | Webhook to be removed
event_name = 'event_name_example' # str | Event to be removed

try:
    # This API removes webhook event mapping
    api_response = api_instance.delete_webhook_event_mapping(version, webhook_name, event_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->delete_webhook_event_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **webhook_name** | **str**| Webhook to be removed | 
 **event_name** | **str**| Event to be removed | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_user_node_integration**
> APISuccessResponse delete_webhook_user_node_integration(version, webhook_name)

This API deletes webhook user node integration

This API deletes the webhook for user node integration 

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
webhook_name = 'webhook_name_example' # str | Webhook to be deleted

try:
    # This API deletes webhook user node integration
    api_response = api_instance.delete_webhook_user_node_integration(version, webhook_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->delete_webhook_user_node_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **webhook_name** | **str**| Webhook to be deleted | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_event_mapping**
> GetWebhookEventMappingResponse get_webhook_event_mapping(version, webhook_name=webhook_name)

Get webhook event mapping information.

This API will get the webhook integration mapping 

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
webhook_name = 'webhook_name_example' # str | Webhook to be retrieved (optional)

try:
    # Get webhook event mapping information.
    api_response = api_instance.get_webhook_event_mapping(version, webhook_name=webhook_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->get_webhook_event_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **webhook_name** | **str**| Webhook to be retrieved | [optional] 

### Return type

[**GetWebhookEventMappingResponse**](GetWebhookEventMappingResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_integration**
> GetWebhookIntegrationResponse get_webhook_integration(version, service_name=service_name, endpoint_name=endpoint_name)

Get webhook information.

This API will get the integration information of webhook.

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
service_name = 'service_name_example' # str |  (optional)
endpoint_name = 'endpoint_name_example' # str |  (optional)

try:
    # Get webhook information.
    api_response = api_instance.get_webhook_integration(version, service_name=service_name, endpoint_name=endpoint_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->get_webhook_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **service_name** | **str**|  | [optional] 
 **endpoint_name** | **str**|  | [optional] 

### Return type

[**GetWebhookIntegrationResponse**](GetWebhookIntegrationResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_user_node_integration**
> GetWebhookUserNodeIntegrationResponse get_webhook_user_node_integration(version, webhook_name=webhook_name)

Get user node webhook integration information.

This API will get the user node webhook integrations 

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
webhook_name = 'webhook_name_example' # str | Webhook to be retrieved (optional)

try:
    # Get user node webhook integration information.
    api_response = api_instance.get_webhook_user_node_integration(version, webhook_name=webhook_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->get_webhook_user_node_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **webhook_name** | **str**| Webhook to be retrieved | [optional] 

### Return type

[**GetWebhookUserNodeIntegrationResponse**](GetWebhookUserNodeIntegrationResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_webhook_integration**
> WebhookAPISuccessResponse remove_webhook_integration(version, service_name, endpoint_name)

This API removes the webhooks configured for integration.

This API allows admin to remove configured webhooks for integration.

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
service_name = 'service_name_example' # str | 
endpoint_name = 'endpoint_name_example' # str | 

try:
    # This API removes the webhooks configured for integration.
    api_response = api_instance.remove_webhook_integration(version, service_name, endpoint_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->remove_webhook_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **service_name** | **str**|  | 
 **endpoint_name** | **str**|  | 

### Return type

[**WebhookAPISuccessResponse**](WebhookAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_event_mapping**
> APISuccessResponse update_webhook_event_mapping(version, body=body)

This API adds webhook event mapping

This API adds the webhook event mapping 

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.PutWebhookEventMappingRequest() # PutWebhookEventMappingRequest | request body for adding a webhook event mapping. (optional)

try:
    # This API adds webhook event mapping
    api_response = api_instance.update_webhook_event_mapping(version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->update_webhook_event_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**PutWebhookEventMappingRequest**](PutWebhookEventMappingRequest.md)| request body for adding a webhook event mapping. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_integration**
> WebhookAPISuccessResponse update_webhook_integration(body, version)

This API updates existing webhook configuration.

This API updates existing webhook configuration for specified integration and its endpoint. <p>&nbsp; &nbsp; <strong>&nbsp;Service Name </strong> : Name of external service to be integrated</p> <p>&nbsp; &nbsp; &nbsp;<strong>Endpoint Name</strong> : A Service may have more than Webhook Endpoints. Endpoint Name of Service which we are integrating to&nbsp;</p> <p>&nbsp; &nbsp; &nbsp;<strong>Enabled</strong> : This flag tells whether this integration is enabled</p> <p>&nbsp;</p></p>

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdateWebhookIntegrationRequest() # UpdateWebhookIntegrationRequest | request body for updating existing Webhook Integration configuration.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API updates existing webhook configuration.
    api_response = api_instance.update_webhook_integration(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->update_webhook_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWebhookIntegrationRequest**](UpdateWebhookIntegrationRequest.md)| request body for updating existing Webhook Integration configuration. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**WebhookAPISuccessResponse**](WebhookAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_user_node_integration**
> APISuccessResponse update_webhook_user_node_integration(operation, version, body=body)

This API updates webhook user node integration.

This API updates the webhook for user node integration <br><br>IMPORTANT NOTES <br>- Identifiers (ex. webhook_name, event_name) cannot be updated. <br>- Only respective request body parameters according to operation will be updated. Any additional ones will be ignored. For example, if 'operation' is 'update_enabled', then only the 'enabled' parameter from request body would be updated, rest all would be ignored.

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
api_instance = rainmaker_api_client.WebhookIntegrationApi(rainmaker_api_client.ApiClient(configuration))
operation = 'operation_example' # str | Operation to be performed (Supported operations:- update_enabled, add_nodes, remove_nodes, add_event, remove_event, update_event, update_active_timestamp)
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.WebhookUserNodeIntegration() # WebhookUserNodeIntegration | request body for updating a webhook for user node integration. (optional)

try:
    # This API updates webhook user node integration.
    api_response = api_instance.update_webhook_user_node_integration(operation, version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookIntegrationApi->update_webhook_user_node_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **str**| Operation to be performed (Supported operations:- update_enabled, add_nodes, remove_nodes, add_event, remove_event, update_event, update_active_timestamp) | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**WebhookUserNodeIntegration**](WebhookUserNodeIntegration.md)| request body for updating a webhook for user node integration. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

