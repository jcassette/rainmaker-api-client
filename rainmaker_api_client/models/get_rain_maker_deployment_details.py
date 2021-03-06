# coding: utf-8

"""
    API Definitions for RainMaker Backend Service

    This Swagger file provides the details about the RainMaker platform APIs.<br><br> There are two types of APIs supported by RainMaker - Unauthenticated and Authenticated.<br> The authenticated APIs are marked in the Swagger file, with a “lock” sign in front of them.<br> For the Unauthenticated APIs, there is no need to provide any authentication tokens in the HTTP header.<br> When the user logs in successfully, he receives access_token in the response. For the Authenticated APIs, this access_token needs to be passed in the \"Authorization\" HTTP header as the authentication token.<br> <br> <b>Note:</b><br><ul><li>RainMaker APIs do not support using double slashes after the resources or methods. Including a double slash goes against HTTP best practices. <br><li>The RainMaker APIs do not support following HTTP headers - data, verify and cookies.</ul>  # noqa: E501

    OpenAPI spec version: 1.1.17-fd1c887_2022-05-24T06:46
    Contact: esp-rainmaker-admin@espressif.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetRainMakerDeploymentDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base_url': 'str',
        'region': 'str',
        'account_id': 'str',
        'build_info': 'str',
        'mqtt_endpoint': 'str',
        'user_pool_id': 'str',
        'app_client_id': 'str'
    }

    attribute_map = {
        'base_url': 'base_url',
        'region': 'region',
        'account_id': 'account_id',
        'build_info': 'build_info',
        'mqtt_endpoint': 'mqtt_endpoint',
        'user_pool_id': 'user_pool_id',
        'app_client_id': 'app_client_id'
    }

    def __init__(self, base_url=None, region=None, account_id=None, build_info=None, mqtt_endpoint=None, user_pool_id=None, app_client_id=None):  # noqa: E501
        """GetRainMakerDeploymentDetails - a model defined in Swagger"""  # noqa: E501
        self._base_url = None
        self._region = None
        self._account_id = None
        self._build_info = None
        self._mqtt_endpoint = None
        self._user_pool_id = None
        self._app_client_id = None
        self.discriminator = None
        if base_url is not None:
            self.base_url = base_url
        if region is not None:
            self.region = region
        if account_id is not None:
            self.account_id = account_id
        if build_info is not None:
            self.build_info = build_info
        if mqtt_endpoint is not None:
            self.mqtt_endpoint = mqtt_endpoint
        if user_pool_id is not None:
            self.user_pool_id = user_pool_id
        if app_client_id is not None:
            self.app_client_id = app_client_id

    @property
    def base_url(self):
        """Gets the base_url of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The base_url of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this GetRainMakerDeploymentDetails.


        :param base_url: The base_url of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def region(self):
        """Gets the region of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The region of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GetRainMakerDeploymentDetails.


        :param region: The region of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def account_id(self):
        """Gets the account_id of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The account_id of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetRainMakerDeploymentDetails.


        :param account_id: The account_id of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def build_info(self):
        """Gets the build_info of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The build_info of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._build_info

    @build_info.setter
    def build_info(self, build_info):
        """Sets the build_info of this GetRainMakerDeploymentDetails.


        :param build_info: The build_info of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._build_info = build_info

    @property
    def mqtt_endpoint(self):
        """Gets the mqtt_endpoint of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The mqtt_endpoint of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._mqtt_endpoint

    @mqtt_endpoint.setter
    def mqtt_endpoint(self, mqtt_endpoint):
        """Sets the mqtt_endpoint of this GetRainMakerDeploymentDetails.


        :param mqtt_endpoint: The mqtt_endpoint of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._mqtt_endpoint = mqtt_endpoint

    @property
    def user_pool_id(self):
        """Gets the user_pool_id of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The user_pool_id of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_pool_id

    @user_pool_id.setter
    def user_pool_id(self, user_pool_id):
        """Sets the user_pool_id of this GetRainMakerDeploymentDetails.


        :param user_pool_id: The user_pool_id of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._user_pool_id = user_pool_id

    @property
    def app_client_id(self):
        """Gets the app_client_id of this GetRainMakerDeploymentDetails.  # noqa: E501


        :return: The app_client_id of this GetRainMakerDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._app_client_id

    @app_client_id.setter
    def app_client_id(self, app_client_id):
        """Sets the app_client_id of this GetRainMakerDeploymentDetails.


        :param app_client_id: The app_client_id of this GetRainMakerDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._app_client_id = app_client_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetRainMakerDeploymentDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetRainMakerDeploymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
