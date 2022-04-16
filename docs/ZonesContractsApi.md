# openapi_client.ZonesContractsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_id_zones_common_configs_patch**](ZonesContractsApi.md#contracts_contract_id_zones_common_configs_patch) | **PATCH** /contracts/{ContractId}/zones/common_configs | DPF契約に紐付くゾーンの共通設定の更新
[**contracts_contract_id_zones_count_get**](ZonesContractsApi.md#contracts_contract_id_zones_count_get) | **GET** /contracts/{ContractId}/zones/count | DPF契約に紐付くゾーンの件数取得
[**contracts_contract_id_zones_get**](ZonesContractsApi.md#contracts_contract_id_zones_get) | **GET** /contracts/{ContractId}/zones | DPF契約に紐付くゾーンの一覧取得


# **contracts_contract_id_zones_common_configs_patch**
> AsyncResponse contracts_contract_id_zones_common_configs_patch(contract_id)

DPF契約に紐付くゾーンの共通設定の更新

指定したContractIdの共通設定を切り替えます。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_contracts_api
from openapi_client.model.patch_contracts_zones import PatchContractsZones
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
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
    api_instance = zones_contracts_api.ZonesContractsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    patch_contracts_zones = PatchContractsZones(
        common_config_id=Id(1),
        zone_ids=[
            SystemId("zone_ids_example"),
        ],
    ) # PatchContractsZones |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DPF契約に紐付くゾーンの共通設定の更新
        api_response = api_instance.contracts_contract_id_zones_common_configs_patch(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesContractsApi->contracts_contract_id_zones_common_configs_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DPF契約に紐付くゾーンの共通設定の更新
        api_response = api_instance.contracts_contract_id_zones_common_configs_patch(contract_id, patch_contracts_zones=patch_contracts_zones)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesContractsApi->contracts_contract_id_zones_common_configs_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **patch_contracts_zones** | [**PatchContractsZones**](PatchContractsZones.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定した共通設定を確認してください not_found | zones | 指定したゾーンを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_zones_count_get**
> GetCount contracts_contract_id_zones_count_get(contract_id)

DPF契約に紐付くゾーンの件数取得

指定したContractIdのDPF契約に紐付くゾーンの件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_contracts_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.zones_state import ZonesState
from openapi_client.model.zone_proxy_enabled import ZoneProxyEnabled
from openapi_client.model.zones_favorite import ZonesFavorite
from openapi_client.model.id import Id
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
    api_instance = zones_contracts_api.ZonesContractsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_service_code = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_network = KeywordsString([]) # KeywordsString |  (optional)
    keywords_state = ZonesState(1) # ZonesState |  (optional)
    keywords_favorite = ZonesFavorite(1) # ZonesFavorite |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_common_config_id = Id(1) # Id |  (optional)
    keywords_zone_proxy_enabled = ZoneProxyEnabled(0) # ZoneProxyEnabled |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DPF契約に紐付くゾーンの件数取得
        api_response = api_instance.contracts_contract_id_zones_count_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesContractsApi->contracts_contract_id_zones_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DPF契約に紐付くゾーンの件数取得
        api_response = api_instance.contracts_contract_id_zones_count_get(contract_id, type=type, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_name=keywords_name, keywords_network=keywords_network, keywords_state=keywords_state, keywords_favorite=keywords_favorite, keywords_description=keywords_description, keywords_common_config_id=keywords_common_config_id, keywords_zone_proxy_enabled=keywords_zone_proxy_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesContractsApi->contracts_contract_id_zones_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_service_code** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_network** | **KeywordsString**|  | [optional]
 **keywords_state** | **ZonesState**|  | [optional]
 **keywords_favorite** | **ZonesFavorite**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_common_config_id** | **Id**|  | [optional]
 **keywords_zone_proxy_enabled** | **ZoneProxyEnabled**|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_zones_get**
> GetZones contracts_contract_id_zones_get(contract_id)

DPF契約に紐付くゾーンの一覧取得

指定したContractIdのDPF契約に紐付くゾーンの一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_contracts_api
from openapi_client.model.get_zones import GetZones
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.zones_state import ZonesState
from openapi_client.model.zone_proxy_enabled import ZoneProxyEnabled
from openapi_client.model.zones_favorite import ZonesFavorite
from openapi_client.model.id import Id
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
    api_instance = zones_contracts_api.ZonesContractsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_service_code = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_network = KeywordsString([]) # KeywordsString |  (optional)
    keywords_state = ZonesState(1) # ZonesState |  (optional)
    keywords_favorite = ZonesFavorite(1) # ZonesFavorite |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_common_config_id = Id(1) # Id |  (optional)
    keywords_zone_proxy_enabled = ZoneProxyEnabled(0) # ZoneProxyEnabled |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DPF契約に紐付くゾーンの一覧取得
        api_response = api_instance.contracts_contract_id_zones_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesContractsApi->contracts_contract_id_zones_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DPF契約に紐付くゾーンの一覧取得
        api_response = api_instance.contracts_contract_id_zones_get(contract_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_name=keywords_name, keywords_network=keywords_network, keywords_state=keywords_state, keywords_favorite=keywords_favorite, keywords_description=keywords_description, keywords_common_config_id=keywords_common_config_id, keywords_zone_proxy_enabled=keywords_zone_proxy_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesContractsApi->contracts_contract_id_zones_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_service_code** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_network** | **KeywordsString**|  | [optional]
 **keywords_state** | **ZonesState**|  | [optional]
 **keywords_favorite** | **ZonesFavorite**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_common_config_id** | **Id**|  | [optional]
 **keywords_zone_proxy_enabled** | **ZoneProxyEnabled**|  | [optional]

### Return type

[**GetZones**](GetZones.md)

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

