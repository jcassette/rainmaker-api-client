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

class StackDeploymentDetails(object):
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
        'stack_name': 'str',
        'created_time_stamp': 'str',
        'last_updated_time_stamp': 'str',
        'version': 'str'
    }

    attribute_map = {
        'stack_name': 'stack_name',
        'created_time_stamp': 'created_time_stamp',
        'last_updated_time_stamp': 'last_updated_time_stamp',
        'version': 'version'
    }

    def __init__(self, stack_name=None, created_time_stamp=None, last_updated_time_stamp=None, version=None):  # noqa: E501
        """StackDeploymentDetails - a model defined in Swagger"""  # noqa: E501
        self._stack_name = None
        self._created_time_stamp = None
        self._last_updated_time_stamp = None
        self._version = None
        self.discriminator = None
        if stack_name is not None:
            self.stack_name = stack_name
        if created_time_stamp is not None:
            self.created_time_stamp = created_time_stamp
        if last_updated_time_stamp is not None:
            self.last_updated_time_stamp = last_updated_time_stamp
        if version is not None:
            self.version = version

    @property
    def stack_name(self):
        """Gets the stack_name of this StackDeploymentDetails.  # noqa: E501


        :return: The stack_name of this StackDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this StackDeploymentDetails.


        :param stack_name: The stack_name of this StackDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._stack_name = stack_name

    @property
    def created_time_stamp(self):
        """Gets the created_time_stamp of this StackDeploymentDetails.  # noqa: E501


        :return: The created_time_stamp of this StackDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._created_time_stamp

    @created_time_stamp.setter
    def created_time_stamp(self, created_time_stamp):
        """Sets the created_time_stamp of this StackDeploymentDetails.


        :param created_time_stamp: The created_time_stamp of this StackDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._created_time_stamp = created_time_stamp

    @property
    def last_updated_time_stamp(self):
        """Gets the last_updated_time_stamp of this StackDeploymentDetails.  # noqa: E501


        :return: The last_updated_time_stamp of this StackDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_time_stamp

    @last_updated_time_stamp.setter
    def last_updated_time_stamp(self, last_updated_time_stamp):
        """Sets the last_updated_time_stamp of this StackDeploymentDetails.


        :param last_updated_time_stamp: The last_updated_time_stamp of this StackDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._last_updated_time_stamp = last_updated_time_stamp

    @property
    def version(self):
        """Gets the version of this StackDeploymentDetails.  # noqa: E501


        :return: The version of this StackDeploymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StackDeploymentDetails.


        :param version: The version of this StackDeploymentDetails.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(StackDeploymentDetails, dict):
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
        if not isinstance(other, StackDeploymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
