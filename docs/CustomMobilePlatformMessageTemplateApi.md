# rainmaker_api_client.CustomMobilePlatformMessageTemplateApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createcustommessagetemplate**](CustomMobilePlatformMessageTemplateApi.md#createcustommessagetemplate) | **POST** /{version}/admin/push_notification/custom_message_template | Create custom mobile platform message template
[**getcustommessagetemplate**](CustomMobilePlatformMessageTemplateApi.md#getcustommessagetemplate) | **GET** /{version}/admin/push_notification/custom_message_template | This API fetches configured custom mobile message template
[**updatecustommessagetemplate**](CustomMobilePlatformMessageTemplateApi.md#updatecustommessagetemplate) | **PUT** /{version}/admin/push_notification/custom_message_template | This API updates the configured custom mobile message template.

# **createcustommessagetemplate**
> APISuccessResponse createcustommessagetemplate(body, version)

Create custom mobile platform message template

This API will be used to create custom mobile platform message template.

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
api_instance = rainmaker_api_client.CustomMobilePlatformMessageTemplateApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CreateCustomMobileMessageTemplate() # CreateCustomMobileMessageTemplate | Request body for creating custom mobile message template. <p>&nbsp; &nbsp; &nbsp;<strong>Event Data</strong> : When event data is enabled, Event's raw data is shared with mobile.</p> <p>&nbsp; &nbsp; &nbsp;<strong>Event Type</strong> : Event topic name.[same as SNS topic name]</p>
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Create custom mobile platform message template
    api_response = api_instance.createcustommessagetemplate(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMobilePlatformMessageTemplateApi->createcustommessagetemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomMobileMessageTemplate**](CreateCustomMobileMessageTemplate.md)| Request body for creating custom mobile message template. &lt;p&gt;&amp;nbsp; &amp;nbsp; &amp;nbsp;&lt;strong&gt;Event Data&lt;/strong&gt; : When event data is enabled, Event&#x27;s raw data is shared with mobile.&lt;/p&gt; &lt;p&gt;&amp;nbsp; &amp;nbsp; &amp;nbsp;&lt;strong&gt;Event Type&lt;/strong&gt; : Event topic name.[same as SNS topic name]&lt;/p&gt; | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcustommessagetemplate**
> GetCustomMobileMessageTemplateResponse getcustommessagetemplate(version, event_type=event_type)

This API fetches configured custom mobile message template

This API fetches configured custom mobile message template.

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
api_instance = rainmaker_api_client.CustomMobilePlatformMessageTemplateApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
event_type = 'event_type_example' # str | event type (optional)

try:
    # This API fetches configured custom mobile message template
    api_response = api_instance.getcustommessagetemplate(version, event_type=event_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMobilePlatformMessageTemplateApi->getcustommessagetemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **event_type** | **str**| event type | [optional] 

### Return type

[**GetCustomMobileMessageTemplateResponse**](GetCustomMobileMessageTemplateResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatecustommessagetemplate**
> InlineResponse2005 updatecustommessagetemplate(body, event_type, version)

This API updates the configured custom mobile message template.

This API updates the configured custom mobile message template.

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
api_instance = rainmaker_api_client.CustomMobilePlatformMessageTemplateApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.PublishMessage() # PublishMessage | Request body for updating custom mobile message template
event_type = 'event_type_example' # str | event type
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API updates the configured custom mobile message template.
    api_response = api_instance.updatecustommessagetemplate(body, event_type, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMobilePlatformMessageTemplateApi->updatecustommessagetemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishMessage**](PublishMessage.md)| Request body for updating custom mobile message template | 
 **event_type** | **str**| event type | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

