# V1alpha1SubmitOpts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | DryRun validates the workflow on the client-side without creating it. This option is not supported in API | [optional] 
**entry_point** | **str** | Entrypoint overrides spec.entrypoint | [optional] 
**generate_name** | **str** | GenerateName overrides metadata.generateName | [optional] 
**instance_id** | **str** | InstanceID binds the Resource to the specified instance ID | [optional] 
**labels** | **str** | Labels adds to metadata.labels | [optional] 
**name** | **str** | Name overrides metadata.name | [optional] 
**owner_reference** | [**V1OwnerReference**](V1OwnerReference.md) | OwnerReference creates a metadata.ownerReference | [optional] 
**parameter_file** | **str** | ParameterFile holds a reference to a parameter file. This option is not supported in API | [optional] 
**parameters** | **list[str]** | Parameters passes input parameters to workflow | [optional] 
**server_dry_run** | **bool** | ServerDryRun validates the workflow on the server-side without creating it | [optional] 
**service_account** | **str** | ServiceAccount runs all pods in the workflow using specified ServiceAccount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


