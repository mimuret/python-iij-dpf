# openapi_client.DnssecApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_dnssec_get**](DnssecApi.md#zones_zone_id_dnssec_get) | **GET** /zones/{ZoneId}/dnssec | DNSSEC情報の取得
[**zones_zone_id_dnssec_ksk_rollover_patch**](DnssecApi.md#zones_zone_id_dnssec_ksk_rollover_patch) | **PATCH** /zones/{ZoneId}/dnssec/ksk_rollover | KSKロールオーバーの開始
[**zones_zone_id_dnssec_patch**](DnssecApi.md#zones_zone_id_dnssec_patch) | **PATCH** /zones/{ZoneId}/dnssec | DNSSEC情報の更新


# **zones_zone_id_dnssec_get**
> GetDnssec zones_zone_id_dnssec_get(zone_id)

DNSSEC情報の取得

DNSSEC情報の一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import dnssec_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_dnssec import GetDnssec
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dnssec_api.DnssecApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # DNSSEC情報の取得
        api_response = api_instance.zones_zone_id_dnssec_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnssecApi->zones_zone_id_dnssec_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetDnssec**](GetDnssec.md)

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

# **zones_zone_id_dnssec_ksk_rollover_patch**
> AsyncResponse zones_zone_id_dnssec_ksk_rollover_patch(zone_id)

KSKロールオーバーの開始

指定したゾーンに対してKSKロールオーバーを開始します。\\ ロールオーバーはds_stateが「3」の場合のみ開始できます。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import dnssec_api
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
    api_instance = dnssec_api.DnssecApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # KSKロールオーバーの開始
        api_response = api_instance.zones_zone_id_dnssec_ksk_rollover_patch(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnssecApi->zones_zone_id_dnssec_ksk_rollover_patch: %s\n" % e)
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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください forbidden | dnssec | DNSSECの状態を確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_dnssec_patch**
> AsyncResponse zones_zone_id_dnssec_patch(zone_id)

DNSSEC情報の更新

DNSSECの情報を更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import dnssec_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.patch_dnssec import PatchDnssec
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dnssec_api.DnssecApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    patch_dnssec = PatchDnssec(None) # PatchDnssec |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DNSSEC情報の更新
        api_response = api_instance.zones_zone_id_dnssec_patch(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnssecApi->zones_zone_id_dnssec_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DNSSEC情報の更新
        api_response = api_instance.zones_zone_id_dnssec_patch(zone_id, patch_dnssec=patch_dnssec)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnssecApi->zones_zone_id_dnssec_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **patch_dnssec** | [**PatchDnssec**](PatchDnssec.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください forbidden | dnssec | DNSSECの状態を確認してください resolve_error | dnssec | DNSSECの状態を確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

