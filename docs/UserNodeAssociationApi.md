# rainmaker_api_client.UserNodeAssociationApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_user_node_mapping**](UserNodeAssociationApi.md#add_remove_user_node_mapping) | **PUT** /{version}/user/nodes/mapping | Add or Remove the User Node mapping
[**add_user_node_sharing**](UserNodeAssociationApi.md#add_user_node_sharing) | **PUT** /{version}/user/nodes/sharing | This API creates the sharing of Nodes between users.
[**add_user_node_sharing_requests**](UserNodeAssociationApi.md#add_user_node_sharing_requests) | **PUT** /{version}/user/nodes/sharing/requests | This API creates the sharing of Nodes between users.
[**addtags**](UserNodeAssociationApi.md#addtags) | **PUT** /{version}/user/nodes | Add tags to Node
[**get_admin_user_nodes**](UserNodeAssociationApi.md#get_admin_user_nodes) | **GET** /{version}/admin/nodes | Get the nodes claimed by the Admin user
[**get_node_status**](UserNodeAssociationApi.md#get_node_status) | **GET** /{version}/user/nodes/status | Get the online or offline status for the node
[**get_user_node_configuration**](UserNodeAssociationApi.md#get_user_node_configuration) | **GET** /{version}/user/nodes/config | Get the configuration for the node
[**get_user_node_mapping_request_status**](UserNodeAssociationApi.md#get_user_node_mapping_request_status) | **GET** /{version}/user/nodes/mapping | Get the status of User Node mapping request
[**get_user_node_sharing**](UserNodeAssociationApi.md#get_user_node_sharing) | **GET** /{version}/user/nodes/sharing | This API fetches the sharing details for the nodes the current user is associated with.
[**get_user_node_sharing_request**](UserNodeAssociationApi.md#get_user_node_sharing_request) | **GET** /{version}/user/nodes/sharing/requests | This API is used to get the sharing requests raised between users.
[**get_user_nodes**](UserNodeAssociationApi.md#get_user_nodes) | **GET** /{version}/user/nodes | Get the nodes associated with the user
[**get_user_nodes_for_admins**](UserNodeAssociationApi.md#get_user_nodes_for_admins) | **GET** /{version}/admin/user/nodes | Get the nodes associated with a user
[**remove_user_node_sharing**](UserNodeAssociationApi.md#remove_user_node_sharing) | **DELETE** /{version}/user/nodes/sharing | This API removes the sharing of Nodes between the users.
[**remove_user_node_sharing_request**](UserNodeAssociationApi.md#remove_user_node_sharing_request) | **DELETE** /{version}/user/nodes/sharing/requests | This API removes the sharing request of Nodes between the users.
[**update_node_certificate_status**](UserNodeAssociationApi.md#update_node_certificate_status) | **PUT** /{version}/admin/nodes | Activate or Deactivate the Node

# **add_remove_user_node_mapping**
> InlineResponse2003 add_remove_user_node_mapping(body, version)

Add or Remove the User Node mapping

<ul> <li>You can optionally specify tags and metadata.</li> <li>Nodes can be searched by tags.</li> <li>If tags are not provided in the request, and <b>esp.location</b> is present in the user's custom_data, then all the keys starting with <b>esp</b> under it are converted to tags.</li> </ul>

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.AddRemoveUserNodeMappingRequest() # AddRemoveUserNodeMappingRequest | Add or Remove User Node Mapping Request Parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # Add or Remove the User Node mapping
    api_response = api_instance.add_remove_user_node_mapping(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->add_remove_user_node_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddRemoveUserNodeMappingRequest**](AddRemoveUserNodeMappingRequest.md)| Add or Remove User Node Mapping Request Parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_node_sharing**
> InlineResponse2004 add_user_node_sharing(body, version)

This API creates the sharing of Nodes between users.

This API allows <ol> <li>Primary users to share the nodes with other users either with primary user role or secondary. User Name of the requested user and nodes are mandatory parameters. Primary flag for adding user with primary role is an optional parameter.Metadata is an optional parameter, used to store an additional info about node sharing request.</li> <li>Requested user can accept or decline the request for node sharing sent by the primary users. Here accept and request_id are mandatory parameters</li> </ol>

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.NodesSharingBody() # NodesSharingBody | Add User Node Sharing / Accept or Decline Sharing Request Parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API creates the sharing of Nodes between users.
    api_response = api_instance.add_user_node_sharing(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->add_user_node_sharing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodesSharingBody**](NodesSharingBody.md)| Add User Node Sharing / Accept or Decline Sharing Request Parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_node_sharing_requests**
> InlineResponse2004 add_user_node_sharing_requests(body, version)

This API creates the sharing of Nodes between users.

This API allows <ol> <li>Primary users to share the nodes with other users either with primary user role or secondary. User Name of the requested user and nodes are mandatory parameters. Primary flag for adding user with primary role is an optional parameter.Metadata is an optional parameter, used to store additional info about node sharing request.</li> <li>Requested user can accept or decline the request for node sharing sent by the primary users. Here accept and request_id are mandatory parameters</li> </ol>

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
body = rainmaker_api_client.SharingRequestsBody() # SharingRequestsBody | Add User Node Sharing / Accept or Decline Sharing Request Parameters
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # This API creates the sharing of Nodes between users.
    api_response = api_instance.add_user_node_sharing_requests(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->add_user_node_sharing_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharingRequestsBody**](SharingRequestsBody.md)| Add User Node Sharing / Accept or Decline Sharing Request Parameters | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addtags**
> APISuccessResponse addtags(node_id, version, body=body)

Add tags to Node

This api is used to attach tags to Node

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
node_id = 'node_id_example' # str | Used to specify nodeId
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.NodeAttachTagsRequest() # NodeAttachTagsRequest | Request body for attaching tags with the node. (optional)

try:
    # Add tags to Node
    api_response = api_instance.addtags(node_id, version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->addtags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Used to specify nodeId | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**NodeAttachTagsRequest**](NodeAttachTagsRequest.md)| Request body for attaching tags with the node. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_user_nodes**
> InlineResponse2006 get_admin_user_nodes(version, num_records=num_records, start_id=start_id, node_id=node_id, type=type, model=model, fw_version=fw_version, tags=tags, node_status=node_status)

Get the nodes claimed by the Admin user

This API is to get the node details of nodes claimed by the admin: <li>When no parameter is passed list of all the nodes and nodeInfo are returned.</li> <li>When type is passed, list of all the nodes and nodeInfo which are of that type are returned.</li> <li>When model & type is passed, list of all the nodes and nodeInfo which are of that model & type are returned.</li> <ul><li><b>Note: type is a required parameter if model is provided.</b></li></ul> <li>When model, type & fw_version is passed, list of all the nodes and nodeInfo which are of that model, type & fw_version are returned.</li> <ul><li><b>Note: model & type is a required parameter if fw_version is provided.</b></li></ul> <li>When node status is passed, list of all the nodes and nodeInfo that have the given status are returned.</li> <ul><li>Node status can also be provided in conjunction with tags, type, model & fw_version</li></ul> <li>When node_id is passed the details of that node (NodeInfo) is returned</li> <p>To support pagination num_records and start_id are present</p> 

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
num_records = 'num_records_example' # str | Used for pagination, number of records to be fetched (optional)
start_id = 'start_id_example' # str | Used for pagination, Start Id of the record to be fetched (optional)
node_id = 'node_id_example' # str | Used to fetch details of particular node (optional)
type = 'type_example' # str | Used to fetch list of nodes based on type. (optional)
model = 'model_example' # str | Used to fetch list of nodes based on model and type. (optional)
fw_version = 'fw_version_example' # str | Used to fetch list of nodes based on model, type & fw_version. (optional)
tags = 'tags_example' # str | Used to fetch list of nodes based on tags. (optional)
node_status = 'node_status_example' # str | Used to fetch list of nodes based on node status. They can be not_activated, online, offline, deactivated. (optional)

try:
    # Get the nodes claimed by the Admin user
    api_response = api_instance.get_admin_user_nodes(version, num_records=num_records, start_id=start_id, node_id=node_id, type=type, model=model, fw_version=fw_version, tags=tags, node_status=node_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_admin_user_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **num_records** | **str**| Used for pagination, number of records to be fetched | [optional] 
 **start_id** | **str**| Used for pagination, Start Id of the record to be fetched | [optional] 
 **node_id** | **str**| Used to fetch details of particular node | [optional] 
 **type** | **str**| Used to fetch list of nodes based on type. | [optional] 
 **model** | **str**| Used to fetch list of nodes based on model and type. | [optional] 
 **fw_version** | **str**| Used to fetch list of nodes based on model, type &amp; fw_version. | [optional] 
 **tags** | **str**| Used to fetch list of nodes based on tags. | [optional] 
 **node_status** | **str**| Used to fetch list of nodes based on node status. They can be not_activated, online, offline, deactivated. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_status**
> NodeConnectivity get_node_status(version, node_id)

Get the online or offline status for the node

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node id

try:
    # Get the online or offline status for the node
    api_response = api_instance.get_node_status(version, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node id | 

### Return type

[**NodeConnectivity**](NodeConnectivity.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_node_configuration**
> NodeConfiguration get_user_node_configuration(version, node_id)

Get the configuration for the node

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node id

try:
    # Get the configuration for the node
    api_response = api_instance.get_user_node_configuration(version, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_user_node_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node id | 

### Return type

[**NodeConfiguration**](NodeConfiguration.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_node_mapping_request_status**
> AddUserNodeMappingRequestStatus get_user_node_mapping_request_status(version, request_id)

Get the status of User Node mapping request

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | request Id

try:
    # Get the status of User Node mapping request
    api_response = api_instance.get_user_node_mapping_request_status(version, request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_user_node_mapping_request_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **request_id** | **str**| request Id | 

### Return type

[**AddUserNodeMappingRequestStatus**](AddUserNodeMappingRequestStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_node_sharing**
> GetUserNodeSharingResponse get_user_node_sharing(version, node_id=node_id)

This API fetches the sharing details for the nodes the current user is associated with.

This API is used to fetch the Node sharing details. Here are the details - <ul><li>When no parameters are passed it returns the sharing details of all the nodes that this user is associated with (Primary or Secondary)</li> <li>When node_id is passed, it returns the sharing details of that node. The requesting user can be Primary or Secondary.</li> <li>If this API is called by the secondary user, the list of other secondary users this node is associated with, is not returned but the sources from where this node was shared will be returned.</li> <ul><li>When <b>NODE</b> is present in the sources array it represents that it was shared via Node sharing</li> <li>Else it was shared via Group sharing and the list will have group Ids</li></ul> </ul>

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node Id of node to get the sharing details (optional)

try:
    # This API fetches the sharing details for the nodes the current user is associated with.
    api_response = api_instance.get_user_node_sharing(version, node_id=node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_user_node_sharing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node Id of node to get the sharing details | [optional] 

### Return type

[**GetUserNodeSharingResponse**](GetUserNodeSharingResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_node_sharing_request**
> GetNodeSharingRequestResponse get_user_node_sharing_request(version, request_id=request_id, primary_user=primary_user, start_request_id=start_request_id, start_user_name=start_user_name, num_records=num_records)

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | request Id (optional)
primary_user = 'primary_user_example' # str | This is a boolean flag, which is used to denote whether to get the requests raised by Primary user(true) or received by secondary users (false). Default value for this flag is false. (optional)
start_request_id = 'start_request_id_example' # str | used in pagination (optional)
start_user_name = 'start_user_name_example' # str | used in pagination along with start_request_id (optional)
num_records = 'num_records_example' # str | used to specify the no of records that must be returned. Default value is 10. The valid values are in the range of 1 to 10. If invalid value is given, default value is used. (optional)

try:
    # This API is used to get the sharing requests raised between users.
    api_response = api_instance.get_user_node_sharing_request(version, request_id=request_id, primary_user=primary_user, start_request_id=start_request_id, start_user_name=start_user_name, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_user_node_sharing_request: %s\n" % e)
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

[**GetNodeSharingRequestResponse**](GetNodeSharingRequestResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_nodes**
> GetNodesList get_user_nodes(version, node_id=node_id, node_details=node_details, status=status, config=config, params=params, start_id=start_id, num_records=num_records, tags=tags)

Get the nodes associated with the user

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | node Id of node to get the node details (optional)
node_details = false # bool | optional flag **(true/false)**, to indicate if the node details are required in the response (optional) (default to false)
status = true # bool | optional flag **(true/false)**, to indicate if the node details should contain status in the response or not. (optional) (default to true)
config = true # bool | optional flag **(true/false)**, to indicate if the node details should contain config in the response or not. (optional) (default to true)
params = true # bool | optional flag **(true/false)**, to indicate if the node details should contain params in the response or not. (optional) (default to true)
start_id = 'start_id_example' # str | use next_id from the response as start_id to fetch the next set of records (optional)
num_records = 'num_records_example' # str | number of nodes to fetch (optional)
tags = 'tags_example' # str | Used to fetch list of nodes based on tags. (optional)

try:
    # Get the nodes associated with the user
    api_response = api_instance.get_user_nodes(version, node_id=node_id, node_details=node_details, status=status, config=config, params=params, start_id=start_id, num_records=num_records, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_user_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| node Id of node to get the node details | [optional] 
 **node_details** | **bool**| optional flag **(true/false)**, to indicate if the node details are required in the response | [optional] [default to false]
 **status** | **bool**| optional flag **(true/false)**, to indicate if the node details should contain status in the response or not. | [optional] [default to true]
 **config** | **bool**| optional flag **(true/false)**, to indicate if the node details should contain config in the response or not. | [optional] [default to true]
 **params** | **bool**| optional flag **(true/false)**, to indicate if the node details should contain params in the response or not. | [optional] [default to true]
 **start_id** | **str**| use next_id from the response as start_id to fetch the next set of records | [optional] 
 **num_records** | **str**| number of nodes to fetch | [optional] 
 **tags** | **str**| Used to fetch list of nodes based on tags. | [optional] 

### Return type

[**GetNodesList**](GetNodesList.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_nodes_for_admins**
> InlineResponse2009 get_user_nodes_for_admins(version, user_id=user_id, user_name=user_name, role=role, start_id=start_id, num_records=num_records)

Get the nodes associated with a user

This API is accessible to superadmins. Fetches the nodes associated with the user with query parameter <b>user_id</b> or <b>user_name</b>. <br>If role is specified as a query parameter (primary or secondary), then the nodes with that role are returned.

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
user_id = 'user_id_example' # str | user_id of the user whose nodes are to be fetched. (optional)
user_name = 'user_name_example' # str | email or phone number of the user whose nodes are to be fetched, whatever user has used to sign up. Example - username@domain.com or +<phone number with country code> (optional)
role = 'role_example' # str | the nodes associated with the user returned will have this specified role. Default - both primary and secondary (optional)
start_id = 'start_id_example' # str | use next_id from the response as start_id to fetch the next set of records (optional)
num_records = 'num_records_example' # str | number of nodes to fetch (optional)

try:
    # Get the nodes associated with a user
    api_response = api_instance.get_user_nodes_for_admins(version, user_id=user_id, user_name=user_name, role=role, start_id=start_id, num_records=num_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->get_user_nodes_for_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **user_id** | **str**| user_id of the user whose nodes are to be fetched. | [optional] 
 **user_name** | **str**| email or phone number of the user whose nodes are to be fetched, whatever user has used to sign up. Example - username@domain.com or +&lt;phone number with country code&gt; | [optional] 
 **role** | **str**| the nodes associated with the user returned will have this specified role. Default - both primary and secondary | [optional] 
 **start_id** | **str**| use next_id from the response as start_id to fetch the next set of records | [optional] 
 **num_records** | **str**| number of nodes to fetch | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_node_sharing**
> InlineResponse2005 remove_user_node_sharing(version, nodes, user_name)

This API removes the sharing of Nodes between the users.

This API allows the primary users to remove the sharing of nodes with other users.

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
nodes = 'nodes_example' # str | Comma separated nodeids (Example nodes=nodeid1,nodeid2)
user_name = 'user_name_example' # str | User Name

try:
    # This API removes the sharing of Nodes between the users.
    api_response = api_instance.remove_user_node_sharing(version, nodes, user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->remove_user_node_sharing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **nodes** | **str**| Comma separated nodeids (Example nodes&#x3D;nodeid1,nodeid2) | 
 **user_name** | **str**| User Name | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_node_sharing_request**
> APISuccessResponse remove_user_node_sharing_request(version, request_id)

This API removes the sharing request of Nodes between the users.

This API allows the primary users to remove the sharing request of nodes with other users.

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
request_id = 'request_id_example' # str | Request Id

try:
    # This API removes the sharing request of Nodes between the users.
    api_response = api_instance.remove_user_node_sharing_request(version, request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->remove_user_node_sharing_request: %s\n" % e)
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

# **update_node_certificate_status**
> APISuccessResponse update_node_certificate_status(activate, node_id, version, body=body)

Activate or Deactivate the Node

This api is used to activate or deactivate the Node or attach tags

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
api_instance = rainmaker_api_client.UserNodeAssociationApi(rainmaker_api_client.ApiClient(configuration))
activate = true # bool | Used for specifying either to activate the node or deactivate the node
node_id = 'node_id_example' # str | Used to specify nodeId
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
body = rainmaker_api_client.NodeAttachTagsRequest() # NodeAttachTagsRequest | Request body for attaching tags with the node. (optional)

try:
    # Activate or Deactivate the Node
    api_response = api_instance.update_node_certificate_status(activate, node_id, version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserNodeAssociationApi->update_node_certificate_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate** | **bool**| Used for specifying either to activate the node or deactivate the node | 
 **node_id** | **str**| Used to specify nodeId | 
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **body** | [**NodeAttachTagsRequest**](NodeAttachTagsRequest.md)| Request body for attaching tags with the node. | [optional] 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

