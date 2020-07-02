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


class V1alpha1NodeStatus(object):
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
        'boundary_id': 'str',
        'children': 'list[str]',
        'daemoned': 'bool',
        'display_name': 'str',
        'finished_at': 'datetime',
        'host_node_name': 'str',
        'id': 'str',
        'inputs': 'V1alpha1Inputs',
        'message': 'str',
        'name': 'str',
        'outbound_nodes': 'list[str]',
        'outputs': 'V1alpha1Outputs',
        'phase': 'str',
        'pod_ip': 'str',
        'resources_duration': 'dict(str, int)',
        'started_at': 'datetime',
        'stored_template_id': 'str',
        'template_name': 'str',
        'template_ref': 'V1alpha1TemplateRef',
        'template_scope': 'str',
        'type': 'str',
        'workflow_template_name': 'str'
    }

    attribute_map = {
        'boundary_id': 'boundaryID',
        'children': 'children',
        'daemoned': 'daemoned',
        'display_name': 'displayName',
        'finished_at': 'finishedAt',
        'host_node_name': 'hostNodeName',
        'id': 'id',
        'inputs': 'inputs',
        'message': 'message',
        'name': 'name',
        'outbound_nodes': 'outboundNodes',
        'outputs': 'outputs',
        'phase': 'phase',
        'pod_ip': 'podIP',
        'resources_duration': 'resourcesDuration',
        'started_at': 'startedAt',
        'stored_template_id': 'storedTemplateID',
        'template_name': 'templateName',
        'template_ref': 'templateRef',
        'template_scope': 'templateScope',
        'type': 'type',
        'workflow_template_name': 'workflowTemplateName'
    }

    def __init__(self, boundary_id=None, children=None, daemoned=None, display_name=None, finished_at=None, host_node_name=None, id=None, inputs=None, message=None, name=None, outbound_nodes=None, outputs=None, phase=None, pod_ip=None, resources_duration=None, started_at=None, stored_template_id=None, template_name=None, template_ref=None, template_scope=None, type=None, workflow_template_name=None):  # noqa: E501
        """V1alpha1NodeStatus - a model defined in Swagger"""  # noqa: E501

        self._boundary_id = None
        self._children = None
        self._daemoned = None
        self._display_name = None
        self._finished_at = None
        self._host_node_name = None
        self._id = None
        self._inputs = None
        self._message = None
        self._name = None
        self._outbound_nodes = None
        self._outputs = None
        self._phase = None
        self._pod_ip = None
        self._resources_duration = None
        self._started_at = None
        self._stored_template_id = None
        self._template_name = None
        self._template_ref = None
        self._template_scope = None
        self._type = None
        self._workflow_template_name = None
        self.discriminator = None

        if boundary_id is not None:
            self.boundary_id = boundary_id
        if children is not None:
            self.children = children
        if daemoned is not None:
            self.daemoned = daemoned
        self.display_name = display_name
        if finished_at is not None:
            self.finished_at = finished_at
        if host_node_name is not None:
            self.host_node_name = host_node_name
        self.id = id
        if inputs is not None:
            self.inputs = inputs
        if message is not None:
            self.message = message
        self.name = name
        if outbound_nodes is not None:
            self.outbound_nodes = outbound_nodes
        if outputs is not None:
            self.outputs = outputs
        if phase is not None:
            self.phase = phase
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if resources_duration is not None:
            self.resources_duration = resources_duration
        if started_at is not None:
            self.started_at = started_at
        if stored_template_id is not None:
            self.stored_template_id = stored_template_id
        if template_name is not None:
            self.template_name = template_name
        if template_ref is not None:
            self.template_ref = template_ref
        if template_scope is not None:
            self.template_scope = template_scope
        self.type = type
        if workflow_template_name is not None:
            self.workflow_template_name = workflow_template_name

    @property
    def boundary_id(self):
        """Gets the boundary_id of this V1alpha1NodeStatus.  # noqa: E501

        BoundaryID indicates the node ID of the associated template root node in which this node belongs to  # noqa: E501

        :return: The boundary_id of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._boundary_id

    @boundary_id.setter
    def boundary_id(self, boundary_id):
        """Sets the boundary_id of this V1alpha1NodeStatus.

        BoundaryID indicates the node ID of the associated template root node in which this node belongs to  # noqa: E501

        :param boundary_id: The boundary_id of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._boundary_id = boundary_id

    @property
    def children(self):
        """Gets the children of this V1alpha1NodeStatus.  # noqa: E501

        Children is a list of child node IDs  # noqa: E501

        :return: The children of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this V1alpha1NodeStatus.

        Children is a list of child node IDs  # noqa: E501

        :param children: The children of this V1alpha1NodeStatus.  # noqa: E501
        :type: list[str]
        """

        self._children = children

    @property
    def daemoned(self):
        """Gets the daemoned of this V1alpha1NodeStatus.  # noqa: E501

        Daemoned tracks whether or not this node was daemoned and need to be terminated  # noqa: E501

        :return: The daemoned of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: bool
        """
        return self._daemoned

    @daemoned.setter
    def daemoned(self, daemoned):
        """Sets the daemoned of this V1alpha1NodeStatus.

        Daemoned tracks whether or not this node was daemoned and need to be terminated  # noqa: E501

        :param daemoned: The daemoned of this V1alpha1NodeStatus.  # noqa: E501
        :type: bool
        """

        self._daemoned = daemoned

    @property
    def display_name(self):
        """Gets the display_name of this V1alpha1NodeStatus.  # noqa: E501

        DisplayName is a human readable representation of the node. Unique within a template boundary  # noqa: E501

        :return: The display_name of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this V1alpha1NodeStatus.

        DisplayName is a human readable representation of the node. Unique within a template boundary  # noqa: E501

        :param display_name: The display_name of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def finished_at(self):
        """Gets the finished_at of this V1alpha1NodeStatus.  # noqa: E501

        Time at which this node completed  # noqa: E501

        :return: The finished_at of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this V1alpha1NodeStatus.

        Time at which this node completed  # noqa: E501

        :param finished_at: The finished_at of this V1alpha1NodeStatus.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def host_node_name(self):
        """Gets the host_node_name of this V1alpha1NodeStatus.  # noqa: E501

        HostNodeName name of the Kubernetes node on which the Pod is running, if applicable  # noqa: E501

        :return: The host_node_name of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._host_node_name

    @host_node_name.setter
    def host_node_name(self, host_node_name):
        """Sets the host_node_name of this V1alpha1NodeStatus.

        HostNodeName name of the Kubernetes node on which the Pod is running, if applicable  # noqa: E501

        :param host_node_name: The host_node_name of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._host_node_name = host_node_name

    @property
    def id(self):
        """Gets the id of this V1alpha1NodeStatus.  # noqa: E501

        ID is a unique identifier of a node within the worklow It is implemented as a hash of the node name, which makes the ID deterministic  # noqa: E501

        :return: The id of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1alpha1NodeStatus.

        ID is a unique identifier of a node within the worklow It is implemented as a hash of the node name, which makes the ID deterministic  # noqa: E501

        :param id: The id of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inputs(self):
        """Gets the inputs of this V1alpha1NodeStatus.  # noqa: E501

        Inputs captures input parameter values and artifact locations supplied to this template invocation  # noqa: E501

        :return: The inputs of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: V1alpha1Inputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this V1alpha1NodeStatus.

        Inputs captures input parameter values and artifact locations supplied to this template invocation  # noqa: E501

        :param inputs: The inputs of this V1alpha1NodeStatus.  # noqa: E501
        :type: V1alpha1Inputs
        """

        self._inputs = inputs

    @property
    def message(self):
        """Gets the message of this V1alpha1NodeStatus.  # noqa: E501

        A human readable message indicating details about why the node is in this condition.  # noqa: E501

        :return: The message of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1alpha1NodeStatus.

        A human readable message indicating details about why the node is in this condition.  # noqa: E501

        :param message: The message of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this V1alpha1NodeStatus.  # noqa: E501

        Name is unique name in the node tree used to generate the node ID  # noqa: E501

        :return: The name of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1NodeStatus.

        Name is unique name in the node tree used to generate the node ID  # noqa: E501

        :param name: The name of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outbound_nodes(self):
        """Gets the outbound_nodes of this V1alpha1NodeStatus.  # noqa: E501

        OutboundNodes tracks the node IDs which are considered \"outbound\" nodes to a template invocation. For every invocation of a template, there are nodes which we considered as \"outbound\". Essentially, these are last nodes in the execution sequence to run, before the template is considered completed. These nodes are then connected as parents to a following step.  In the case of single pod steps (i.e. container, script, resource templates), this list will be nil since the pod itself is already considered the \"outbound\" node. In the case of DAGs, outbound nodes are the \"target\" tasks (tasks with no children). In the case of steps, outbound nodes are all the containers involved in the last step group. NOTE: since templates are composable, the list of outbound nodes are carried upwards when a DAG/steps template invokes another DAG/steps template. In other words, the outbound nodes of a template, will be a superset of the outbound nodes of its last children.  # noqa: E501

        :return: The outbound_nodes of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._outbound_nodes

    @outbound_nodes.setter
    def outbound_nodes(self, outbound_nodes):
        """Sets the outbound_nodes of this V1alpha1NodeStatus.

        OutboundNodes tracks the node IDs which are considered \"outbound\" nodes to a template invocation. For every invocation of a template, there are nodes which we considered as \"outbound\". Essentially, these are last nodes in the execution sequence to run, before the template is considered completed. These nodes are then connected as parents to a following step.  In the case of single pod steps (i.e. container, script, resource templates), this list will be nil since the pod itself is already considered the \"outbound\" node. In the case of DAGs, outbound nodes are the \"target\" tasks (tasks with no children). In the case of steps, outbound nodes are all the containers involved in the last step group. NOTE: since templates are composable, the list of outbound nodes are carried upwards when a DAG/steps template invokes another DAG/steps template. In other words, the outbound nodes of a template, will be a superset of the outbound nodes of its last children.  # noqa: E501

        :param outbound_nodes: The outbound_nodes of this V1alpha1NodeStatus.  # noqa: E501
        :type: list[str]
        """

        self._outbound_nodes = outbound_nodes

    @property
    def outputs(self):
        """Gets the outputs of this V1alpha1NodeStatus.  # noqa: E501

        Outputs captures output parameter values and artifact locations produced by this template invocation  # noqa: E501

        :return: The outputs of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: V1alpha1Outputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this V1alpha1NodeStatus.

        Outputs captures output parameter values and artifact locations produced by this template invocation  # noqa: E501

        :param outputs: The outputs of this V1alpha1NodeStatus.  # noqa: E501
        :type: V1alpha1Outputs
        """

        self._outputs = outputs

    @property
    def phase(self):
        """Gets the phase of this V1alpha1NodeStatus.  # noqa: E501

        Phase a simple, high-level summary of where the node is in its lifecycle. Can be used as a state machine.  # noqa: E501

        :return: The phase of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1alpha1NodeStatus.

        Phase a simple, high-level summary of where the node is in its lifecycle. Can be used as a state machine.  # noqa: E501

        :param phase: The phase of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def pod_ip(self):
        """Gets the pod_ip of this V1alpha1NodeStatus.  # noqa: E501

        PodIP captures the IP of the pod for daemoned steps  # noqa: E501

        :return: The pod_ip of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        """Sets the pod_ip of this V1alpha1NodeStatus.

        PodIP captures the IP of the pod for daemoned steps  # noqa: E501

        :param pod_ip: The pod_ip of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._pod_ip = pod_ip

    @property
    def resources_duration(self):
        """Gets the resources_duration of this V1alpha1NodeStatus.  # noqa: E501

        ResourcesDuration is indicative, but not accurate, resource duration. This is populated when the nodes completes.  # noqa: E501

        :return: The resources_duration of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._resources_duration

    @resources_duration.setter
    def resources_duration(self, resources_duration):
        """Sets the resources_duration of this V1alpha1NodeStatus.

        ResourcesDuration is indicative, but not accurate, resource duration. This is populated when the nodes completes.  # noqa: E501

        :param resources_duration: The resources_duration of this V1alpha1NodeStatus.  # noqa: E501
        :type: dict(str, int)
        """

        self._resources_duration = resources_duration

    @property
    def started_at(self):
        """Gets the started_at of this V1alpha1NodeStatus.  # noqa: E501

        Time at which this node started  # noqa: E501

        :return: The started_at of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this V1alpha1NodeStatus.

        Time at which this node started  # noqa: E501

        :param started_at: The started_at of this V1alpha1NodeStatus.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def stored_template_id(self):
        """Gets the stored_template_id of this V1alpha1NodeStatus.  # noqa: E501

        StoredTemplateID is the ID of stored template. DEPRECATED: This value is not used anymore.  # noqa: E501

        :return: The stored_template_id of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._stored_template_id

    @stored_template_id.setter
    def stored_template_id(self, stored_template_id):
        """Sets the stored_template_id of this V1alpha1NodeStatus.

        StoredTemplateID is the ID of stored template. DEPRECATED: This value is not used anymore.  # noqa: E501

        :param stored_template_id: The stored_template_id of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._stored_template_id = stored_template_id

    @property
    def template_name(self):
        """Gets the template_name of this V1alpha1NodeStatus.  # noqa: E501

        TemplateName is the template name which this node corresponds to. Not applicable to virtual nodes (e.g. Retry, StepGroup)  # noqa: E501

        :return: The template_name of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this V1alpha1NodeStatus.

        TemplateName is the template name which this node corresponds to. Not applicable to virtual nodes (e.g. Retry, StepGroup)  # noqa: E501

        :param template_name: The template_name of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def template_ref(self):
        """Gets the template_ref of this V1alpha1NodeStatus.  # noqa: E501

        TemplateRef is the reference to the template resource which this node corresponds to. Not applicable to virtual nodes (e.g. Retry, StepGroup)  # noqa: E501

        :return: The template_ref of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: V1alpha1TemplateRef
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this V1alpha1NodeStatus.

        TemplateRef is the reference to the template resource which this node corresponds to. Not applicable to virtual nodes (e.g. Retry, StepGroup)  # noqa: E501

        :param template_ref: The template_ref of this V1alpha1NodeStatus.  # noqa: E501
        :type: V1alpha1TemplateRef
        """

        self._template_ref = template_ref

    @property
    def template_scope(self):
        """Gets the template_scope of this V1alpha1NodeStatus.  # noqa: E501

        TemplateScope is the template scope in which the template of this node was retrieved.  # noqa: E501

        :return: The template_scope of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._template_scope

    @template_scope.setter
    def template_scope(self, template_scope):
        """Sets the template_scope of this V1alpha1NodeStatus.

        TemplateScope is the template scope in which the template of this node was retrieved.  # noqa: E501

        :param template_scope: The template_scope of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._template_scope = template_scope

    @property
    def type(self):
        """Gets the type of this V1alpha1NodeStatus.  # noqa: E501

        Type indicates type of node  # noqa: E501

        :return: The type of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1NodeStatus.

        Type indicates type of node  # noqa: E501

        :param type: The type of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def workflow_template_name(self):
        """Gets the workflow_template_name of this V1alpha1NodeStatus.  # noqa: E501

        WorkflowTemplateName is the WorkflowTemplate resource name on which the resolved template of this node is retrieved. DEPRECATED: This value is not used anymore.  # noqa: E501

        :return: The workflow_template_name of this V1alpha1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._workflow_template_name

    @workflow_template_name.setter
    def workflow_template_name(self, workflow_template_name):
        """Sets the workflow_template_name of this V1alpha1NodeStatus.

        WorkflowTemplateName is the WorkflowTemplate resource name on which the resolved template of this node is retrieved. DEPRECATED: This value is not used anymore.  # noqa: E501

        :param workflow_template_name: The workflow_template_name of this V1alpha1NodeStatus.  # noqa: E501
        :type: str
        """

        self._workflow_template_name = workflow_template_name

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
        if issubclass(V1alpha1NodeStatus, dict):
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
        if not isinstance(other, V1alpha1NodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
