# rainmaker_api_client.MailDeliveryFailureLogsApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getmailfailures**](MailDeliveryFailureLogsApi.md#getmailfailures) | **GET** /{version}/admin/mail_failures | Get the logs of failures occurred while sending emails

# **getmailfailures**
> GetMailFailureLogsResponse getmailfailures(version, email_id=email_id, failure_type=failure_type, timestamp=timestamp, start_id=start_id, num_records=num_records)

Get the logs of failures occurred while sending emails

This API is used to fetch the details of failure occurred while sending emails to users. Mail failure logs can be fetched by reciepent email ID or Failure Type(Bounce/Complaint/Delivery).Pagination is supported with num_records and start_id query parameters. timestamp query param can be used to fetch records after that timestamp.

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.MailDeliveryFailureLogsApi()
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
email_id = 'email_id_example' # str |  (optional)
failure_type = 'failure_type_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
start_id = 'start_id_example' # str |  (optional)
num_records = 'num_records_example' # str |  (optional)

try:
    # Get the logs of failures occurred while sending emails
    api_response = api_instance.getmailfailures(version, email_id=email_id, failure_type=failure_type, timestamp=timestamp, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDeliveryFailureLogsApi->getmailfailures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **email_id** | **str**|  | [optional] 
 **failure_type** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **start_id** | **str**|  | [optional] 
 **num_records** | **str**|  | [optional] 

### Return type

[**GetMailFailureLogsResponse**](GetMailFailureLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

