# rainmaker_api_client.CustomUserDataForSuperadminsApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_data_for_admins**](CustomUserDataForSuperadminsApi.md#get_user_data_for_admins) | **GET** /{version}/admin/custom_data | Get the Custom user data
[**store_user_data_for_admins**](CustomUserDataForSuperadminsApi.md#store_user_data_for_admins) | **PUT** /{version}/admin/custom_data | Store the custom User data

# **get_user_data_for_admins**
> InlineResponse2002 get_user_data_for_admins(version, user_id=user_id, user_email=user_email, user_phone_number=user_phone_number)

Get the Custom user data

Fetches the custom user data of the user whose id, email or phone_number is provided in query parameters. Can be accessed by super admin users.

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
api_instance = rainmaker_api_client.CustomUserDataForSuperadminsApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_id = 'user_id_example' # str | user_id of the user whose data is to be fetched. (optional)
user_email = 'user_email_example' # str | email of the user whose data is to be fetched, if user has used email to sign up. Example - username@domain.com (optional)
user_phone_number = 'user_phone_number_example' # str | phone_number of the user whose data is to be fetched, if user has used phone_number to sign up. Example - <+Mobile Number with country code> (optional)

try:
    # Get the Custom user data
    api_response = api_instance.get_user_data_for_admins(version, user_id=user_id, user_email=user_email, user_phone_number=user_phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserDataForSuperadminsApi->get_user_data_for_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_id** | **str**| user_id of the user whose data is to be fetched. | [optional] 
 **user_email** | **str**| email of the user whose data is to be fetched, if user has used email to sign up. Example - username@domain.com | [optional] 
 **user_phone_number** | **str**| phone_number of the user whose data is to be fetched, if user has used phone_number to sign up. Example - &lt;+Mobile Number with country code&gt; | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_user_data_for_admins**
> UserDataRequestResponse store_user_data_for_admins(version, body=body, user_id=user_id, user_email=user_email, user_phone_number=user_phone_number)

Store the custom User data

To store or update the custom user data of the user whose id, email or phone_number is provided in query parameters. Can be accessed by super admin users.. <b>Operations on Data:</b> <ul> <li>The data can be deleted by putting data: <b>null</b>. <li>If the key is already present, then the value will be replaced. Arrays will also be replaced entirely. <li>If the key is not present, then the value will be added. <li>If the value is <b>null</b>, then the key-value will be deleted. </ul><b>Note</b>: The JSON size should not exceed 399 KB.

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
api_instance = rainmaker_api_client.CustomUserDataForSuperadminsApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.AdminCustomDataBody() # AdminCustomDataBody |  (optional)
user_id = 'user_id_example' # str | user_id of the user whose data is to be updated (optional)
user_email = 'user_email_example' # str | email of the user whose data is to be updated, if user has used email to sign up. Example - username@domain.com (optional)
user_phone_number = 'user_phone_number_example' # str | phone_number of the user whose data is to be updated, if user has used phone_number to sign up. Example - <+Mobile Number with country code> (optional)

try:
    # Store the custom User data
    api_response = api_instance.store_user_data_for_admins(version, body=body, user_id=user_id, user_email=user_email, user_phone_number=user_phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserDataForSuperadminsApi->store_user_data_for_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**AdminCustomDataBody**](AdminCustomDataBody.md)|  | [optional] 
 **user_id** | **str**| user_id of the user whose data is to be updated | [optional] 
 **user_email** | **str**| email of the user whose data is to be updated, if user has used email to sign up. Example - username@domain.com | [optional] 
 **user_phone_number** | **str**| phone_number of the user whose data is to be updated, if user has used phone_number to sign up. Example - &lt;+Mobile Number with country code&gt; | [optional] 

### Return type

[**UserDataRequestResponse**](UserDataRequestResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

