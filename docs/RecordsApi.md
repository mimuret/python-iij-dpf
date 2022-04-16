# openapi_client.RecordsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_records_count_get**](RecordsApi.md#zones_zone_id_records_count_get) | **GET** /zones/{ZoneId}/records/count | レコードの件数取得
[**zones_zone_id_records_currents_count_get**](RecordsApi.md#zones_zone_id_records_currents_count_get) | **GET** /zones/{ZoneId}/records/currents/count | DNS反映済レコードの件数取得
[**zones_zone_id_records_currents_get**](RecordsApi.md#zones_zone_id_records_currents_get) | **GET** /zones/{ZoneId}/records/currents | DNS反映済レコードの一覧取得
[**zones_zone_id_records_diffs_count_get**](RecordsApi.md#zones_zone_id_records_diffs_count_get) | **GET** /zones/{ZoneId}/records/diffs/count | レコードの編集差分の件数取得
[**zones_zone_id_records_diffs_get**](RecordsApi.md#zones_zone_id_records_diffs_get) | **GET** /zones/{ZoneId}/records/diffs | レコードの編集差分の一覧取得
[**zones_zone_id_records_get**](RecordsApi.md#zones_zone_id_records_get) | **GET** /zones/{ZoneId}/records | レコードの一覧取得
[**zones_zone_id_records_post**](RecordsApi.md#zones_zone_id_records_post) | **POST** /zones/{ZoneId}/records | レコードの作成
[**zones_zone_id_records_record_id_changes_delete**](RecordsApi.md#zones_zone_id_records_record_id_changes_delete) | **DELETE** /zones/{ZoneId}/records/{RecordId}/changes | 編集中レコードの取消
[**zones_zone_id_records_record_id_delete**](RecordsApi.md#zones_zone_id_records_record_id_delete) | **DELETE** /zones/{ZoneId}/records/{RecordId} | レコードの削除
[**zones_zone_id_records_record_id_get**](RecordsApi.md#zones_zone_id_records_record_id_get) | **GET** /zones/{ZoneId}/records/{RecordId} | レコードの取得
[**zones_zone_id_records_record_id_patch**](RecordsApi.md#zones_zone_id_records_record_id_patch) | **PATCH** /zones/{ZoneId}/records/{RecordId} | レコードの更新


# **zones_zone_id_records_count_get**
> GetCount zones_zone_id_records_count_get(zone_id)

レコードの件数取得

レコード情報の件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.records_rrtype import RecordsRrtype
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_count import GetCount
from openapi_client.model.records_ttl import RecordsTtl
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_ttl = RecordsTtl(1) # RecordsTtl |  (optional)
    keywords_rrtype = RecordsRrtype("A") # RecordsRrtype |  (optional)
    keywords_rdata = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # レコードの件数取得
        api_response = api_instance.zones_zone_id_records_count_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # レコードの件数取得
        api_response = api_instance.zones_zone_id_records_count_get(zone_id, type=type, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_ttl=keywords_ttl, keywords_rrtype=keywords_rrtype, keywords_rdata=keywords_rdata, keywords_description=keywords_description, keywords_operator=keywords_operator)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_ttl** | **RecordsTtl**|  | [optional]
 **keywords_rrtype** | **RecordsRrtype**|  | [optional]
 **keywords_rdata** | **KeywordsString**|  | [optional]
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

# **zones_zone_id_records_currents_count_get**
> GetCount zones_zone_id_records_currents_count_get(zone_id)

DNS反映済レコードの件数取得

現在DNSに登録されているレコードの件数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.records_rrtype import RecordsRrtype
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_count import GetCount
from openapi_client.model.records_ttl import RecordsTtl
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_ttl = RecordsTtl(1) # RecordsTtl |  (optional)
    keywords_rrtype = RecordsRrtype("A") # RecordsRrtype |  (optional)
    keywords_rdata = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DNS反映済レコードの件数取得
        api_response = api_instance.zones_zone_id_records_currents_count_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_currents_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DNS反映済レコードの件数取得
        api_response = api_instance.zones_zone_id_records_currents_count_get(zone_id, type=type, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_ttl=keywords_ttl, keywords_rrtype=keywords_rrtype, keywords_rdata=keywords_rdata, keywords_description=keywords_description, keywords_operator=keywords_operator)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_currents_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_ttl** | **RecordsTtl**|  | [optional]
 **keywords_rrtype** | **RecordsRrtype**|  | [optional]
 **keywords_rdata** | **KeywordsString**|  | [optional]
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

# **zones_zone_id_records_currents_get**
> GetRecords zones_zone_id_records_currents_get(zone_id)

DNS反映済レコードの一覧取得

現在DNSに登録されているレコードの一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.records_rrtype import RecordsRrtype
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.search_limit import SearchLimit
from openapi_client.model.records_ttl import RecordsTtl
from openapi_client.model.get_records import GetRecords
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_ttl = RecordsTtl(1) # RecordsTtl |  (optional)
    keywords_rrtype = RecordsRrtype("A") # RecordsRrtype |  (optional)
    keywords_rdata = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DNS反映済レコードの一覧取得
        api_response = api_instance.zones_zone_id_records_currents_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_currents_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DNS反映済レコードの一覧取得
        api_response = api_instance.zones_zone_id_records_currents_get(zone_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_ttl=keywords_ttl, keywords_rrtype=keywords_rrtype, keywords_rdata=keywords_rdata, keywords_description=keywords_description, keywords_operator=keywords_operator)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_currents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_ttl** | **RecordsTtl**|  | [optional]
 **keywords_rrtype** | **RecordsRrtype**|  | [optional]
 **keywords_rdata** | **KeywordsString**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_operator** | **KeywordsString**|  | [optional]

### Return type

[**GetRecords**](GetRecords.md)

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

# **zones_zone_id_records_diffs_count_get**
> GetCount zones_zone_id_records_diffs_count_get(zone_id)

レコードの編集差分の件数取得

現在DNSに登録されているレコードと反映予定のレコードの差分数を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.records_rrtype import RecordsRrtype
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_count import GetCount
from openapi_client.model.records_ttl import RecordsTtl
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_ttl = RecordsTtl(1) # RecordsTtl |  (optional)
    keywords_rrtype = RecordsRrtype("A") # RecordsRrtype |  (optional)
    keywords_rdata = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # レコードの編集差分の件数取得
        api_response = api_instance.zones_zone_id_records_diffs_count_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_diffs_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # レコードの編集差分の件数取得
        api_response = api_instance.zones_zone_id_records_diffs_count_get(zone_id, type=type, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_ttl=keywords_ttl, keywords_rrtype=keywords_rrtype, keywords_rdata=keywords_rdata, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_diffs_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_ttl** | **RecordsTtl**|  | [optional]
 **keywords_rrtype** | **RecordsRrtype**|  | [optional]
 **keywords_rdata** | **KeywordsString**|  | [optional]
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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_records_diffs_get**
> GetRecordsDiffs zones_zone_id_records_diffs_get(zone_id)

レコードの編集差分の一覧取得

現在DNSに登録されているレコードと反映予定のレコードの差分一覧を取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.get_records_diffs import GetRecordsDiffs
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.records_rrtype import RecordsRrtype
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.search_limit import SearchLimit
from openapi_client.model.records_ttl import RecordsTtl
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_ttl = RecordsTtl(1) # RecordsTtl |  (optional)
    keywords_rrtype = RecordsRrtype("A") # RecordsRrtype |  (optional)
    keywords_rdata = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # レコードの編集差分の一覧取得
        api_response = api_instance.zones_zone_id_records_diffs_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_diffs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # レコードの編集差分の一覧取得
        api_response = api_instance.zones_zone_id_records_diffs_get(zone_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_ttl=keywords_ttl, keywords_rrtype=keywords_rrtype, keywords_rdata=keywords_rdata, keywords_description=keywords_description)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_diffs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_ttl** | **RecordsTtl**|  | [optional]
 **keywords_rrtype** | **RecordsRrtype**|  | [optional]
 **keywords_rdata** | **KeywordsString**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]

### Return type

[**GetRecordsDiffs**](GetRecordsDiffs.md)

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

# **zones_zone_id_records_get**
> GetRecords zones_zone_id_records_get(zone_id)

レコードの一覧取得

レコード情報の一覧を取得します。\\ \"_keywords\" から始まるパラメータは、合計で30個まで指定可能です。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.search_type import SearchType
from openapi_client.model.keywords_string import KeywordsString
from openapi_client.model.system_id import SystemId
from openapi_client.model.records_rrtype import RecordsRrtype
from openapi_client.model.search_offset import SearchOffset
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.search_limit import SearchLimit
from openapi_client.model.records_ttl import RecordsTtl
from openapi_client.model.get_records import GetRecords
from pprint import pprint
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    type = SearchType("AND") # SearchType |  (optional)
    offset = SearchOffset(0) # SearchOffset |  (optional)
    limit = SearchLimit(100) # SearchLimit |  (optional)
    keywords_full_text = KeywordsString([]) # KeywordsString |  (optional)
    keywords_name = KeywordsString([]) # KeywordsString |  (optional)
    keywords_ttl = RecordsTtl(1) # RecordsTtl |  (optional)
    keywords_rrtype = RecordsRrtype("A") # RecordsRrtype |  (optional)
    keywords_rdata = KeywordsString([]) # KeywordsString |  (optional)
    keywords_description = KeywordsString([]) # KeywordsString |  (optional)
    keywords_operator = KeywordsString([]) # KeywordsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # レコードの一覧取得
        api_response = api_instance.zones_zone_id_records_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # レコードの一覧取得
        api_response = api_instance.zones_zone_id_records_get(zone_id, type=type, offset=offset, limit=limit, keywords_full_text=keywords_full_text, keywords_name=keywords_name, keywords_ttl=keywords_ttl, keywords_rrtype=keywords_rrtype, keywords_rdata=keywords_rdata, keywords_description=keywords_description, keywords_operator=keywords_operator)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **type** | **SearchType**|  | [optional]
 **offset** | **SearchOffset**|  | [optional]
 **limit** | **SearchLimit**|  | [optional]
 **keywords_full_text** | **KeywordsString**|  | [optional]
 **keywords_name** | **KeywordsString**|  | [optional]
 **keywords_ttl** | **RecordsTtl**|  | [optional]
 **keywords_rrtype** | **RecordsRrtype**|  | [optional]
 **keywords_rdata** | **KeywordsString**|  | [optional]
 **keywords_description** | **KeywordsString**|  | [optional]
 **keywords_operator** | **KeywordsString**|  | [optional]

### Return type

[**GetRecords**](GetRecords.md)

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

# **zones_zone_id_records_post**
> AsyncResponse zones_zone_id_records_post(zone_id)

レコードの作成

新しくレコードを作成します。\\ **[編集中レコードのゾーン反映](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch)**を実行するまでは権威サーバには反映されません。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.post_record import PostRecord
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
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    post_record = PostRecord(
        name=RecordsName("name_example"),
        ttl=RecordsTtl(1),
        rrtype="A",
        rdata=RecordsRdata([
            {
                value="value_example",
            },
        ]),
        description=Description(""),
    ) # PostRecord |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # レコードの作成
        api_response = api_instance.zones_zone_id_records_post(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # レコードの作成
        api_response = api_instance.zones_zone_id_records_post(zone_id, post_record=post_record)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **post_record** | [**PostRecord**](PostRecord.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください forbidden | zone | ゾーンプロキシの設定が有効のため操作できません invalid | schema | 指定したパラメータを確認してください invalid | record | レコードとして不正な形式です duplicated | record | 同一nameおよびrrtypeのレコードがすでに作成されています invalid | name | 指定したnameを確認してください cname_and_other_mixed | name | 指定したnameがCNAMEと同一です corresponding_ns_not_found | name | 指定したDSレコードのnameに対応するNSレコードが存在していません invalid_quotes | rdata | TXTレコードのrdataは「\&quot;」で囲むようにしてください invalid | rdata | 指定したrdataを確認してください reference_not_found | rdata | 参照先が存在しません reference_alias | rdata | 指定した参照先がCNAMEです multiple_rdata_found | rdata | 指定したレコードタイプでは複数のrdataを指定することはできません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_records_record_id_changes_delete**
> AsyncResponse zones_zone_id_records_record_id_changes_delete(zone_id, record_id)

編集中レコードの取消

指定したRecordIdのレコードの操作を取消します。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
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
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    record_id = SystemId("RecordId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # 編集中レコードの取消
        api_response = api_instance.zones_zone_id_records_record_id_changes_delete(zone_id, record_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_record_id_changes_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **record_id** | **SystemId**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください forbidden | zone | ゾーンプロキシの設定が有効のため操作できません invalid | schema | 指定したパラメータを確認してください not_found | record | 指定したRecordIdを確認してください forbidden | record | レコードの状態を確認してください duplicated | record | 同一nameおよびrrtypeのレコードがすでに存在しています cname_and_other_mixed | name | 指定したNameがCNAMEと同一のため操作できません corresponding_ns_not_found | name | 指定したDSレコードのnameに対応するNSレコードが存在していません invalid | rrtype | 指定したrrtypeを確認してください reference_not_found | rdata | 参照先が存在しないレコードが存在するため取り消しできません reference_alias | rdata | 指定した参照先がCNAMEです  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_records_record_id_delete**
> AsyncResponse zones_zone_id_records_record_id_delete(zone_id, record_id)

レコードの削除

指定したRecordIdのレコードを削除します。\\ **[編集中レコードのゾーン反映](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch)**を実行するまでは権威サーバには反映されません。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
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
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    record_id = SystemId("RecordId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # レコードの削除
        api_response = api_instance.zones_zone_id_records_record_id_delete(zone_id, record_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_record_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **record_id** | **SystemId**| ID |

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください forbidden | zone | ゾーンプロキシの設定が有効のため操作できません invalid | schema | 指定したパラメータを確認してください not_found | record | 指定したRecordIdを確認してください forbidden | record | レコードの状態を確認してください soa_not_found | record | SOAレコードの削除はできません apex_ns_not_found | record | Zone APEXのNSレコードのため削除はできません corresponding_ns_not_found | name | 同一nameのDSレコードが存在するためNSレコードの削除はできません reference_not_found | rdata | 参照先が存在しないため削除できません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_records_record_id_get**
> GetRecord zones_zone_id_records_record_id_get(zone_id, record_id)

レコードの取得

指定したRecordIdのレコードを取得します。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.system_id import SystemId
from openapi_client.model.get_record import GetRecord
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
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    record_id = SystemId("RecordId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # レコードの取得
        api_response = api_instance.zones_zone_id_records_record_id_get(zone_id, record_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_record_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **record_id** | **SystemId**| ID |

### Return type

[**GetRecord**](GetRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください invalid | schema | 指定したパラメータを確認してください not_found | record | 指定したRecordIdを確認してください  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_records_record_id_patch**
> AsyncResponse zones_zone_id_records_record_id_patch(zone_id, record_id)

レコードの更新

指定したRecordIdのレコードを更新します。\\ **[編集中レコードのゾーン反映](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch)**を実行するまでは権威サーバには反映されません。  ### Authorizations dpf_write 

### Example


```python
import time
import openapi_client
from openapi_client.api import records_api
from openapi_client.model.patch_record import PatchRecord
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
    api_instance = records_api.RecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID
    record_id = SystemId("RecordId_example") # SystemId | ID
    patch_record = PatchRecord(
        ttl=RecordsTtl(1),
        rdata=RecordsRdata([
            {
                value="value_example",
            },
        ]),
        description=Description(""),
    ) # PatchRecord |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # レコードの更新
        api_response = api_instance.zones_zone_id_records_record_id_patch(zone_id, record_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_record_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # レコードの更新
        api_response = api_instance.zones_zone_id_records_record_id_patch(zone_id, record_id, patch_record=patch_record)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->zones_zone_id_records_record_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |
 **record_id** | **SystemId**| ID |
 **patch_record** | [**PatchRecord**](PatchRecord.md)|  | [optional]

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
**400** | Bad Request  &lt;details close&gt; &lt;summary&gt;ErrorDetails&lt;/summary&gt;  code | attribute | 対処方法 -----|-----------|---------- not_found | zone | 指定したZoneIdを確認してください forbidden | zone | ゾーンプロキシの設定が有効のため操作できません invalid | schema | 指定したパラメータを確認してください not_found | record | 指定したRecordIdを確認してください forbidden | record | レコードの状態を確認してください invalid | record | レコードとして不正な形式です invalid_quotes | rdata | TXTレコードのrdataは「\&quot;」で囲むようにしてください invalid | rdata | 指定したrdataを確認してください reference_not_found | rdata | 参照先が存在しません reference_alias | rdata | 指定した参照先がCNAMEです multiple_rdata_found | rdata | 指定したレコードタイプでは複数のrdataを指定することはできません  &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

