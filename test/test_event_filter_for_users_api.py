# coding: utf-8

"""
    API Definitions for RainMaker Backend Service

    This Swagger file provides the details about the RainMaker platform APIs.<br><br> There are two types of APIs supported by RainMaker - Unauthenticated and Authenticated.<br> The authenticated APIs are marked in the Swagger file, with a “lock” sign in front of them.<br> For the Unauthenticated APIs, there is no need to provide any authentication tokens in the HTTP header.<br> When the user logs in successfully, he receives access_token in the response. For the Authenticated APIs, this access_token needs to be passed in the \"Authorization\" HTTP header as the authentication token.<br> <br> <b>Note:</b><br><ul><li>RainMaker APIs do not support using double slashes after the resources or methods. Including a double slash goes against HTTP best practices. <br><li>The RainMaker APIs do not support following HTTP headers - data, verify and cookies.</ul>  # noqa: E501

    OpenAPI spec version: 1.1.17-fd1c887_2022-05-24T06:46
    Contact: esp-rainmaker-admin@espressif.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import rainmaker_api_client
from rainmaker_api_client.api.event_filter_for_users_api import EventFilterForUsersApi  # noqa: E501
from rainmaker_api_client.rest import ApiException


class TestEventFilterForUsersApi(unittest.TestCase):
    """EventFilterForUsersApi unit test stubs"""

    def setUp(self):
        self.api = EventFilterForUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_event_filter(self):
        """Test case for add_user_event_filter

        This API adds event filter for given event and entity (user or node).  # noqa: E501
        """
        pass

    def test_get_user_event_filter(self):
        """Test case for get_user_event_filter

        Get Integration event filter information.  # noqa: E501
        """
        pass

    def test_remove_user_event_filter(self):
        """Test case for remove_user_event_filter

        This API removes the Integration event filter.  # noqa: E501
        """
        pass

    def test_update_user_event_filter(self):
        """Test case for update_user_event_filter

        This API updates event filter for given event and entity (user or node)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
