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


class V1alpha1ArtifactLocation(object):
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
        'archive_logs': 'bool',
        'artifactory': 'V1alpha1ArtifactoryArtifact',
        'gcs': 'V1alpha1GCSArtifact',
        'git': 'V1alpha1GitArtifact',
        'hdfs': 'V1alpha1HDFSArtifact',
        'http': 'V1alpha1HTTPArtifact',
        'oss': 'V1alpha1OSSArtifact',
        'raw': 'V1alpha1RawArtifact',
        's3': 'V1alpha1S3Artifact'
    }

    attribute_map = {
        'archive_logs': 'archiveLogs',
        'artifactory': 'artifactory',
        'gcs': 'gcs',
        'git': 'git',
        'hdfs': 'hdfs',
        'http': 'http',
        'oss': 'oss',
        'raw': 'raw',
        's3': 's3'
    }

    def __init__(self, archive_logs=None, artifactory=None, gcs=None, git=None, hdfs=None, http=None, oss=None, raw=None, s3=None):  # noqa: E501
        """V1alpha1ArtifactLocation - a model defined in Swagger"""  # noqa: E501

        self._archive_logs = None
        self._artifactory = None
        self._gcs = None
        self._git = None
        self._hdfs = None
        self._http = None
        self._oss = None
        self._raw = None
        self._s3 = None
        self.discriminator = None

        if archive_logs is not None:
            self.archive_logs = archive_logs
        if artifactory is not None:
            self.artifactory = artifactory
        if gcs is not None:
            self.gcs = gcs
        if git is not None:
            self.git = git
        if hdfs is not None:
            self.hdfs = hdfs
        if http is not None:
            self.http = http
        if oss is not None:
            self.oss = oss
        if raw is not None:
            self.raw = raw
        if s3 is not None:
            self.s3 = s3

    @property
    def archive_logs(self):
        """Gets the archive_logs of this V1alpha1ArtifactLocation.  # noqa: E501

        ArchiveLogs indicates if the container logs should be archived  # noqa: E501

        :return: The archive_logs of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: bool
        """
        return self._archive_logs

    @archive_logs.setter
    def archive_logs(self, archive_logs):
        """Sets the archive_logs of this V1alpha1ArtifactLocation.

        ArchiveLogs indicates if the container logs should be archived  # noqa: E501

        :param archive_logs: The archive_logs of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: bool
        """

        self._archive_logs = archive_logs

    @property
    def artifactory(self):
        """Gets the artifactory of this V1alpha1ArtifactLocation.  # noqa: E501

        Artifactory contains artifactory artifact location details  # noqa: E501

        :return: The artifactory of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1ArtifactoryArtifact
        """
        return self._artifactory

    @artifactory.setter
    def artifactory(self, artifactory):
        """Sets the artifactory of this V1alpha1ArtifactLocation.

        Artifactory contains artifactory artifact location details  # noqa: E501

        :param artifactory: The artifactory of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1ArtifactoryArtifact
        """

        self._artifactory = artifactory

    @property
    def gcs(self):
        """Gets the gcs of this V1alpha1ArtifactLocation.  # noqa: E501

        GCS contains GCS artifact location details  # noqa: E501

        :return: The gcs of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1GCSArtifact
        """
        return self._gcs

    @gcs.setter
    def gcs(self, gcs):
        """Sets the gcs of this V1alpha1ArtifactLocation.

        GCS contains GCS artifact location details  # noqa: E501

        :param gcs: The gcs of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1GCSArtifact
        """

        self._gcs = gcs

    @property
    def git(self):
        """Gets the git of this V1alpha1ArtifactLocation.  # noqa: E501

        Git contains git artifact location details  # noqa: E501

        :return: The git of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1GitArtifact
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this V1alpha1ArtifactLocation.

        Git contains git artifact location details  # noqa: E501

        :param git: The git of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1GitArtifact
        """

        self._git = git

    @property
    def hdfs(self):
        """Gets the hdfs of this V1alpha1ArtifactLocation.  # noqa: E501

        HDFS contains HDFS artifact location details  # noqa: E501

        :return: The hdfs of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1HDFSArtifact
        """
        return self._hdfs

    @hdfs.setter
    def hdfs(self, hdfs):
        """Sets the hdfs of this V1alpha1ArtifactLocation.

        HDFS contains HDFS artifact location details  # noqa: E501

        :param hdfs: The hdfs of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1HDFSArtifact
        """

        self._hdfs = hdfs

    @property
    def http(self):
        """Gets the http of this V1alpha1ArtifactLocation.  # noqa: E501

        HTTP contains HTTP artifact location details  # noqa: E501

        :return: The http of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1HTTPArtifact
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this V1alpha1ArtifactLocation.

        HTTP contains HTTP artifact location details  # noqa: E501

        :param http: The http of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1HTTPArtifact
        """

        self._http = http

    @property
    def oss(self):
        """Gets the oss of this V1alpha1ArtifactLocation.  # noqa: E501

        OSS contains OSS artifact location details  # noqa: E501

        :return: The oss of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1OSSArtifact
        """
        return self._oss

    @oss.setter
    def oss(self, oss):
        """Sets the oss of this V1alpha1ArtifactLocation.

        OSS contains OSS artifact location details  # noqa: E501

        :param oss: The oss of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1OSSArtifact
        """

        self._oss = oss

    @property
    def raw(self):
        """Gets the raw of this V1alpha1ArtifactLocation.  # noqa: E501

        Raw contains raw artifact location details  # noqa: E501

        :return: The raw of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1RawArtifact
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this V1alpha1ArtifactLocation.

        Raw contains raw artifact location details  # noqa: E501

        :param raw: The raw of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1RawArtifact
        """

        self._raw = raw

    @property
    def s3(self):
        """Gets the s3 of this V1alpha1ArtifactLocation.  # noqa: E501

        S3 contains S3 artifact location details  # noqa: E501

        :return: The s3 of this V1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1alpha1S3Artifact
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this V1alpha1ArtifactLocation.

        S3 contains S3 artifact location details  # noqa: E501

        :param s3: The s3 of this V1alpha1ArtifactLocation.  # noqa: E501
        :type: V1alpha1S3Artifact
        """

        self._s3 = s3

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
        if issubclass(V1alpha1ArtifactLocation, dict):
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
        if not isinstance(other, V1alpha1ArtifactLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
