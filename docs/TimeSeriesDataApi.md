# rainmaker_api_client.TimeSeriesDataApi

All URIs are relative to *https://{API Url}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ts_data**](TimeSeriesDataApi.md#get_ts_data) | **GET** /{version}/user/nodes/tsdata | This API is used to get the Time Series Data

# **get_ts_data**
> TSAPISuccessResponse get_ts_data(version, node_id, param_name, aggregate=aggregate, aggregation_interval=aggregation_interval, type=type, week_start=week_start, start_time=start_time, end_time=end_time, num_intervals=num_intervals, start_id=start_id, num_records=num_records, timezone=timezone)

This API is used to get the Time Series Data

<p>This API is used to get the time series data for various measures like temperature, humidity, electric current, etc. reported by nodes. This information can be queried based on parameter name and aggregation interval. <br>The data can be retrieved for different aggregation intervals like minute, hour, day, week, month or year clubbed with query parameters <b>num_intervals</b> to specify the number of interval starting from today or <b>start_time and end_time</b> to specify the date and time range. <ol> <li><b>Minute</b> - Max Interval: 1 day or 1440 minutes</li> <li><b>Hour</b> - Max Interval: 1 day or 24 hours</li> <li><b>Day</b> - Max Interval: 31 days and end_time must be strictly greater than the start_time.</li> <li><b>Week</b> - Max Interval: 12 weeks. week_start parameter is used to specify the start Day of the week. Ex: Monday</li> <li><b>Month</b> - Max Interval: 12 months</li> <li><b>Year</b> - Max Interval: 5 years</li> <li><b>Raw</b> - Max Interval: 31 days</li> </ol></p> <p>Aggregates supported by different data types: <ol> <li><b>float</b> - All</li> <li><b>int</b> - All</li> <li><b>bool</b> - raw, latest, count</li> <li><b>string</b> - raw, latest, count</li> </ol></p> <p><font color='red'>Note: </font> <li>If aggregate is provided then either <b>start_time and end_time</b> or <b>num_interval</b> needs to be provided for each query.</li> <li>If aggregate is not provided then raw data is returned for last 7 days.</li> <li>The Range of data that is retrieved are [StartTime,EndTime) or [ CurrentTime - NumInterval, CurrentTime)</li> <li>When using start_id the inputs passed (apart from start_id and num_records) need to be kept the same for every call.</li> <li>Aggregate: latest is not supported for AggregationInterval: Month and Year</li> <li>When TimeZone is provided the start time and end time are also in the provided time zone</li> </p>

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
api_instance = rainmaker_api_client.TimeSeriesDataApi(rainmaker_api_client.ApiClient(configuration))
version = 'version_example' # str | API Version (Current supported API Version is 'v1')
node_id = 'node_id_example' # str | This parameter is used to specify the node ID for which measures needs to be fetched.
param_name = 'param_name_example' # str | Some examples of the parameter names are - <li>temperature</li> <li>humidity</li> <li>electric_current</li> A single valid measure need to be passed.
aggregate = 'raw' # str | Following aggregate functions are supported - (To be changed) <li><b>raw</b> - Returns all the actual values reported by device in given time range. This is the default value for the parameter.</li> <li><b>latest</b> - Returns the last entry reported by the device for the given aggregation interval and time range</li> <li><b>min</b> - Returns the min value reported by the device for the given aggregation interval and time range</li> <li><b>max</b> - Returns the max value reported by the device for the given aggregation interval and time range</li> <li><b>count</b> - Returns the number of values reported by the device for the given aggregation interval and time range</li> <li><b>avg</b> - Returns the avg values reported by the device for the given aggregation interval and time range</li> <br> Only one aggregate function can be specified at a time. (optional) (default to raw)
aggregation_interval = 'aggregation_interval_example' # str | This parameter is used to specify the aggregation interval for the params. They can be - <li>minute</li> <li>hour</li> <li>day</li> <li>week</li> <li>month</li> <li>year</li> <p>It is not applicable when aggregate is passed as raw.</p> (optional)
type = 'float' # str | This parameter is used to specify the data type of the param. They can be - <li>float</li> <li>int</li> <li>bool</li> <li>string</li> (optional) (default to float)
week_start = 'Monday' # str | This parameter is used to specify the start day of the week. This field is case insensitive. Only applicable in cases were the time_interval value is <b>week</b>. (optional) (default to Monday)
start_time = 1.2 # float | This parameter is used to set the start time. The expected Format for start time is epoch time in seconds. Ex: 1628557200 (optional)
end_time = 1.2 # float | This parameter is used to set the end time. The expected Format for end_date is epoch time in seconds. Ex: 1628557200 (optional)
num_intervals = 1.2 # float | The user can specify either the start_time and end_time or num_intervals parameter. If the num_intervals is specified, then the API will fetch the data from the current time for the previous 'n' intervals. <p>i.e <br> If <i>time_interval=day, aggregate=avg, parameter_name=temperature , device_id=1234</i> <br> <i>num_intervals=5</i> <br> The output would have data for previous 5 days starting from today. Not Applicable for Aggregate=Raw.</p> (optional)
start_id = 'start_id_example' # str | This parameter is used for pagination. <br><b>The pagination token can be used for up to 5 Query Invocations, OR for a duration of up to 1 hour whichever comes first.</b> (optional)
num_records = 200 # float | This parameter is used for pagination. Max Value = 200 (optional) (default to 200)
timezone = 'UTC' # str | This parameter is used to set the timezone(location) from where the query is made, based on <a href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>IANA Tz Database name</a>. TimeZone can also be provided like EST but location name is preferred. This field is case-insensitive. (optional) (default to UTC)

