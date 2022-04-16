# openapi_client.CcSecNotifiedServersApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete**](CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete) | **DELETE** /common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId} | DNS NOTIFY設定の削除
[**common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get**](CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId} | DNS NOTIFY設定の取得
[**common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch**](CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch) | **PATCH** /common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId} | DNS NOTIFY設定の更新
[**common_configs_common_config_id_cc_sec_notified_servers_get**](CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_notified_servers | DNS NOTIFY設定の一覧取得
[**common_configs_common_config_id_cc_sec_notified_servers_post**](CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_post) | **POST** /common_configs/{CommonConfigId}/cc_sec_notified_servers | DNS NOTIFY設定の作成


# **common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete**
> AsyncResponse common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete(common_config_id, cc_sec_notified_server_id)

DNS NOTIFY設定の削除

指定したCcSecNotifiedServerIdのDNS NOTIFYを削除します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_notified_servers_api
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
    api_instance = cc_sec_notified_servers_api.CcSecNotifiedServersApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_sec_notified_server_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # DNS NOTIFY設定の削除
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete(common_config_id, cc_sec_notified_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_sec_notified_server_id** | **Id**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_sec_notified_server | 指定したCcSecNotifiedServerIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get**
> GetCcSecNotifiedServer common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get(common_config_id, cc_sec_notified_server_id)

DNS NOTIFY設定の取得

指定したCcSecNotifiedServerIdのDNS NOTIFYを取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_notified_servers_api
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_cc_sec_notified_server import GetCcSecNotifiedServer
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
    api_instance = cc_sec_notified_servers_api.CcSecNotifiedServersApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_sec_notified_server_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # DNS NOTIFY設定の取得
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get(common_config_id, cc_sec_notified_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_sec_notified_server_id** | **Id**| ID |

### Return type

[**GetCcSecNotifiedServer**](GetCcSecNotifiedServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_sec_notified_server | 指定したCcSecNotifiedServerIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch**
> AsyncResponse common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch(common_config_id, cc_sec_notified_server_id)

DNS NOTIFY設定の更新

指定したCcSecNotifiedServerIdのDNS NOTIFYを更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_notified_servers_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.patch_cc_sec_notified_server import PatchCcSecNotifiedServer
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
    api_instance = cc_sec_notified_servers_api.CcSecNotifiedServersApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_sec_notified_server_id = Id(1) # Id | ID
    patch_cc_sec_notified_server = PatchCcSecNotifiedServer(
        tsig_id=TsigId(1),
        address="address_example",
    ) # PatchCcSecNotifiedServer |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DNS NOTIFY設定の更新
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch(common_config_id, cc_sec_notified_server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DNS NOTIFY設定の更新
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch(common_config_id, cc_sec_notified_server_id, patch_cc_sec_notified_server=patch_cc_sec_notified_server)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_sec_notified_server_id** | **Id**| ID |
 **patch_cc_sec_notified_server** | [**PatchCcSecNotifiedServer**](PatchCcSecNotifiedServer.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_sec_notified_server | 指定したCcSecNotifiedServerIdを確認してください not_found | tsig | 指定したTSIGを確認してください invalid | address | 指定したaddressを確認してください duplicated | address | 指定したaddressを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_sec_notified_servers_get**
> GetCcSecNotifiedServers common_configs_common_config_id_cc_sec_notified_servers_get(common_config_id)

DNS NOTIFY設定の一覧取得

DNS NOTIFYの設定の一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_notified_servers_api
from openapi_client.model.get_cc_sec_notified_servers import GetCcSecNotifiedServers
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
    api_instance = cc_sec_notified_servers_api.CcSecNotifiedServersApi(api_client)
    common_config_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # DNS NOTIFY設定の一覧取得
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_get(common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |

### Return type

[**GetCcSecNotifiedServers**](GetCcSecNotifiedServers.md)

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

# **common_configs_common_config_id_cc_sec_notified_servers_post**
> AsyncResponse common_configs_common_config_id_cc_sec_notified_servers_post(common_config_id)

DNS NOTIFY設定の作成

新しくDNS NOFITYを作成します。\\ 作成できる最大件数は256件です。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_notified_servers_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.post_cc_sec_notified_server import PostCcSecNotifiedServer
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
    api_instance = cc_sec_notified_servers_api.CcSecNotifiedServersApi(api_client)
    common_config_id = Id(1) # Id | ID
    post_cc_sec_notified_server = PostCcSecNotifiedServer(
        tsig_id=TsigId(1),
        address="address_example",
    ) # PostCcSecNotifiedServer |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DNS NOTIFY設定の作成
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_post(common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DNS NOTIFY設定の作成
        api_response = api_instance.common_configs_common_config_id_cc_sec_notified_servers_post(common_config_id, post_cc_sec_notified_server=post_cc_sec_notified_server)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecNotifiedServersApi->common_configs_common_config_id_cc_sec_notified_servers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **post_cc_sec_notified_server** | [**PostCcSecNotifiedServer**](PostCcSecNotifiedServer.md)|  | [optional]

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

