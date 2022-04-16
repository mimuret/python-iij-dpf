# openapi_client.CommonConfigsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_id_common_configs_common_config_id_copy_post**](CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_copy_post) | **POST** /contracts/{ContractId}/common_configs/{CommonConfigId}/copy | 共通設定のコピー
[**contracts_contract_id_common_configs_common_config_id_delete**](CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_delete) | **DELETE** /contracts/{ContractId}/common_configs/{CommonConfigId} | 共通設定の削除
[**contracts_contract_id_common_configs_common_config_id_get**](CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_get) | **GET** /contracts/{ContractId}/common_configs/{CommonConfigId} | 共通設定の取得
[**contracts_contract_id_common_configs_common_config_id_managed_dns_patch**](CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_managed_dns_patch) | **PATCH** /contracts/{ContractId}/common_configs/{CommonConfigId}/managed_dns | マネージドDNSサーバの状態更新
[**contracts_contract_id_common_configs_common_config_id_patch**](CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_patch) | **PATCH** /contracts/{ContractId}/common_configs/{CommonConfigId} | 共通設定の更新
[**contracts_contract_id_common_configs_count_get**](CommonConfigsApi.md#contracts_contract_id_common_configs_count_get) | **GET** /contracts/{ContractId}/common_configs/count | 共通設定の件数取得
[**contracts_contract_id_common_configs_default_patch**](CommonConfigsApi.md#contracts_contract_id_common_configs_default_patch) | **PATCH** /contracts/{ContractId}/common_configs/default | 初期適用される共通設定の更新
[**contracts_contract_id_common_configs_get**](CommonConfigsApi.md#contracts_contract_id_common_configs_get) | **GET** /contracts/{ContractId}/common_configs | 共通設定の一覧取得
[**contracts_contract_id_common_configs_post**](CommonConfigsApi.md#contracts_contract_id_common_configs_post) | **POST** /contracts/{ContractId}/common_configs | 共通設定の作成


# **contracts_contract_id_common_configs_common_config_id_copy_post**
> AsyncResponse contracts_contract_id_common_configs_common_config_id_copy_post(contract_id, common_config_id)

共通設定のコピー

指定した共通設定と同じ内容の共通設定を別の共通設定名で作成します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.post_common_config import PostCommonConfig
from openapi_client.model.system_id import SystemId
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    common_config_id = Id(1) # Id | ID
    post_common_config = PostCommonConfig(
        name=CommonConfigName("name_example"),
        description=Description(""),
    ) # PostCommonConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 共通設定のコピー
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_copy_post(contract_id, common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_copy_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 共通設定のコピー
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_copy_post(contract_id, common_config_id, post_common_config=post_common_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_copy_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **common_config_id** | **Id**| ID |
 **post_common_config** | [**PostCommonConfig**](PostCommonConfig.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定したCommonConfigIdを確認してください duplicated | name | 指定したnameを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_common_config_id_delete**
> AsyncResponse contracts_contract_id_common_configs_common_config_id_delete(contract_id, common_config_id)

共通設定の削除

指定したCommonConfigIdの共通設定を削除します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    common_config_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # 共通設定の削除
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_delete(contract_id, common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **common_config_id** | **Id**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定したCommonConfigIdを確認してください forbidden | common_config | 参照元が存在しているため削除できません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_common_config_id_get**
> GetCommonConfig contracts_contract_id_common_configs_common_config_id_get(contract_id, common_config_id)

共通設定の取得

指定したCommonConfigIdの共通設定を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.get_common_config import GetCommonConfig
from openapi_client.model.system_id import SystemId
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    common_config_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # 共通設定の取得
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_get(contract_id, common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **common_config_id** | **Id**| ID |

### Return type

[**GetCommonConfig**](GetCommonConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定したCommonConfigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_common_config_id_managed_dns_patch**
> AsyncResponse contracts_contract_id_common_configs_common_config_id_managed_dns_patch(contract_id, common_config_id)

マネージドDNSサーバの状態更新

マネージドDNSサーバをプライマリネームサーバとして有効もしくは無効とするかの切り替えを行えます。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.system_id import SystemId
from openapi_client.model.patch_managed_dns import PatchManagedDns
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    common_config_id = Id(1) # Id | ID
    patch_managed_dns = PatchManagedDns(
        managed_dns_enabled=ManagedDnsEnabled(0),
    ) # PatchManagedDns |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # マネージドDNSサーバの状態更新
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_managed_dns_patch(contract_id, common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_managed_dns_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # マネージドDNSサーバの状態更新
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_managed_dns_patch(contract_id, common_config_id, patch_managed_dns=patch_managed_dns)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_managed_dns_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **common_config_id** | **Id**| ID |
 **patch_managed_dns** | [**PatchManagedDns**](PatchManagedDns.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定したCommonConfigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_common_config_id_patch**
> AsyncResponse contracts_contract_id_common_configs_common_config_id_patch(contract_id, common_config_id)

共通設定の更新

指定したCommonConfigIdの共通設定を更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.patch_common_config import PatchCommonConfig
from openapi_client.model.system_id import SystemId
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    common_config_id = Id(1) # Id | ID
    patch_common_config = PatchCommonConfig(
        name=CommonConfigName("name_example"),
        description=Description(""),
    ) # PatchCommonConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 共通設定の更新
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_patch(contract_id, common_config_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 共通設定の更新
        api_response = api_instance.contracts_contract_id_common_configs_common_config_id_patch(contract_id, common_config_id, patch_common_config=patch_common_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_common_config_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **common_config_id** | **Id**| ID |
 **patch_common_config** | [**PatchCommonConfig**](PatchCommonConfig.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定したCommonConfigIdを確認してください duplicated | name | 指定したnameを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_count_get**
> GetCount contracts_contract_id_common_configs_count_get(contract_id)

共通設定の件数取得

共通設定の件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 共通設定の件数取得
        api_response = api_instance.contracts_contract_id_common_configs_count_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 共通設定の件数取得
        api_response = api_instance.contracts_contract_id_common_configs_count_get(contract_id, type=type, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_default_patch**
> AsyncResponse contracts_contract_id_common_configs_default_patch(contract_id)

初期適用される共通設定の更新

ゾーンを新規追加した場合に、自動で適用される共通設定を切り替えます。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.patch_default_common_config import PatchDefaultCommonConfig
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    patch_default_common_config = PatchDefaultCommonConfig(
        common_config_id=Id(1),
    ) # PatchDefaultCommonConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 初期適用される共通設定の更新
        api_response = api_instance.contracts_contract_id_common_configs_default_patch(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_default_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 初期適用される共通設定の更新
        api_response = api_instance.contracts_contract_id_common_configs_default_patch(contract_id, patch_default_common_config=patch_default_common_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_default_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **patch_default_common_config** | [**PatchDefaultCommonConfig**](PatchDefaultCommonConfig.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | common_config | 指定したCommonConfigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_common_configs_get**
> GetCommonConfigs contracts_contract_id_common_configs_get(contract_id)

共通設定の一覧取得

共通設定の一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_common_configs import GetCommonConfigs
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 共通設定の一覧取得
        api_response = api_instance.contracts_contract_id_common_configs_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 共通設定の一覧取得
        api_response = api_instance.contracts_contract_id_common_configs_get(contract_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]

### Return type

[**GetCommonConfigs**](GetCommonConfigs.md)

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

# **contracts_contract_id_common_configs_post**
> AsyncResponse contracts_contract_id_common_configs_post(contract_id)

共通設定の作成

新しく共通設定を作成します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import common_configs_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.post_common_config import PostCommonConfig
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
    api_instance = common_configs_api.CommonConfigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    post_common_config = PostCommonConfig(
        name=CommonConfigName("name_example"),
        description=Description(""),
    ) # PostCommonConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 共通設定の作成
        api_response = api_instance.contracts_contract_id_common_configs_post(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 共通設定の作成
        api_response = api_instance.contracts_contract_id_common_configs_post(contract_id, post_common_config=post_common_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommonConfigsApi->contracts_contract_id_common_configs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **post_common_config** | [**PostCommonConfig**](PostCommonConfig.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください duplicated | name | 指定したnameを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

