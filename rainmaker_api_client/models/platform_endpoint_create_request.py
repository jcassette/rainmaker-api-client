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

class PlatformEndpointCreateRequest(object):
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
        'platform_application_name': 'str',
        'mobile_device_token': 'str'
    }

    attribute_map = {
        'platform_application_name': 'platform_application_name',
        'mobile_device_token': 'mobile_device_token'
    }

    def __init__(self, platform_application_name=None, mobile_device_token=None):  # noqa: E501
        """PlatformEndpointCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._platform_application_name = None
        self._mobile_device_token = None
        self.discriminator = None
        if platform_application_name is not None:
            self.platform_application_name = platform_application_name
        if mobile_device_token is not None:
            self.mobile_device_token = mobile_device_token

    @property
    def platform_application_name(self):
        """Gets the platform_application_name of this PlatformEndpointCreateRequest.  # noqa: E501


        :return: The platform_application_name of this PlatformEndpointCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._platform_application_name

    @platform_application_name.setter
    def platform_application_name(self, platform_application_name):
        """Sets the platform_application_name of this PlatformEndpointCreateRequest.


        :param platform_application_name: The platform_application_name of this PlatformEndpointCreateRequest.  # noqa: E501
        :type: str
        """

        self._platform_application_name = platform_application_name

    @property
    def mobile_device_token(self):
        """Gets the mobile_device_token of this PlatformEndpointCreateRequest.  # noqa: E501


        :return: The mobile_device_token of this PlatformEndpointCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_device_token

    @mobile_device_token.setter
    def mobile_device_token(self, mobile_device_token):
        """Sets the mobile_device_token of this PlatformEndpointCreateRequest.


        :param mobile_device_token: The mobile_device_token of this PlatformEndpointCreateRequest.  # noqa: E501
        :type: str
        """

        self._mobile_device_token = mobile_device_token

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
        if issubclass(PlatformEndpointCreateRequest, dict):
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
        if not isinstance(other, PlatformEndpointCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
