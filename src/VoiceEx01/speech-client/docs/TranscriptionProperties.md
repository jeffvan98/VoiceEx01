# TranscriptionProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word_level_timestamps_enabled** | **bool** | A value indicating whether word level timestamps are requested. The default value is &#x60;false&#x60;. | [optional] 
**display_form_word_level_timestamps_enabled** | **bool** | A value indicating whether word level timestamps for the display form are requested. The default value is &#x60;false&#x60;. | [optional] 
**channels** | **list[int]** | A collection of the requested channel numbers. In the default case, the channels 0 and 1 are considered. | [optional] 
**punctuation_mode** | [**PunctuationMode**](PunctuationMode.md) |  | [optional] 
**profanity_filter_mode** | [**ProfanityFilterMode**](ProfanityFilterMode.md) |  | [optional] 
**destination_container_url** | **str** | The requested destination container. ### Remarks ### When a destination container is used in combination with a &#x60;timeToLive&#x60;, the metadata of a transcription will be deleted normally, but the data stored in the destination container, including transcription results, will remain untouched, because no delete permissions are required for this container.  To support automatic cleanup, either configure blob lifetimes on the container, or use \&quot;Bring your own Storage (BYOS)\&quot; instead of &#x60;destinationContainerUrl&#x60;, where blobs can be cleaned up. | [optional] 
**time_to_live_hours** | **int** | How long the transcription will be kept in the system after it has completed. Once the transcription reaches the time to live after completion(successful or failed) it will be automatically deleted.  Note: When using BYOS (bring your own storage), the result files on the customer owned storage account will also be deleted.Use either destinationContainerUrl to specify a separate container for result files which will not be deleted when the timeToLive expires, or retrieve the result files through the API and store them as needed.  The shortest supported duration is 6 hours, the longest supported duration is 31 days. 2 days (48 hours) is the recommended default value when data is consumed directly. | 
**language_identification** | [**LanguageIdentificationProperties**](LanguageIdentificationProperties.md) |  | [optional] 
**diarization** | [**DiarizationProperties**](DiarizationProperties.md) |  | [optional] 
**error** | [**EntityError**](EntityError.md) |  | [optional] 
**duration_milliseconds** | **int** | The duration in milliseconds of the transcription. Durations larger than 2^53-1 are not supported to ensure compatibility with JavaScript integers. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


