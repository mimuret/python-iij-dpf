# openapi_client.DelegationsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delegations_count_get**](DelegationsApi.md#delegations_count_get) | **GET** /delegations/count | ネームサーバ申請候補の件数取得
[**delegations_get**](DelegationsApi.md#delegations_get) | **GET** /delegations | ネームサーバ申請候補の一覧取得
[**delegations_post**](DelegationsApi.md#delegations_post) | **POST** /delegations | ネームサーバ申請


# **delegations_count_get**
> GetCount delegations_count_get()

ネームサーバ申請候補の件数取得

ネームサーバとして申請可能なゾーンの候補の件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import delegations_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.delegations_requested import DelegationsRequested
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.zones_favorite import ZonesFavorite
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
    api_instance = delegations_api.DelegationsApi(api_client)
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_service_code = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_network = KeywordsString([]) # KeywordsString |  (optional)
    keywords_favorite = ZonesFavorite(1) # ZonesFavorite |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_requested = DelegationsRequested(0) # DelegationsRequested |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ネームサーバ申請候補の件数取得
        api_response = api_instance.delegations_count_get(type=type, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_name=keywords_name, keywords_network=keywords_network, keywords_favorite=keywords_favorite, keywords_description=keywords_description, keywords_requested=keywords_requested)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DelegationsApi->delegations_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_service_code** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_network** | **KeywordsString**|  | [optional]
 **keywords_favorite** | **ZonesFavorite**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_requested** | **DelegationsRequested**|  | [optional]

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

# **delegations_get**
> GetDelegations delegations_get()

ネームサーバ申請候補の一覧取得

ネームサーバとして申請可能なゾーンの候補の一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import delegations_api
from openapi_client.model.get_delegations import GetDelegations
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.delegations_requested import DelegationsRequested
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.zones_favorite import ZonesFavorite
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
    api_instance = delegations_api.DelegationsApi(api_client)
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_service_code = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_network = KeywordsString([]) # KeywordsString |  (optional)
    keywords_favorite = ZonesFavorite(1) # ZonesFavorite |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_requested = DelegationsRequested(0) # DelegationsRequested |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ネームサーバ申請候補の一覧取得
        api_response = api_instance.delegations_get(type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_service_code=keywords_service_code, keywords_name=keywords_name, keywords_network=keywords_network, keywords_favorite=keywords_favorite, keywords_description=keywords_description, keywords_requested=keywords_requested)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DelegationsApi->delegations_get: %s\n" % e)
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
 **keywords_favorite** | **ZonesFavorite**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_requested** | **DelegationsRequested**|  | [optional]

### Return type

[**GetDelegations**](GetDelegations.md)

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

# **delegations_post**
> AsyncResponse delegations_post()

ネームサーバ申請

指定したゾーンを申請します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import delegations_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.post_delegations import PostDelegations
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
    api_instance = delegations_api.DelegationsApi(api_client)
    post_delegations = PostDelegations(None) # PostDelegations |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ネームサーバ申請
        api_response = api_instance.delegations_post(post_delegations=post_delegations)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DelegationsApi->delegations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_delegations** | [**PostDelegations**](PostDelegations.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zones | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

