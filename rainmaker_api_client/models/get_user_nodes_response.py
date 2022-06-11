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

class GetUserNodesResponse(object):
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
        'primary': 'GetUserNodesResponsePrimary',
        'secondary': 'GetUserNodesResponseSecondary',
        'total': 'float',
        'next_id': 'str'
    }

    attribute_map = {
        'primary': 'primary',
        'secondary': 'secondary',
        'total': 'total',
        'next_id': 'next_id'
    }

    def __init__(self, primary=None, secondary=None, total=None, next_id=None):  # noqa: E501
        """GetUserNodesResponse - a model defined in Swagger"""  # noqa: E501
        self._primary = None
        self._secondary = None
        self._total = None
        self._next_id = None
        self.discriminator = None
        if primary is not None:
            self.primary = primary
        if secondary is not None:
            self.secondary = secondary
        if total is not None:
            self.total = total
        if next_id is not None:
            self.next_id = next_id

    @property
    def primary(self):
        """Gets the primary of this GetUserNodesResponse.  # noqa: E501


        :return: The primary of this GetUserNodesResponse.  # noqa: E501
        :rtype: GetUserNodesResponsePrimary
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this GetUserNodesResponse.


        :param primary: The primary of this GetUserNodesResponse.  # noqa: E501
        :type: GetUserNodesResponsePrimary
        """

        self._primary = primary

    @property
    def secondary(self):
        """Gets the secondary of this GetUserNodesResponse.  # noqa: E501


        :return: The secondary of this GetUserNodesResponse.  # noqa: E501
        :rtype: GetUserNodesResponseSecondary
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this GetUserNodesResponse.


        :param secondary: The secondary of this GetUserNodesResponse.  # noqa: E501
        :type: GetUserNodesResponseSecondary
        """

        self._secondary = secondary

    @property
    def total(self):
        """Gets the total of this GetUserNodesResponse.  # noqa: E501


        :return: The total of this GetUserNodesResponse.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetUserNodesResponse.


        :param total: The total of this GetUserNodesResponse.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def next_id(self):
        """Gets the next_id of this GetUserNodesResponse.  # noqa: E501


        :return: The next_id of this GetUserNodesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_id

    @next_id.setter
    def next_id(self, next_id):
        """Sets the next_id of this GetUserNodesResponse.


        :param next_id: The next_id of this GetUserNodesResponse.  # noqa: E501
        :type: str
        """

        self._next_id = next_id

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
        if issubclass(GetUserNodesResponse, dict):
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
        if not isinstance(other, GetUserNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other