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

class UpdatePolicyPolicyJson(object):
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
        'version': 'str',
        'filters': 'list[UpdatePolicyPolicyJsonFilters]',
        'statement': 'list[UpdatePolicyPolicyJsonStatement]'
    }

    attribute_map = {
        'version': 'version',
        'filters': 'filters',
        'statement': 'statement'
    }

    def __init__(self, version=None, filters=None, statement=None):  # noqa: E501
        """UpdatePolicyPolicyJson - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._filters = None
        self._statement = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if filters is not None:
            self.filters = filters
        if statement is not None:
            self.statement = statement

    @property
    def version(self):
        """Gets the version of this UpdatePolicyPolicyJson.  # noqa: E501


        :return: The version of this UpdatePolicyPolicyJson.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdatePolicyPolicyJson.


        :param version: The version of this UpdatePolicyPolicyJson.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def filters(self):
        """Gets the filters of this UpdatePolicyPolicyJson.  # noqa: E501


        :return: The filters of this UpdatePolicyPolicyJson.  # noqa: E501
        :rtype: list[UpdatePolicyPolicyJsonFilters]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this UpdatePolicyPolicyJson.


        :param filters: The filters of this UpdatePolicyPolicyJson.  # noqa: E501
        :type: list[UpdatePolicyPolicyJsonFilters]
        """

        self._filters = filters

    @property
    def statement(self):
        """Gets the statement of this UpdatePolicyPolicyJson.  # noqa: E501


        :return: The statement of this UpdatePolicyPolicyJson.  # noqa: E501
        :rtype: list[UpdatePolicyPolicyJsonStatement]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this UpdatePolicyPolicyJson.


        :param statement: The statement of this UpdatePolicyPolicyJson.  # noqa: E501
        :type: list[UpdatePolicyPolicyJsonStatement]
        """

        self._statement = statement

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
        if issubclass(UpdatePolicyPolicyJson, dict):
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
        if not isinstance(other, UpdatePolicyPolicyJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
