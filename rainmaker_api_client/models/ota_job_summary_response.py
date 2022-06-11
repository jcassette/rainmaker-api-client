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

class OtaJobSummaryResponse(object):
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
        'triggered': 'int',
        'started': 'int',
        'in_progress': 'int',
        'rejected': 'int',
        'delayed': 'int',
        'success': 'int',
        'failed': 'int',
        'total': 'int'
    }

    attribute_map = {
        'triggered': 'triggered',
        'started': 'started',
        'in_progress': 'in_progress',
        'rejected': 'rejected',
        'delayed': 'delayed',
        'success': 'success',
        'failed': 'failed',
        'total': 'total'
    }

    def __init__(self, triggered=None, started=None, in_progress=None, rejected=None, delayed=None, success=None, failed=None, total=None):  # noqa: E501
        """OtaJobSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._triggered = None
        self._started = None
        self._in_progress = None
        self._rejected = None
        self._delayed = None
        self._success = None
        self._failed = None
        self._total = None
        self.discriminator = None
        if triggered is not None:
            self.triggered = triggered
        if started is not None:
            self.started = started
        if in_progress is not None:
            self.in_progress = in_progress
        if rejected is not None:
            self.rejected = rejected
        if delayed is not None:
            self.delayed = delayed
        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if total is not None:
            self.total = total

    @property
    def triggered(self):
        """Gets the triggered of this OtaJobSummaryResponse.  # noqa: E501


        :return: The triggered of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._triggered

    @triggered.setter
    def triggered(self, triggered):
        """Sets the triggered of this OtaJobSummaryResponse.


        :param triggered: The triggered of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._triggered = triggered

    @property
    def started(self):
        """Gets the started of this OtaJobSummaryResponse.  # noqa: E501


        :return: The started of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this OtaJobSummaryResponse.


        :param started: The started of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._started = started

    @property
    def in_progress(self):
        """Gets the in_progress of this OtaJobSummaryResponse.  # noqa: E501


        :return: The in_progress of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this OtaJobSummaryResponse.


        :param in_progress: The in_progress of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._in_progress = in_progress

    @property
    def rejected(self):
        """Gets the rejected of this OtaJobSummaryResponse.  # noqa: E501


        :return: The rejected of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._rejected

    @rejected.setter
    def rejected(self, rejected):
        """Sets the rejected of this OtaJobSummaryResponse.


        :param rejected: The rejected of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._rejected = rejected

    @property
    def delayed(self):
        """Gets the delayed of this OtaJobSummaryResponse.  # noqa: E501


        :return: The delayed of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._delayed

    @delayed.setter
    def delayed(self, delayed):
        """Sets the delayed of this OtaJobSummaryResponse.


        :param delayed: The delayed of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._delayed = delayed

    @property
    def success(self):
        """Gets the success of this OtaJobSummaryResponse.  # noqa: E501


        :return: The success of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this OtaJobSummaryResponse.


        :param success: The success of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._success = success

    @property
    def failed(self):
        """Gets the failed of this OtaJobSummaryResponse.  # noqa: E501


        :return: The failed of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this OtaJobSummaryResponse.


        :param failed: The failed of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def total(self):
        """Gets the total of this OtaJobSummaryResponse.  # noqa: E501


        :return: The total of this OtaJobSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OtaJobSummaryResponse.


        :param total: The total of this OtaJobSummaryResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(OtaJobSummaryResponse, dict):
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
        if not isinstance(other, OtaJobSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other