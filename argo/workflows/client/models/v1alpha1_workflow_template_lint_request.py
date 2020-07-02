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


class V1alpha1WorkflowTemplateLintRequest(object):
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
        'create_options': 'V1CreateOptions',
        'namespace': 'str',
        'template': 'V1alpha1WorkflowTemplate'
    }

    attribute_map = {
        'create_options': 'createOptions',
        'namespace': 'namespace',
        'template': 'template'
    }

    def __init__(self, create_options=None, namespace=None, template=None):  # noqa: E501
        """V1alpha1WorkflowTemplateLintRequest - a model defined in Swagger"""  # noqa: E501

        self._create_options = None
        self._namespace = None
        self._template = None
        self.discriminator = None

        if create_options is not None:
            self.create_options = create_options
        if namespace is not None:
            self.namespace = namespace
        if template is not None:
            self.template = template

    @property
    def create_options(self):
        """Gets the create_options of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501


        :return: The create_options of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501
        :rtype: V1CreateOptions
        """
        return self._create_options

    @create_options.setter
    def create_options(self, create_options):
        """Sets the create_options of this V1alpha1WorkflowTemplateLintRequest.


        :param create_options: The create_options of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501
        :type: V1CreateOptions
        """

        self._create_options = create_options

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501


        :return: The namespace of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1WorkflowTemplateLintRequest.


        :param namespace: The namespace of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def template(self):
        """Gets the template of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501


        :return: The template of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501
        :rtype: V1alpha1WorkflowTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1WorkflowTemplateLintRequest.


        :param template: The template of this V1alpha1WorkflowTemplateLintRequest.  # noqa: E501
        :type: V1alpha1WorkflowTemplate
        """

        self._template = template

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
        if issubclass(V1alpha1WorkflowTemplateLintRequest, dict):
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
        if not isinstance(other, V1alpha1WorkflowTemplateLintRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
