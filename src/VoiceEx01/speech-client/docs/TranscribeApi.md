# swagger_client.TranscribeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcriptions_transcribe**](TranscribeApi.md#transcriptions_transcribe) | **POST** /transcriptions:transcribe | Synchronous transcription of an audio file.


# **transcriptions_transcribe**
> TranscribeResult transcriptions_transcribe(api_version, audio, definition=definition)

Synchronous transcription of an audio file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TranscribeApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
audio = '/path/to/file.txt' # file | The content of the audio file to be transcribed. The audio file must be shorter than 2 hours in audio duration and smaller than 250 MB in size.
definition = 'definition_example' # str | Metadata for a transcription request. This field contains a JSON-serialized object of type `TranscribeDefinition`. (optional)

try:
    # Synchronous transcription of an audio file.
    api_response = api_instance.transcriptions_transcribe(api_version, audio, definition=definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranscribeApi->transcriptions_transcribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **audio** | **file**| The content of the audio file to be transcribed. The audio file must be shorter than 2 hours in audio duration and smaller than 250 MB in size. | 
 **definition** | **str**| Metadata for a transcription request. This field contains a JSON-serialized object of type &#x60;TranscribeDefinition&#x60;. | [optional] 

### Return type

[**TranscribeResult**](TranscribeResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

