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


class V1VsphereVirtualDiskVolumeSource(object):
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
        'fs_type': 'str',
        'storage_policy_id': 'str',
        'storage_policy_name': 'str',
        'volume_path': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'storage_policy_id': 'storagePolicyID',
        'storage_policy_name': 'storagePolicyName',
        'volume_path': 'volumePath'
    }

    def __init__(self, fs_type=None, storage_policy_id=None, storage_policy_name=None, volume_path=None):  # noqa: E501
        """V1VsphereVirtualDiskVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._fs_type = None
        self._storage_policy_id = None
        self._storage_policy_name = None
        self._volume_path = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if storage_policy_id is not None:
            self.storage_policy_id = storage_policy_id
        if storage_policy_name is not None:
            self.storage_policy_name = storage_policy_name
        self.volume_path = volume_path

    @property
    def fs_type(self):
        """Gets the fs_type of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1VsphereVirtualDiskVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def storage_policy_id(self):
        """Gets the storage_policy_id of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501

        Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.  # noqa: E501

        :return: The storage_policy_id of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._storage_policy_id

    @storage_policy_id.setter
    def storage_policy_id(self, storage_policy_id):
        """Sets the storage_policy_id of this V1VsphereVirtualDiskVolumeSource.

        Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.  # noqa: E501

        :param storage_policy_id: The storage_policy_id of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :type: str
        """

        self._storage_policy_id = storage_policy_id

    @property
    def storage_policy_name(self):
        """Gets the storage_policy_name of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501

        Storage Policy Based Management (SPBM) profile name.  # noqa: E501

        :return: The storage_policy_name of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._storage_policy_name

    @storage_policy_name.setter
    def storage_policy_name(self, storage_policy_name):
        """Sets the storage_policy_name of this V1VsphereVirtualDiskVolumeSource.

        Storage Policy Based Management (SPBM) profile name.  # noqa: E501

        :param storage_policy_name: The storage_policy_name of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :type: str
        """

        self._storage_policy_name = storage_policy_name

    @property
    def volume_path(self):
        """Gets the volume_path of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501

        Path that identifies vSphere volume vmdk  # noqa: E501

        :return: The volume_path of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume_path

    @volume_path.setter
    def volume_path(self, volume_path):
        """Sets the volume_path of this V1VsphereVirtualDiskVolumeSource.

        Path that identifies vSphere volume vmdk  # noqa: E501

        :param volume_path: The volume_path of this V1VsphereVirtualDiskVolumeSource.  # noqa: E501
        :type: str
        """
        if volume_path is None:
            raise ValueError("Invalid value for `volume_path`, must not be `None`")  # noqa: E501

        self._volume_path = volume_path

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
        if issubclass(V1VsphereVirtualDiskVolumeSource, dict):
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
        if not isinstance(other, V1VsphereVirtualDiskVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
