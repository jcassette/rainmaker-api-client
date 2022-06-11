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

class UserGetOtaStatusResponse(object):
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
        'node_id': 'str',
        'status': 'str',
        'additional_info': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'node_id': 'node_id',
        'status': 'status',
        'additional_info': 'additional_info',
        'timestamp': 'timestamp'
    }

    def __init__(self, node_id=None, status=None, additional_info=None, timestamp=None):  # noqa: E501
        """UserGetOtaStatusResponse - a model defined in Swagger"""  # noqa: E501
        self._node_id = None
        self._status = None
        self._additional_info = None
        self._timestamp = None
        self.discriminator = None
        if node_id is not None:
            self.node_id = node_id
        if status is not None:
            self.status = status
        if additional_info is not None:
            self.additional_info = additional_info
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def node_id(self):
        """Gets the node_id of this UserGetOtaStatusResponse.  # noqa: E501


        :return: The node_id of this UserGetOtaStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UserGetOtaStatusResponse.


        :param node_id: The node_id of this UserGetOtaStatusResponse.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def status(self):
        """Gets the status of this UserGetOtaStatusResponse.  # noqa: E501


        :return: The status of this UserGetOtaStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserGetOtaStatusResponse.


        :param status: The status of this UserGetOtaStatusResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def additional_info(self):
        """Gets the additional_info of this UserGetOtaStatusResponse.  # noqa: E501


        :return: The additional_info of this UserGetOtaStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this UserGetOtaStatusResponse.


        :param additional_info: The additional_info of this UserGetOtaStatusResponse.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def timestamp(self):
        """Gets the timestamp of this UserGetOtaStatusResponse.  # noqa: E501


        :return: The timestamp of this UserGetOtaStatusResponse.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UserGetOtaStatusResponse.


        :param timestamp: The timestamp of this UserGetOtaStatusResponse.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

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
        if issubclass(UserGetOtaStatusResponse, dict):
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
        if not isinstance(other, UserGetOtaStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
