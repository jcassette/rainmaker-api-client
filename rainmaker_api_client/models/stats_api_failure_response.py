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

class StatsAPIFailureResponse(object):
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
        'status': 'str',
        'error_code': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'error_code': 'error_code',
        'description': 'description'
    }

    def __init__(self, status=None, error_code=None, description=None):  # noqa: E501
        """StatsAPIFailureResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._error_code = None
        self._description = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description

    @property
    def status(self):
        """Gets the status of this StatsAPIFailureResponse.  # noqa: E501


        :return: The status of this StatsAPIFailureResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatsAPIFailureResponse.


        :param status: The status of this StatsAPIFailureResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this StatsAPIFailureResponse.  # noqa: E501


        :return: The error_code of this StatsAPIFailureResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this StatsAPIFailureResponse.


        :param error_code: The error_code of this StatsAPIFailureResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this StatsAPIFailureResponse.  # noqa: E501


        :return: The description of this StatsAPIFailureResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StatsAPIFailureResponse.


        :param description: The description of this StatsAPIFailureResponse.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(StatsAPIFailureResponse, dict):
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
        if not isinstance(other, StatsAPIFailureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
