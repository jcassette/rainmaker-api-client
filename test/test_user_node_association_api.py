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
from rainmaker_api_client.api.user_node_association_api import UserNodeAssociationApi  # noqa: E501
from rainmaker_api_client.rest import ApiException


class TestUserNodeAssociationApi(unittest.TestCase):
    """UserNodeAssociationApi unit test stubs"""

    def setUp(self):
        self.api = UserNodeAssociationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_remove_user_node_mapping(self):
        """Test case for add_remove_user_node_mapping

        Add or Remove the User Node mapping  # noqa: E501
        """
        pass

    def test_add_user_node_sharing(self):
        """Test case for add_user_node_sharing

        This API creates the sharing of Nodes between users.  # noqa: E501
        """
        pass

    def test_add_user_node_sharing_requests(self):
        """Test case for add_user_node_sharing_requests

        This API creates the sharing of Nodes between users.  # noqa: E501
        """
        pass

    def test_addtags(self):
        """Test case for addtags

        Add tags to Node  # noqa: E501
        """
        pass

    def test_get_admin_user_nodes(self):
        """Test case for get_admin_user_nodes

        Get the nodes claimed by the Admin user  # noqa: E501
        """
        pass

    def test_get_node_status(self):
        """Test case for get_node_status

        Get the online or offline status for the node  # noqa: E501
        """
        pass

    def test_get_user_node_configuration(self):
        """Test case for get_user_node_configuration

        Get the configuration for the node  # noqa: E501
        """
        pass

    def test_get_user_node_mapping_request_status(self):
        """Test case for get_user_node_mapping_request_status

        Get the status of User Node mapping request  # noqa: E501
        """
        pass

    def test_get_user_node_sharing(self):
        """Test case for get_user_node_sharing

        This API fetches the sharing details for the nodes the current user is associated with.  # noqa: E501
        """
        pass

    def test_get_user_node_sharing_request(self):
        """Test case for get_user_node_sharing_request

        This API is used to get the sharing requests raised between users.  # noqa: E501
        """
        pass

    def test_get_user_nodes(self):
        """Test case for get_user_nodes

        Get the nodes associated with the user  # noqa: E501
        """
        pass

    def test_get_user_nodes_for_admins(self):
        """Test case for get_user_nodes_for_admins

        Get the nodes associated with a user  # noqa: E501
        """
        pass

    def test_remove_user_node_sharing(self):
        """Test case for remove_user_node_sharing

        This API removes the sharing of Nodes between the users.  # noqa: E501
        """
        pass

    def test_remove_user_node_sharing_request(self):
        """Test case for remove_user_node_sharing_request

        This API removes the sharing request of Nodes between the users.  # noqa: E501
        """
        pass

    def test_update_node_certificate_status(self):
        """Test case for update_node_certificate_status

        Activate or Deactivate the Node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
