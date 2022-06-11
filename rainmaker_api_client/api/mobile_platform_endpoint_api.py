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


class MobilePlatformEndpointApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deleteplatformendpoint(self, version, **kwargs):  # noqa: E501
        """This API removes the configured platform endpoint.  # noqa: E501

        This API removes the configured platform endpoint. Either mobile_device_token or endpoint must be specified in query params.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deleteplatformendpoint(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :param str mobile_device_token: mobile device token
        :param str endpoint: platform endpoint ARN
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deleteplatformendpoint_with_http_info(version, **kwargs)  # noqa: E501
        else:
            (data) = self.deleteplatformendpoint_with_http_info(version, **kwargs)  # noqa: E501
            return data

    def deleteplatformendpoint_with_http_info(self, version, **kwargs):  # noqa: E501
        """This API removes the configured platform endpoint.  # noqa: E501

        This API removes the configured platform endpoint. Either mobile_device_token or endpoint must be specified in query params.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deleteplatformendpoint_with_http_info(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :param str mobile_device_token: mobile device token
        :param str endpoint: platform endpoint ARN
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'mobile_device_token', 'endpoint']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deleteplatformendpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `deleteplatformendpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'mobile_device_token' in params:
            query_params.append(('mobile_device_token', params['mobile_device_token']))  # noqa: E501
        if 'endpoint' in params:
            query_params.append(('endpoint', params['endpoint']))  # noqa: E501

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
            '/{version}/user/push_notification/mobile_platform_endpoint', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getplatformendpoint(self, version, **kwargs):  # noqa: E501
        """This API fetches configured platform endpoints  # noqa: E501

        This API fetches configured platform endpoints  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getplatformendpoint(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: GetPlatformEndpointResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getplatformendpoint_with_http_info(version, **kwargs)  # noqa: E501
        else:
            (data) = self.getplatformendpoint_with_http_info(version, **kwargs)  # noqa: E501
            return data

    def getplatformendpoint_with_http_info(self, version, **kwargs):  # noqa: E501
        """This API fetches configured platform endpoints  # noqa: E501

        This API fetches configured platform endpoints  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getplatformendpoint_with_http_info(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: GetPlatformEndpointResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getplatformendpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `getplatformendpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

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
            '/{version}/user/push_notification/mobile_platform_endpoint', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPlatformEndpointResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def platformendpointcreation(self, body, version, **kwargs):  # noqa: E501
        """Creates the new platform endpoint for the user's Mobile device  # noqa: E501

        This API will be called from the Mobile App by the end user, to subscribe to Push Notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.platformendpointcreation(body, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlatformEndpointCreateRequest body: Request body for creating new platform application, Valid values for platform are GCM, APNS or APNS_SANDBOX. (required)
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: PlatformEndpointAPISuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.platformendpointcreation_with_http_info(body, version, **kwargs)  # noqa: E501
        else:
            (data) = self.platformendpointcreation_with_http_info(body, version, **kwargs)  # noqa: E501
            return data

    def platformendpointcreation_with_http_info(self, body, version, **kwargs):  # noqa: E501
        """Creates the new platform endpoint for the user's Mobile device  # noqa: E501

        This API will be called from the Mobile App by the end user, to subscribe to Push Notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.platformendpointcreation_with_http_info(body, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlatformEndpointCreateRequest body: Request body for creating new platform application, Valid values for platform are GCM, APNS or APNS_SANDBOX. (required)
        :param str version: API Version (Current supported API Version is 'v1') (required)
        :return: PlatformEndpointAPISuccessResponse
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
                    " to method platformendpointcreation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `platformendpointcreation`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `platformendpointcreation`")  # noqa: E501

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
            '/{version}/user/push_notification/mobile_platform_endpoint', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlatformEndpointAPISuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)