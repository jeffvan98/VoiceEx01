# TranscribeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locales** | **list[str]** | A list of possible locales for the transcription. If not specified, the locale of the speech in the audio is detected automatically from all supported locales. | [optional] 
**models** | **dict(str, str)** | Maps some or all candidate locales to a model URI to be used for transcription. If no mapping is given, the default model for the locale is used. | [optional] 
**profanity_filter_mode** | [**ProfanityFilterMode**](ProfanityFilterMode.md) |  | [optional] 
**diarization** | [**TranscribeDiarizationProperties**](TranscribeDiarizationProperties.md) |  | [optional] 
**channels** | **list[int]** | The 0-based indices of the channels to be transcribed separately. If not specified, multiple channels are merged and transcribed jointly. Only up to two channels are supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


