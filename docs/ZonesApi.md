# openapi_client.ZonesApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_count_get**](ZonesApi.md#zones_count_get) | **GET** /zones/count | ゾーンの件数取得
[**zones_get**](ZonesApi.md#zones_get) | **GET** /zones | ゾーンの一覧取得
[**zones_zone_id_changes_delete**](ZonesApi.md#zones_zone_id_changes_delete) | **DELETE** /zones/{ZoneId}/changes | 編集中レコードの一括取消
[**zones_zone_id_changes_patch**](ZonesApi.md#zones_zone_id_changes_patch) | **PATCH** /zones/{ZoneId}/changes | 編集中レコードのゾーン反映
[**zones_zone_id_contract_get**](ZonesApi.md#zones_zone_id_contract_get) | **GET** /zones/{ZoneId}/contract | ゾーンに紐付くDPF契約情報の取得
[**zones_zone_id_get**](ZonesApi.md#zones_zone_id_get) | **GET** /zones/{ZoneId} | ゾーンの取得
[**zones_zone_id_managed_dns_servers_get**](ZonesApi.md#zones_zone_id_managed_dns_servers_get) | **GET** /zones/{ZoneId}/managed_dns_servers | マネージドDNSサーバの一覧取得
[**zones_zone_id_patch**](ZonesApi.md#zones_zone_id_patch) | **PATCH** /zones/{ZoneId} | ゾーンの更新


# **zones_count_get**
> GetCount zones_count_get()

ゾーンの件数取得

DPF契約に紐付くゾーンの件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
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
    api_instance = zones_api.ZonesApi(api_client)
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
    # and optional values
    try:
        # ゾーンの件数取得
        api_response = api_instance.zones_count_get(type=type, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_name=keywords_name, keywords_network=keywords_network, keywords_state=keywords_state, keywords_favorite=keywords_favorite, keywords_description=keywords_description, keywords_common_config_id=keywords_common_config_id, keywords_zone_proxy_enabled=keywords_zone_proxy_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_get**
> GetZones zones_get()

ゾーンの一覧取得

DPF契約に紐付くゾーンの一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
from openapi_client.model.get_zones import GetZones
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
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
    api_instance = zones_api.ZonesApi(api_client)
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
    # and optional values
    try:
        # ゾーンの一覧取得
        api_response = api_instance.zones_get(type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_name=keywords_name, keywords_network=keywords_network, keywords_state=keywords_state, keywords_favorite=keywords_favorite, keywords_description=keywords_description, keywords_common_config_id=keywords_common_config_id, keywords_zone_proxy_enabled=keywords_zone_proxy_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_changes_delete**
> AsyncResponse zones_zone_id_changes_delete(zone_id)

編集中レコードの一括取消

編集中のレコードの操作を一括で取り消します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
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
    api_instance = zones_api.ZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # 編集中レコードの一括取消
        api_response = api_instance.zones_zone_id_changes_delete(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_changes_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください forbidden | zone | ゾーンプロキシの設定が有効のため操作できません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_changes_patch**
> AsyncResponse zones_zone_id_changes_patch(zone_id)

編集中レコードのゾーン反映

編集中のレコードの操作を反映します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
from openapi_client.model.patch_zone_commit import PatchZoneCommit
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
    api_instance = zones_api.ZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    patch_zone_commit = PatchZoneCommit(
        description=Description(""),
    ) # PatchZoneCommit |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 編集中レコードのゾーン反映
        api_response = api_instance.zones_zone_id_changes_patch(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_changes_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 編集中レコードのゾーン反映
        api_response = api_instance.zones_zone_id_changes_patch(zone_id, patch_zone_commit=patch_zone_commit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_changes_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **patch_zone_commit** | [**PatchZoneCommit**](PatchZoneCommit.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください forbidden | zone | ゾーンプロキシの設定が有効のため操作できません reference_not_found | rdata | rdetaの参照先が存在しません resolve_error | rdata | 名前解決ができないゾーンが含まれています  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_contract_get**
> GetContract zones_zone_id_contract_get(zone_id)

ゾーンに紐付くDPF契約情報の取得

指定したZoneIdのゾーンに紐付くDPF契約情報を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
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
    api_instance = zones_api.ZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーンに紐付くDPF契約情報の取得
        api_response = api_instance.zones_zone_id_contract_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_contract_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_get**
> GetZone zones_zone_id_get(zone_id)

ゾーンの取得

指定したZoneIdのゾーンを取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_zone import GetZone
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = zones_api.ZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーンの取得
        api_response = api_instance.zones_zone_id_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetZone**](GetZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_managed_dns_servers_get**
> GetManagedServers zones_zone_id_managed_dns_servers_get(zone_id)

マネージドDNSサーバの一覧取得

指定したZoneIdのマネージドDNSサーバの一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
from openapi_client.model.get_managed_servers import GetManagedServers
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
    api_instance = zones_api.ZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # マネージドDNSサーバの一覧取得
        api_response = api_instance.zones_zone_id_managed_dns_servers_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_managed_dns_servers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetManagedServers**](GetManagedServers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_patch**
> AsyncResponse zones_zone_id_patch(zone_id)

ゾーンの更新

指定したZoneIdのゾーンを更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import zones_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.patch_zone import PatchZone
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
    api_instance = zones_api.ZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    patch_zone = PatchZone(
        favorite=ZonesFavorite(1),
        description=Description(""),
    ) # PatchZone |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーンの更新
        api_response = api_instance.zones_zone_id_patch(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーンの更新
        api_response = api_instance.zones_zone_id_patch(zone_id, patch_zone=patch_zone)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->zones_zone_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **patch_zone** | [**PatchZone**](PatchZone.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

