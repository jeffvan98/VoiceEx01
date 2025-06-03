# DatasetProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_line_count** | **int** | The number of lines accepted for this data set. | [optional] 
**rejected_line_count** | **int** | The number of lines rejected for this data set. | [optional] 
**duration_milliseconds** | **int** | The total duration in milliseconds of the datasets if it contains audio files. Durations larger than 2^53-1 are not supported to ensure compatibility with JavaScript integers. | [optional] [default to 0]
**text_normalization_kind** | [**TextNormalizationKind**](TextNormalizationKind.md) |  | [optional] 
**error** | [**EntityError**](EntityError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


