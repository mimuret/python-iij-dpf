# openapi_client.JobsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_request_id_get**](JobsApi.md#jobs_request_id_get) | **GET** /jobs/{RequestId} | 非同期リクエストの状態確認


# **jobs_request_id_get**
> GetJobs jobs_request_id_get(request_id)

非同期リクエストの状態確認

ジョブの進捗状況を取得します。\\ このAPIの詳しい利用方法は、**[非同期リクエスト](#section/利用方法/非同期リクエスト)**を参照してください。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import jobs_api
from openapi_client.model.get_jobs import GetJobs
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.request_id import RequestId
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    request_id = RequestId("RequestId_example") # RequestId | ID

    # example passing only required values which don't have defaults set
    try:
        # 非同期リクエストの状態確認
        api_response = api_instance.jobs_request_id_get(request_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JobsApi->jobs_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **RequestId**| ID |

### Return type

[**GetJobs**](GetJobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | request_id | 指定したRequestIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

