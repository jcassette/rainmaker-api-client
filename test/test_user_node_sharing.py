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
from rainmaker_api_client.models.user_node_sharing import UserNodeSharing  # noqa: E501
from rainmaker_api_client.rest import ApiException


class TestUserNodeSharing(unittest.TestCase):
    """UserNodeSharing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserNodeSharing(self):
        """Test UserNodeSharing"""
        # FIXME: construct object with mandatory attributes with example values
        # model = rainmaker_api_client.models.user_node_sharing.UserNodeSharing()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
