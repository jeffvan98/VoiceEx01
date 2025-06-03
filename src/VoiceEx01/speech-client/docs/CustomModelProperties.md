# CustomModelProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecation_dates** | [**CustomModelDeprecationDates**](CustomModelDeprecationDates.md) |  | [optional] 
**custom_model_weight_percent** | **int** | The weight of custom model between 1 (1% custom model and 99% base model) and 100 (100% custom model and 0% base model). When this property is not set, the service chooses a suitable value (get the model to retrieve the selected weight). Start without using this property. If needed, choose a larger (or smaller) weight to increase (or decrease) the impact of the custom model. | [optional] 
**features** | [**CustomModelFeatures**](CustomModelFeatures.md) |  | [optional] 
**error** | [**EntityError**](EntityError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


