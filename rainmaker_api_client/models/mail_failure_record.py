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

class MailFailureRecord(object):
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
        'email_id': 'str',
        'timestamp': 'float',
        'failure_type': 'str',
        'subject': 'str',
        'reason': 'str',
        'failure_sub_type': 'str'
    }

    attribute_map = {
        'email_id': 'email_id',
        'timestamp': 'timestamp',
        'failure_type': 'failure_type',
        'subject': 'subject',
        'reason': 'reason',
        'failure_sub_type': 'failure_sub_type'
    }

    def __init__(self, email_id=None, timestamp=None, failure_type=None, subject=None, reason=None, failure_sub_type=None):  # noqa: E501
        """MailFailureRecord - a model defined in Swagger"""  # noqa: E501
        self._email_id = None
        self._timestamp = None
        self._failure_type = None
        self._subject = None
        self._reason = None
        self._failure_sub_type = None
        self.discriminator = None
        if email_id is not None:
            self.email_id = email_id
        if timestamp is not None:
            self.timestamp = timestamp
        if failure_type is not None:
            self.failure_type = failure_type
        if subject is not None:
            self.subject = subject
        if reason is not None:
            self.reason = reason
        if failure_sub_type is not None:
            self.failure_sub_type = failure_sub_type

    @property
    def email_id(self):
        """Gets the email_id of this MailFailureRecord.  # noqa: E501


        :return: The email_id of this MailFailureRecord.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this MailFailureRecord.


        :param email_id: The email_id of this MailFailureRecord.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def timestamp(self):
        """Gets the timestamp of this MailFailureRecord.  # noqa: E501


        :return: The timestamp of this MailFailureRecord.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MailFailureRecord.


        :param timestamp: The timestamp of this MailFailureRecord.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def failure_type(self):
        """Gets the failure_type of this MailFailureRecord.  # noqa: E501


        :return: The failure_type of this MailFailureRecord.  # noqa: E501
        :rtype: str
        """
        return self._failure_type

    @failure_type.setter
    def failure_type(self, failure_type):
        """Sets the failure_type of this MailFailureRecord.


        :param failure_type: The failure_type of this MailFailureRecord.  # noqa: E501
        :type: str
        """

        self._failure_type = failure_type

    @property
    def subject(self):
        """Gets the subject of this MailFailureRecord.  # noqa: E501


        :return: The subject of this MailFailureRecord.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MailFailureRecord.


        :param subject: The subject of this MailFailureRecord.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def reason(self):
        """Gets the reason of this MailFailureRecord.  # noqa: E501


        :return: The reason of this MailFailureRecord.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MailFailureRecord.


        :param reason: The reason of this MailFailureRecord.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def failure_sub_type(self):
        """Gets the failure_sub_type of this MailFailureRecord.  # noqa: E501


        :return: The failure_sub_type of this MailFailureRecord.  # noqa: E501
        :rtype: str
        """
        return self._failure_sub_type

    @failure_sub_type.setter
    def failure_sub_type(self, failure_sub_type):
        """Sets the failure_sub_type of this MailFailureRecord.


        :param failure_sub_type: The failure_sub_type of this MailFailureRecord.  # noqa: E501
        :type: str
        """

        self._failure_sub_type = failure_sub_type

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
        if issubclass(MailFailureRecord, dict):
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
        if not isinstance(other, MailFailureRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
