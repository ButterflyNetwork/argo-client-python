# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: 2.5.0-rc3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1ItemValue(object):
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
        'bool_val': 'bool',
        'list_val': 'list[str]',
        'map_val': 'dict(str, str)',
        'num_val': 'str',
        'str_val': 'str',
        'type': 'int'
    }

    attribute_map = {
        'bool_val': 'BoolVal',
        'list_val': 'ListVal',
        'map_val': 'MapVal',
        'num_val': 'NumVal',
        'str_val': 'StrVal',
        'type': 'Type'
    }

    def __init__(self, bool_val=None, list_val=None, map_val=None, num_val=None, str_val=None, type=None):  # noqa: E501
        """V1alpha1ItemValue - a model defined in Swagger"""  # noqa: E501

        self._bool_val = None
        self._list_val = None
        self._map_val = None
        self._num_val = None
        self._str_val = None
        self._type = None
        self.discriminator = None

        self.bool_val = bool_val
        self.list_val = list_val
        self.map_val = map_val
        self.num_val = num_val
        self.str_val = str_val
        self.type = type

    @property
    def bool_val(self):
        """Gets the bool_val of this V1alpha1ItemValue.  # noqa: E501


        :return: The bool_val of this V1alpha1ItemValue.  # noqa: E501
        :rtype: bool
        """
        return self._bool_val

    @bool_val.setter
    def bool_val(self, bool_val):
        """Sets the bool_val of this V1alpha1ItemValue.


        :param bool_val: The bool_val of this V1alpha1ItemValue.  # noqa: E501
        :type: bool
        """
        if bool_val is None:
            raise ValueError("Invalid value for `bool_val`, must not be `None`")  # noqa: E501

        self._bool_val = bool_val

    @property
    def list_val(self):
        """Gets the list_val of this V1alpha1ItemValue.  # noqa: E501


        :return: The list_val of this V1alpha1ItemValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_val

    @list_val.setter
    def list_val(self, list_val):
        """Sets the list_val of this V1alpha1ItemValue.


        :param list_val: The list_val of this V1alpha1ItemValue.  # noqa: E501
        :type: list[str]
        """
        if list_val is None:
            raise ValueError("Invalid value for `list_val`, must not be `None`")  # noqa: E501

        self._list_val = list_val

    @property
    def map_val(self):
        """Gets the map_val of this V1alpha1ItemValue.  # noqa: E501


        :return: The map_val of this V1alpha1ItemValue.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._map_val

    @map_val.setter
    def map_val(self, map_val):
        """Sets the map_val of this V1alpha1ItemValue.


        :param map_val: The map_val of this V1alpha1ItemValue.  # noqa: E501
        :type: dict(str, str)
        """
        if map_val is None:
            raise ValueError("Invalid value for `map_val`, must not be `None`")  # noqa: E501

        self._map_val = map_val

    @property
    def num_val(self):
        """Gets the num_val of this V1alpha1ItemValue.  # noqa: E501


        :return: The num_val of this V1alpha1ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._num_val

    @num_val.setter
    def num_val(self, num_val):
        """Sets the num_val of this V1alpha1ItemValue.


        :param num_val: The num_val of this V1alpha1ItemValue.  # noqa: E501
        :type: str
        """
        if num_val is None:
            raise ValueError("Invalid value for `num_val`, must not be `None`")  # noqa: E501

        self._num_val = num_val

    @property
    def str_val(self):
        """Gets the str_val of this V1alpha1ItemValue.  # noqa: E501


        :return: The str_val of this V1alpha1ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._str_val

    @str_val.setter
    def str_val(self, str_val):
        """Sets the str_val of this V1alpha1ItemValue.


        :param str_val: The str_val of this V1alpha1ItemValue.  # noqa: E501
        :type: str
        """
        if str_val is None:
            raise ValueError("Invalid value for `str_val`, must not be `None`")  # noqa: E501

        self._str_val = str_val

    @property
    def type(self):
        """Gets the type of this V1alpha1ItemValue.  # noqa: E501


        :return: The type of this V1alpha1ItemValue.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1ItemValue.


        :param type: The type of this V1alpha1ItemValue.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(V1alpha1ItemValue, dict):
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
        if not isinstance(other, V1alpha1ItemValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
