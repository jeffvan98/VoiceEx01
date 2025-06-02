# Phrase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | The 0-based channel index. Only present if channel separation is enabled. | [optional] 
**speaker** | **int** | A unique integer number that is assigned to each speaker detected in the audio without particular order. Only present if speaker diarization is enabled. | [optional] 
**offset_milliseconds** | **int** | The start offset of the phrase in milliseconds. | 
**duration_milliseconds** | **int** | The duration of the phrase in milliseconds. | 
**text** | **str** | The transcribed text of the phrase. | 
**words** | [**list[Word]**](Word.md) | The words that make up the phrase. Only present if word-level timestamps are enabled. | [optional] 
**locale** | **str** | The locale of the phrase. | [optional] 
**confidence** | **float** | The confidence value for the phrase. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


