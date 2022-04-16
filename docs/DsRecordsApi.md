# openapi_client.DsRecordsApi

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_ds_records_get**](DsRecordsApi.md#zones_zone_id_ds_records_get) | **GET** /zones/{ZoneId}/ds_records | DSレコードの一覧取得


# **zones_zone_id_ds_records_get**
> GetDsRecords zones_zone_id_ds_records_get(zone_id)

DSレコードの一覧取得

上位のネームサーバに登録が必要なDSレコードを取得できます。  ### Authorizations dpf_read 

### Example


```python
import time
import openapi_client
from openapi_client.api import ds_records_api
from openapi_client.model.get_ds_records import GetDsRecords
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
    api_instance = ds_records_api.DsRecordsApi(api_client)
    zone_id = SystemId("ZoneId_example") # SystemId | ID

    # example passing only required values which don't have defaults set
    try:
        # DSレコードの一覧取得
        api_response = api_instance.zones_zone_id_ds_records_get(zone_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DsRecordsApi->zones_zone_id_ds_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **SystemId**| ID |

### Return type

[**GetDsRecords**](GetDsRecords.md)

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

