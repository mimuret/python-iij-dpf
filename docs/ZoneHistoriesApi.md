# openapi_client.ZoneHistoriesApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_zone_histories_count_get**](ZoneHistoriesApi.md#zones_zone_id_zone_histories_count_get) | **GET** /zones/{ZoneId}/zone_histories/count | ゾーン反映履歴の件数取得
[**zones_zone_id_zone_histories_get**](ZoneHistoriesApi.md#zones_zone_id_zone_histories_get) | **GET** /zones/{ZoneId}/zone_histories | ゾーン反映履歴の一覧取得
[**zones_zone_id_zone_histories_zone_history_id_text_get**](ZoneHistoriesApi.md#zones_zone_id_zone_histories_zone_history_id_text_get) | **GET** /zones/{ZoneId}/zone_histories/{ZoneHistoryId}/text | ゾーン反映時のRFC1035形式のテキストの取得


# **zones_zone_id_zone_histories_count_get**
> GetCount zones_zone_id_zone_histories_count_get(zone_id)

ゾーン反映履歴の件数取得

ゾーン反映の履歴の件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zone_histories_api
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
    api_instance = zone_histories_api.ZoneHistoriesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーン反映履歴の件数取得
        api_response = api_instance.zones_zone_id_zone_histories_count_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneHistoriesApi->zones_zone_id_zone_histories_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーン反映履歴の件数取得
        api_response = api_instance.zones_zone_id_zone_histories_count_get(zone_id, type=type, keywords_full_text=keywords_full_text, keywords_description=keywords_description, keywords_operator=keywords_operator)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneHistoriesApi->zones_zone_id_zone_histories_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_operator** | **KeywordsString**|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_zone_histories_get**
> GetZoneHistories zones_zone_id_zone_histories_get(zone_id)

ゾーン反映履歴の一覧取得

ゾーン反映の履歴の一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zone_histories_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.search_order import SearchOrder
from openapi_client.model.system_id import SystemId
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.get_zone_histories import GetZoneHistories
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
    api_instance = zone_histories_api.ZoneHistoriesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)
    order = SearchOrder("ASC") # SearchOrder | ソート順 (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーン反映履歴の一覧取得
        api_response = api_instance.zones_zone_id_zone_histories_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneHistoriesApi->zones_zone_id_zone_histories_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーン反映履歴の一覧取得
        api_response = api_instance.zones_zone_id_zone_histories_get(zone_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_description=keywords_description, keywords_operator=keywords_operator, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneHistoriesApi->zones_zone_id_zone_histories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_operator** | **KeywordsString**|  | [optional]
 **order** | **SearchOrder**| ソート順 | [optional]

### Return type

[**GetZoneHistories**](GetZoneHistories.md)

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

# **zones_zone_id_zone_histories_zone_history_id_text_get**
> GetZoneHistoriesText zones_zone_id_zone_histories_zone_history_id_text_get(zone_id, zone_history_id)

ゾーン反映時のRFC1035形式のテキストの取得

ゾーン反映の履歴をRFC1035形式のテキストファイルで取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import zone_histories_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.get_zone_histories_text import GetZoneHistoriesText
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
    api_instance = zone_histories_api.ZoneHistoriesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    zone_history_id = Id(1) # Id | ID

    # example passing only required values which don't have defaults set
    try:
        # ゾーン反映時のRFC1035形式のテキストの取得
        api_response = api_instance.zones_zone_id_zone_histories_zone_history_id_text_get(zone_id, zone_history_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZoneHistoriesApi->zones_zone_id_zone_histories_zone_history_id_text_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **zone_history_id** | **Id**| ID |

### Return type

[**GetZoneHistoriesText**](GetZoneHistoriesText.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | zone_history | 指定したZoneHistoryIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

