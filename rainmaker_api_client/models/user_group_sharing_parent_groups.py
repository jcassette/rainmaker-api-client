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

class UserGroupSharingParentGroups(object):
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
        'group_id': 'str',
        'group_name': 'str',
        'group_type': 'str',
        'mutually_exclusive': 'bool',
        'parent_group': 'UserGroupSharingParentGroupsParentGroup'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'group_type': 'group_type',
        'mutually_exclusive': 'mutually_exclusive',
        'parent_group': 'parent_group'
    }

    def __init__(self, group_id=None, group_name=None, group_type=None, mutually_exclusive=None, parent_group=None):  # noqa: E501
        """UserGroupSharingParentGroups - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._group_name = None
        self._group_type = None
        self._mutually_exclusive = None
        self._parent_group = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if group_type is not None:
            self.group_type = group_type
        if mutually_exclusive is not None:
            self.mutually_exclusive = mutually_exclusive
        if parent_group is not None:
            self.parent_group = parent_group

    @property
    def group_id(self):
        """Gets the group_id of this UserGroupSharingParentGroups.  # noqa: E501


        :return: The group_id of this UserGroupSharingParentGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UserGroupSharingParentGroups.


        :param group_id: The group_id of this UserGroupSharingParentGroups.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this UserGroupSharingParentGroups.  # noqa: E501


        :return: The group_name of this UserGroupSharingParentGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UserGroupSharingParentGroups.


        :param group_name: The group_name of this UserGroupSharingParentGroups.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_type(self):
        """Gets the group_type of this UserGroupSharingParentGroups.  # noqa: E501


        :return: The group_type of this UserGroupSharingParentGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this UserGroupSharingParentGroups.


        :param group_type: The group_type of this UserGroupSharingParentGroups.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def mutually_exclusive(self):
        """Gets the mutually_exclusive of this UserGroupSharingParentGroups.  # noqa: E501


        :return: The mutually_exclusive of this UserGroupSharingParentGroups.  # noqa: E501
        :rtype: bool
        """
        return self._mutually_exclusive

    @mutually_exclusive.setter
    def mutually_exclusive(self, mutually_exclusive):
        """Sets the mutually_exclusive of this UserGroupSharingParentGroups.


        :param mutually_exclusive: The mutually_exclusive of this UserGroupSharingParentGroups.  # noqa: E501
        :type: bool
        """

        self._mutually_exclusive = mutually_exclusive

    @property
    def parent_group(self):
        """Gets the parent_group of this UserGroupSharingParentGroups.  # noqa: E501


        :return: The parent_group of this UserGroupSharingParentGroups.  # noqa: E501
        :rtype: UserGroupSharingParentGroupsParentGroup
        """
        return self._parent_group

    @parent_group.setter
    def parent_group(self, parent_group):
        """Sets the parent_group of this UserGroupSharingParentGroups.


        :param parent_group: The parent_group of this UserGroupSharingParentGroups.  # noqa: E501
        :type: UserGroupSharingParentGroupsParentGroup
        """

        self._parent_group = parent_group

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
        if issubclass(UserGroupSharingParentGroups, dict):
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
        if not isinstance(other, UserGroupSharingParentGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
