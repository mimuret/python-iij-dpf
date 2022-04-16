# openapi_client.DefaultTtlApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_default_ttl_changes_delete**](DefaultTtlApi.md#zones_zone_id_default_ttl_changes_delete) | **DELETE** /zones/{ZoneId}/default_ttl/changes | 編集中デフォルトTTLの取消
[**zones_zone_id_default_ttl_diffs_get**](DefaultTtlApi.md#zones_zone_id_default_ttl_diffs_get) | **GET** /zones/{ZoneId}/default_ttl/diffs | デフォルトTTLの編集差分の取得
[**zones_zone_id_default_ttl_get**](DefaultTtlApi.md#zones_zone_id_default_ttl_get) | **GET** /zones/{ZoneId}/default_ttl | デフォルトTTLの取得
[**zones_zone_id_default_ttl_patch**](DefaultTtlApi.md#zones_zone_id_default_ttl_patch) | **PATCH** /zones/{ZoneId}/default_ttl | デフォルトTTLの更新


# **zones_zone_id_default_ttl_changes_delete**
> AsyncResponse zones_zone_id_default_ttl_changes_delete(zone_id)

編集中デフォルトTTLの取消

デフォルトTTLの操作を取消します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import default_ttl_api
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
    api_instance = default_ttl_api.DefaultTtlApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # 編集中デフォルトTTLの取消
        api_response = api_instance.zones_zone_id_default_ttl_changes_delete(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultTtlApi->zones_zone_id_default_ttl_changes_delete: %s\n" % e)
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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください forbidden | default_ttl | デフォルトTTLの状態を確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_default_ttl_diffs_get**
> GetDefaultTtlDiffs zones_zone_id_default_ttl_diffs_get(zone_id)

デフォルトTTLの編集差分の取得

現在DNSに登録されているデフォルトTTLと反映予定のデフォルトTTLの差分一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import default_ttl_api
from openapi_client.model.get_default_ttl_diffs import GetDefaultTtlDiffs
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
    api_instance = default_ttl_api.DefaultTtlApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # デフォルトTTLの編集差分の取得
        api_response = api_instance.zones_zone_id_default_ttl_diffs_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultTtlApi->zones_zone_id_default_ttl_diffs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetDefaultTtlDiffs**](GetDefaultTtlDiffs.md)

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

# **zones_zone_id_default_ttl_get**
> GetDefaultTtl zones_zone_id_default_ttl_get(zone_id)

デフォルトTTLの取得

デフォルトTTLの一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import default_ttl_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.get_default_ttl import GetDefaultTtl
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
    api_instance = default_ttl_api.DefaultTtlApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # デフォルトTTLの取得
        api_response = api_instance.zones_zone_id_default_ttl_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultTtlApi->zones_zone_id_default_ttl_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetDefaultTtl**](GetDefaultTtl.md)

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

# **zones_zone_id_default_ttl_patch**
> AsyncResponse zones_zone_id_default_ttl_patch(zone_id)

デフォルトTTLの更新

デフォルトTTLを更新します。\\ **[編集中レコードのゾーン反映](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch)**を実行するまでは権威サーバには反映されません。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import default_ttl_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.patch_default_ttl import PatchDefaultTtl
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_ttl_api.DefaultTtlApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    patch_default_ttl = PatchDefaultTtl(
        value=DefaultTtlValue(1),
    ) # PatchDefaultTtl |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # デフォルトTTLの更新
        api_response = api_instance.zones_zone_id_default_ttl_patch(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultTtlApi->zones_zone_id_default_ttl_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # デフォルトTTLの更新
        api_response = api_instance.zones_zone_id_default_ttl_patch(zone_id, patch_default_ttl=patch_default_ttl)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultTtlApi->zones_zone_id_default_ttl_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **patch_default_ttl** | [**PatchDefaultTtl**](PatchDefaultTtl.md)|  | [optional]

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

