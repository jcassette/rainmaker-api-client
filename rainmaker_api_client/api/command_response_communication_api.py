# coding: utf-8

"""
    API Definitions for RainMaker Backend Service

    This Swagger file provides the details about the RainMaker platform APIs.<br><br> There are two types of APIs supported by RainMaker - Unauthenticated and Authenticated.<br> The authenticated APIs are marked in the Swagger file, with a “lock” sign in front of them.<br> For the Unauthenticated APIs, there is no need to provide any authentication tokens in the HTTP header.<br> When the user logs in successfully, he receives access_token in the response. For the Authenticated APIs, this access_token needs to be passed in the \"Authorization\" HTTP header as the authentication token.<br> <br> <b>Note:</b><br><ul><li>RainMaker APIs do not support using double slashes after the resources or methods. Including a double slash goes against HTTP best practices. <br><li>The RainMaker APIs do not support following HTTP headers - data, verify and cookies.</ul>  # noqa: E501

    OpenAPI spec version: 1.1.17-fd1c887_2022-05-24T06:46
    Contact: esp-rainmaker-admin@espressif.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rainmaker_api_client.api_client import ApiClient


class CommandResponseCommunicationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_cmd_response_requests(self, version, request_id, **kwargs):  # noqa: E501
        """Get the Command Response Requests  # noqa: E501

        Get the Command Response Requests for a given request id. If node id is provided then request corresponding to the request id and node id is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cmd_response_requests(version, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :param str request_id: ID of the command response request. (required)
        :param str node_id: ID of the node
        :param str start_id: Used for pagination.
        :param float num_records: Used for pagination, number of records to be fetched.
        :return: CmdResponseGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cmd_response_requests_with_http_info(version, request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cmd_response_requests_with_http_info(version, request_id, **kwargs)  # noqa: E501
            return data

    def get_cmd_response_requests_with_http_info(self, version, request_id, **kwargs):  # noqa: E501
        """Get the Command Response Requests  # noqa: E501

        Get the Command Response Requests for a given request id. If node id is provided then request corresponding to the request id and node id is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cmd_response_requests_with_http_info(version, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :param str request_id: ID of the command response request. (required)
        :param str node_id: ID of the node
        :param str start_id: Used for pagination.
        :param float num_records: Used for pagination, number of records to be fetched.
        :return: CmdResponseGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'request_id', 'node_id', 'start_id', 'num_records']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cmd_response_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_cmd_response_requests`")  # noqa: E501
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `get_cmd_response_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_id' in params:
            query_params.append(('request_id', params['request_id']))  # noqa: E501
        if 'node_id' in params:
            query_params.append(('node_id', params['node_id']))  # noqa: E501
        if 'start_id' in params:
            query_params.append(('start_id', params['start_id']))  # noqa: E501
        if 'num_records' in params:
            query_params.append(('num_records', params['num_records']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{version}/user/nodes/cmd', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CmdResponseGetRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cmd_response_requests2(self, version, request_id, **kwargs):  # noqa: E501
        """Get the Command Response Requests  # noqa: E501

        Get the Command Response Requests for a given request id. If node id is provided then request corresponding to the request id and node id is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cmd_response_requests2(version, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :param str request_id: ID of the command response request. (required)
        :param str node_id: ID of the node
        :param str start_id: Used for pagination.
        :param float num_records: Used for pagination, number of records to be fetched.
        :return: CmdResponseGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cmd_response_requests2_with_http_info(version, request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cmd_response_requests2_with_http_info(version, request_id, **kwargs)  # noqa: E501
            return data

    def get_cmd_response_requests2_with_http_info(self, version, request_id, **kwargs):  # noqa: E501
        """Get the Command Response Requests  # noqa: E501

        Get the Command Response Requests for a given request id. If node id is provided then request corresponding to the request id and node id is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cmd_response_requests2_with_http_info(version, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :param str request_id: ID of the command response request. (required)
        :param str node_id: ID of the node
        :param str start_id: Used for pagination.
        :param float num_records: Used for pagination, number of records to be fetched.
        :return: CmdResponseGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'request_id', 'node_id', 'start_id', 'num_records']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cmd_response_requests2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_cmd_response_requests2`")  # noqa: E501
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `get_cmd_response_requests2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_id' in params:
            query_params.append(('request_id', params['request_id']))  # noqa: E501
        if 'node_id' in params:
            query_params.append(('node_id', params['node_id']))  # noqa: E501
        if 'start_id' in params:
            query_params.append(('start_id', params['start_id']))  # noqa: E501
        if 'num_records' in params:
            query_params.append(('num_records', params['num_records']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{version}/admin/nodes/cmd', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CmdResponseGetRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_cmd_response_requests(self, body, version, **kwargs):  # noqa: E501
        """Add a Command Response Request  # noqa: E501

        Used to add a Command Response Request. There can be maximum of 25 nodes in a single request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_cmd_response_requests(body, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CmdResponsePostRequest body: Add a request to Command Response (required)
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: CmdResponsePostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_cmd_response_requests_with_http_info(body, version, **kwargs)  # noqa: E501
        else:
            (data) = self.post_cmd_response_requests_with_http_info(body, version, **kwargs)  # noqa: E501
            return data

    def post_cmd_response_requests_with_http_info(self, body, version, **kwargs):  # noqa: E501
        """Add a Command Response Request  # noqa: E501

        Used to add a Command Response Request. There can be maximum of 25 nodes in a single request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_cmd_response_requests_with_http_info(body, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CmdResponsePostRequest body: Add a request to Command Response (required)
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: CmdResponsePostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_cmd_response_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_cmd_response_requests`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `post_cmd_response_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{version}/user/nodes/cmd', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CmdResponsePostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_cmd_response_requests_admin(self, body, version, **kwargs):  # noqa: E501
        """Add a Command Response Request  # noqa: E501

        Used to add a Command Response Request. There can be maximum of 25 nodes in a single request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_cmd_response_requests_admin(body, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CmdResponsePostRequest body: Add a request to Command Response (required)
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: CmdResponsePostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_cmd_response_requests_admin_with_http_info(body, version, **kwargs)  # noqa: E501
        else:
            (data) = self.post_cmd_response_requests_admin_with_http_info(body, version, **kwargs)  # noqa: E501
            return data

    def post_cmd_response_requests_admin_with_http_info(self, body, version, **kwargs):  # noqa: E501
        """Add a Command Response Request  # noqa: E501

        Used to add a Command Response Request. There can be maximum of 25 nodes in a single request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_cmd_response_requests_admin_with_http_info(body, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CmdResponsePostRequest body: Add a request to Command Response (required)
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: CmdResponsePostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_cmd_response_requests_admin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_cmd_response_requests_admin`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `post_cmd_response_requests_admin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{version}/admin/nodes/cmd', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CmdResponsePostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)