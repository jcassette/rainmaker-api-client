# rainmaker_api_client.IOTEndpointApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_iot_end_point**](IOTEndpointApi.md#get_iot_end_point) | **GET** /mqtt_host | Fetch the IOT endpoint

# **get_iot_end_point**
> FetchMqttEndpointResponse get_iot_end_point()

Fetch the IOT endpoint

This API will Get the IOT endpoint

### Example
```python
from __future__ import print_function
import time
import rainmaker_api_client
from rainmaker_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rainmaker_api_client.IOTEndpointApi()

try:
    # Fetch the IOT endpoint
    api_response = api_instance.get_iot_end_point()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IOTEndpointApi->get_iot_end_point: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FetchMqttEndpointResponse**](FetchMqttEndpointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

