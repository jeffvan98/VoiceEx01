# swagger_client.CustomSpeechEndpointsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_create**](CustomSpeechEndpointsApi.md#endpoints_create) | **POST** /endpoints | Creates a new endpoint.
[**endpoints_delete**](CustomSpeechEndpointsApi.md#endpoints_delete) | **DELETE** /endpoints/{id} | Deletes the endpoint identified by the given ID.
[**endpoints_get**](CustomSpeechEndpointsApi.md#endpoints_get) | **GET** /endpoints/{id} | Gets the endpoint identified by the given ID.
[**endpoints_list**](CustomSpeechEndpointsApi.md#endpoints_list) | **GET** /endpoints | Gets the list of endpoints for the authenticated subscription.
[**endpoints_list_supported_locales**](CustomSpeechEndpointsApi.md#endpoints_list_supported_locales) | **GET** /endpoints/locales | Gets a list of supported locales for endpoint creations.
[**endpoints_update**](CustomSpeechEndpointsApi.md#endpoints_update) | **PATCH** /endpoints/{id} | Updates the metadata of the endpoint identified by the given ID.


# **endpoints_create**
> Endpoint endpoints_create(api_version, endpoint)

Creates a new endpoint.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
endpoint = swagger_client.Endpoint() # Endpoint | The details of the endpoint.

try:
    # Creates a new endpoint.
    api_response = api_instance.endpoints_create(api_version, endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **endpoint** | [**Endpoint**](Endpoint.md)| The details of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete**
> endpoints_delete(id, api_version)

Deletes the endpoint identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Deletes the endpoint identified by the given ID.
    api_instance.endpoints_delete(id, api_version)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **api_version** | **str**| The requested api version. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get**
> Endpoint endpoints_get(id, api_version)

Gets the endpoint identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets the endpoint identified by the given ID.
    api_response = api_instance.endpoints_get(id, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **api_version** | **str**| The requested api version. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list**
> PaginatedEndpoints endpoints_list(api_version, skip=skip, top=top, filter=filter)

Gets the list of endpoints for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available endpoints.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=locale eq 'en-US' (optional)

try:
    # Gets the list of endpoints for the authenticated subscription.
    api_response = api_instance.endpoints_list(api_version, skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested api version. | 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available endpoints.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;locale eq &#39;en-US&#39; | [optional] 

### Return type

[**PaginatedEndpoints**](PaginatedEndpoints.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_supported_locales**
> list[str] endpoints_list_supported_locales(api_version)

Gets a list of supported locales for endpoint creations.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The requested api version.

try:
    # Gets a list of supported locales for endpoint creations.
    api_response = api_instance.endpoints_list_supported_locales(api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_list_supported_locales: %s\n" % e)
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

# **endpoints_update**
> Endpoint endpoints_update(id, api_version, endpoint_update)

Updates the metadata of the endpoint identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
api_version = 'api_version_example' # str | The requested api version.
endpoint_update = swagger_client.EndpointUpdate() # EndpointUpdate | The updated values for the endpoint.

try:
    # Updates the metadata of the endpoint identified by the given ID.
    api_response = api_instance.endpoints_update(id, api_version, endpoint_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **api_version** | **str**| The requested api version. | 
 **endpoint_update** | [**EndpointUpdate**](EndpointUpdate.md)| The updated values for the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

