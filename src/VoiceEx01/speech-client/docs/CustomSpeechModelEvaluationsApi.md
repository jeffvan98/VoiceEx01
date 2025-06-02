# swagger_client.CustomSpeechModelEvaluationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluations_create**](CustomSpeechModelEvaluationsApi.md#evaluations_create) | **POST** /evaluations | Creates a new evaluation.
[**evaluations_delete**](CustomSpeechModelEvaluationsApi.md#evaluations_delete) | **DELETE** /evaluations/{id} | Deletes the evaluation identified by the given ID.
[**evaluations_get**](CustomSpeechModelEvaluationsApi.md#evaluations_get) | **GET** /evaluations/{id} | Gets the evaluation identified by the given ID.
[**evaluations_get_file**](CustomSpeechModelEvaluationsApi.md#evaluations_get_file) | **GET** /evaluations/{id}/files/{fileId} | Gets one specific file (identified with fileId) from an evaluation (identified with id).
[**evaluations_list**](CustomSpeechModelEvaluationsApi.md#evaluations_list) | **GET** /evaluations | Gets the list of evaluations for the authenticated subscription.
[**evaluations_list_files**](CustomSpeechModelEvaluationsApi.md#evaluations_list_files) | **GET** /evaluations/{id}/files | Gets the files of the evaluation identified by the given ID.
[**evaluations_list_supported_locales**](CustomSpeechModelEvaluationsApi.md#evaluations_list_supported_locales) | **GET** /evaluations/locales | Gets a list of supported locales for evaluations.
[**evaluations_update**](CustomSpeechModelEvaluationsApi.md#evaluations_update) | **PATCH** /evaluations/{id} | Updates the mutable details of the evaluation identified by its id.


# **evaluations_create**
> Evaluation evaluations_create(api_version, evaluation)

Creates a new evaluation.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
evaluation = swagger_client.Evaluation() # Evaluation | The details of the new evaluation.

try:
    # Creates a new evaluation.
    api_response = api_instance.evaluations_create(api_version, evaluation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **evaluation** | [**Evaluation**](Evaluation.md)| The details of the new evaluation. | 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_delete**
> evaluations_delete(id, api_version)

Deletes the evaluation identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the evaluation.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Deletes the evaluation identified by the given ID.
    api_instance.evaluations_delete(id, api_version)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the evaluation. | 
 **api_version** | **str**| The requested api version. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_get**
> Evaluation evaluations_get(id, api_version)

Gets the evaluation identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the evaluation.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the evaluation identified by the given ID.
    api_response = api_instance.evaluations_get(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the evaluation. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_get_file**
> File evaluations_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)

Gets one specific file (identified with fileId) from an evaluation (identified with id).

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the evaluation.
file_id = 'file_id_example' # str | The identifier of the file.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. (optional)

try:
    # Gets one specific file (identified with fileId) from an evaluation (identified with id).
    api_response = api_instance.evaluations_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the evaluation. | 
 **file_id** | [**str**](.md)| The identifier of the file. | 
 **api_version** | **str**| The requested api version. | 
 **sas_lifetime_minutes** | **int**| This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don&#39;t have BYOS enabled. For speech resources              that don&#39;t have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list**
> PaginatedEvaluations evaluations_list(api_version, skip=skip, top=top, filter=filter)

Gets the list of evaluations for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available evaluations.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status and locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=displayName eq 'My evaluation' (optional)

try:
    # Gets the list of evaluations for the authenticated subscription.
    api_response = api_instance.evaluations_list(api_version, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available evaluations.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status and locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;displayName eq &#39;My evaluation&#39; | [optional] 

### Return type

[**PaginatedEvaluations**](PaginatedEvaluations.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list_files**
> PaginatedFiles evaluations_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)

Gets the files of the evaluation identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the evaluation.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. (optional)
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter=name eq 'myaudio.wav' and kind eq 'Audio' (optional)

try:
    # Gets the files of the evaluation identified by the given ID.
    api_response = api_instance.evaluations_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the evaluation. | 
 **api_version** | **str**| The requested api version. | 
 **sas_lifetime_minutes** | **int**| This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don&#39;t have BYOS enabled. For speech resources              that don&#39;t have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. | [optional] 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;name eq &#39;myaudio.wav&#39; and kind eq &#39;Audio&#39; | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list_supported_locales**
> list[str] evaluations_list_supported_locales(api_version)

Gets a list of supported locales for evaluations.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets a list of supported locales for evaluations.
    api_response = api_instance.evaluations_list_supported_locales(api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_list_supported_locales: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_update**
> Evaluation evaluations_update(id, api_version, evaluation_update)

Updates the mutable details of the evaluation identified by its id.

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
api_instance = swagger_client.CustomSpeechModelEvaluationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the evaluation.
api_version = 'api_version_example' # str | The requested api version.
evaluation_update = swagger_client.EvaluationUpdate() # EvaluationUpdate | The object containing the updated fields of the evaluation.

try:
    # Updates the mutable details of the evaluation identified by its id.
    api_response = api_instance.evaluations_update(id, api_version, evaluation_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelEvaluationsApi->evaluations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the evaluation. | 
 **api_version** | **str**| The requested api version. | 
 **evaluation_update** | [**EvaluationUpdate**](EvaluationUpdate.md)| The object containing the updated fields of the evaluation. | 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

