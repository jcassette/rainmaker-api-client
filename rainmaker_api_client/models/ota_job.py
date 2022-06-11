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

class OTAJob(object):
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
        'ota_job_id': 'str',
        'ota_job_name': 'str',
        'ota_image_id': 'str',
        'completed_count': 'int',
        'total_count': 'int',
        'triggered_timestamp': 'str',
        'nodes': 'list[str]',
        'status': 'str',
        'archived': 'bool',
        'metadata': 'object',
        'user_approval': 'bool',
        'notify_flag': 'bool',
        'groups': 'list[str]',
        'rejected_count': 'int'
    }

    attribute_map = {
        'ota_job_id': 'ota_job_id',
        'ota_job_name': 'ota_job_name',
        'ota_image_id': 'ota_image_id',
        'completed_count': 'completed_count',
        'total_count': 'total_count',
        'triggered_timestamp': 'triggered_timestamp',
        'nodes': 'nodes',
        'status': 'status',
        'archived': 'archived',
        'metadata': 'metadata',
        'user_approval': 'user_approval',
        'notify_flag': 'notify_flag',
        'groups': 'groups',
        'rejected_count': 'rejected_count'
    }

    def __init__(self, ota_job_id=None, ota_job_name=None, ota_image_id=None, completed_count=None, total_count=None, triggered_timestamp=None, nodes=None, status=None, archived=None, metadata=None, user_approval=None, notify_flag=None, groups=None, rejected_count=None):  # noqa: E501
        """OTAJob - a model defined in Swagger"""  # noqa: E501
        self._ota_job_id = None
        self._ota_job_name = None
        self._ota_image_id = None
        self._completed_count = None
        self._total_count = None
        self._triggered_timestamp = None
        self._nodes = None
        self._status = None
        self._archived = None
        self._metadata = None
        self._user_approval = None
        self._notify_flag = None
        self._groups = None
        self._rejected_count = None
        self.discriminator = None
        self.ota_job_id = ota_job_id
        self.ota_job_name = ota_job_name
        self.ota_image_id = ota_image_id
        self.completed_count = completed_count
        self.total_count = total_count
        self.triggered_timestamp = triggered_timestamp
        if nodes is not None:
            self.nodes = nodes
        self.status = status
        if archived is not None:
            self.archived = archived
        if metadata is not None:
            self.metadata = metadata
        if user_approval is not None:
            self.user_approval = user_approval
        if notify_flag is not None:
            self.notify_flag = notify_flag
        if groups is not None:
            self.groups = groups
        if rejected_count is not None:
            self.rejected_count = rejected_count

    @property
    def ota_job_id(self):
        """Gets the ota_job_id of this OTAJob.  # noqa: E501


        :return: The ota_job_id of this OTAJob.  # noqa: E501
        :rtype: str
        """
        return self._ota_job_id

    @ota_job_id.setter
    def ota_job_id(self, ota_job_id):
        """Sets the ota_job_id of this OTAJob.


        :param ota_job_id: The ota_job_id of this OTAJob.  # noqa: E501
        :type: str
        """
        if ota_job_id is None:
            raise ValueError("Invalid value for `ota_job_id`, must not be `None`")  # noqa: E501

        self._ota_job_id = ota_job_id

    @property
    def ota_job_name(self):
        """Gets the ota_job_name of this OTAJob.  # noqa: E501


        :return: The ota_job_name of this OTAJob.  # noqa: E501
        :rtype: str
        """
        return self._ota_job_name

    @ota_job_name.setter
    def ota_job_name(self, ota_job_name):
        """Sets the ota_job_name of this OTAJob.


        :param ota_job_name: The ota_job_name of this OTAJob.  # noqa: E501
        :type: str
        """
        if ota_job_name is None:
            raise ValueError("Invalid value for `ota_job_name`, must not be `None`")  # noqa: E501

        self._ota_job_name = ota_job_name

    @property
    def ota_image_id(self):
        """Gets the ota_image_id of this OTAJob.  # noqa: E501


        :return: The ota_image_id of this OTAJob.  # noqa: E501
        :rtype: str
        """
        return self._ota_image_id

    @ota_image_id.setter
    def ota_image_id(self, ota_image_id):
        """Sets the ota_image_id of this OTAJob.


        :param ota_image_id: The ota_image_id of this OTAJob.  # noqa: E501
        :type: str
        """
        if ota_image_id is None:
            raise ValueError("Invalid value for `ota_image_id`, must not be `None`")  # noqa: E501

        self._ota_image_id = ota_image_id

    @property
    def completed_count(self):
        """Gets the completed_count of this OTAJob.  # noqa: E501


        :return: The completed_count of this OTAJob.  # noqa: E501
        :rtype: int
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count):
        """Sets the completed_count of this OTAJob.


        :param completed_count: The completed_count of this OTAJob.  # noqa: E501
        :type: int
        """
        if completed_count is None:
            raise ValueError("Invalid value for `completed_count`, must not be `None`")  # noqa: E501

        self._completed_count = completed_count

    @property
    def total_count(self):
        """Gets the total_count of this OTAJob.  # noqa: E501


        :return: The total_count of this OTAJob.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this OTAJob.


        :param total_count: The total_count of this OTAJob.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def triggered_timestamp(self):
        """Gets the triggered_timestamp of this OTAJob.  # noqa: E501


        :return: The triggered_timestamp of this OTAJob.  # noqa: E501
        :rtype: str
        """
        return self._triggered_timestamp

    @triggered_timestamp.setter
    def triggered_timestamp(self, triggered_timestamp):
        """Sets the triggered_timestamp of this OTAJob.


        :param triggered_timestamp: The triggered_timestamp of this OTAJob.  # noqa: E501
        :type: str
        """
        if triggered_timestamp is None:
            raise ValueError("Invalid value for `triggered_timestamp`, must not be `None`")  # noqa: E501

        self._triggered_timestamp = triggered_timestamp

    @property
    def nodes(self):
        """Gets the nodes of this OTAJob.  # noqa: E501


        :return: The nodes of this OTAJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this OTAJob.


        :param nodes: The nodes of this OTAJob.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def status(self):
        """Gets the status of this OTAJob.  # noqa: E501


        :return: The status of this OTAJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OTAJob.


        :param status: The status of this OTAJob.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["active", "cancelled", "finished", "triggered"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def archived(self):
        """Gets the archived of this OTAJob.  # noqa: E501


        :return: The archived of this OTAJob.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this OTAJob.


        :param archived: The archived of this OTAJob.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def metadata(self):
        """Gets the metadata of this OTAJob.  # noqa: E501


        :return: The metadata of this OTAJob.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OTAJob.


        :param metadata: The metadata of this OTAJob.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def user_approval(self):
        """Gets the user_approval of this OTAJob.  # noqa: E501


        :return: The user_approval of this OTAJob.  # noqa: E501
        :rtype: bool
        """
        return self._user_approval

    @user_approval.setter
    def user_approval(self, user_approval):
        """Sets the user_approval of this OTAJob.


        :param user_approval: The user_approval of this OTAJob.  # noqa: E501
        :type: bool
        """

        self._user_approval = user_approval

    @property
    def notify_flag(self):
        """Gets the notify_flag of this OTAJob.  # noqa: E501


        :return: The notify_flag of this OTAJob.  # noqa: E501
        :rtype: bool
        """
        return self._notify_flag

    @notify_flag.setter
    def notify_flag(self, notify_flag):
        """Sets the notify_flag of this OTAJob.


        :param notify_flag: The notify_flag of this OTAJob.  # noqa: E501
        :type: bool
        """

        self._notify_flag = notify_flag

    @property
    def groups(self):
        """Gets the groups of this OTAJob.  # noqa: E501


        :return: The groups of this OTAJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OTAJob.


        :param groups: The groups of this OTAJob.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def rejected_count(self):
        """Gets the rejected_count of this OTAJob.  # noqa: E501


        :return: The rejected_count of this OTAJob.  # noqa: E501
        :rtype: int
        """
        return self._rejected_count

    @rejected_count.setter
    def rejected_count(self, rejected_count):
        """Sets the rejected_count of this OTAJob.


        :param rejected_count: The rejected_count of this OTAJob.  # noqa: E501
        :type: int
        """

        self._rejected_count = rejected_count

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
        if issubclass(OTAJob, dict):
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
        if not isinstance(other, OTAJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other