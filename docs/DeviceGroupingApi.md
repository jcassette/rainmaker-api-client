# rainmaker_api_client.DeviceGroupingApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptor_deny_user_group_sharing_requests**](DeviceGroupingApi.md#acceptor_deny_user_group_sharing_requests) | **PUT** /{version}/user/node_group/sharing/requests | This API creates the sharing of Node Groups between users.
[**add_user_group_sharing**](DeviceGroupingApi.md#add_user_group_sharing) | **PUT** /{version}/user/node_group/sharing | This API creates the sharing of Groups between users.
[**admingetdevicegroup**](DeviceGroupingApi.md#admingetdevicegroup) | **GET** /{version}/admin/node_group | Get admin device group
[**createdevicegroup**](DeviceGroupingApi.md#createdevicegroup) | **POST** /{version}/admin/node_group | Create admin device group
[**deletedevicegroup**](DeviceGroupingApi.md#deletedevicegroup) | **DELETE** /{version}/admin/node_group | Delete admin device group
[**get_user_group_sharing**](DeviceGroupingApi.md#get_user_group_sharing) | **GET** /{version}/user/node_group/sharing | This API fetches the sharing details for the nodes the current user is associated with.
[**get_user_group_sharing_request**](DeviceGroupingApi.md#get_user_group_sharing_request) | **GET** /{version}/user/node_group/sharing/requests | This API is used to get the sharing requests raised between users.
[**remove_user_group_sharing**](DeviceGroupingApi.md#remove_user_group_sharing) | **DELETE** /{version}/user/node_group/sharing | This API removes the sharing of Groups between the users.
[**remove_user_group_sharing_request**](DeviceGroupingApi.md#remove_user_group_sharing_request) | **DELETE** /{version}/user/node_group/sharing/requests | This API removes the sharing request of Groups between the users.
[**updatedevicegroup**](DeviceGroupingApi.md#updatedevicegroup) | **PUT** /{version}/admin/node_group | Update admin device group
[**usercreatedevicegroup**](DeviceGroupingApi.md#usercreatedevicegroup) | **POST** /{version}/user/node_group | Create the user device group
[**userdeletedevicegroup**](DeviceGroupingApi.md#userdeletedevicegroup) | **DELETE** /{version}/user/node_group | Delete user device group
[**usergetdevicegroup**](DeviceGroupingApi.md#usergetdevicegroup) | **GET** /{version}/user/node_group | Get user device group
[**userupdatedevicegroup**](DeviceGroupingApi.md#userupdatedevicegroup) | **PUT** /{version}/user/node_group | Update user device group

# **acceptor_deny_user_group_sharing_requests**
> InlineResponse2004 acceptor_deny_user_group_sharing_requests(body, version)

This API creates the sharing of Node Groups between users.

This API allows Secondary or Primary user to accept or decline the request for node group sharing sent by the primary users.Here accept and request_id are mandatory parameters

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.AcceptOrDeclineNodeSharingRequest() # AcceptOrDeclineNodeSharingRequest | Accept or Decline Sharing Request
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API creates the sharing of Node Groups between users.
    api_response = api_instance.acceptor_deny_user_group_sharing_requests(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->acceptor_deny_user_group_sharing_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AcceptOrDeclineNodeSharingRequest**](AcceptOrDeclineNodeSharingRequest.md)| Accept or Decline Sharing Request | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_group_sharing**
> InlineResponse2004 add_user_group_sharing(body, version)

This API creates the sharing of Groups between users.

This API allows Primary users to share the groups with other users either with primary or secondary user role. User Name of the secondary user and groups are mandatory parameters.Primary flag to make the users as primary is an optional parameter. Metadata is an optional parameter, used to store additional info about node sharing request.

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.AddUserGroupSharingRequest() # AddUserGroupSharingRequest | Add User Group Sharing
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API creates the sharing of Groups between users.
    api_response = api_instance.add_user_group_sharing(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->add_user_group_sharing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddUserGroupSharingRequest**](AddUserGroupSharingRequest.md)| Add User Group Sharing | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admingetdevicegroup**
> GetAdminDeviceGroupResponse admingetdevicegroup(version, group_id=group_id, group_name=group_name, node_details=node_details, node_type=node_type, node_model=node_model, node_fw_version=node_fw_version, start_id=start_id, num_records=num_records)

Get admin device group

This API will get the details about the admin device group. <ol><li> By Default all the groups with their sub-groups will be returned</li> <li>start_id and num_records are used for pagination of groups.</li> <li>When group_id or group_name is passed then details of that group will be returned, with nodes and subgroups.</li> <ul><li>To get node details set node_details flag to true.</li> <li>start_id and num_records are used for pagination of nodes and node_details.</li> <li>when node details is requested then nodes array will be removed from the output.</li> </ul> <li>If a group is created based on a <i>group_query</i> with some node type, model and firmware version and <b>node_model</b>, <b>node_type</b> and/or <b>node_fw_version</b> are provided, then all the groups that have the exact same <i>group_query</i> filters are returned. <br><font color='red'>Note</font> - If for any such group, some nodes' type, model or firmware version is changed, then the <b>regroup</b> option provided in the PUT API should be used.</li> </ol>

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
group_id = 'group_id_example' # str | group Id (optional)
group_name = 'group_name_example' # str | group Name (optional)
node_details = false # bool | optional flag **(true/false)**, to indicate if the node_details is required in the response (optional) (default to false)
node_type = 'node_type_example' # str | node_type in group_query based group searching (optional)
node_model = 'node_model_example' # str | node_model in group_query based group searching (optional)
node_fw_version = 'node_fw_version_example' # str | node_fw_version in group_query based group searching (optional)
start_id = 'start_id_example' # str | This is used for the pagination (optional)
num_records = '25' # str | This is used for the pagination (optional) (default to 25)

try:
    # Get admin device group
    api_response = api_instance.admingetdevicegroup(version, group_id=group_id, group_name=group_name, node_details=node_details, node_type=node_type, node_model=node_model, node_fw_version=node_fw_version, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->admingetdevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **group_id** | **str**| group Id | [optional] 
 **group_name** | **str**| group Name | [optional] 
 **node_details** | **bool**| optional flag **(true/false)**, to indicate if the node_details is required in the response | [optional] [default to false]
 **node_type** | **str**| node_type in group_query based group searching | [optional] 
 **node_model** | **str**| node_model in group_query based group searching | [optional] 
 **node_fw_version** | **str**| node_fw_version in group_query based group searching | [optional] 
 **start_id** | **str**| This is used for the pagination | [optional] 
 **num_records** | **str**| This is used for the pagination | [optional] [default to 25]

### Return type

[**GetAdminDeviceGroupResponse**](GetAdminDeviceGroupResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createdevicegroup**
> CreateDeviceGroupResponse createdevicegroup(body, version)

Create admin device group

This API will create admin device group

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.AdminNodeGroupBody() # AdminNodeGroupBody | Request body for creating new device group. <br><br><b>Mandatory Parameters:</b> <ul><li>group_name</li></ul> <br> <b>Optional Parameters:</b> <ol><li>nodes -> the list of nodes to be added to the group. </li> <li>parent_group_id</li> <li>description</li> <li>type</li> <li>node_fw_version</li> <li>node_model</li> <li>node_type</li></ol> <br><b>If the nodes list is not specified, then node group is created, without any nodes in it.</b> <br>Note: node_fw_version, node_model, node_type cannot be specified with parent_group_id and nodes.
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Create admin device group
    api_response = api_instance.createdevicegroup(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->createdevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminNodeGroupBody**](AdminNodeGroupBody.md)| Request body for creating new device group. &lt;br&gt;&lt;br&gt;&lt;b&gt;Mandatory Parameters:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;group_name&lt;/li&gt;&lt;/ul&gt; &lt;br&gt; &lt;b&gt;Optional Parameters:&lt;/b&gt; &lt;ol&gt;&lt;li&gt;nodes -&gt; the list of nodes to be added to the group. &lt;/li&gt; &lt;li&gt;parent_group_id&lt;/li&gt; &lt;li&gt;description&lt;/li&gt; &lt;li&gt;type&lt;/li&gt; &lt;li&gt;node_fw_version&lt;/li&gt; &lt;li&gt;node_model&lt;/li&gt; &lt;li&gt;node_type&lt;/li&gt;&lt;/ol&gt; &lt;br&gt;&lt;b&gt;If the nodes list is not specified, then node group is created, without any nodes in it.&lt;/b&gt; &lt;br&gt;Note: node_fw_version, node_model, node_type cannot be specified with parent_group_id and nodes. | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**CreateDeviceGroupResponse**](CreateDeviceGroupResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletedevicegroup**
> APISuccessResponse deletedevicegroup(version, group_id)

Delete admin device group

This API will delete admin device group

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
group_id = 'group_id_example' # str | group id

try:
    # Delete admin device group
    api_response = api_instance.deletedevicegroup(version, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->deletedevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **group_id** | **str**| group id | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_sharing**
> GetUserGroupSharingResponse get_user_group_sharing(version, group_id=group_id, sub_groups=sub_groups, metadata=metadata, parent_groups=parent_groups)

This API fetches the sharing details for the nodes the current user is associated with.

This API is used to fetch the Group sharing details. Here are the details - <ul><li>When no parameters are passed it returns the sharing details of all the groups that this user is associated with (Primary or Secondary)</li> <li>When group_id is passed, it returns the sharing details of that group. The requesting user can be Primary or Secondary.</li> <li>When sub_groups is set as true(with or without groupId), it returns the sharing details of the sub groups as well. The requesting user can be Primary or Secondary.</li> <li>When parent_groups is set as true(with or without groupId), it returns the sharing details of the parent groups as well. The requesting user can be Primary or Secondary.</li> <li>If the Get group sharing API is called by the secondary user, the list of other secondary users this group is associated with, will not be returned.</li></ul>

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
group_id = 'group_id_example' # str | group_id of group to get the sharing details (optional)
sub_groups = false # bool | When set to true returns details of sub-group as well. (optional) (default to false)
metadata = false # bool | When set to true returns metadata that was set during sharing. (optional) (default to false)
parent_groups = false # bool | group_id of group to get the sharing details (optional) (default to false)

try:
    # This API fetches the sharing details for the nodes the current user is associated with.
    api_response = api_instance.get_user_group_sharing(version, group_id=group_id, sub_groups=sub_groups, metadata=metadata, parent_groups=parent_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->get_user_group_sharing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **group_id** | **str**| group_id of group to get the sharing details | [optional] 
 **sub_groups** | **bool**| When set to true returns details of sub-group as well. | [optional] [default to false]
 **metadata** | **bool**| When set to true returns metadata that was set during sharing. | [optional] [default to false]
 **parent_groups** | **bool**| group_id of group to get the sharing details | [optional] [default to false]

### Return type

[**GetUserGroupSharingResponse**](GetUserGroupSharingResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_sharing_request**
> GetGroupSharingRequestResponse get_user_group_sharing_request(version, request_id=request_id, primary_user=primary_user, start_request_id=start_request_id, start_user_name=start_user_name, num_records=num_records)

This API is used to get the sharing requests raised between users.

This API allows the primary and secondary users to get the sharing requests. <ol> <li>To get the requests raised by primary user, with primary_user flag set as true</li> <li>To get the requests received by secondary user</li> <li>To get the details of a request by request_id</li> </ol> To support pagination start_request_id, start_user_name, num_records are added to the API.

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | request Id (optional)
primary_user = 'primary_user_example' # str | This is a boolean flag, which is used to denote whether to get the requests raised by Primary user(true) or received by secondary users (false). Default value for this flag is false. (optional)
start_request_id = 'start_request_id_example' # str | used in pagination (optional)
start_user_name = 'start_user_name_example' # str | used in pagination along with start_request_id (optional)
num_records = 'num_records_example' # str | used to specify the no of records that must be returned. Default value is 10. The valid values are in the range of 1 to 10. If invalid value is given, default value is used. (optional)

try:
    # This API is used to get the sharing requests raised between users.
    api_response = api_instance.get_user_group_sharing_request(version, request_id=request_id, primary_user=primary_user, start_request_id=start_request_id, start_user_name=start_user_name, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->get_user_group_sharing_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request_id** | **str**| request Id | [optional] 
 **primary_user** | **str**| This is a boolean flag, which is used to denote whether to get the requests raised by Primary user(true) or received by secondary users (false). Default value for this flag is false. | [optional] 
 **start_request_id** | **str**| used in pagination | [optional] 
 **start_user_name** | **str**| used in pagination along with start_request_id | [optional] 
 **num_records** | **str**| used to specify the no of records that must be returned. Default value is 10. The valid values are in the range of 1 to 10. If invalid value is given, default value is used. | [optional] 

### Return type

[**GetGroupSharingRequestResponse**](GetGroupSharingRequestResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_group_sharing**
> InlineResponse2005 remove_user_group_sharing(version, groups, user_name)

This API removes the sharing of Groups between the users.

This API allows the primary users to remove the sharing of groups with other users.It also allows secondary users to remove their own sharing with the groups.

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
groups = 'groups_example' # str | Comma separated group_ids (Example groups=group_id1,group_id2)
user_name = 'user_name_example' # str | User Name

try:
    # This API removes the sharing of Groups between the users.
    api_response = api_instance.remove_user_group_sharing(version, groups, user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->remove_user_group_sharing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **groups** | **str**| Comma separated group_ids (Example groups&#x3D;group_id1,group_id2) | 
 **user_name** | **str**| User Name | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_group_sharing_request**
> APISuccessResponse remove_user_group_sharing_request(version, request_id)

This API removes the sharing request of Groups between the users.

This API allows the primary users to remove the sharing request of groups with other users.

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | Request Id

try:
    # This API removes the sharing request of Groups between the users.
    api_response = api_instance.remove_user_group_sharing_request(version, request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->remove_user_group_sharing_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request_id** | **str**| Request Id | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatedevicegroup**
> APISuccessResponse updatedevicegroup(body, group_id, version)

Update admin device group

This API will update admin device group

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdateAdminDeviceGroupRequest() # UpdateAdminDeviceGroupRequest | Request body for updating the existing node group. <ol> <li>Using this API, the user can either add or remove the nodes to the group or change the parameters of the group like group name and type. <li>The value of operation can be <b>add or remove</b>. <li>While adding or removing nodes, nodes array is required to be specified in the request body. <li>For updating group name, description and type , the new values for these parameters need to be specified. <li><b>regroup</b> - this parameter is applicable to only <i>group_query</i> based groups. If a group is created based on a <i>group_query</i> and some nodes' type, model or firmware version is changed, then the <b>regroup</b> option removes nodes which no longer satisfy the <i>group_query</i> and adds newly added/updated nodes which match the <i>group_query</i>. </ol>
group_id = 'group_id_example' # str | group Id
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Update admin device group
    api_response = api_instance.updatedevicegroup(body, group_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->updatedevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAdminDeviceGroupRequest**](UpdateAdminDeviceGroupRequest.md)| Request body for updating the existing node group. &lt;ol&gt; &lt;li&gt;Using this API, the user can either add or remove the nodes to the group or change the parameters of the group like group name and type. &lt;li&gt;The value of operation can be &lt;b&gt;add or remove&lt;/b&gt;. &lt;li&gt;While adding or removing nodes, nodes array is required to be specified in the request body. &lt;li&gt;For updating group name, description and type , the new values for these parameters need to be specified. &lt;li&gt;&lt;b&gt;regroup&lt;/b&gt; - this parameter is applicable to only &lt;i&gt;group_query&lt;/i&gt; based groups. If a group is created based on a &lt;i&gt;group_query&lt;/i&gt; and some nodes&#x27; type, model or firmware version is changed, then the &lt;b&gt;regroup&lt;/b&gt; option removes nodes which no longer satisfy the &lt;i&gt;group_query&lt;/i&gt; and adds newly added/updated nodes which match the &lt;i&gt;group_query&lt;/i&gt;. &lt;/ol&gt; | 
 **group_id** | **str**| group Id | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usercreatedevicegroup**
> CreateDeviceGroupResponse usercreatedevicegroup(body, version)

Create the user device group

This API is used for creating new node group. The maximum level for the Node Group hierarchy can be upto three.

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.CreateDeviceGroupRequest() # CreateDeviceGroupRequest | Request body for creating new device group. <br><br><b>Mandatory Parameters:</b> <ul><li>group_name</li></ul> <br> <b>Optional Parameters:</b> <ol><li>nodes -> the list of nodes to be added to the group. </li> <li>parent_group_id</li> <li>description</li> <li>type</li></li> <li>mutually_exclusive -> When mutually_exclusive flag is true, group will be considered as Mutually exclusive group i.e Nodes which are part of this group can't be part of the other mutually exclusive groups having same group type and same parent(Groups having no parent IDs can also be considered having same parent)</ol> <br><b>If the nodes list is not specified, then node group is created, without any nodes in it.</b>
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Create the user device group
    api_response = api_instance.usercreatedevicegroup(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->usercreatedevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDeviceGroupRequest**](CreateDeviceGroupRequest.md)| Request body for creating new device group. &lt;br&gt;&lt;br&gt;&lt;b&gt;Mandatory Parameters:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;group_name&lt;/li&gt;&lt;/ul&gt; &lt;br&gt; &lt;b&gt;Optional Parameters:&lt;/b&gt; &lt;ol&gt;&lt;li&gt;nodes -&gt; the list of nodes to be added to the group. &lt;/li&gt; &lt;li&gt;parent_group_id&lt;/li&gt; &lt;li&gt;description&lt;/li&gt; &lt;li&gt;type&lt;/li&gt;&lt;/li&gt; &lt;li&gt;mutually_exclusive -&gt; When mutually_exclusive flag is true, group will be considered as Mutually exclusive group i.e Nodes which are part of this group can&#x27;t be part of the other mutually exclusive groups having same group type and same parent(Groups having no parent IDs can also be considered having same parent)&lt;/ol&gt; &lt;br&gt;&lt;b&gt;If the nodes list is not specified, then node group is created, without any nodes in it.&lt;/b&gt; | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**CreateDeviceGroupResponse**](CreateDeviceGroupResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userdeletedevicegroup**
> APISuccessResponse userdeletedevicegroup(version, group_id)

Delete user device group

This API will delete user device group if user is primary.It allows secondary user to remove their own sharing with the group

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
group_id = 'group_id_example' # str | group id

try:
    # Delete user device group
    api_response = api_instance.userdeletedevicegroup(version, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->userdeletedevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **group_id** | **str**| group id | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergetdevicegroup**
> GetUserDeviceGroupResponse usergetdevicegroup(version, group_id=group_id, optional_group_name=optional_group_name, node_list=node_list, sub_groups=sub_groups, node_details=node_details, start_id=start_id, num_records=num_records)

Get user device group

This API will get the details about the user device group. <ol><li>By Default all the groups with their details will be returned</li> <li>To get list of nodes in a group or for all groups, set node_list flag to true.</li> <li>To get sub groups in a group or for all groups, set sub_groups flag to true.</li> <li>start_id and num_records are used for pagination of groups.</li> <li>When group_id is passes then details of that group will be returned.</li> <li>When group_name is passes then details of that group will be returned.</li> <ul> <li>To get node details set node_details flag to true.</li> <li>When node details is requested, the nodes array will be removed from the output.</li></ul> <li>The node_details flag is applicable only when group_id or group_name is passed</li> </ol>

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
group_id = 'group_id_example' # str | group Id (optional)
optional_group_name = 'optional_group_name_example' # str | group Name (optional)
node_list = false # bool | optional flag **(true/false)**, to indicate if the node list is required in the response (optional) (default to false)
sub_groups = false # bool | optional flag **(true/false)**, to indicate if the sub groups list is required in the response (optional) (default to false)
node_details = false # bool | optional flag **(true/false)**, to indicate if the node_details is required in the response (optional) (default to false)
start_id = 'start_id_example' # str | This is used for the pagination (optional)
num_records = '25' # str | This is used for the pagination (optional) (default to 25)

try:
    # Get user device group
    api_response = api_instance.usergetdevicegroup(version, group_id=group_id, optional_group_name=optional_group_name, node_list=node_list, sub_groups=sub_groups, node_details=node_details, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->usergetdevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **group_id** | **str**| group Id | [optional] 
 **optional_group_name** | **str**| group Name | [optional] 
 **node_list** | **bool**| optional flag **(true/false)**, to indicate if the node list is required in the response | [optional] [default to false]
 **sub_groups** | **bool**| optional flag **(true/false)**, to indicate if the sub groups list is required in the response | [optional] [default to false]
 **node_details** | **bool**| optional flag **(true/false)**, to indicate if the node_details is required in the response | [optional] [default to false]
 **start_id** | **str**| This is used for the pagination | [optional] 
 **num_records** | **str**| This is used for the pagination | [optional] [default to 25]

### Return type

[**GetUserDeviceGroupResponse**](GetUserDeviceGroupResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userupdatedevicegroup**
> APISuccessResponse userupdatedevicegroup(body, group_id, version)

Update user device group

This API will update user device group

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
api_instance = rainmaker_api_client.DeviceGroupingApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.UpdateDeviceGroupRequest() # UpdateDeviceGroupRequest | Request body for updating the existing node group. <ol><li>Using this API, the user can either add or remove the nodes to the group or change the parameters of the group like group name and type. <li>The value of operation can be <b>add or remove</b>. <li>While adding or removing nodes, nodes array is required to be specified in the request body. <li>For updating group name, description and type , the new values for these parameters need to be specified. <li>mutually_exclusive -> When mutually_exclusive flag is true, group will be considered as Mutually exclusive group i.e Nodes which are part of this group can't be part of the other mutually exclusive groups having same group type and same parent(Groups having no parent IDs can also be considered having same parent)
group_id = 'group_id_example' # str | group Id
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Update user device group
    api_response = api_instance.userupdatedevicegroup(body, group_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupingApi->userupdatedevicegroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDeviceGroupRequest**](UpdateDeviceGroupRequest.md)| Request body for updating the existing node group. &lt;ol&gt;&lt;li&gt;Using this API, the user can either add or remove the nodes to the group or change the parameters of the group like group name and type. &lt;li&gt;The value of operation can be &lt;b&gt;add or remove&lt;/b&gt;. &lt;li&gt;While adding or removing nodes, nodes array is required to be specified in the request body. &lt;li&gt;For updating group name, description and type , the new values for these parameters need to be specified. &lt;li&gt;mutually_exclusive -&gt; When mutually_exclusive flag is true, group will be considered as Mutually exclusive group i.e Nodes which are part of this group can&#x27;t be part of the other mutually exclusive groups having same group type and same parent(Groups having no parent IDs can also be considered having same parent) | 
 **group_id** | **str**| group Id | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

