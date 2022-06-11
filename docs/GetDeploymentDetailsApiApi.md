# rainmaker_api_client.GetDeploymentDetailsApiApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployment_details**](GetDeploymentDetailsApiApi.md#get_deployment_details) | **GET** /{version}/admin/rainmaker_deployment_details | Get the deployment details

# **get_deployment_details**
> InlineResponse20012 get_deployment_details(version, email_mobile_userpool=email_mobile_userpool, pre_requisite=pre_requisite)

Get the deployment details

This API is used to fetch the deployment details

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.GetDeploymentDetailsApiApi()
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
email_mobile_userpool = false # bool |  (optional) (default to false)
pre_requisite = false # bool |  (optional) (default to false)

try:
    # Get the deployment details
    api_response = api_instance.get_deployment_details(version, email_mobile_userpool=email_mobile_userpool, pre_requisite=pre_requisite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDeploymentDetailsApiApi->get_deployment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **email_mobile_userpool** | **bool**|  | [optional] [default to false]
 **pre_requisite** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

