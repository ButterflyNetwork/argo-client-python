# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: release-2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1LogEntry(object):
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
        'content': 'str',
        'pod_name': 'str'
    }

    attribute_map = {
        'content': 'content',
        'pod_name': 'podName'
    }

    def __init__(self, content=None, pod_name=None):  # noqa: E501
        """V1alpha1LogEntry - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._pod_name = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def content(self):
        """Gets the content of this V1alpha1LogEntry.  # noqa: E501


        :return: The content of this V1alpha1LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this V1alpha1LogEntry.


        :param content: The content of this V1alpha1LogEntry.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def pod_name(self):
        """Gets the pod_name of this V1alpha1LogEntry.  # noqa: E501


        :return: The pod_name of this V1alpha1LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this V1alpha1LogEntry.


        :param pod_name: The pod_name of this V1alpha1LogEntry.  # noqa: E501
        :type: str
        """

        self._pod_name = pod_name

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
        if issubclass(V1alpha1LogEntry, dict):
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
        if not isinstance(other, V1alpha1LogEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
