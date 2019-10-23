# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: 2.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.models.v1alpha1_artifact_location import V1alpha1ArtifactLocation  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_dag_template import V1alpha1DAGTemplate  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_inputs import V1alpha1Inputs  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_metadata import V1alpha1Metadata  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_outputs import V1alpha1Outputs  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_resource_template import V1alpha1ResourceTemplate  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_script_template import V1alpha1ScriptTemplate  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_user_container import V1alpha1UserContainer  # noqa: F401,E501
from argo.workflows.client.models.v1alpha1_workflow_step import V1alpha1WorkflowStep  # noqa: F401,E501

from kubernetes.client.models import V1Affinity
from kubernetes.client.models import V1Container
from kubernetes.client.models import V1Toleration
from kubernetes.client.models import V1Volume

class V1alpha1Template(object):
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
        'active_deadline_seconds': 'int',
        'affinity': 'V1Affinity',
        'archive_location': 'V1alpha1ArtifactLocation',
        'container': 'V1Container',
        'daemon': 'bool',
        'dag': 'V1alpha1DAGTemplate',
        'init_containers': 'list[V1alpha1UserContainer]',
        'inputs': 'V1alpha1Inputs',
        'metadata': 'V1alpha1Metadata',
        'name': 'str',
        'node_selector': 'dict(str, str)',
        'outputs': 'V1alpha1Outputs',
        'parallelism': 'int',
        'priority': 'int',
        'priority_class_name': 'str',
        'resource': 'V1alpha1ResourceTemplate',
        'retry_strategy': 'V1alpha1RetryStrategy',
        'scheduler_name': 'str',
        'script': 'V1alpha1ScriptTemplate',
        'sidecars': 'list[V1alpha1UserContainer]',
        'steps': 'list[list[V1alpha1WorkflowStep]]',
        'suspend': 'object',
        'tolerations': 'list[V1Toleration]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'affinity': 'affinity',
        'archive_location': 'archiveLocation',
        'container': 'container',
        'daemon': 'daemon',
        'dag': 'dag',
        'init_containers': 'initContainers',
        'inputs': 'inputs',
        'metadata': 'metadata',
        'name': 'name',
        'node_selector': 'nodeSelector',
        'outputs': 'outputs',
        'parallelism': 'parallelism',
        'priority': 'priority',
        'priority_class_name': 'priorityClassName',
        'resource': 'resource',
        'retry_strategy': 'retryStrategy',
        'scheduler_name': 'schedulerName',
        'script': 'script',
        'sidecars': 'sidecars',
        'steps': 'steps',
        'suspend': 'suspend',
        'tolerations': 'tolerations',
        'volumes': 'volumes'
    }

    def __init__(self, active_deadline_seconds=None, affinity=None, archive_location=None, container=None, daemon=None, dag=None, init_containers=None, inputs=None, metadata=None, name=None, node_selector=None, outputs=None, parallelism=None, priority=None, priority_class_name=None, resource=None, retry_strategy=None, scheduler_name=None, script=None, sidecars=None, steps=None, suspend=None, tolerations=None, volumes=None):  # noqa: E501
        """V1alpha1Template - a model defined in Swagger"""  # noqa: E501

        self._active_deadline_seconds = None
        self._affinity = None
        self._archive_location = None
        self._container = None
        self._daemon = None
        self._dag = None
        self._init_containers = None
        self._inputs = None
        self._metadata = None
        self._name = None
        self._node_selector = None
        self._outputs = None
        self._parallelism = None
        self._priority = None
        self._priority_class_name = None
        self._resource = None
        self._retry_strategy = None
        self._scheduler_name = None
        self._script = None
        self._sidecars = None
        self._steps = None
        self._suspend = None
        self._tolerations = None
        self._volumes = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if affinity is not None:
            self.affinity = affinity
        if archive_location is not None:
            self.archive_location = archive_location
        if container is not None:
            self.container = container
        if daemon is not None:
            self.daemon = daemon
        if dag is not None:
            self.dag = dag
        if init_containers is not None:
            self.init_containers = init_containers
        if inputs is not None:
            self.inputs = inputs
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if node_selector is not None:
            self.node_selector = node_selector
        if outputs is not None:
            self.outputs = outputs
        if parallelism is not None:
            self.parallelism = parallelism
        if priority is not None:
            self.priority = priority
        if priority_class_name is not None:
            self.priority_class_name = priority_class_name
        if resource is not None:
            self.resource = resource
        if retry_strategy is not None:
            self.retry_strategy = retry_strategy
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name
        if script is not None:
            self.script = script
        if sidecars is not None:
            self.sidecars = sidecars
        if steps is not None:
            self.steps = steps
        if suspend is not None:
            self.suspend = suspend
        if tolerations is not None:
            self.tolerations = tolerations
        if volumes is not None:
            self.volumes = volumes

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V1alpha1Template.  # noqa: E501

        Optional duration in seconds relative to the StartTime that the pod may be active on a node before the system actively tries to terminate the pod; value must be positive integer This field is only applicable to container and script templates.  # noqa: E501

        :return: The active_deadline_seconds of this V1alpha1Template.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V1alpha1Template.

        Optional duration in seconds relative to the StartTime that the pod may be active on a node before the system actively tries to terminate the pod; value must be positive integer This field is only applicable to container and script templates.  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this V1alpha1Template.  # noqa: E501
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def affinity(self):
        """Gets the affinity of this V1alpha1Template.  # noqa: E501

        Affinity sets the pod's scheduling constraints Overrides the affinity set at the workflow level (if any)  # noqa: E501

        :return: The affinity of this V1alpha1Template.  # noqa: E501
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this V1alpha1Template.

        Affinity sets the pod's scheduling constraints Overrides the affinity set at the workflow level (if any)  # noqa: E501

        :param affinity: The affinity of this V1alpha1Template.  # noqa: E501
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def archive_location(self):
        """Gets the archive_location of this V1alpha1Template.  # noqa: E501

        Location in which all files related to the step will be stored (logs, artifacts, etc...). Can be overridden by individual items in Outputs. If omitted, will use the default artifact repository location configured in the controller, appended with the <workflowname>/<nodename> in the key.  # noqa: E501

        :return: The archive_location of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ArtifactLocation
        """
        return self._archive_location

    @archive_location.setter
    def archive_location(self, archive_location):
        """Sets the archive_location of this V1alpha1Template.

        Location in which all files related to the step will be stored (logs, artifacts, etc...). Can be overridden by individual items in Outputs. If omitted, will use the default artifact repository location configured in the controller, appended with the <workflowname>/<nodename> in the key.  # noqa: E501

        :param archive_location: The archive_location of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ArtifactLocation
        """

        self._archive_location = archive_location

    @property
    def container(self):
        """Gets the container of this V1alpha1Template.  # noqa: E501

        Container is the main container image to run in the pod  # noqa: E501

        :return: The container of this V1alpha1Template.  # noqa: E501
        :rtype: V1Container
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this V1alpha1Template.

        Container is the main container image to run in the pod  # noqa: E501

        :param container: The container of this V1alpha1Template.  # noqa: E501
        :type: V1Container
        """

        self._container = container

    @property
    def daemon(self):
        """Gets the daemon of this V1alpha1Template.  # noqa: E501

        Deamon will allow a workflow to proceed to the next step so long as the container reaches readiness  # noqa: E501

        :return: The daemon of this V1alpha1Template.  # noqa: E501
        :rtype: bool
        """
        return self._daemon

    @daemon.setter
    def daemon(self, daemon):
        """Sets the daemon of this V1alpha1Template.

        Deamon will allow a workflow to proceed to the next step so long as the container reaches readiness  # noqa: E501

        :param daemon: The daemon of this V1alpha1Template.  # noqa: E501
        :type: bool
        """

        self._daemon = daemon

    @property
    def dag(self):
        """Gets the dag of this V1alpha1Template.  # noqa: E501

        DAG template subtype which runs a DAG  # noqa: E501

        :return: The dag of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1DAGTemplate
        """
        return self._dag

    @dag.setter
    def dag(self, dag):
        """Sets the dag of this V1alpha1Template.

        DAG template subtype which runs a DAG  # noqa: E501

        :param dag: The dag of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1DAGTemplate
        """

        self._dag = dag

    @property
    def init_containers(self):
        """Gets the init_containers of this V1alpha1Template.  # noqa: E501

        InitContainers is a list of containers which run before the main container.  # noqa: E501

        :return: The init_containers of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1alpha1UserContainer]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """Sets the init_containers of this V1alpha1Template.

        InitContainers is a list of containers which run before the main container.  # noqa: E501

        :param init_containers: The init_containers of this V1alpha1Template.  # noqa: E501
        :type: list[V1alpha1UserContainer]
        """

        self._init_containers = init_containers

    @property
    def inputs(self):
        """Gets the inputs of this V1alpha1Template.  # noqa: E501

        Inputs describe what inputs parameters and artifacts are supplied to this template  # noqa: E501

        :return: The inputs of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Inputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this V1alpha1Template.

        Inputs describe what inputs parameters and artifacts are supplied to this template  # noqa: E501

        :param inputs: The inputs of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Inputs
        """

        self._inputs = inputs

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1Template.  # noqa: E501

        Metdata sets the pods's metadata, i.e. annotations and labels  # noqa: E501

        :return: The metadata of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1Template.

        Metdata sets the pods's metadata, i.e. annotations and labels  # noqa: E501

        :param metadata: The metadata of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Metadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this V1alpha1Template.  # noqa: E501

        Name is the name of the template  # noqa: E501

        :return: The name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Template.

        Name is the name of the template  # noqa: E501

        :param name: The name of this V1alpha1Template.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_selector(self):
        """Gets the node_selector of this V1alpha1Template.  # noqa: E501

        NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level.  # noqa: E501

        :return: The node_selector of this V1alpha1Template.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this V1alpha1Template.

        NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level.  # noqa: E501

        :param node_selector: The node_selector of this V1alpha1Template.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def outputs(self):
        """Gets the outputs of this V1alpha1Template.  # noqa: E501

        Outputs describe the parameters and artifacts that this template produces  # noqa: E501

        :return: The outputs of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Outputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this V1alpha1Template.

        Outputs describe the parameters and artifacts that this template produces  # noqa: E501

        :param outputs: The outputs of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Outputs
        """

        self._outputs = outputs

    @property
    def parallelism(self):
        """Gets the parallelism of this V1alpha1Template.  # noqa: E501

        Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total.  # noqa: E501

        :return: The parallelism of this V1alpha1Template.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this V1alpha1Template.

        Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total.  # noqa: E501

        :param parallelism: The parallelism of this V1alpha1Template.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def priority(self):
        """Gets the priority of this V1alpha1Template.  # noqa: E501

        Priority to apply to workflow pods.  # noqa: E501

        :return: The priority of this V1alpha1Template.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this V1alpha1Template.

        Priority to apply to workflow pods.  # noqa: E501

        :param priority: The priority of this V1alpha1Template.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def priority_class_name(self):
        """Gets the priority_class_name of this V1alpha1Template.  # noqa: E501

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :return: The priority_class_name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._priority_class_name

    @priority_class_name.setter
    def priority_class_name(self, priority_class_name):
        """Sets the priority_class_name of this V1alpha1Template.

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :param priority_class_name: The priority_class_name of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._priority_class_name = priority_class_name

    @property
    def resource(self):
        """Gets the resource of this V1alpha1Template.  # noqa: E501

        Resource template subtype which can run k8s resources  # noqa: E501

        :return: The resource of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ResourceTemplate
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1alpha1Template.

        Resource template subtype which can run k8s resources  # noqa: E501

        :param resource: The resource of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ResourceTemplate
        """

        self._resource = resource

    @property
    def retry_strategy(self):
        """Gets the retry_strategy of this V1alpha1Template.  # noqa: E501

        RetryStrategy describes how to retry a template when it fails  # noqa: E501

        :return: The retry_strategy of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1RetryStrategy
        """
        return self._retry_strategy

    @retry_strategy.setter
    def retry_strategy(self, retry_strategy):
        """Sets the retry_strategy of this V1alpha1Template.

        RetryStrategy describes how to retry a template when it fails  # noqa: E501

        :param retry_strategy: The retry_strategy of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1RetryStrategy
        """

        self._retry_strategy = retry_strategy

    @property
    def scheduler_name(self):
        """Gets the scheduler_name of this V1alpha1Template.  # noqa: E501

        If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler.  # noqa: E501

        :return: The scheduler_name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        """Sets the scheduler_name of this V1alpha1Template.

        If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler.  # noqa: E501

        :param scheduler_name: The scheduler_name of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._scheduler_name = scheduler_name

    @property
    def script(self):
        """Gets the script of this V1alpha1Template.  # noqa: E501

        Script runs a portion of code against an interpreter  # noqa: E501

        :return: The script of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ScriptTemplate
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this V1alpha1Template.

        Script runs a portion of code against an interpreter  # noqa: E501

        :param script: The script of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ScriptTemplate
        """

        self._script = script

    @property
    def sidecars(self):
        """Gets the sidecars of this V1alpha1Template.  # noqa: E501

        Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes  # noqa: E501

        :return: The sidecars of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1alpha1UserContainer]
        """
        return self._sidecars

    @sidecars.setter
    def sidecars(self, sidecars):
        """Sets the sidecars of this V1alpha1Template.

        Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes  # noqa: E501

        :param sidecars: The sidecars of this V1alpha1Template.  # noqa: E501
        :type: list[V1alpha1UserContainer]
        """

        self._sidecars = sidecars

    @property
    def steps(self):
        """Gets the steps of this V1alpha1Template.  # noqa: E501

        Steps define a series of sequential/parallel workflow steps  # noqa: E501

        :return: The steps of this V1alpha1Template.  # noqa: E501
        :rtype: list[list[V1alpha1WorkflowStep]]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1alpha1Template.

        Steps define a series of sequential/parallel workflow steps  # noqa: E501

        :param steps: The steps of this V1alpha1Template.  # noqa: E501
        :type: list[list[V1alpha1WorkflowStep]]
        """

        self._steps = steps

    @property
    def suspend(self):
        """Gets the suspend of this V1alpha1Template.  # noqa: E501

        Suspend template subtype which can suspend a workflow when reaching the step  # noqa: E501

        :return: The suspend of this V1alpha1Template.  # noqa: E501
        :rtype: object
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1alpha1Template.

        Suspend template subtype which can suspend a workflow when reaching the step  # noqa: E501

        :param suspend: The suspend of this V1alpha1Template.  # noqa: E501
        :type: object
        """

        self._suspend = suspend

    @property
    def tolerations(self):
        """Gets the tolerations of this V1alpha1Template.  # noqa: E501

        Tolerations to apply to workflow pods.  # noqa: E501

        :return: The tolerations of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this V1alpha1Template.

        Tolerations to apply to workflow pods.  # noqa: E501

        :param tolerations: The tolerations of this V1alpha1Template.  # noqa: E501
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def volumes(self):
        """Gets the volumes of this V1alpha1Template.  # noqa: E501

        Volumes is a list of volumes that can be mounted by containers in a template.  # noqa: E501

        :return: The volumes of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this V1alpha1Template.

        Volumes is a list of volumes that can be mounted by containers in a template.  # noqa: E501

        :param volumes: The volumes of this V1alpha1Template.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
