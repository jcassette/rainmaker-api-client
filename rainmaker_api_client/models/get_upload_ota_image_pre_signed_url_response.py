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

class GetUploadOTAImagePreSignedUrlResponse(object):
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
        'ota_image_id': 'str',
        'upload_url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'ota_image_id': 'ota_image_id',
        'upload_url': 'upload_url',
        'status': 'status'
    }

    def __init__(self, ota_image_id=None, upload_url=None, status=None):  # noqa: E501
        """GetUploadOTAImagePreSignedUrlResponse - a model defined in Swagger"""  # noqa: E501
        self._ota_image_id = None
        self._upload_url = None
        self._status = None
        self.discriminator = None
        if ota_image_id is not None:
            self.ota_image_id = ota_image_id
        if upload_url is not None:
            self.upload_url = upload_url
        if status is not None:
            self.status = status

    @property
    def ota_image_id(self):
        """Gets the ota_image_id of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501


        :return: The ota_image_id of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._ota_image_id

    @ota_image_id.setter
    def ota_image_id(self, ota_image_id):
        """Sets the ota_image_id of this GetUploadOTAImagePreSignedUrlResponse.


        :param ota_image_id: The ota_image_id of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501
        :type: str
        """

        self._ota_image_id = ota_image_id

    @property
    def upload_url(self):
        """Gets the upload_url of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501


        :return: The upload_url of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this GetUploadOTAImagePreSignedUrlResponse.


        :param upload_url: The upload_url of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501
        :type: str
        """

        self._upload_url = upload_url

    @property
    def status(self):
        """Gets the status of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501


        :return: The status of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetUploadOTAImagePreSignedUrlResponse.


        :param status: The status of this GetUploadOTAImagePreSignedUrlResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(GetUploadOTAImagePreSignedUrlResponse, dict):
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
        if not isinstance(other, GetUploadOTAImagePreSignedUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other