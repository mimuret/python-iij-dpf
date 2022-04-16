# openapi_client.LogsZonesApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_logs_count_get**](LogsZonesApi.md#zones_zone_id_logs_count_get) | **GET** /zones/{ZoneId}/logs/count | ゾーン操作ログの件数取得
[**zones_zone_id_logs_get**](LogsZonesApi.md#zones_zone_id_logs_get) | **GET** /zones/{ZoneId}/logs | ゾーン操作ログの一覧取得


# **zones_zone_id_logs_count_get**
> GetCount zones_zone_id_logs_count_get(zone_id)

ゾーン操作ログの件数取得

ゾーンを操作したログの件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import logs_zones_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.zones_logs_type import ZonesLogsType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.zones_logs_status import ZonesLogsStatus
from openapi_client.model.zones_logs_operation import ZonesLogsOperation
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
    api_instance = logs_zones_api.LogsZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    start_date = "start_date_example" # str | 開始日 (optional)
    end_date = "end_date_example" # str | 終了日 (optional)
    time_zone = "+00:00" # str | タイムゾーン (optional) if omitted the server will use the default value of "+00:00"
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_log_type = ZonesLogsType("service") # ZonesLogsType |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operation = ZonesLogsOperation("updating_default_ttl") # ZonesLogsOperation |  (optional)
    keywords_target = KeywordsString([]) # KeywordsString |  (optional)
    keywords_detail = KeywordsString([]) # KeywordsString |  (optional)
    keywords_request_id = KeywordsString([]) # KeywordsString |  (optional)
    keywords_status = ZonesLogsStatus("start") # ZonesLogsStatus |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーン操作ログの件数取得
        api_response = api_instance.zones_zone_id_logs_count_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LogsZonesApi->zones_zone_id_logs_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーン操作ログの件数取得
        api_response = api_instance.zones_zone_id_logs_count_get(zone_id, type=type, start_date=start_date, end_date=end_date, time_zone=time_zone, keywords_full_text=keywords_full_text, keywords_log_type=keywords_log_type, keywords_operator=keywords_operator, keywords_operation=keywords_operation, keywords_target=keywords_target, keywords_detail=keywords_detail, keywords_request_id=keywords_request_id, keywords_status=keywords_status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LogsZonesApi->zones_zone_id_logs_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **start_date** | **str**| 開始日 | [optional]
 **end_date** | **str**| 終了日 | [optional]
 **time_zone** | **str**| タイムゾーン | [optional] if omitted the server will use the default value of "+00:00"
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_log_type** | **ZonesLogsType**|  | [optional]
 **keywords_operator** | **KeywordsString**|  | [optional]
 **keywords_operation** | **ZonesLogsOperation**|  | [optional]
 **keywords_target** | **KeywordsString**|  | [optional]
 **keywords_detail** | **KeywordsString**|  | [optional]
 **keywords_request_id** | **KeywordsString**|  | [optional]
 **keywords_status** | **ZonesLogsStatus**|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください invalid | start_date | 指定した日付を確認してください invalid | end_date | 指定した日付を確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_logs_get**
> GetZonesLogs zones_zone_id_logs_get(zone_id)

ゾーン操作ログの一覧取得

ゾーンを操作したログの一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import logs_zones_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.zones_logs_type import ZonesLogsType
from openapi_client.model.search_logs_offset import SearchLogsOffset
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.search_order import SearchOrder
from openapi_client.model.system_id import SystemId
from openapi_client.model.zones_logs_status import ZonesLogsStatus
from openapi_client.model.zones_logs_operation import ZonesLogsOperation
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_zones_logs import GetZonesLogs
from openapi_client.model.search_logs_limit import SearchLogsLimit
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = logs_zones_api.LogsZonesApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchLogsOffset(0) # SearchLogsOffset |  (optional)
    limit = SearchLogsLimit(100) # SearchLogsLimit |  (optional)
    start_date = "start_date_example" # str | 開始日 (optional)
    end_date = "end_date_example" # str | 終了日 (optional)
    time_zone = "+00:00" # str | タイムゾーン (optional) if omitted the server will use the default value of "+00:00"
    order = SearchOrder("ASC") # SearchOrder | ソート順 (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_log_type = ZonesLogsType("service") # ZonesLogsType |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operation = ZonesLogsOperation("updating_default_ttl") # ZonesLogsOperation |  (optional)
    keywords_target = KeywordsString([]) # KeywordsString |  (optional)
    keywords_detail = KeywordsString([]) # KeywordsString |  (optional)
    keywords_request_id = KeywordsString([]) # KeywordsString |  (optional)
    keywords_status = ZonesLogsStatus("start") # ZonesLogsStatus |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ゾーン操作ログの一覧取得
        api_response = api_instance.zones_zone_id_logs_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LogsZonesApi->zones_zone_id_logs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ゾーン操作ログの一覧取得
        api_response = api_instance.zones_zone_id_logs_get(zone_id, type=type, offset=offset, limit=limit, start_date=start_date, end_date=end_date, time_zone=time_zone, order=order, keywords_full_text=keywords_full_text, keywords_log_type=keywords_log_type, keywords_operator=keywords_operator, keywords_operation=keywords_operation, keywords_target=keywords_target, keywords_detail=keywords_detail, keywords_request_id=keywords_request_id, keywords_status=keywords_status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LogsZonesApi->zones_zone_id_logs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchLogsOffset**|  | [optional]
 **limit** | **SearchLogsLimit**|  | [optional]
 **start_date** | **str**| 開始日 | [optional]
 **end_date** | **str**| 終了日 | [optional]
 **time_zone** | **str**| タイムゾーン | [optional] if omitted the server will use the default value of "+00:00"
 **order** | **SearchOrder**| ソート順 | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_log_type** | **ZonesLogsType**|  | [optional]
 **keywords_operator** | **KeywordsString**|  | [optional]
 **keywords_operation** | **ZonesLogsOperation**|  | [optional]
 **keywords_target** | **KeywordsString**|  | [optional]
 **keywords_detail** | **KeywordsString**|  | [optional]
 **keywords_request_id** | **KeywordsString**|  | [optional]
 **keywords_status** | **ZonesLogsStatus**|  | [optional]

### Return type

[**GetZonesLogs**](GetZonesLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください invalid | start_date | 指定した日付を確認してください invalid | end_date | 指定した日付を確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

