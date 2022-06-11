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

class APNSPlatformApplicationCreateRequest(object):
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
        'platform': 'str',
        'name': 'str',
        'ssl_certificate': 'str',
        'private_key': 'str'
    }

    attribute_map = {
        'platform': 'platform',
        'name': 'name',
        'ssl_certificate': 'ssl_certificate',
        'private_key': 'private_key'
    }

    def __init__(self, platform=None, name=None, ssl_certificate=None, private_key=None):  # noqa: E501
        """APNSPlatformApplicationCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._platform = None
        self._name = None
        self._ssl_certificate = None
        self._private_key = None
        self.discriminator = None
        if platform is not None:
            self.platform = platform
        if name is not None:
            self.name = name
        if ssl_certificate is not None:
            self.ssl_certificate = ssl_certificate
        if private_key is not None:
            self.private_key = private_key

    @property
    def platform(self):
        """Gets the platform of this APNSPlatformApplicationCreateRequest.  # noqa: E501


        :return: The platform of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this APNSPlatformApplicationCreateRequest.


        :param platform: The platform of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def name(self):
        """Gets the name of this APNSPlatformApplicationCreateRequest.  # noqa: E501


        :return: The name of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this APNSPlatformApplicationCreateRequest.


        :param name: The name of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ssl_certificate(self):
        """Gets the ssl_certificate of this APNSPlatformApplicationCreateRequest.  # noqa: E501


        :return: The ssl_certificate of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._ssl_certificate

    @ssl_certificate.setter
    def ssl_certificate(self, ssl_certificate):
        """Sets the ssl_certificate of this APNSPlatformApplicationCreateRequest.


        :param ssl_certificate: The ssl_certificate of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :type: str
        """

        self._ssl_certificate = ssl_certificate

    @property
    def private_key(self):
        """Gets the private_key of this APNSPlatformApplicationCreateRequest.  # noqa: E501


        :return: The private_key of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this APNSPlatformApplicationCreateRequest.


        :param private_key: The private_key of this APNSPlatformApplicationCreateRequest.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

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
        if issubclass(APNSPlatformApplicationCreateRequest, dict):
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
        if not isinstance(other, APNSPlatformApplicationCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
