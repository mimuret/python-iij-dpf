# openapi_client.PingApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_get**](PingApi.md#ping_get) | **GET** /ping | API疎通確認


# **ping_get**
> GetPing ping_get()

API疎通確認

APIへの疎通を確認できます。  ### Authorizations dpf_read\\ dpf_write\\ dpf_contract 

### Example


```python
import time
import openapi_client
from openapi_client.api import ping_api
from openapi_client.model.get_ping import GetPing
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ping_api.PingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API疎通確認
        api_response = api_instance.ping_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PingApi->ping_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPing**](GetPing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

