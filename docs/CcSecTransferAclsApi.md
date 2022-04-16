# openapi_client.CcSecTransferAclsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete**](CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete) | **DELETE** /common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId} | ゾーン転送ACLの削除
[**common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get**](CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId} | ゾーン転送ACLの取得
[**common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch**](CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch) | **PATCH** /common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId} | ゾーン転送ACLの更新
[**common_configs_common_config_id_cc_sec_transfer_acls_get**](CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_transfer_acls | ゾーン転送ACLの一覧取得
[**common_configs_common_config_id_cc_sec_transfer_acls_post**](CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_post) | **POST** /common_configs/{CommonConfigId}/cc_sec_transfer_acls | ゾーン転送ACLの作成


# **common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete**
> AsyncResponse common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete(common_config_id, cc_sec_transfer_acl_id)

ゾーン転送ACLの削除

指定したCcSecTransferAclIdのゾーン転送ACLを削除します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_transfer_acls_api
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
    api_instance = cc_sec_transfer_acls_api.CcSecTransferAclsApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_sec_transfer_acl_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーン転送ACLの削除
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete(common_config_id, cc_sec_transfer_acl_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_sec_transfer_acl_id** | **Id**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_sec_transfer_acl | 指定したCcSecTransferAclIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get**
> GetCcSecTransferAcl common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get(common_config_id, cc_sec_transfer_acl_id)

ゾーン転送ACLの取得

指定したCcSecTransferAclIdのゾーン転送ACLを取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_transfer_acls_api
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.id import Id
from openapi_client.model.get_cc_sec_transfer_acl import GetCcSecTransferAcl
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cc_sec_transfer_acls_api.CcSecTransferAclsApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_sec_transfer_acl_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーン転送ACLの取得
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get(common_config_id, cc_sec_transfer_acl_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_sec_transfer_acl_id** | **Id**| ID |

### Return type

[**GetCcSecTransferAcl**](GetCcSecTransferAcl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_sec_transfer_acl | 指定したCcSecTransferAclIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch**
> AsyncResponse common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch(common_config_id, cc_sec_transfer_acl_id)

ゾーン転送ACLの更新

指定したCcSecTransferAclIdのゾーン転送ACLを更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_transfer_acls_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.patch_cc_sec_transfer_acl import PatchCcSecTransferAcl
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
    api_instance = cc_sec_transfer_acls_api.CcSecTransferAclsApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_sec_transfer_acl_id = Id(1) # Id | ID
    patch_cc_sec_transfer_acl = PatchCcSecTransferAcl(
        tsig_id=TsigId(1),
        network="network_example",
    ) # PatchCcSecTransferAcl |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーン転送ACLの更新
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch(common_config_id, cc_sec_transfer_acl_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーン転送ACLの更新
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch(common_config_id, cc_sec_transfer_acl_id, patch_cc_sec_transfer_acl=patch_cc_sec_transfer_acl)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **cc_sec_transfer_acl_id** | **Id**| ID |
 **patch_cc_sec_transfer_acl** | [**PatchCcSecTransferAcl**](PatchCcSecTransferAcl.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | cc_sec_transfer_acl | 指定したCcSecTransferAclIdを確認してください not_found | tsig | 指定したTSIGを確認してください invalid | network | 指定したnetworkを確認してください duplicated | network | 指定したnetworkを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_configs_common_config_id_cc_sec_transfer_acls_get**
> GetCcSecTransferAcls common_configs_common_config_id_cc_sec_transfer_acls_get(common_config_id)

ゾーン転送ACLの一覧取得

ゾーン転送ACLの設定の一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_transfer_acls_api
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_cc_sec_transfer_acls import GetCcSecTransferAcls
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
    api_instance = cc_sec_transfer_acls_api.CcSecTransferAclsApi(api_client)
    common_config_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーン転送ACLの一覧取得
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_get(common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |

### Return type

[**GetCcSecTransferAcls**](GetCcSecTransferAcls.md)

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

# **common_configs_common_config_id_cc_sec_transfer_acls_post**
> AsyncResponse common_configs_common_config_id_cc_sec_transfer_acls_post(common_config_id)

ゾーン転送ACLの作成

新しくゾーン転送ACLを作成します。\\ 作成できる最大件数は5件です。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import cc_sec_transfer_acls_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.post_cc_sec_transfer_acl import PostCcSecTransferAcl
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
    api_instance = cc_sec_transfer_acls_api.CcSecTransferAclsApi(api_client)
    common_config_id = Id(1) # Id | ID
    post_cc_sec_transfer_acl = PostCcSecTransferAcl(
        tsig_id=TsigId(1),
        network="network_example",
    ) # PostCcSecTransferAcl |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーン転送ACLの作成
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_post(common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーン転送ACLの作成
        api_response = api_instance.common_configs_common_config_id_cc_sec_transfer_acls_post(common_config_id, post_cc_sec_transfer_acl=post_cc_sec_transfer_acl)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcSecTransferAclsApi->common_configs_common_config_id_cc_sec_transfer_acls_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_config_id** | **Id**| ID |
 **post_cc_sec_transfer_acl** | [**PostCcSecTransferAcl**](PostCcSecTransferAcl.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | common_config | 指定したCommonConfigIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTSIG鍵を確認してください invalid | network | 指定したnetworkを確認してください too_many | network | 登録の上限数を超えています duplicated | network | 指定したnetworkを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

