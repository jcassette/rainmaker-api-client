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

class UpdateDeviceGroupRequest(object):
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
        'group_name': 'str',
        'operation': 'str',
        'type': 'str',
        'mutually_exclusive': 'bool',
        'nodes': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'operation': 'operation',
        'type': 'type',
        'mutually_exclusive': 'mutually_exclusive',
        'nodes': 'nodes',
        'description': 'description'
    }

    def __init__(self, group_name=None, operation=None, type=None, mutually_exclusive=None, nodes=None, description=None):  # noqa: E501
        """UpdateDeviceGroupRequest - a model defined in Swagger"""  # noqa: E501
        self._group_name = None
        self._operation = None
        self._type = None
        self._mutually_exclusive = None
        self._nodes = None
        self._description = None
        self.discriminator = None
        if group_name is not None:
            self.group_name = group_name
        if operation is not None:
            self.operation = operation
        if type is not None:
            self.type = type
        if mutually_exclusive is not None:
            self.mutually_exclusive = mutually_exclusive
        if nodes is not None:
            self.nodes = nodes
        if description is not None:
            self.description = description

    @property
    def group_name(self):
        """Gets the group_name of this UpdateDeviceGroupRequest.  # noqa: E501


        :return: The group_name of this UpdateDeviceGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UpdateDeviceGroupRequest.


        :param group_name: The group_name of this UpdateDeviceGroupRequest.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def operation(self):
        """Gets the operation of this UpdateDeviceGroupRequest.  # noqa: E501


        :return: The operation of this UpdateDeviceGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this UpdateDeviceGroupRequest.


        :param operation: The operation of this UpdateDeviceGroupRequest.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def type(self):
        """Gets the type of this UpdateDeviceGroupRequest.  # noqa: E501


        :return: The type of this UpdateDeviceGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateDeviceGroupRequest.


        :param type: The type of this UpdateDeviceGroupRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def mutually_exclusive(self):
        """Gets the mutually_exclusive of this UpdateDeviceGroupRequest.  # noqa: E501


        :return: The mutually_exclusive of this UpdateDeviceGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._mutually_exclusive

    @mutually_exclusive.setter
    def mutually_exclusive(self, mutually_exclusive):
        """Sets the mutually_exclusive of this UpdateDeviceGroupRequest.


        :param mutually_exclusive: The mutually_exclusive of this UpdateDeviceGroupRequest.  # noqa: E501
        :type: bool
        """

        self._mutually_exclusive = mutually_exclusive

    @property
    def nodes(self):
        """Gets the nodes of this UpdateDeviceGroupRequest.  # noqa: E501


        :return: The nodes of this UpdateDeviceGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this UpdateDeviceGroupRequest.


        :param nodes: The nodes of this UpdateDeviceGroupRequest.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def description(self):
        """Gets the description of this UpdateDeviceGroupRequest.  # noqa: E501


        :return: The description of this UpdateDeviceGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDeviceGroupRequest.


        :param description: The description of this UpdateDeviceGroupRequest.  # noqa: E501
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
        if issubclass(UpdateDeviceGroupRequest, dict):
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
        if not isinstance(other, UpdateDeviceGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
