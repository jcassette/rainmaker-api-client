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
from rainmaker_api_client.api.device_grouping_api import DeviceGroupingApi  # noqa: E501
from rainmaker_api_client.rest import ApiException


class TestDeviceGroupingApi(unittest.TestCase):
    """DeviceGroupingApi unit test stubs"""

    def setUp(self):
        self.api = DeviceGroupingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acceptor_deny_user_group_sharing_requests(self):
        """Test case for acceptor_deny_user_group_sharing_requests

        This API creates the sharing of Node Groups between users.  # noqa: E501
        """
        pass

    def test_add_user_group_sharing(self):
        """Test case for add_user_group_sharing

        This API creates the sharing of Groups between users.  # noqa: E501
        """
        pass

    def test_admingetdevicegroup(self):
        """Test case for admingetdevicegroup

        Get admin device group  # noqa: E501
        """
        pass

    def test_createdevicegroup(self):
        """Test case for createdevicegroup

        Create admin device group  # noqa: E501
        """
        pass

    def test_deletedevicegroup(self):
        """Test case for deletedevicegroup

        Delete admin device group  # noqa: E501
        """
        pass

    def test_get_user_group_sharing(self):
        """Test case for get_user_group_sharing

        This API fetches the sharing details for the nodes the current user is associated with.  # noqa: E501
        """
        pass

    def test_get_user_group_sharing_request(self):
        """Test case for get_user_group_sharing_request

        This API is used to get the sharing requests raised between users.  # noqa: E501
        """
        pass

    def test_remove_user_group_sharing(self):
        """Test case for remove_user_group_sharing

        This API removes the sharing of Groups between the users.  # noqa: E501
        """
        pass

    def test_remove_user_group_sharing_request(self):
        """Test case for remove_user_group_sharing_request

        This API removes the sharing request of Groups between the users.  # noqa: E501
        """
        pass

    def test_updatedevicegroup(self):
        """Test case for updatedevicegroup

        Update admin device group  # noqa: E501
        """
        pass

    def test_usercreatedevicegroup(self):
        """Test case for usercreatedevicegroup

        Create the user device group  # noqa: E501
        """
        pass

    def test_userdeletedevicegroup(self):
        """Test case for userdeletedevicegroup

        Delete user device group  # noqa: E501
        """
        pass

    def test_usergetdevicegroup(self):
        """Test case for usergetdevicegroup

        Get user device group  # noqa: E501
        """
        pass

    def test_userupdatedevicegroup(self):
        """Test case for userupdatedevicegroup

        Update user device group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
