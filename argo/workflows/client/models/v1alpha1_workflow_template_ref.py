# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: release-2.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1WorkflowTemplateRef(object):
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
        'cluster_scope': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'cluster_scope': 'clusterScope',
        'name': 'name'
    }

    def __init__(self, cluster_scope=None, name=None):  # noqa: E501
        """V1alpha1WorkflowTemplateRef - a model defined in Swagger"""  # noqa: E501

        self._cluster_scope = None
        self._name = None
        self.discriminator = None

        if cluster_scope is not None:
            self.cluster_scope = cluster_scope
        if name is not None:
            self.name = name

    @property
    def cluster_scope(self):
        """Gets the cluster_scope of this V1alpha1WorkflowTemplateRef.  # noqa: E501

        ClusterScope indicates the referred template is cluster scoped (i.e. a ClusterWorkflowTemplate).  # noqa: E501

        :return: The cluster_scope of this V1alpha1WorkflowTemplateRef.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_scope

    @cluster_scope.setter
    def cluster_scope(self, cluster_scope):
        """Sets the cluster_scope of this V1alpha1WorkflowTemplateRef.

        ClusterScope indicates the referred template is cluster scoped (i.e. a ClusterWorkflowTemplate).  # noqa: E501

        :param cluster_scope: The cluster_scope of this V1alpha1WorkflowTemplateRef.  # noqa: E501
        :type: bool
        """

        self._cluster_scope = cluster_scope

    @property
    def name(self):
        """Gets the name of this V1alpha1WorkflowTemplateRef.  # noqa: E501

        Name is the resource name of the workflow template.  # noqa: E501

        :return: The name of this V1alpha1WorkflowTemplateRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1WorkflowTemplateRef.

        Name is the resource name of the workflow template.  # noqa: E501

        :param name: The name of this V1alpha1WorkflowTemplateRef.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(V1alpha1WorkflowTemplateRef, dict):
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
        if not isinstance(other, V1alpha1WorkflowTemplateRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
