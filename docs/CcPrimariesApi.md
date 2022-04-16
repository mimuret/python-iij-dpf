# openapi_client.CcPrimariesApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_configs_common_config_id_cc_primaries_cc_primary_id_delete**](CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_cc_primary_id_delete) | **DELETE** /common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId} | プライマリネームサーバ設定の削除
[**common_configs_common_config_id_cc_primaries_cc_primary_id_get**](CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_cc_primary_id_get) | **GET** /common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId} | プライマリネームサーバ設定の取得
[**common_configs_common_config_id_cc_primaries_cc_primary_id_patch**](CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_cc_primary_id_patch) | **PATCH** /common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId} | プライマリネームサーバ設定の更新
[**common_configs_common_config_id_cc_primaries_get**](CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_get) | **GET** /common_configs/{CommonConfigId}/cc_primaries | プライマリネームサーバ設定の一覧取得
[**common_configs_common_config_id_cc_primaries_post**](CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_post) | **POST** /common_configs/{CommonConfigId}/cc_primaries | プライマリネームサーバ設定の作成


# **common_configs_common_config_id_cc_primaries_cc_primary_id_delete**
> AsyncResponse common_configs_common_config_id_cc_primaries_cc_primary_id_delete(common_config_id, cc_primary_id)

プライマリネームサーバ設定の削除

指定したCcPrimaryIdのプライマリネームサーバを削除します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_primaries_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cc_primaries_api.CcPrimariesApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_primary_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # プライマリネームサーバ設定の削除
        api_response = api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_delete(common_config_id, cc_primary_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_cc_primary_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_primary_id** | **Id**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_primary | 指定したCcPrimaryIdを確認してください forbidden | cc_primary | 有効のため削除できません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_primaries_cc_primary_id_get**
> GetCcPrimary common_configs_common_config_id_cc_primaries_cc_primary_id_get(common_config_id, cc_primary_id)

プライマリネームサーバ設定の取得

指定したCcPrimaryIdのプライマリネームサーバを取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_primaries_api
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_cc_primary import GetCcPrimary
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cc_primaries_api.CcPrimariesApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_primary_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # プライマリネームサーバ設定の取得
        api_response = api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_get(common_config_id, cc_primary_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_cc_primary_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_primary_id** | **Id**| ID |

### Return type

[**GetCcPrimary**](GetCcPrimary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_primary | 指定したCcPrimaryIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_primaries_cc_primary_id_patch**
> AsyncResponse common_configs_common_config_id_cc_primaries_cc_primary_id_patch(common_config_id, cc_primary_id)

プライマリネームサーバ設定の更新

指定したCcPrimaryIdのプライマリネームサーバを更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_primaries_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.patch_cc_primary import PatchCcPrimary
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cc_primaries_api.CcPrimariesApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_primary_id = Id(1) # Id | ID
    patch_cc_primary = PatchCcPrimary(
        tsig_id=TsigId(1),
        address="address_example",
        enabled=CcPrimaryEnabled(0),
    ) # PatchCcPrimary |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # プライマリネームサーバ設定の更新
        api_response = api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_patch(common_config_id, cc_primary_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_cc_primary_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # プライマリネームサーバ設定の更新
        api_response = api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_patch(common_config_id, cc_primary_id, patch_cc_primary=patch_cc_primary)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_cc_primary_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_primary_id** | **Id**| ID |
 **patch_cc_primary** | [**PatchCcPrimary**](PatchCcPrimary.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_primary | 指定したCcPrimaryIdを確認してください not_found | tsig | 指定したTSIGを確認してください invalid | address | 指定したaddressを確認してください duplicated | address | 指定したaddressを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_primaries_get**
> GetCcPrimaries common_configs_common_config_id_cc_primaries_get(common_config_id)

プライマリネームサーバ設定の一覧取得

プライマリネームサーバの設定の一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_primaries_api
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_cc_primaries import GetCcPrimaries
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cc_primaries_api.CcPrimariesApi(api_client)
    common_config_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # プライマリネームサーバ設定の一覧取得
        api_response = api_instance.common_configs_common_config_id_cc_primaries_get(common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |

### Return type

[**GetCcPrimaries**](GetCcPrimaries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_primaries_post**
> AsyncResponse common_configs_common_config_id_cc_primaries_post(common_config_id)

プライマリネームサーバ設定の作成

新しくプライマリネームサーバを作成します。\\ 作成できる最大件数は5件です。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_primaries_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.post_cc_primary import PostCcPrimary
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cc_primaries_api.CcPrimariesApi(api_client)
    common_config_id = Id(1) # Id | ID
    post_cc_primary = PostCcPrimary(
        tsig_id=TsigId(1),
        address="address_example",
    ) # PostCcPrimary |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # プライマリネームサーバ設定の作成
        api_response = api_instance.common_configs_common_config_id_cc_primaries_post(common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # プライマリネームサーバ設定の作成
        api_response = api_instance.common_configs_common_config_id_cc_primaries_post(common_config_id, post_cc_primary=post_cc_primary)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **post_cc_primary** | [**PostCcPrimary**](PostCcPrimary.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTSIG鍵を確認してください invalid | address | 指定したaddressを確認してください too_many | address | 登録の上限数を超えています duplicated | address | 既に登録されています  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

