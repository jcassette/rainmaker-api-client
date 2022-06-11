# rainmaker_api_client.PublishMessageApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publish_message**](PublishMessageApi.md#publish_message) | **POST** /{version}/admin/push_notification/publish_message | Publish message to user&#x27;s device

# **publish_message**
> APISuccessResponse publish_message(body, version, email=email, user_id=user_id)

Publish message to user's device

This API will be used to publish messages to user's device in a bulk of 100000 users. At least one of <b>email</b> or <b>user_id</b> list needs to be provided.    <b>user_id</b> has more preference over <b>email</b>.

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
api_instance = rainmaker_api_client.PublishMessageApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.PublishMessage() # PublishMessage | Request body for publish message
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
email = 'email_example' # str | Comma separated email ids and the maximum number of email ids that can be specified are 100000 (optional)
user_id = 'user_id_example' # str | Comma separated user ids and the maximum number of user ids that can be specified are 100000 (optional)

try:
    # Publish message to user's device
    api_response = api_instance.publish_message(body, version, email=email, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishMessageApi->publish_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishMessage**](PublishMessage.md)| Request body for publish message | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **email** | **str**| Comma separated email ids and the maximum number of email ids that can be specified are 100000 | [optional] 
 **user_id** | **str**| Comma separated user ids and the maximum number of user ids that can be specified are 100000 | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

