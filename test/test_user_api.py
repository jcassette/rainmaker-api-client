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
from rainmaker_api_client.api.user_api import UserApi  # noqa: E501
from rainmaker_api_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forgotpassword(self):
        """Test case for forgotpassword

        Handle forgot password request from the user  # noqa: E501
        """
        pass

    def test_forgotpassword_mobile(self):
        """Test case for forgotpassword_mobile

        Handle forgot password request from the user  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Fetches the details of current user  # noqa: E501
        """
        pass

    def test_get_user_mobile(self):
        """Test case for get_user_mobile

        Fetches the details of current user  # noqa: E501
        """
        pass

    def test_login(self):
        """Test case for login

        Handle login or extend session request from the user  # noqa: E501
        """
        pass

    def test_login2(self):
        """Test case for login2

        Handle login or extend session request from the user  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Log out user from the session  # noqa: E501
        """
        pass

    def test_password(self):
        """Test case for password

        Handle password change request from the user  # noqa: E501
        """
        pass

    def test_password_mobile(self):
        """Test case for password_mobile

        Handle password change request from the user  # noqa: E501
        """
        pass

    def test_userattributeupdate(self):
        """Test case for userattributeupdate

        Updates Name and Phone number of the user  # noqa: E501
        """
        pass

    def test_usercreation(self):
        """Test case for usercreation

        Creates the new user or confirms the user  # noqa: E501
        """
        pass

    def test_usercreation_mobile(self):
        """Test case for usercreation_mobile

        Creates the new user or confirms the user. The user can specify his email address or the mobile number with country code for creating his account.  # noqa: E501
        """
        pass

    def test_userdeletion(self):
        """Test case for userdeletion

        Deletes user account  # noqa: E501
        """
        pass

    def test_userdeletion_mobile(self):
        """Test case for userdeletion_mobile

        Deletes user account  # noqa: E501
        """
        pass

    def test_usernameupdate(self):
        """Test case for usernameupdate

        Updates Name of the user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()