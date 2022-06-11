# rainmaker_api_client.StatisticalServiceApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatisticalServiceApi.md#get_stats) | **GET** /{version}/admin/stats_info | This API is used to get the statistical info
[**init_stats**](StatisticalServiceApi.md#init_stats) | **POST** /{version}/admin/stats_init | To Initialize data for stats service

# **get_stats**
> StatsAPISuccessResponse get_stats(version, metric_name=metric_name, duration=duration, start_date=start_date, end_date=end_date, start_month=start_month, end_month=end_month, start_year=start_year, end_year=end_year, timezone=timezone)

This API is used to get the statistical info

This API is used to get the statistical information for the various Rainmaker operational parameters like, number of registered users or number of registered nodes, etc. This information can be queried based on the parameter name and the duration. <br>The metrics data can be retrieved based on daily count, weekly count, monthly count or yearly count.  Only one duration parameter can be specified as the query parameter. <ol> <li>If none of these stats parameters or duration is specified in the request parameter, then the values for all the stats parameters with their total count is returned as the response.</li> <li>Daily Count -  The start_date and end_date parameters are used to specify the date range, which is only applicable for daily_count. The difference between start and end dates can be maximum of 31 days and the end_date must be strictly greater than the start_date. The start date and end date should be specified in the YYYY-MM-DD format.</li> <li>Weekly Count - The start_month, start_year, end_month, end_year parameters are used to specify the date range for weekly_count. The weekly data can be queried for upto 3 Months</li> <li>Monthly Count - The start_month, start_year, end_month, end_year parameters are used to specify the date range for monthly_count. The monthly data can be queried for upto 12 Months</li> <li>Yearly Count - The start_year, end_year parameters are used to specify the date range for yearly_count. The yearly data can be queried for upto 5 years.</li> </ol>

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
api_instance = rainmaker_api_client.StatisticalServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
metric_name = 'metric_name_example' # str | There are various metrics supported. They are - <li>num_registered_users</li> <li>num_registered_nodes</li> <li>num_users_with_nodes</li> <li>num_users_without_nodes</li> <li>num_timed_out_node_association_reqs</li> <li>num_claimed_nodes</li> <li>num_online_nodes</li> <li>num_offline_nodes</li> Multiple stats parameters can be retrieved in one request, these parameters need to be separated by comma in the request. (optional)
duration = 'duration_example' # str | This parameter is user to set the duration of the count .They can be - <li>daily_count</li> <li>weekly_count</li> <li>monthly_count</li> <li>yearly_count</li> Multiple duration parameters cannot be specified in one request (optional)
start_date = 'start_date_example' # str | This parameter is used to set the start_date, which is applicable only for daily_count. The expected Format for start_date is YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | This parameter is used to set the end_date, which is applicable only for daily_count. The expected Format for end_date is YYYY-MM-DD (optional)
start_month = 'start_month_example' # str | This parameter is used to set the start_month, which is applicable only for weekly_count and monthly_count. The expected Format for start_month is month name like January. This field is case-insensitive. (optional)
end_month = 'end_month_example' # str | This parameter is used to set the end_month, which is applicable only for weekly_count and monthly_count. The expected Format for end_month is month name like January. This field is case-insensitive. (optional)
start_year = 'start_year_example' # str | This parameter is used to set the start_year, which is applicable only for weekly_count, monthly_count and yearly_count. The expected Format for start_year is YYYY (optional)
end_year = 'end_year_example' # str | This parameter is used to set the end_year, which is applicable only for weekly_count, monthly_count and yearly_count. The expected Format for end_year is YYYY (optional)
timezone = 'UTC' # str | This parameter is used to set the timezone(location) from where the query is made, based on <a href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>IANA Tz Database name</a>. TimeZone can also be provided like EST but location name is preferred. This field is case-insensitive. (optional) (default to UTC)

try:
    # This API is used to get the statistical info
    api_response = api_instance.get_stats(version, metric_name=metric_name, duration=duration, start_date=start_date, end_date=end_date, start_month=start_month, end_month=end_month, start_year=start_year, end_year=end_year, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticalServiceApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **metric_name** | **str**| There are various metrics supported. They are - &lt;li&gt;num_registered_users&lt;/li&gt; &lt;li&gt;num_registered_nodes&lt;/li&gt; &lt;li&gt;num_users_with_nodes&lt;/li&gt; &lt;li&gt;num_users_without_nodes&lt;/li&gt; &lt;li&gt;num_timed_out_node_association_reqs&lt;/li&gt; &lt;li&gt;num_claimed_nodes&lt;/li&gt; &lt;li&gt;num_online_nodes&lt;/li&gt; &lt;li&gt;num_offline_nodes&lt;/li&gt; Multiple stats parameters can be retrieved in one request, these parameters need to be separated by comma in the request. | [optional] 
 **duration** | **str**| This parameter is user to set the duration of the count .They can be - &lt;li&gt;daily_count&lt;/li&gt; &lt;li&gt;weekly_count&lt;/li&gt; &lt;li&gt;monthly_count&lt;/li&gt; &lt;li&gt;yearly_count&lt;/li&gt; Multiple duration parameters cannot be specified in one request | [optional] 
 **start_date** | **str**| This parameter is used to set the start_date, which is applicable only for daily_count. The expected Format for start_date is YYYY-MM-DD | [optional] 
 **end_date** | **str**| This parameter is used to set the end_date, which is applicable only for daily_count. The expected Format for end_date is YYYY-MM-DD | [optional] 
 **start_month** | **str**| This parameter is used to set the start_month, which is applicable only for weekly_count and monthly_count. The expected Format for start_month is month name like January. This field is case-insensitive. | [optional] 
 **end_month** | **str**| This parameter is used to set the end_month, which is applicable only for weekly_count and monthly_count. The expected Format for end_month is month name like January. This field is case-insensitive. | [optional] 
 **start_year** | **str**| This parameter is used to set the start_year, which is applicable only for weekly_count, monthly_count and yearly_count. The expected Format for start_year is YYYY | [optional] 
 **end_year** | **str**| This parameter is used to set the end_year, which is applicable only for weekly_count, monthly_count and yearly_count. The expected Format for end_year is YYYY | [optional] 
 **timezone** | **str**| This parameter is used to set the timezone(location) from where the query is made, based on &lt;a href&#x3D;&#x27;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones&#x27;&gt;IANA Tz Database name&lt;/a&gt;. TimeZone can also be provided like EST but location name is preferred. This field is case-insensitive. | [optional] [default to UTC]

### Return type

[**StatsAPISuccessResponse**](StatsAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_stats**
> APISuccessResponse init_stats(version)

To Initialize data for stats service

This API is used to initialize data onto the stats table.

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
api_instance = rainmaker_api_client.StatisticalServiceApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')

try:
    # To Initialize data for stats service
    api_response = api_instance.init_stats(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticalServiceApi->init_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 

### Return type

[**APISuccessResponse**](APISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

