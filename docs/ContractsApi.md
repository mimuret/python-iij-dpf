# openapi_client.ContractsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_id_get**](ContractsApi.md#contracts_contract_id_get) | **GET** /contracts/{ContractId} | DPF契約情報の取得
[**contracts_contract_id_patch**](ContractsApi.md#contracts_contract_id_patch) | **PATCH** /contracts/{ContractId} | DPF契約情報の更新
[**contracts_count_get**](ContractsApi.md#contracts_count_get) | **GET** /contracts/count | DPF契約情報の件数取得
[**contracts_get**](ContractsApi.md#contracts_get) | **GET** /contracts | DPF契約情報の一覧取得


# **contracts_contract_id_get**
> GetContract contracts_contract_id_get(contract_id)

DPF契約情報の取得

指定したContractIdのDPF契約を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import contracts_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.get_contract import GetContract
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
    api_instance = contracts_api.ContractsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # DPF契約情報の取得
        api_response = api_instance.contracts_contract_id_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsApi->contracts_contract_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |

### Return type

[**GetContract**](GetContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_patch**
> AsyncResponse contracts_contract_id_patch(contract_id)

DPF契約情報の更新

指定したContractIdのDPF契約を更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import contracts_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.patch_contract import PatchContract
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    patch_contract = PatchContract(
        favorite=ContractFavorite(1),
        description=Description(""),
    ) # PatchContract |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DPF契約情報の更新
        api_response = api_instance.contracts_contract_id_patch(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsApi->contracts_contract_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DPF契約情報の更新
        api_response = api_instance.contracts_contract_id_patch(contract_id, patch_contract=patch_contract)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsApi->contracts_contract_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **patch_contract** | [**PatchContract**](PatchContract.md)|  | [optional]

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_count_get**
> GetCount contracts_count_get()

DPF契約情報の件数取得

DPF契約の件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import contracts_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.contract_plan import ContractPlan
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.contract_state import ContractState
from openapi_client.model.contract_favorite import ContractFavorite
from openapi_client.model.get_count import GetCount
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_service_code = KeywordsString([]) # KeywordsString |  (optional)
    keywords_plan = ContractPlan(1) # ContractPlan |  (optional)
    keywords_state = ContractState(1) # ContractState |  (optional)
    keywords_favorite = ContractFavorite(1) # ContractFavorite |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DPF契約情報の件数取得
        api_response = api_instance.contracts_count_get(type=type, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_plan=keywords_plan, keywords_state=keywords_state, keywords_favorite=keywords_favorite, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsApi->contracts_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_service_code** | **KeywordsString**|  | [optional]
 **keywords_plan** | **ContractPlan**|  | [optional]
 **keywords_state** | **ContractState**|  | [optional]
 **keywords_favorite** | **ContractFavorite**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]

### Return type

[**GetCount**](GetCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get**
> GetContracts contracts_get()

DPF契約情報の一覧取得

DPF契約情報の一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import contracts_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.contract_plan import ContractPlan
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.contract_state import ContractState
from openapi_client.model.get_contracts import GetContracts
from openapi_client.model.contract_favorite import ContractFavorite
from openapi_client.model.search_limit import SearchLimit
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_service_code = KeywordsString([]) # KeywordsString |  (optional)
    keywords_plan = ContractPlan(1) # ContractPlan |  (optional)
    keywords_state = ContractState(1) # ContractState |  (optional)
    keywords_favorite = ContractFavorite(1) # ContractFavorite |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DPF契約情報の一覧取得
        api_response = api_instance.contracts_get(type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_plan=keywords_plan, keywords_state=keywords_state, keywords_favorite=keywords_favorite, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsApi->contracts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_service_code** | **KeywordsString**|  | [optional]
 **keywords_plan** | **ContractPlan**|  | [optional]
 **keywords_state** | **ContractState**|  | [optional]
 **keywords_favorite** | **ContractFavorite**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]

### Return type

[**GetContracts**](GetContracts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

