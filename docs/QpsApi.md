# openapi_client.QpsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_id_qps_histories_get**](QpsApi.md#contracts_contract_id_qps_histories_get) | **GET** /contracts/{ContractId}/qps/histories | 月別のQPSの一覧取得


# **contracts_contract_id_qps_histories_get**
> GetQpsHistories contracts_contract_id_qps_histories_get(contract_id)

月別のQPSの一覧取得

DPF契約の月別のQPSを取得できます。\\ DPF契約に紐付くゾーンの月別のQPSと、\\ ゾーンのクエリ数を元に集計したDPF契約の月別のQPSが取得できます。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import qps_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.get_qps_histories import GetQpsHistories
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qps_api.QpsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # 月別のQPSの一覧取得
        api_response = api_instance.contracts_contract_id_qps_histories_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QpsApi->contracts_contract_id_qps_histories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |

### Return type

[**GetQpsHistories**](GetQpsHistories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

