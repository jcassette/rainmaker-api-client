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

class AutomationTrigger(object):
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
        'name': 'str',
        'automation_id': 'str',
        'enabled': 'bool',
        'node_id': 'str',
        'event_type': 'str',
        'metadata': 'str',
        'events': 'list[AddAutomationTriggerRequestEvents]',
        'event_operator': 'str',
        'actions': 'list[AddAutomationTriggerRequestActions]'
    }

    attribute_map = {
        'name': 'name',
        'automation_id': 'automation_id',
        'enabled': 'enabled',
        'node_id': 'node_id',
        'event_type': 'event_type',
        'metadata': 'metadata',
        'events': 'events',
        'event_operator': 'event_operator',
        'actions': 'actions'
    }

    def __init__(self, name=None, automation_id=None, enabled=None, node_id=None, event_type=None, metadata=None, events=None, event_operator=None, actions=None):  # noqa: E501
        """AutomationTrigger - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._automation_id = None
        self._enabled = None
        self._node_id = None
        self._event_type = None
        self._metadata = None
        self._events = None
        self._event_operator = None
        self._actions = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if automation_id is not None:
            self.automation_id = automation_id
        if enabled is not None:
            self.enabled = enabled
        if node_id is not None:
            self.node_id = node_id
        if event_type is not None:
            self.event_type = event_type
        if metadata is not None:
            self.metadata = metadata
        if events is not None:
            self.events = events
        if event_operator is not None:
            self.event_operator = event_operator
        if actions is not None:
            self.actions = actions

    @property
    def name(self):
        """Gets the name of this AutomationTrigger.  # noqa: E501


        :return: The name of this AutomationTrigger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutomationTrigger.


        :param name: The name of this AutomationTrigger.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def automation_id(self):
        """Gets the automation_id of this AutomationTrigger.  # noqa: E501


        :return: The automation_id of this AutomationTrigger.  # noqa: E501
        :rtype: str
        """
        return self._automation_id

    @automation_id.setter
    def automation_id(self, automation_id):
        """Sets the automation_id of this AutomationTrigger.


        :param automation_id: The automation_id of this AutomationTrigger.  # noqa: E501
        :type: str
        """

        self._automation_id = automation_id

    @property
    def enabled(self):
        """Gets the enabled of this AutomationTrigger.  # noqa: E501


        :return: The enabled of this AutomationTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AutomationTrigger.


        :param enabled: The enabled of this AutomationTrigger.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def node_id(self):
        """Gets the node_id of this AutomationTrigger.  # noqa: E501


        :return: The node_id of this AutomationTrigger.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AutomationTrigger.


        :param node_id: The node_id of this AutomationTrigger.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def event_type(self):
        """Gets the event_type of this AutomationTrigger.  # noqa: E501


        :return: The event_type of this AutomationTrigger.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this AutomationTrigger.


        :param event_type: The event_type of this AutomationTrigger.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def metadata(self):
        """Gets the metadata of this AutomationTrigger.  # noqa: E501


        :return: The metadata of this AutomationTrigger.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AutomationTrigger.


        :param metadata: The metadata of this AutomationTrigger.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def events(self):
        """Gets the events of this AutomationTrigger.  # noqa: E501


        :return: The events of this AutomationTrigger.  # noqa: E501
        :rtype: list[AddAutomationTriggerRequestEvents]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this AutomationTrigger.


        :param events: The events of this AutomationTrigger.  # noqa: E501
        :type: list[AddAutomationTriggerRequestEvents]
        """

        self._events = events

    @property
    def event_operator(self):
        """Gets the event_operator of this AutomationTrigger.  # noqa: E501


        :return: The event_operator of this AutomationTrigger.  # noqa: E501
        :rtype: str
        """
        return self._event_operator

    @event_operator.setter
    def event_operator(self, event_operator):
        """Sets the event_operator of this AutomationTrigger.


        :param event_operator: The event_operator of this AutomationTrigger.  # noqa: E501
        :type: str
        """

        self._event_operator = event_operator

    @property
    def actions(self):
        """Gets the actions of this AutomationTrigger.  # noqa: E501


        :return: The actions of this AutomationTrigger.  # noqa: E501
        :rtype: list[AddAutomationTriggerRequestActions]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AutomationTrigger.


        :param actions: The actions of this AutomationTrigger.  # noqa: E501
        :type: list[AddAutomationTriggerRequestActions]
        """

        self._actions = actions

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
        if issubclass(AutomationTrigger, dict):
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
        if not isinstance(other, AutomationTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
