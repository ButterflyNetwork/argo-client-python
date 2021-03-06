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


class V1alpha1InfoResponse(object):
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
        'links': 'list[V1alpha1Link]',
        'managed_namespace': 'str'
    }

    attribute_map = {
        'links': 'links',
        'managed_namespace': 'managedNamespace'
    }

    def __init__(self, links=None, managed_namespace=None):  # noqa: E501
        """V1alpha1InfoResponse - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._managed_namespace = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if managed_namespace is not None:
            self.managed_namespace = managed_namespace

    @property
    def links(self):
        """Gets the links of this V1alpha1InfoResponse.  # noqa: E501


        :return: The links of this V1alpha1InfoResponse.  # noqa: E501
        :rtype: list[V1alpha1Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this V1alpha1InfoResponse.


        :param links: The links of this V1alpha1InfoResponse.  # noqa: E501
        :type: list[V1alpha1Link]
        """

        self._links = links

    @property
    def managed_namespace(self):
        """Gets the managed_namespace of this V1alpha1InfoResponse.  # noqa: E501


        :return: The managed_namespace of this V1alpha1InfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._managed_namespace

    @managed_namespace.setter
    def managed_namespace(self, managed_namespace):
        """Sets the managed_namespace of this V1alpha1InfoResponse.


        :param managed_namespace: The managed_namespace of this V1alpha1InfoResponse.  # noqa: E501
        :type: str
        """

        self._managed_namespace = managed_namespace

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
        if issubclass(V1alpha1InfoResponse, dict):
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
        if not isinstance(other, V1alpha1InfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
