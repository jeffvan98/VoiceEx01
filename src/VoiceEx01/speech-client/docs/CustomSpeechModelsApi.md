# swagger_client.CustomSpeechModelsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**models_authorize_copy**](CustomSpeechModelsApi.md#models_authorize_copy) | **POST** /models:authorizecopy | Allows another speech resource (source) to copy a model to this speech resource (target).
[**models_copy**](CustomSpeechModelsApi.md#models_copy) | **POST** /models/{id}:copy | Copies a model from one subscription to another.
[**models_create**](CustomSpeechModelsApi.md#models_create) | **POST** /models | Creates a new model.
[**models_delete**](CustomSpeechModelsApi.md#models_delete) | **DELETE** /models/{id} | Deletes the model identified by the given ID.
[**models_get_base_model**](CustomSpeechModelsApi.md#models_get_base_model) | **GET** /models/base/{id} | Gets the base model identified by the given ID.
[**models_get_base_model_manifest**](CustomSpeechModelsApi.md#models_get_base_model_manifest) | **GET** /models/base/{id}/manifest | Returns an manifest for this base model which can be used in an on-premise container.
[**models_get_custom_model**](CustomSpeechModelsApi.md#models_get_custom_model) | **GET** /models/{id} | Gets the model identified by the given ID.
[**models_get_custom_model_manifest**](CustomSpeechModelsApi.md#models_get_custom_model_manifest) | **GET** /models/{id}/manifest | Returns an manifest for this model which can be used in an on-premise container.
[**models_get_file**](CustomSpeechModelsApi.md#models_get_file) | **GET** /models/{id}/files/{fileId} | Gets one specific file (identified with fileId) from a model (identified with id).
[**models_list_base_models**](CustomSpeechModelsApi.md#models_list_base_models) | **GET** /models/base | Gets the list of base models for the authenticated subscription.
[**models_list_custom_models**](CustomSpeechModelsApi.md#models_list_custom_models) | **GET** /models | Gets the list of custom models for the authenticated subscription.
[**models_list_files**](CustomSpeechModelsApi.md#models_list_files) | **GET** /models/{id}/files | Gets the files of the model identified by the given ID.
[**models_list_supported_locales**](CustomSpeechModelsApi.md#models_list_supported_locales) | **GET** /models/locales | Gets a list of supported locales for model adaptation.
[**models_update**](CustomSpeechModelsApi.md#models_update) | **PATCH** /models/{id} | Updates the metadata of the model identified by the given ID.


# **models_authorize_copy**
> ModelCopyAuthorization models_authorize_copy(api_version, model_copy_authorization_definition)

Allows another speech resource (source) to copy a model to this speech resource (target).

This method can be used to allow copying a model from another speech resource.  Only custom models can be copied from another speech resource.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
model_copy_authorization_definition = swagger_client.ModelCopyAuthorizationDefinition() # ModelCopyAuthorizationDefinition | The body contains the Azure Resource ID of the source speech resource.

try:
    # Allows another speech resource (source) to copy a model to this speech resource (target).
    api_response = api_instance.models_authorize_copy(api_version, model_copy_authorization_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_authorize_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **model_copy_authorization_definition** | [**ModelCopyAuthorizationDefinition**](ModelCopyAuthorizationDefinition.md)| The body contains the Azure Resource ID of the source speech resource. | 

### Return type

[**ModelCopyAuthorization**](ModelCopyAuthorization.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_copy**
> Operation models_copy(id, api_version, model_copy_authorization)

Copies a model from one subscription to another.

This method can be used to copy a model from this speech resource to a target one.  The authorization is obtained on the target speech resource.  Only custom models can be copied to another speech resource.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model that will be copied.
api_version = 'api_version_example' # str | The requested api version.
model_copy_authorization = swagger_client.ModelCopyAuthorization() # ModelCopyAuthorization | The body contains the authorization to copy to the target speech resource.

try:
    # Copies a model from one subscription to another.
    api_response = api_instance.models_copy(id, api_version, model_copy_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model that will be copied. | 
 **api_version** | **str**| The requested api version. | 
 **model_copy_authorization** | [**ModelCopyAuthorization**](ModelCopyAuthorization.md)| The body contains the authorization to copy to the target speech resource. | 

### Return type

[**Operation**](Operation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create**
> CustomModel models_create(api_version, model)

Creates a new model.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
model = swagger_client.CustomModel() # CustomModel | The details of the new model.

try:
    # Creates a new model.
    api_response = api_instance.models_create(api_version, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **model** | [**CustomModel**](CustomModel.md)| The details of the new model. | 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_delete**
> models_delete(id, api_version)

Deletes the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Deletes the model identified by the given ID.
    api_instance.models_delete(id, api_version)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 
 **api_version** | **str**| The requested api version. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_base_model**
> BaseModel models_get_base_model(id, api_version)

Gets the base model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the base model.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the base model identified by the given ID.
    api_response = api_instance.models_get_base_model(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_get_base_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the base model. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**BaseModel**](BaseModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_base_model_manifest**
> ModelManifest models_get_base_model_manifest(id, sas_lifetime_minutes, api_version)

Returns an manifest for this base model which can be used in an on-premise container.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the model to generate a manifest for.
sas_lifetime_minutes = 56 # int | The duration in minutes that an SAS url should be valid.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Returns an manifest for this base model which can be used in an on-premise container.
    api_response = api_instance.models_get_base_model_manifest(id, sas_lifetime_minutes, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_get_base_model_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the model to generate a manifest for. | 
 **sas_lifetime_minutes** | **int**| The duration in minutes that an SAS url should be valid. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**ModelManifest**](ModelManifest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_custom_model**
> CustomModel models_get_custom_model(id, api_version)

Gets the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the model identified by the given ID.
    api_response = api_instance.models_get_custom_model(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_get_custom_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_custom_model_manifest**
> ModelManifest models_get_custom_model_manifest(id, sas_lifetime_minutes, api_version)

Returns an manifest for this model which can be used in an on-premise container.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the model to generate a manifest for.
sas_lifetime_minutes = 56 # int | The duration in minutes that an SAS url should be valid.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Returns an manifest for this model which can be used in an on-premise container.
    api_response = api_instance.models_get_custom_model_manifest(id, sas_lifetime_minutes, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_get_custom_model_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the model to generate a manifest for. | 
 **sas_lifetime_minutes** | **int**| The duration in minutes that an SAS url should be valid. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**ModelManifest**](ModelManifest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get_file**
> File models_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)

Gets one specific file (identified with fileId) from a model (identified with id).

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.
file_id = 'file_id_example' # str | The identifier of the file.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. (optional)

try:
    # Gets one specific file (identified with fileId) from a model (identified with id).
    api_response = api_instance.models_get_file(id, file_id, api_version, sas_lifetime_minutes=sas_lifetime_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 
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

# **models_list_base_models**
> PaginatedBaseModels models_list_base_models(api_version, skip=skip, top=top, filter=filter)

Gets the list of base models for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available base models.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=status eq 'NotStarted' or status eq 'Running' (optional)

try:
    # Gets the list of base models for the authenticated subscription.
    api_response = api_instance.models_list_base_models(api_version, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_list_base_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available base models.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;status eq &#39;NotStarted&#39; or status eq &#39;Running&#39; | [optional] 

### Return type

[**PaginatedBaseModels**](PaginatedBaseModels.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list_custom_models**
> PaginatedCustomModels models_list_custom_models(api_version, skip=skip, top=top, filter=filter)

Gets the list of custom models for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available models.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=status eq 'NotStarted' or status eq 'Running' (optional)

try:
    # Gets the list of custom models for the authenticated subscription.
    api_response = api_instance.models_list_custom_models(api_version, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_list_custom_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available models.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;status eq &#39;NotStarted&#39; or status eq &#39;Running&#39; | [optional] 

### Return type

[**PaginatedCustomModels**](PaginatedCustomModels.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list_files**
> PaginatedFiles models_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)

Gets the files of the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.
api_version = 'api_version_example' # str | The requested api version.
sas_lifetime_minutes = 56 # int | This parameter defines the duration in minutes for which an SAS url should be valid.              The parameter can only be used for operations on speech resources that don't have BYOS enabled. For speech resources              that don't have BYOS enabled, the default SAS validity duration is 12 hours.              For speech resources with BYOS, returned urls do not contain an SAS token. (optional)
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter=name eq 'myaudio.wav' and kind eq 'Audio' (optional)

try:
    # Gets the files of the model identified by the given ID.
    api_response = api_instance.models_list_files(id, api_version, sas_lifetime_minutes=sas_lifetime_minutes, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 
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

# **models_list_supported_locales**
> list[str] models_list_supported_locales(api_version)

Gets a list of supported locales for model adaptation.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets a list of supported locales for model adaptation.
    api_response = api_instance.models_list_supported_locales(api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_list_supported_locales: %s\n" % e)
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

# **models_update**
> CustomModel models_update(id, api_version, model_update)

Updates the metadata of the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.
api_version = 'api_version_example' # str | The requested api version.
model_update = swagger_client.ModelUpdate() # ModelUpdate | The updated values for the model.

try:
    # Updates the metadata of the model identified by the given ID.
    api_response = api_instance.models_update(id, api_version, model_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->models_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 
 **api_version** | **str**| The requested api version. | 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)| The updated values for the model. | 

### Return type

[**CustomModel**](CustomModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

