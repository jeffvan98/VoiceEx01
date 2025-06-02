# SharedModelFeatures

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_transcriptions_submit** | **bool** | A value indicating whether submission of transcription jobs is supported (POST /transcriptions:submit). | [optional] 
**supports_transcriptions_transcribe** | **bool** | A value indicating whether the transcribe action is supported (POST /transcriptions:transcribe). | [optional] 
**supports_endpoints** | **bool** | A value indicating whether creation of endpoints for live transcription is supported. | [optional] 
**supports_transcriptions_on_speech_containers** | **bool** | A value indicating whether this model can be used for transcription on speech container. This feature can be added on existing models when it becomes usable on speech container. | [optional] 
**supported_output_formats** | [**list[OutputFormatType]**](OutputFormatType.md) | Supported output formats. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


