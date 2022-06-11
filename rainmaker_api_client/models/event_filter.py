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

class EventFilter(object):
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
        'event_type': 'str',
        'entitiy_id': 'str',
        'entity_type': 'str',
        'enabled': 'bool',
        'enabled_for_integrations': 'list[str]'
    }

    attribute_map = {
        'event_type': 'event_type',
        'entitiy_id': 'entitiy_id',
        'entity_type': 'entity_type',
        'enabled': 'enabled',
        'enabled_for_integrations': 'enabled_for_integrations'
    }

    def __init__(self, event_type=None, entitiy_id=None, entity_type=None, enabled=None, enabled_for_integrations=None):  # noqa: E501
        """EventFilter - a model defined in Swagger"""  # noqa: E501
        self._event_type = None
        self._entitiy_id = None
        self._entity_type = None
        self._enabled = None
        self._enabled_for_integrations = None
        self.discriminator = None
        if event_type is not None:
            self.event_type = event_type
        if entitiy_id is not None:
            self.entitiy_id = entitiy_id
        if entity_type is not None:
            self.entity_type = entity_type
        if enabled is not None:
            self.enabled = enabled
        if enabled_for_integrations is not None:
            self.enabled_for_integrations = enabled_for_integrations

    @property
    def event_type(self):
        """Gets the event_type of this EventFilter.  # noqa: E501


        :return: The event_type of this EventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventFilter.


        :param event_type: The event_type of this EventFilter.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def entitiy_id(self):
        """Gets the entitiy_id of this EventFilter.  # noqa: E501


        :return: The entitiy_id of this EventFilter.  # noqa: E501
        :rtype: str
        """
        return self._entitiy_id

    @entitiy_id.setter
    def entitiy_id(self, entitiy_id):
        """Sets the entitiy_id of this EventFilter.


        :param entitiy_id: The entitiy_id of this EventFilter.  # noqa: E501
        :type: str
        """

        self._entitiy_id = entitiy_id

    @property
    def entity_type(self):
        """Gets the entity_type of this EventFilter.  # noqa: E501


        :return: The entity_type of this EventFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EventFilter.


        :param entity_type: The entity_type of this EventFilter.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def enabled(self):
        """Gets the enabled of this EventFilter.  # noqa: E501


        :return: The enabled of this EventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EventFilter.


        :param enabled: The enabled of this EventFilter.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def enabled_for_integrations(self):
        """Gets the enabled_for_integrations of this EventFilter.  # noqa: E501


        :return: The enabled_for_integrations of this EventFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabled_for_integrations

    @enabled_for_integrations.setter
    def enabled_for_integrations(self, enabled_for_integrations):
        """Sets the enabled_for_integrations of this EventFilter.


        :param enabled_for_integrations: The enabled_for_integrations of this EventFilter.  # noqa: E501
        :type: list[str]
        """

        self._enabled_for_integrations = enabled_for_integrations

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
        if issubclass(EventFilter, dict):
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
        if not isinstance(other, EventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
