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


class V1LabelSelectorRequirement(object):
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
        'key': 'str',
        'operator': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, key=None, operator=None, values=None):  # noqa: E501
        """V1LabelSelectorRequirement - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._operator = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.operator = operator
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this V1LabelSelectorRequirement.  # noqa: E501

        key is the label key that the selector applies to.  # noqa: E501

        :return: The key of this V1LabelSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1LabelSelectorRequirement.

        key is the label key that the selector applies to.  # noqa: E501

        :param key: The key of this V1LabelSelectorRequirement.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def operator(self):
        """Gets the operator of this V1LabelSelectorRequirement.  # noqa: E501

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.  # noqa: E501

        :return: The operator of this V1LabelSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this V1LabelSelectorRequirement.

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.  # noqa: E501

        :param operator: The operator of this V1LabelSelectorRequirement.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def values(self):
        """Gets the values of this V1LabelSelectorRequirement.  # noqa: E501

        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.  # noqa: E501

        :return: The values of this V1LabelSelectorRequirement.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1LabelSelectorRequirement.

        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.  # noqa: E501

        :param values: The values of this V1LabelSelectorRequirement.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(V1LabelSelectorRequirement, dict):
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
        if not isinstance(other, V1LabelSelectorRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
