# swagger_client.CustomSpeechTranscriptionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcriptions_delete**](CustomSpeechTranscriptionsApi.md#transcriptions_delete) | **DELETE** /transcriptions/{id} | Deletes the specified transcription task.
[**transcriptions_get**](CustomSpeechTranscriptionsApi.md#transcriptions_get) | **GET** /transcriptions/{id} | Gets the transcription identified by the given ID.
[**transcriptions_get_file**](CustomSpeechTranscriptionsApi.md#transcriptions_get_file) | **GET** /transcriptions/{id}/files/{fileId} | Gets one specific file (identified with fileId) from a transcription (identified with id).
[**transcriptions_list**](CustomSpeechTranscriptionsApi.md#transcriptions_list) | **GET** /transcriptions | Gets a list of transcriptions for the authenticated subscription.
[**transcriptions_list_files**](CustomSpeechTranscriptionsApi.md#transcriptions_list_files) | **GET** /transcriptions/{id}/files | Gets the files of the transcription identified by the given ID.
[**transcriptions_list_supported_locales**](CustomSpeechTranscriptionsApi.md#transcriptions_list_supported_locales) | **GET** /transcriptions/locales | Gets a list of supported locales for offline transcriptions.
[**transcriptions_submit**](CustomSpeechTranscriptionsApi.md#transcriptions_submit) | **POST** /transcriptions:submit | Submits a new transcription job.
[**transcriptions_update**](CustomSpeechTranscriptionsApi.md#transcriptions_update) | **PATCH** /transcriptions/{id} | Updates the mutable details of the transcription identified by its ID.


# **transcriptions_delete**
> transcriptions_delete(id, api_version)

Deletes the specified transcription task.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Deletes the specified transcription task.
    api_instance.transcriptions_delete(id, api_version)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 
 **api_version** | **str**| The requested api version. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_get**
> Transcription transcriptions_get(id, api_version)

Gets the transcription identified by the given ID.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the transcription identified by the given ID.
    api_response = api_instance.transcriptions_get(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_get_file**
> File transcriptions_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)

Gets one specific file (identified with fileId) from a transcription (identified with id).

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.
file_id = 'file_id_example' # str | The identifier of the file.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled and transcriptions without a destinationContainerUrl. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS and transcriptions with a destinationContainerUrl, returned urls do not contain an SAS token. (optional)

try:
    # Gets one specific file (identified with fileId) from a transcription (identified with id).
    api_response = api_instance.transcriptions_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 
 **file_id** | [**str**](.md)| The identifier of the file. | 
 **api_version** | **str**| The requested api version. | 
 **sas_lifetime_minutes** | **int**| This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don&#39;t have BYOS enabled and transcriptions without a destinationContainerUrl. For speech resources              that don&#39;t have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS and transcriptions with a destinationContainerUrl, returned urls do not contain an SAS token. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_list**
> PaginatedTranscriptions transcriptions_list(api_version, skip=skip, top=top, filter=filter)

Gets a list of transcriptions for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available transcriptions.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=createdDateTime gt 2022-02-01T11:00:00Z (optional)

try:
    # Gets a list of transcriptions for the authenticated subscription.
    api_response = api_instance.transcriptions_list(api_version, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available transcriptions.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;createdDateTime gt 2022-02-01T11:00:00Z | [optional] 

### Return type

[**PaginatedTranscriptions**](PaginatedTranscriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_list_files**
> PaginatedFiles transcriptions_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)

Gets the files of the transcription identified by the given ID.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled and transcriptions without a destinationContainerUrl. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS and transcriptions with a destinationContainerUrl, returned urls do not contain an SAS token. (optional)
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter=name eq 'myaudio.wav.json' and kind eq 'Transcription' (optional)

try:
    # Gets the files of the transcription identified by the given ID.
    api_response = api_instance.transcriptions_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 
 **api_version** | **str**| The requested api version. | 
 **sas_lifetime_minutes** | **int**| This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don&#39;t have BYOS enabled and transcriptions without a destinationContainerUrl. For speech resources              that don&#39;t have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS and transcriptions with a destinationContainerUrl, returned urls do not contain an SAS token. | [optional] 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;name eq &#39;myaudio.wav.json&#39; and kind eq &#39;Transcription&#39; | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_list_supported_locales**
> TranscriptionLocales transcriptions_list_supported_locales(api_version)

Gets a list of supported locales for offline transcriptions.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets a list of supported locales for offline transcriptions.
    api_response = api_instance.transcriptions_list_supported_locales(api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_list_supported_locales: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 

### Return type

[**TranscriptionLocales**](TranscriptionLocales.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_submit**
> Transcription transcriptions_submit(api_version, transcription)

Submits a new transcription job.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
transcription = swagger_client.Transcription() # Transcription | The details of the new transcription.

try:
    # Submits a new transcription job.
    api_response = api_instance.transcriptions_submit(api_version, transcription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **transcription** | [**Transcription**](Transcription.md)| The details of the new transcription. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcriptions_update**
> Transcription transcriptions_update(id, api_version, transcription_update)

Updates the mutable details of the transcription identified by its ID.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.
api_version = 'api_version_example' # str | The requested api version.
transcription_update = swagger_client.TranscriptionUpdate() # TranscriptionUpdate | The updated values for the transcription.

try:
    # Updates the mutable details of the transcription identified by its ID.
    api_response = api_instance.transcriptions_update(id, api_version, transcription_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->transcriptions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 
 **api_version** | **str**| The requested api version. | 
 **transcription_update** | [**TranscriptionUpdate**](TranscriptionUpdate.md)| The updated values for the transcription. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

