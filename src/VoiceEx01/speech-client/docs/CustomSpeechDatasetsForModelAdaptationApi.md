# swagger_client.CustomSpeechDatasetsForModelAdaptationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasets_commit_blocks**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_commit_blocks) | **POST** /datasets/{id}/blocks:commit | Commit block list to complete the upload of the dataset.
[**datasets_create**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_create) | **POST** /datasets | Uploads and creates a new dataset by getting the data from a specified URL or starts waiting for data blocks to be uploaded.
[**datasets_delete**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_delete) | **DELETE** /datasets/{id} | Deletes the specified dataset.
[**datasets_get**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_get) | **GET** /datasets/{id} | Gets the dataset identified by the given ID.
[**datasets_get_blocks**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_get_blocks) | **GET** /datasets/{id}/blocks | Gets the list of uploaded blocks for this dataset.
[**datasets_get_file**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_get_file) | **GET** /datasets/{id}/files/{fileId} | Gets one specific file (identified with fileId) from a dataset (identified with id).
[**datasets_list**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_list) | **GET** /datasets | Gets a list of datasets for the authenticated subscription.
[**datasets_list_files**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_list_files) | **GET** /datasets/{id}/files | Gets the files of the dataset identified by the given ID.
[**datasets_list_supported_locales**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_list_supported_locales) | **GET** /datasets/locales | Gets a list of supported locales for datasets.
[**datasets_update**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_update) | **PATCH** /datasets/{id} | Updates the mutable details of the dataset identified by its ID.
[**datasets_upload_block**](CustomSpeechDatasetsForModelAdaptationApi.md#datasets_upload_block) | **PUT** /datasets/{id}/blocks | Upload a block of data for the dataset. The maximum size of the block is 8MiB.


# **datasets_commit_blocks**
> datasets_commit_blocks(id, api_version, block_list)

Commit block list to complete the upload of the dataset.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
api_version = 'api_version_example' # str | The requested api version.
block_list = [swagger_client.CommitBlocksEntry()] # list[CommitBlocksEntry] | The list of blocks that compile the dataset.

try:
    # Commit block list to complete the upload of the dataset.
    api_instance.datasets_commit_blocks(id, api_version, block_list)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_commit_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **api_version** | **str**| The requested api version. | 
 **block_list** | [**list[CommitBlocksEntry]**](CommitBlocksEntry.md)| The list of blocks that compile the dataset. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_create**
> Dataset datasets_create(api_version, dataset)

Uploads and creates a new dataset by getting the data from a specified URL or starts waiting for data blocks to be uploaded.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
dataset = swagger_client.Dataset() # Dataset | Definition for the new dataset.

try:
    # Uploads and creates a new dataset by getting the data from a specified URL or starts waiting for data blocks to be uploaded.
    api_response = api_instance.datasets_create(api_version, dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **dataset** | [**Dataset**](Dataset.md)| Definition for the new dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_delete**
> datasets_delete(id, api_version)

Deletes the specified dataset.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Deletes the specified dataset.
    api_instance.datasets_delete(id, api_version)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **api_version** | **str**| The requested api version. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get**
> Dataset datasets_get(id, api_version)

Gets the dataset identified by the given ID.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the dataset identified by the given ID.
    api_response = api_instance.datasets_get(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get_blocks**
> UploadedBlocks datasets_get_blocks(id, api_version)

Gets the list of uploaded blocks for this dataset.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the list of uploaded blocks for this dataset.
    api_response = api_instance.datasets_get_blocks(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_get_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**UploadedBlocks**](UploadedBlocks.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get_file**
> File datasets_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)

Gets one specific file (identified with fileId) from a dataset (identified with id).

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
file_id = 'file_id_example' # str | The identifier of the file.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. (optional)

try:
    # Gets one specific file (identified with fileId) from a dataset (identified with id).
    api_response = api_instance.datasets_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
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

# **datasets_list**
> PaginatedDatasets datasets_list(api_version, skip=skip, top=top, filter=filter)

Gets a list of datasets for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available datasets.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              -Example:               filter=createdDateTime gt 2022-02-01T11:00:00Z and displayName eq 'My dataset' (optional)

try:
    # Gets a list of datasets for the authenticated subscription.
    api_response = api_instance.datasets_list(api_version, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available datasets.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              -Example:               filter&#x3D;createdDateTime gt 2022-02-01T11:00:00Z and displayName eq &#39;My dataset&#39; | [optional] 

### Return type

[**PaginatedDatasets**](PaginatedDatasets.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_list_files**
> PaginatedFiles datasets_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)

Gets the files of the dataset identified by the given ID.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. (optional)
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter=name eq 'myaudio.wav' and kind eq 'Audio' (optional)

try:
    # Gets the files of the dataset identified by the given ID.
    api_response = api_instance.datasets_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
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

# **datasets_list_supported_locales**
> DatasetLocales datasets_list_supported_locales(api_version)

Gets a list of supported locales for datasets.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets a list of supported locales for datasets.
    api_response = api_instance.datasets_list_supported_locales(api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_list_supported_locales: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 

### Return type

[**DatasetLocales**](DatasetLocales.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_update**
> Dataset datasets_update(id, api_version, dataset_update)

Updates the mutable details of the dataset identified by its ID.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
api_version = 'api_version_example' # str | The requested api version.
dataset_update = swagger_client.DatasetUpdate() # DatasetUpdate | The updated values for the dataset.

try:
    # Updates the mutable details of the dataset identified by its ID.
    api_response = api_instance.datasets_update(id, api_version, dataset_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **api_version** | **str**| The requested api version. | 
 **dataset_update** | [**DatasetUpdate**](DatasetUpdate.md)| The updated values for the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_upload_block**
> datasets_upload_block(id, blockid, api_version, body)

Upload a block of data for the dataset. The maximum size of the block is 8MiB.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
blockid = 'blockid_example' # str | A valid Base64 string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size. For a given blob, the length of the value specified for the blockid parameter must be the same size for each block. Note that the Base64 string must be URL-encoded.
api_version = 'api_version_example' # str | The requested api version.
body = 'B' # str | 

try:
    # Upload a block of data for the dataset. The maximum size of the block is 8MiB.
    api_instance.datasets_upload_block(id, blockid, api_version, body)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->datasets_upload_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **blockid** | **str**| A valid Base64 string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size. For a given blob, the length of the value specified for the blockid parameter must be the same size for each block. Note that the Base64 string must be URL-encoded. | 
 **api_version** | **str**| The requested api version. | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

