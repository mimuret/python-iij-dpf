# openapi_client.TsigsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_id_tsigs_count_get**](TsigsApi.md#contracts_contract_id_tsigs_count_get) | **GET** /contracts/{ContractId}/tsigs/count | TSIG鍵の件数取得
[**contracts_contract_id_tsigs_get**](TsigsApi.md#contracts_contract_id_tsigs_get) | **GET** /contracts/{ContractId}/tsigs | TSIG鍵の一覧取得
[**contracts_contract_id_tsigs_post**](TsigsApi.md#contracts_contract_id_tsigs_post) | **POST** /contracts/{ContractId}/tsigs | TSIG鍵の作成
[**contracts_contract_id_tsigs_tsig_id_common_configs_count_get**](TsigsApi.md#contracts_contract_id_tsigs_tsig_id_common_configs_count_get) | **GET** /contracts/{ContractId}/tsigs/{TsigId}/common_configs/count | TSIG鍵を利用している共通設定の件数取得
[**contracts_contract_id_tsigs_tsig_id_common_configs_get**](TsigsApi.md#contracts_contract_id_tsigs_tsig_id_common_configs_get) | **GET** /contracts/{ContractId}/tsigs/{TsigId}/common_configs | TSIG鍵を利用している共通設定の一覧取得
[**contracts_contract_id_tsigs_tsig_id_delete**](TsigsApi.md#contracts_contract_id_tsigs_tsig_id_delete) | **DELETE** /contracts/{ContractId}/tsigs/{TsigId} | TSIG鍵の削除
[**contracts_contract_id_tsigs_tsig_id_get**](TsigsApi.md#contracts_contract_id_tsigs_tsig_id_get) | **GET** /contracts/{ContractId}/tsigs/{TsigId} | TSIG鍵の取得
[**contracts_contract_id_tsigs_tsig_id_patch**](TsigsApi.md#contracts_contract_id_tsigs_tsig_id_patch) | **PATCH** /contracts/{ContractId}/tsigs/{TsigId} | TSIG鍵の更新


# **contracts_contract_id_tsigs_count_get**
> GetCount contracts_contract_id_tsigs_count_get(contract_id)

TSIG鍵の件数取得

TSIG鍵の件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵の件数取得
        api_response = api_instance.contracts_contract_id_tsigs_count_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TSIG鍵の件数取得
        api_response = api_instance.contracts_contract_id_tsigs_count_get(contract_id, type=type, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_count_get: %s\n" % e)
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

# **contracts_contract_id_tsigs_get**
> GetTsigs contracts_contract_id_tsigs_get(contract_id)

TSIG鍵の一覧取得

TSIG鍵情報の一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.get_tsigs import GetTsigs
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵の一覧取得
        api_response = api_instance.contracts_contract_id_tsigs_get(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TSIG鍵の一覧取得
        api_response = api_instance.contracts_contract_id_tsigs_get(contract_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_get: %s\n" % e)
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

[**GetTsigs**](GetTsigs.md)

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

# **contracts_contract_id_tsigs_post**
> AsyncResponse contracts_contract_id_tsigs_post(contract_id)

TSIG鍵の作成

新しくTSIG鍵を作成します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
from openapi_client.model.post_tsig import PostTsig
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    post_tsig = PostTsig(
        name=TsigsPostName("name_example"),
        description=Description(""),
    ) # PostTsig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵の作成
        api_response = api_instance.contracts_contract_id_tsigs_post(contract_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TSIG鍵の作成
        api_response = api_instance.contracts_contract_id_tsigs_post(contract_id, post_tsig=post_tsig)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **post_tsig** | [**PostTsig**](PostTsig.md)|  | [optional]

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

# **contracts_contract_id_tsigs_tsig_id_common_configs_count_get**
> GetCount contracts_contract_id_tsigs_tsig_id_common_configs_count_get(contract_id, tsig_id)

TSIG鍵を利用している共通設定の件数取得

指定したTSIG鍵を使用している共通設定の件数を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.bad_request import BadRequest
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    tsig_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵を利用している共通設定の件数取得
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_common_configs_count_get(contract_id, tsig_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_common_configs_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **tsig_id** | **Id**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTsigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_tsigs_tsig_id_common_configs_get**
> GetTsigsCommonConfigs contracts_contract_id_tsigs_tsig_id_common_configs_get(contract_id, tsig_id)

TSIG鍵を利用している共通設定の一覧取得

指定したTSIG鍵を使用している共通設定の一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_tsigs_common_configs import GetTsigsCommonConfigs
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    tsig_id = Id(1) # Id | ID
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵を利用している共通設定の一覧取得
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_common_configs_get(contract_id, tsig_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_common_configs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TSIG鍵を利用している共通設定の一覧取得
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_common_configs_get(contract_id, tsig_id, offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_common_configs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **tsig_id** | **Id**| ID |
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]

### Return type

[**GetTsigsCommonConfigs**](GetTsigsCommonConfigs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTsigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_tsigs_tsig_id_delete**
> AsyncResponse contracts_contract_id_tsigs_tsig_id_delete(contract_id, tsig_id)

TSIG鍵の削除

指定したTsigIdのTSIG鍵を削除します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    tsig_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵の削除
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_delete(contract_id, tsig_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **tsig_id** | **Id**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTsigIdを確認してください forbidden | tsig | 参照元が存在しているため削除できません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_tsigs_tsig_id_get**
> GetTsig contracts_contract_id_tsigs_tsig_id_get(contract_id, tsig_id)

TSIG鍵の取得

指定したTsigIdのTSIG鍵を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
from openapi_client.model.get_tsig import GetTsig
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    tsig_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵の取得
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_get(contract_id, tsig_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **tsig_id** | **Id**| ID |

### Return type

[**GetTsig**](GetTsig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTsigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_contract_id_tsigs_tsig_id_patch**
> AsyncResponse contracts_contract_id_tsigs_tsig_id_patch(contract_id, tsig_id)

TSIG鍵の更新

指定したTsigIdのTSIG鍵を更新します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import tsigs_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.patch_tsig import PatchTsig
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
    api_instance = tsigs_api.TsigsApi(api_client)
    contract_id = SystemId("ContractId_example") # SystemId | ID
    tsig_id = Id(1) # Id | ID
    patch_tsig = PatchTsig(
        description=Description(""),
    ) # PatchTsig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # TSIG鍵の更新
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_patch(contract_id, tsig_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TSIG鍵の更新
        api_response = api_instance.contracts_contract_id_tsigs_tsig_id_patch(contract_id, tsig_id, patch_tsig=patch_tsig)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TsigsApi->contracts_contract_id_tsigs_tsig_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **SystemId**| ID |
 **tsig_id** | **Id**| ID |
 **patch_tsig** | [**PatchTsig**](PatchTsig.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | contract | 指定したContractIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | tsig | 指定したTsigIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

