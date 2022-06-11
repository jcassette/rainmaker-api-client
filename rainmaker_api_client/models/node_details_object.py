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

class NodeDetailsObject(object):
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
        'id': 'str',
        'role': 'str',
        'status': 'NodeConnectivity',
        'config': 'NodeConfiguration',
        'params': 'SetParamsRequestBody'
    }

    attribute_map = {
        'id': 'id',
        'role': 'role',
        'status': 'status',
        'config': 'config',
        'params': 'params'
    }

    def __init__(self, id=None, role=None, status=None, config=None, params=None):  # noqa: E501
        """NodeDetailsObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._role = None
        self._status = None
        self._config = None
        self._params = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if config is not None:
            self.config = config
        if params is not None:
            self.params = params

    @property
    def id(self):
        """Gets the id of this NodeDetailsObject.  # noqa: E501


        :return: The id of this NodeDetailsObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeDetailsObject.


        :param id: The id of this NodeDetailsObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def role(self):
        """Gets the role of this NodeDetailsObject.  # noqa: E501


        :return: The role of this NodeDetailsObject.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NodeDetailsObject.


        :param role: The role of this NodeDetailsObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["primary", "secondary"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def status(self):
        """Gets the status of this NodeDetailsObject.  # noqa: E501


        :return: The status of this NodeDetailsObject.  # noqa: E501
        :rtype: NodeConnectivity
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeDetailsObject.


        :param status: The status of this NodeDetailsObject.  # noqa: E501
        :type: NodeConnectivity
        """

        self._status = status

    @property
    def config(self):
        """Gets the config of this NodeDetailsObject.  # noqa: E501


        :return: The config of this NodeDetailsObject.  # noqa: E501
        :rtype: NodeConfiguration
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this NodeDetailsObject.


        :param config: The config of this NodeDetailsObject.  # noqa: E501
        :type: NodeConfiguration
        """

        self._config = config

    @property
    def params(self):
        """Gets the params of this NodeDetailsObject.  # noqa: E501


        :return: The params of this NodeDetailsObject.  # noqa: E501
        :rtype: SetParamsRequestBody
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this NodeDetailsObject.


        :param params: The params of this NodeDetailsObject.  # noqa: E501
        :type: SetParamsRequestBody
        """

        self._params = params

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
        if issubclass(NodeDetailsObject, dict):
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
        if not isinstance(other, NodeDetailsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other