try:
    # This API is used to get the Time Series Data
    api_response = api_instance.get_ts_data(version, node_id, param_name, aggregate=aggregate, aggregation_interval=aggregation_interval, type=type, week_start=week_start, start_time=start_time, end_time=end_time, num_intervals=num_intervals, start_id=start_id, num_records=num_records, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesDataApi->get_ts_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API Version (Current supported API Version is &#x27;v1&#x27;) | 
 **node_id** | **str**| This parameter is used to specify the node ID for which measures needs to be fetched. | 
 **param_name** | **str**| Some examples of the parameter names are - &lt;li&gt;temperature&lt;/li&gt; &lt;li&gt;humidity&lt;/li&gt; &lt;li&gt;electric_current&lt;/li&gt; A single valid measure need to be passed. | 
 **aggregate** | **str**| Following aggregate functions are supported - (To be changed) &lt;li&gt;&lt;b&gt;raw&lt;/b&gt; - Returns all the actual values reported by device in given time range. This is the default value for the parameter.&lt;/li&gt; &lt;li&gt;&lt;b&gt;latest&lt;/b&gt; - Returns the last entry reported by the device for the given aggregation interval and time range&lt;/li&gt; &lt;li&gt;&lt;b&gt;min&lt;/b&gt; - Returns the min value reported by the device for the given aggregation interval and time range&lt;/li&gt; &lt;li&gt;&lt;b&gt;max&lt;/b&gt; - Returns the max value reported by the device for the given aggregation interval and time range&lt;/li&gt; &lt;li&gt;&lt;b&gt;count&lt;/b&gt; - Returns the number of values reported by the device for the given aggregation interval and time range&lt;/li&gt; &lt;li&gt;&lt;b&gt;avg&lt;/b&gt; - Returns the avg values reported by the device for the given aggregation interval and time range&lt;/li&gt; &lt;br&gt; Only one aggregate function can be specified at a time. | [optional] [default to raw]
 **aggregation_interval** | **str**| This parameter is used to specify the aggregation interval for the params. They can be - &lt;li&gt;minute&lt;/li&gt; &lt;li&gt;hour&lt;/li&gt; &lt;li&gt;day&lt;/li&gt; &lt;li&gt;week&lt;/li&gt; &lt;li&gt;month&lt;/li&gt; &lt;li&gt;year&lt;/li&gt; &lt;p&gt;It is not applicable when aggregate is passed as raw.&lt;/p&gt; | [optional] 
 **type** | **str**| This parameter is used to specify the data type of the param. They can be - &lt;li&gt;float&lt;/li&gt; &lt;li&gt;int&lt;/li&gt; &lt;li&gt;bool&lt;/li&gt; &lt;li&gt;string&lt;/li&gt; | [optional] [default to float]
 **week_start** | **str**| This parameter is used to specify the start day of the week. This field is case insensitive. Only applicable in cases were the time_interval value is &lt;b&gt;week&lt;/b&gt;. | [optional] [default to Monday]
 **start_time** | **float**| This parameter is used to set the start time. The expected Format for start time is epoch time in seconds. Ex: 1628557200 | [optional] 
 **end_time** | **float**| This parameter is used to set the end time. The expected Format for end_date is epoch time in seconds. Ex: 1628557200 | [optional] 
 **num_intervals** | **float**| The user can specify either the start_time and end_time or num_intervals parameter. If the num_intervals is specified, then the API will fetch the data from the current time for the previous &#x27;n&#x27; intervals. &lt;p&gt;i.e &lt;br&gt; If &lt;i&gt;time_interval&#x3D;day, aggregate&#x3D;avg, parameter_name&#x3D;temperature , device_id&#x3D;1234&lt;/i&gt; &lt;br&gt; &lt;i&gt;num_intervals&#x3D;5&lt;/i&gt; &lt;br&gt; The output would have data for previous 5 days starting from today. Not Applicable for Aggregate&#x3D;Raw.&lt;/p&gt; | [optional] 
 **start_id** | **str**| This parameter is used for pagination. &lt;br&gt;&lt;b&gt;The pagination token can be used for up to 5 Query Invocations, OR for a duration of up to 1 hour whichever comes first.&lt;/b&gt; | [optional] 
 **num_records** | **float**| This parameter is used for pagination. Max Value &#x3D; 200 | [optional] [default to 200]
 **timezone** | **str**| This parameter is used to set the timezone(location) from where the query is made, based on &lt;a href&#x3D;&#x27;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones&#x27;&gt;IANA Tz Database name&lt;/a&gt;. TimeZone can also be provided like EST but location name is preferred. This field is case-insensitive. | [optional] [default to UTC]

### Return type

[**TSAPISuccessResponse**](TSAPISuccessResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

