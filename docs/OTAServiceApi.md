# rainmaker_api_client.OTAServiceApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminuploadotaimage**](OTAServiceApi.md#adminuploadotaimage) | **POST** /{version}/admin/otaimage | This API is used for uploading a new Firmware image
[**archive_or_unarchive_ota_image**](OTAServiceApi.md#archive_or_unarchive_ota_image) | **PUT** /{version}/admin/otaimage | Archive/Unarchive an OTA image
[**cancel_or_archive_ota_job**](OTAServiceApi.md#cancel_or_archive_ota_job) | **PUT** /{version}/admin/otajob | Cancel/Archive an OTA job
[**createotajob**](OTAServiceApi.md#createotajob) | **POST** /{version}/admin/otajob | This API creates a new OTA job
[**delete_ota_image**](OTAServiceApi.md#delete_ota_image) | **DELETE** /{version}/admin/otaimage | Delete the  OTA Image for the user
[**get_ota_image**](OTAServiceApi.md#get_ota_image) | **GET** /{version}/admin/otaimage | Get the details about OTA images for the user
[**get_ota_job**](OTAServiceApi.md#get_ota_job) | **GET** /{version}/admin/otajob | Get the details about OTA jobs for the user
[**get_ota_job_status**](OTAServiceApi.md#get_ota_job_status) | **GET** /{version}/admin/otajob/status | This API provides status of the the OTA job
[**get_ota_job_status_summary**](OTAServiceApi.md#get_ota_job_status_summary) | **GET** /{version}/admin/otajob/status/summary | This API provides summary of the the OTA job
[**getnodeotastatus**](OTAServiceApi.md#getnodeotastatus) | **GET** /{version}/user/nodes/ota_status | Get latest status of OTA update for the node associated with the user
[**getotaupdate**](OTAServiceApi.md#getotaupdate) | **GET** /{version}/user/nodes/ota_update | Get latest OTA update for the node associated with the user
[**o_ta_image_upload_confirm_url**](OTAServiceApi.md#o_ta_image_upload_confirm_url) | **POST** /{version}/admin/otaimage/upload_confirm | This API is used to confirm the upload Firmware image.
[**o_ta_image_upload_request_url**](OTAServiceApi.md#o_ta_image_upload_request_url) | **GET** /{version}/admin/otaimage/upload_request | Get pre-signed url to upload the firmware image to S3
[**postotaupdate**](OTAServiceApi.md#postotaupdate) | **POST** /{version}/user/nodes/ota_update | Push OTA update to the node
[**useruploadotaimage**](OTAServiceApi.md#useruploadotaimage) | **POST** /{version}/user/otaimage | API for the end user to upload a new firmware image

# **adminuploadotaimage**
> OtaImageCreateResponse adminuploadotaimage(body, version)

This API is used for uploading a new Firmware image

This API uploads the new Firmware image to Rainmaker Cloud.

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.OtaImageCreateRequest() # OtaImageCreateRequest | Request body for uploading new firmware image. List of optional parameters <ul> <li>fw_version</li> <li>model</li> <li>type</li> </ul> <h3>These above parameters will be fetched from base64_fwimage when not passed in request body.<br> If absent in both places then error will be returned.</h3>
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API is used for uploading a new Firmware image
    api_response = api_instance.adminuploadotaimage(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->adminuploadotaimage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OtaImageCreateRequest**](OtaImageCreateRequest.md)| Request body for uploading new firmware image. List of optional parameters &lt;ul&gt; &lt;li&gt;fw_version&lt;/li&gt; &lt;li&gt;model&lt;/li&gt; &lt;li&gt;type&lt;/li&gt; &lt;/ul&gt; &lt;h3&gt;These above parameters will be fetched from base64_fwimage when not passed in request body.&lt;br&gt; If absent in both places then error will be returned.&lt;/h3&gt; | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**OtaImageCreateResponse**](OtaImageCreateResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_or_unarchive_ota_image**
> APISuccessResponse archive_or_unarchive_ota_image(version, ota_image_id, archive)

Archive/Unarchive an OTA image

This API archives/unarchives the OTA image for the user

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
ota_image_id = 'ota_image_id_example' # str | OTA image id
archive = true # bool | Archives the image when true and unarchives the image when false

try:
    # Archive/Unarchive an OTA image
    api_response = api_instance.archive_or_unarchive_ota_image(version, ota_image_id, archive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->archive_or_unarchive_ota_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **ota_image_id** | **str**| OTA image id | 
 **archive** | **bool**| Archives the image when true and unarchives the image when false | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_or_archive_ota_job**
> OTACancelJob cancel_or_archive_ota_job(body, version)

Cancel/Archive an OTA job

This API cancels/archives OTA job. The user needs to specify the OTA Job Id and archive flag in request body. <br><b>NOTE: An OTA Job can be archived only when it is in canceled state.</b>

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.OtaJobCancelRequest() # OtaJobCancelRequest | Request body for cancelling/archiving OTA Job
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Cancel/Archive an OTA job
    api_response = api_instance.cancel_or_archive_ota_job(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->cancel_or_archive_ota_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OtaJobCancelRequest**](OtaJobCancelRequest.md)| Request body for cancelling/archiving OTA Job | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**OTACancelJob**](OTACancelJob.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createotajob**
> OtaJobCreateResponse createotajob(body, version, force_push=force_push, user_approval=user_approval, notify=notify)

This API creates a new OTA job

This API creates a new OTA job. The user needs to specify the OTA Image ID, Job name, nodes and/or groups. Currently, the OTA update can be pushed for upto 100 nodes and/or 10 groups of nodes or all claimed nodes (Group:FFFF-FFFF) in a single request. For pushing the OTA Update to a group of nodes, the **groups** parameter must be filled with a list of group IDs. For pushing the OTA update to all the claimed nodes, user needs to specify the group_id as **FFFF-FFFF** <br><b>NOTE: The OTA image must have unarchived status.</b>

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.OtaJobCreateRequest() # OtaJobCreateRequest | Request body for creating a new OTA Job
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
force_push = 'false' # str | Force push OTA image (optional) (default to false)
user_approval = 'false' # str | If true, OTA can be pushed to node by end users (optional) (default to false)
notify = 'false' # str | Indicates if end user should be notified about OTA job (optional) (default to false)

try:
    # This API creates a new OTA job
    api_response = api_instance.createotajob(body, version, force_push=force_push, user_approval=user_approval, notify=notify)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->createotajob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OtaJobCreateRequest**](OtaJobCreateRequest.md)| Request body for creating a new OTA Job | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **force_push** | **str**| Force push OTA image | [optional] [default to false]
 **user_approval** | **str**| If true, OTA can be pushed to node by end users | [optional] [default to false]
 **notify** | **str**| Indicates if end user should be notified about OTA job | [optional] [default to false]

### Return type

[**OtaJobCreateResponse**](OtaJobCreateResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ota_image**
> APISuccessResponse delete_ota_image(version, ota_image_id, force_delete=force_delete)

Delete the  OTA Image for the user

This API deletes the OTA image for the user, if it is not used in any of the OTA jobs. If the OTA image is used in any of the OTA jobs, an error is returned.

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
ota_image_id = 'ota_image_id_example' # str | OTA Image Id
force_delete = 'false' # str | Delete the OTA Image forcefully (Even if it is associated with any cancelled OTA Job) (optional) (default to false)

try:
    # Delete the  OTA Image for the user
    api_response = api_instance.delete_ota_image(version, ota_image_id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->delete_ota_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **ota_image_id** | **str**| OTA Image Id | 
 **force_delete** | **str**| Delete the OTA Image forcefully (Even if it is associated with any cancelled OTA Job) | [optional] [default to false]

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ota_image**
> InlineResponse2007 get_ota_image(version, ota_image_id=ota_image_id, image_name=image_name, type=type, model=model, num_records=num_records, start_id=start_id, contains=contains, archived=archived, all=all)

Get the details about OTA images for the user

This API gives the details about the OTA image. If the ota_image_id or the ota_image_name is not specified, all the images for the user are returned. <li>If contains flag is set to true, pattern search will be applied on image_name specified.</li>

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
ota_image_id = 'ota_image_id_example' # str | OTA Image Id (optional)
image_name = 'image_name_example' # str | OTA Image Name (optional)
type = 'type_example' # str | OTA Image Type (optional)
model = 'model_example' # str | OTA Image Model (optional)
num_records = 'num_records_example' # str | Used for pagination, number of records to be fetched (optional)
start_id = 'start_id_example' # str | Used for pagination, Start Id of the record to be fetched (optional)
contains = false # bool | For pattern search on image_name (optional) (default to false)
archived = false # bool | If set to true, will return only archived OTA images (optional) (default to false)
all = false # bool | If set to true, will return all images irrespective of archived status (optional) (default to false)

try:
    # Get the details about OTA images for the user
    api_response = api_instance.get_ota_image(version, ota_image_id=ota_image_id, image_name=image_name, type=type, model=model, num_records=num_records, start_id=start_id, contains=contains, archived=archived, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->get_ota_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **ota_image_id** | **str**| OTA Image Id | [optional] 
 **image_name** | **str**| OTA Image Name | [optional] 
 **type** | **str**| OTA Image Type | [optional] 
 **model** | **str**| OTA Image Model | [optional] 
 **num_records** | **str**| Used for pagination, number of records to be fetched | [optional] 
 **start_id** | **str**| Used for pagination, Start Id of the record to be fetched | [optional] 
 **contains** | **bool**| For pattern search on image_name | [optional] [default to false]
 **archived** | **bool**| If set to true, will return only archived OTA images | [optional] [default to false]
 **all** | **bool**| If set to true, will return all images irrespective of archived status | [optional] [default to false]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ota_job**
> InlineResponse2008 get_ota_job(version, ota_job_id=ota_job_id, ota_job_name=ota_job_name, ota_image_id=ota_image_id, num_records=num_records, start_id=start_id, archived=archived, all=all)

Get the details about OTA jobs for the user

This API provides the details about the OTA job created by the user. <ol><li>If the user specifies <b>ota_job_id</b> or <b>ota_job_name</b>, then the details about the specific job are returned. In case of ota_job_name all jobs which contain the pattern are returned.</li> <li>If <b>ota_image_id</b> is provided then the latest ota job that is not archived by the user with that image id will be returned and if <b>archived</b> is set as true then latest ota job that is archived by the user with that image id will be returned </li> <li>If <b>archived</b> is provided as true, then the all ota job that are archived by the user will be returned</li> <li>If <b>all</b> is provided as true, then all the OTA jobs created by the user are returned</li> <li>else the details about all the OTA jobs that have been created by the user and are not archived will be returned.</li></ol>

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
ota_job_id = 'ota_job_id_example' # str | OTA Job Id (optional)
ota_job_name = 'ota_job_name_example' # str | OTA Job name - Pattern (optional)
ota_image_id = 'ota_image_id_example' # str | OTA Image Id (optional)
num_records = 'num_records_example' # str | Used for pagination, number of records to be fetched (optional)
start_id = 'start_id_example' # str | Used for pagination, Start Id of the record to be fetched (optional)
archived = false # bool | Flag to get archived ota jobs. [Valid values are true/false] (optional) (default to false)
all = false # bool | Flag to get all the ota jobs irrespective whether a job is archived or not. [Valid values are true/false] (optional) (default to false)

try:
    # Get the details about OTA jobs for the user
    api_response = api_instance.get_ota_job(version, ota_job_id=ota_job_id, ota_job_name=ota_job_name, ota_image_id=ota_image_id, num_records=num_records, start_id=start_id, archived=archived, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->get_ota_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **ota_job_id** | **str**| OTA Job Id | [optional] 
 **ota_job_name** | **str**| OTA Job name - Pattern | [optional] 
 **ota_image_id** | **str**| OTA Image Id | [optional] 
 **num_records** | **str**| Used for pagination, number of records to be fetched | [optional] 
 **start_id** | **str**| Used for pagination, Start Id of the record to be fetched | [optional] 
 **archived** | **bool**| Flag to get archived ota jobs. [Valid values are true/false] | [optional] [default to false]
 **all** | **bool**| Flag to get all the ota jobs irrespective whether a job is archived or not. [Valid values are true/false] | [optional] [default to false]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ota_job_status**
> OtaJobNodeStatusResponse get_ota_job_status(version, ota_job_id, node_id=node_id, summary=summary, num_records=num_records, start_id=start_id)

This API provides status of the the OTA job

This API provides the status of the OTA job. It provides the details about the OTA job and the latest OTA status for the nodes. 

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
ota_job_id = 'ota_job_id_example' # str | OTA Job Id
node_id = 'node_id_example' # str | node Id (optional)
summary = true # bool | OTA Job summary (optional)
num_records = 'num_records_example' # str | Used for pagination, number of records to be fetched (optional)
start_id = 'start_id_example' # str | Used for pagination, Start Id of the record to be fetched (optional)

try:
    # This API provides status of the the OTA job
    api_response = api_instance.get_ota_job_status(version, ota_job_id, node_id=node_id, summary=summary, num_records=num_records, start_id=start_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->get_ota_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **ota_job_id** | **str**| OTA Job Id | 
 **node_id** | **str**| node Id | [optional] 
 **summary** | **bool**| OTA Job summary | [optional] 
 **num_records** | **str**| Used for pagination, number of records to be fetched | [optional] 
 **start_id** | **str**| Used for pagination, Start Id of the record to be fetched | [optional] 

### Return type

[**OtaJobNodeStatusResponse**](OtaJobNodeStatusResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ota_job_status_summary**
> OtaJobSummaryResponse get_ota_job_status_summary(version, ota_job_id)

This API provides summary of the the OTA job

This API provides the summary of the OTA job. It provides the count of nodes with various OTA status -  **triggered, in_progress, success, failed and the total count**. 

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
ota_job_id = 'v1' # str | OTA Job Id (default to v1)

try:
    # This API provides summary of the the OTA job
    api_response = api_instance.get_ota_job_status_summary(version, ota_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->get_ota_job_status_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **ota_job_id** | **str**| OTA Job Id | [default to v1]

### Return type

[**OtaJobSummaryResponse**](OtaJobSummaryResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getnodeotastatus**
> UserGetOtaStatusResponse getnodeotastatus(version, node_id, ota_job_id)

Get latest status of OTA update for the node associated with the user

Using this API the end user can check the latest status of the OTA Job, for node which is associated with his account

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node Id
ota_job_id = 'ota_job_id_example' # str | OTA Job Id

try:
    # Get latest status of OTA update for the node associated with the user
    api_response = api_instance.getnodeotastatus(version, node_id, ota_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->getnodeotastatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node Id | 
 **ota_job_id** | **str**| OTA Job Id | 

### Return type

[**UserGetOtaStatusResponse**](UserGetOtaStatusResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getotaupdate**
> UserOTAUpdateRequest getotaupdate(version, node_id)

Get latest OTA update for the node associated with the user

Using this API the end user can check if there is any OTA update, for the node which is associated with his account

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node Id

try:
    # Get latest OTA update for the node associated with the user
    api_response = api_instance.getotaupdate(version, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->getotaupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node Id | 

### Return type

[**UserOTAUpdateRequest**](UserOTAUpdateRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_ta_image_upload_confirm_url**
> OtaImageCreateResponse o_ta_image_upload_confirm_url(body, version)

This API is used to confirm the upload Firmware image.

After the admin uploads the OTA image to S3 bucket, this API needs to be called. It is expected that the admin will upload the OTA image binary separately using a suitable tool with the help of the pre-signed upload URL returned by the <b>GET: /admin/otaimage/upload_request</b>. <br><ul> <li><b>fw_version</b> and <b>model</b> should be provided if not present in the uploaded OTA image binary. It can also be used to override the binary <b>fw_version</b> and <b>model</b>. <li>It returns the S3 URL of the OTA image.</li> <li>If you have uploaded an invalid OTA Image file, it will be deleted completely. You will have to reupload a valid one on the <b>upload_url</b> again.</ul>

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.OTAImageUploadConfirmRequest() # OTAImageUploadConfirmRequest | Request body for confirming OTA image upload
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API is used to confirm the upload Firmware image.
    api_response = api_instance.o_ta_image_upload_confirm_url(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->o_ta_image_upload_confirm_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OTAImageUploadConfirmRequest**](OTAImageUploadConfirmRequest.md)| Request body for confirming OTA image upload | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**OtaImageCreateResponse**](OtaImageCreateResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_ta_image_upload_request_url**
> GetUploadOTAImagePreSignedUrlResponse o_ta_image_upload_request_url(version, image_name)

Get pre-signed url to upload the firmware image to S3

This API is used to fetch presigned upload_url (<b>Validity:</b> 1 hour) to upload the firmware image. <br><br>The user needs to specify the OTA <b>image_name</b>. This <b>image_name</b> is independent of the firmware image binary file name.  <br><br><b>Note:</b><ul><li>If already existing OTA <b>image_name</b> is given and the OTA image is not referenced by any OTA job, it will be replaced. This action cannot be undone.</li><li> The client will have to send a PUT HTTP request to the <b>upload_url</b> with headers -<br> ```'Content-type': 'application/octet-stream','x-amz-acl': 'public-read'```</li><li> If <b>upload_url</b> is expired you will get a <b>403 Forbidden</b> response. You may fetch a new <b>upload_url</b>.</li><li>Maximum supported OTA Image size is <font color='red'>16 MB</font>.</li></ul>

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
image_name = 'image_name_example' # str | Name of the OTA firmware image to be uploaded

try:
    # Get pre-signed url to upload the firmware image to S3
    api_response = api_instance.o_ta_image_upload_request_url(version, image_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->o_ta_image_upload_request_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **image_name** | **str**| Name of the OTA firmware image to be uploaded | 

### Return type

[**GetUploadOTAImagePreSignedUrlResponse**](GetUploadOTAImagePreSignedUrlResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postotaupdate**
> APISuccessResponse postotaupdate(version, body=body)

Push OTA update to the node

Using this API the end user can push OTA update to the node which is associated with his account

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.UserPushOtaUpdateRequest() # UserPushOtaUpdateRequest | Request body for uploading new firmware image. ota_job_id and node_id are required parameters. (optional)

try:
    # Push OTA update to the node
    api_response = api_instance.postotaupdate(version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->postotaupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**UserPushOtaUpdateRequest**](UserPushOtaUpdateRequest.md)| Request body for uploading new firmware image. ota_job_id and node_id are required parameters. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **useruploadotaimage**
> UserOTAImageResponse useruploadotaimage(body, version)

API for the end user to upload a new firmware image

Using this API end user can upload a new firmware image. Using image url received in the response, the user can push the OTA for the device

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
api_instance = rainmaker_api_client.OTAServiceApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UserOTAImageRequest() # UserOTAImageRequest | Request body for uploading new firmware image. type is optional parameter.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # API for the end user to upload a new firmware image
    api_response = api_instance.useruploadotaimage(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OTAServiceApi->useruploadotaimage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserOTAImageRequest**](UserOTAImageRequest.md)| Request body for uploading new firmware image. type is optional parameter. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**UserOTAImageResponse**](UserOTAImageResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

