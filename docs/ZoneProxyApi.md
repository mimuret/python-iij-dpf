# openapi_client.ZoneProxyApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_zone_proxy_get**](ZoneProxyApi.md#zones_zone_id_zone_proxy_get) | **GET** /zones/{ZoneId}/zone_proxy | ゾーンプロキシ設定の取得
[**zones_zone_id_zone_proxy_health_check_get**](ZoneProxyApi.md#zones_zone_id_zone_proxy_health_check_get) | **GET** /zones/{ZoneId}/zone_proxy/health_check | プライマリネームサーバのヘルスチェック結果の取得
[**zones_zone_id_zone_proxy_patch**](ZoneProxyApi.md#zones_zone_id_zone_proxy_patch) | **PATCH** /zones/{ZoneId}/zone_proxy | ゾーンプロキシ設定の更新


# **zones_zone_id_zone_proxy_get**
> GetZoneProxy zones_zone_id_zone_proxy_get(zone_id)

ゾーンプロキシ設定の取得

ゾーンプロキシの設定を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zone_proxy_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.get_zone_proxy import GetZoneProxy
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
    api_instance = zone_proxy_api.ZoneProxyApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーンプロキシ設定の取得
        api_response = api_instance.zones_zone_id_zone_proxy_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneProxyApi->zones_zone_id_zone_proxy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetZoneProxy**](GetZoneProxy.md)

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

# **zones_zone_id_zone_proxy_health_check_get**
> GetZoneProxyHealth zones_zone_id_zone_proxy_health_check_get(zone_id)

プライマリネームサーバのヘルスチェック結果の取得

ゾーン転送のヘルスチェック結果の一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zone_proxy_api
from openapi_client.model.get_zone_proxy_health import GetZoneProxyHealth
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
    api_instance = zone_proxy_api.ZoneProxyApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # プライマリネームサーバのヘルスチェック結果の取得
        api_response = api_instance.zones_zone_id_zone_proxy_health_check_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneProxyApi->zones_zone_id_zone_proxy_health_check_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetZoneProxyHealth**](GetZoneProxyHealth.md)

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

# **zones_zone_id_zone_proxy_patch**
> AsyncResponse zones_zone_id_zone_proxy_patch(zone_id)

ゾーンプロキシ設定の更新

ゾーンプロキシの設定を更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import zone_proxy_api
from openapi_client.model.patch_zone_proxy import PatchZoneProxy
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
    api_instance = zone_proxy_api.ZoneProxyApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    patch_zone_proxy = PatchZoneProxy(
        enabled=ZoneProxyEnabled(0),
    ) # PatchZoneProxy |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーンプロキシ設定の更新
        api_response = api_instance.zones_zone_id_zone_proxy_patch(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneProxyApi->zones_zone_id_zone_proxy_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーンプロキシ設定の更新
        api_response = api_instance.zones_zone_id_zone_proxy_patch(zone_id, patch_zone_proxy=patch_zone_proxy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneProxyApi->zones_zone_id_zone_proxy_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **patch_zone_proxy** | [**PatchZoneProxy**](PatchZoneProxy.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください forbidden | zone | 編集中のレコードが存在しているため有効化できません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

