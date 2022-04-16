# openapi-client
# はじめに

## DPF-APIについて
IIJ DNSプラットフォームサービスでは、DNSレコードやゾーン情報などを、\\
お客様が用意したプログラムから自動的に操作するためのAPI機能を提供しています。\\
以降、IIJ DNSプラットフォームサービスを「DPF」、DPFが提供するAPIを「DPF-API」あるいは単に「API」と表記します。\\
DPF-APIの利用には、DPFの契約とIIJ IDサービスの契約が必要となります。

本リファレンスマニュアルは**[OpenAPI](https://www.openapis.org/)**に準拠しています。

## サポート範囲
DPF-APIを呼び出すためのプログラム、及びそのプログラムを稼働させるためのサーバは、お客様にてご用意ください。\\
お客様にご用意いただくプログラムの開発、利用、動作についてのお問い合わせは承ることができません。

以下の事項についてのお問い合わせは、弊社**[サポートセンター](https://help.iij.ad.jp/)**にて承ります。
- DPF-APIの挙動が本リファレンスマニュアルと異なる場合
- DPF-APIがシステムエラーを応答した場合

## 参考資料
- IIJ DNSプラットフォームサービス オンラインマニュアル
  - [https://manual.iij.jp/dpf/help/](https://manual.iij.jp/dpf/help/)

- IIJ IDサービス オンラインマニュアル
  - [https://manual.iij.jp/iid/admin-help/](https://manual.iij.jp/iid/admin-help/)

# 利用方法
DPF-APIは、URLとHTTPリクエストヘッダ、HTTPリクエストボディでパラメータを指定して利用します。\\
また、IIJ IDサービスのアクセストークンと管理対象の権限設定が必要です。

## リクエスト仕様

項目 | 規格
-----|-----
プロトコル | HTTP/1.1、HTTP/2（https）
HTTPメソッド | GET、PATCH、POST、DELETE
フォーマット | JSON
文字コード | UTF-8
タイムアウト | 300秒

- httpでのリクエストは受け付けません。必ずhttpsを使用してください。
- DPF-APIを呼び出すプログラムは、リクエスト先が正当なものであることを確認するため、SSL証明書を検証することを推奨します。
- 短期間に極めて多数のリクエストが行われた場合、サービスの健全性を保つためにリクエストを制限する場合があります。

### アクセストークン
APIリクエストの際にIIJ IDサービスによって発行されたアクセストークンをAuthorizationヘッダに指定する必要があります。\\
各APIにより必要となるアクセス権の範囲（許可するスコープ）が異なるのでご注意ください。

アクセストークン作成時に指定できる「許可するスコープ」は以下のとおりです。

許可するスコープ | 実行できるAPI
-----------------|------------
dpf_read | 参照系API
dpf_write | 更新系、及び参照系API
dpf_contract | 契約系API

発行済のアクセストークンは、**[IIJ IDサービス](https://www.auth.iij.jp/console/)**の「アクセストークンの管理」より確認できます。\\
DPF-APIを利用する場合は「利用するリソースサーバ」の設定で「IIJ DNSサービスAPI」を選択してください。\\
アクセストークン管理方法のマニュアルは**[こちら](https://manual.iij.jp/iid/admin-help/9054382.html)**を参照してください。

### 管理対象の権限設定
DPFでは、管理対象となるサービスやゾーン単位での参照、編集権限を細かく設定できます。\\
アクセストークンの許可するスコープが適切であっても、管理対象の権限が付与されていない場合はAPIを実行できません。\\
管理対象の権限設定のマニュアルは**[こちら](https://manual.iij.jp/dpf/help/19004706.html#IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B-IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%B8%E7%AE%A1%E7%90%86%E6%A8%A9%E9%99%90%E3%82%92%E4%BB%98%E4%B8%8E%E3%81%99%E3%82%8B)**を参照してください。

## HTTPリクエスト

### 例
```
<HTTPメソッド> /dpf/<version>/<APIパス> HTTP/1.1
Host: api.dns-platform.jp
Authorization: Bearer <access_token>
Content-Type: application/json; charset=UTF-8

<HTTPリクエストボディ: JSON形式のAPI固有のパラメータ>
```

### リクエストパラメータ
DPF-APIで指定するパラメータは以下のとおりです。\\
リクエストパラメータに同一のキーが含まれる場合の動作は保証されません。

共通 | 指定箇所 | パラメータ | 意味
-----|----------|------------|-----
共通 | HTTPメソッド | HTTPメソッド | HTTPメソッド（値：GET、PATCH、POST、DELETE）
共通 | URL | version | DPF-APIバージョン（値：v1）
個別 | URL | APIパス | API名称やAPI個別のパラメータの組み合わせ（参照：**[API一覧](#section/API)**）
共通 | HTTPヘッダー | access_token | IIJ IDアクセストークン（参照：**[IIJ IDサービス](https://www.auth.iij.jp/console/)**）
個別 | HTTPボディ | APIごとに異なる | JSON形式のパラメータ（参照：**[API一覧](#section/API)**）

## HTTPレスポンス

### 成功レスポンス
APIごとにレスポンスが異なりますので、**[該当のAPI](#section/API)**を参照してください。

### エラーレスポンス
HTTPステータスコード、及びレスポンスボディによってクライアントプログラムにエラーを通知します。

#### 例：アクセストークンが誤っている
```
{
  \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",
  \"error_type\": \"ParameterError\",
  \"error_message\": \"There are invalid parameters.\",
  \"error_details\": [
    {
      \"code\": \"invalid\",
      \"attribute\": \"access_token\"
    }
  ]
}
```

#### エラーコード一覧
HTTP Status Code | error_type | error_message | code | attribute | 説明 | 対処方法
-----------------|------------|---------------|------|-----------|------|---------
400 | ParameterError | There are invalid parameters. | invalid | access_token | 指定したアクセストークンに誤りがあります | アクセストークンを確認してください
400 | ParameterError | JSON parse error occurred. | - | - | パラメータとして不正なJSON文字列が指定されました | リクエストのパラメータを確認してください
400 | ParameterError | There are invalid parameters. | （API個別） | （API個別） | 不正なパラメータが指定されました | 各APIのエラーコードを確認してください
404 | NotFound | Specified resource not found. | - | - | アクセスURLが正しくありません <br> 存在しないAPIが指定されました <br> 指定された以外のHTTPメソッドが指定されました | 左記の内容を確認してください
429 | TooManyRequests | Too many requests. | - | - | 大量のAPIリクエストが送信されました | 単位時間当たりのAPIリクエスト数を確認してください
500 | SystemError | System error occurred. | - | - | システム障害が発生しました | **[サポートセンター](https://help.iij.ad.jp/)**へお問い合わせください
504 | GatewayTimeout | Gateway timeout. | - | - | リクエストがタイムアウトしました | しばらく待ってから再度リクエストしてください

## 非同期リクエスト

DPF-APIにおけるGET以外のAPIは全て非同期APIです。\\
非同期APIはリクエストを受け付けると即座にレスポンスを返却しますが、\\
リクエストに対する実際の処理は非同期で行われます。

非同期リクエストの受け付けに成功した場合のHTTPステータスコードは202で、\\
返却されたレスポンスボディには、処理進捗を確認するためのURL（jobs_url）が含まれます。\\
このjobs_urlに対してGETリクエストをすることで進捗状況を確認できます。

進捗状況を確認した際、非同期処理が正常に終了していた場合は、\\
返却されたレスポンスボディには、対象リソースを取得するためのURL（resources_url）が含まれます。\\
このresources_urlに対してGETリクエストをすることで実行結果を確認できます。

### 例
#### 非同期リクエストのレスポンス
```
HTTP/1.1 202 Accepted
Date: Mon, 26 Mar 20XX hh:mm:dd GMT
Content-Type: application/json; charset=utf-8
〜 略 〜

{
  \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",
  \"jobs_url\": \"https://api.dns-platform.jp/dpf/<version>/jobs/<request_id>\"
}
```

#### GETリクエスト
```
GET /dpf/<version>/jobs/<request_id> HTTP/1.1
Host: api.dns-platform.jp
Authorization: Bearer <access_token>
Content-Type: application/json; charset=UTF-8

{}
```

#### 進捗状況のレスポンス
```
HTTP/1.1 200 OK
Date: Mon, 26 Mar 20XX hh:mm:dd GMT
Content-Type: application/json; charset=utf-8
〜 略 〜

{
  \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",
  \"resources_url\": <resources_url>,
  \"status\": \"SUCCESSFUL\"
}
```

# API一覧
DPF-APIではIIJ DNSプラットフォームサービスに関する以下の操作を行うことができます。

## IIJ DNSプラットフォームサービス

### cc_primaries
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/get) | プライマリネームサーバ設定の一覧取得 | dpf_read
  POST | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/post) | プライマリネームサーバ設定の作成 | dpf_write
  GET | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/get) | プライマリネームサーバ設定の取得 | dpf_read
  PATCH | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/patch) | プライマリネームサーバ設定の更新 | dpf_write
  DELETE | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/delete) | プライマリネームサーバ設定の削除 | dpf_write

### cc_sec_notified_servers
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/get) | DNS NOTIFY設定の一覧取得 | dpf_read
  POST | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/post) | DNS NOTIFY設定の作成 | dpf_write
  GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/get) | DNS NOTIFY設定の取得 | dpf_read
  PATCH | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/patch) | DNS NOTIFY設定の更新 | dpf_write
  DELETE | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/delete) | DNS NOTIFY設定の削除 | dpf_write

### cc_sec_transfer_acls
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/get) | ゾーン転送ACLの一覧取得 | dpf_read
  POST | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/post) | ゾーン転送ACLの作成 | dpf_write
  GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/get) | ゾーン転送ACLの取得 | dpf_read
  PATCH | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/patch) | ゾーン転送ACLの更新 | dpf_write
  DELETE | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/delete) | ゾーン転送ACLの削除 | dpf_write

### common_configs
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/get) | 共通設定の一覧取得 | dpf_read
  POST | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/post) | 共通設定の作成 | dpf_write
  GET | [/contracts/{ContractId}/common_configs/count](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1count/get) | 共通設定の件数取得 | dpf_read
  PATCH | [/contracts/{ContractId}/common_configs/default](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1default/patch) | 初期適用される共通設定の更新 | dpf_write
  GET | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/get) | 共通設定の取得 | dpf_read
  PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/patch) | 共通設定の更新 | dpf_write
  DELETE | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/delete) | 共通設定の削除 | dpf_write
  POST | [/contracts/{ContractId}/common_configs/{CommonConfigId}/copy](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1copy/post) | 共通設定のコピー | dpf_write
  PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}/managed_dns](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1managed_dns/patch) | マネージドDNSサーバの状態更新 | dpf_write

### contracts
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts](#tag/contracts/paths/~1contracts/get) | DPF契約情報の一覧取得 | dpf_read
  GET | [/contracts/count](#tag/contracts/paths/~1contracts~1count/get) | DPF契約情報の件数取得 | dpf_read
  GET | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/get) | DPF契約情報の取得 | dpf_read
  PATCH | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/patch) | DPF契約情報の更新 | dpf_write

### contract_partners
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts/{ContractId}/contract_partners](#tag/contract_partners/paths/~1contracts~1{ContractId}~1contract_partners/get) | DPF連携サービスの一覧取得 | dpf_read

### logs (contracts)
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts/{ContractId}/logs](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs/get) | DPF契約操作ログの一覧取得 | dpf_read
  GET | [/contracts/{ContractId}/logs/count](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs~1count/get) | DPF契約操作ログの件数取得 | dpf_read

### qps
HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts/{ContractId}/qps/histories](#tag/qps/paths/~1contracts~1{ContractId}~1qps~1histories/get) | 月別のQPSの一覧取得 | dpf_read

### tsigs
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/get) | TSIG鍵の一覧取得 | dpf_read
  POST | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/post) | TSIG鍵の作成 | dpf_write
  GET | [/contracts/{ContractId}/tsigs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1count/get) | TSIG鍵の件数取得 | dpf_read
  GET | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/get) | TSIG鍵の取得 | dpf_read
  PATCH | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/patch) | TSIG鍵の更新 | dpf_write
  DELETE | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/delete) | TSIG鍵の削除 | dpf_write
  GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs/get) | TSIG鍵を利用している共通設定の一覧取得 | dpf_read
  GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs~1count/get) | TSIG鍵を利用している共通設定の件数取得 | dpf_read

### zones (contracts)
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/contracts/{ContractId}/zones](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones/get) | DPF契約に紐付くゾーンの一覧取得 | dpf_read
  PATCH | [/contracts/{ContractId}/zones/common_configs](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1common_configs/patch) | DPF契約に紐付くゾーンの共通設定の更新 | dpf_write
  GET | [/contracts/{ContractId}/zones/count](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1count/get) | DPF契約に紐付くゾーンの件数取得 | dpf_read

## IIJマネージドDNSサービス

### default_ttl
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/get) | デフォルトTTLの取得 | dpf_read
  PATCH | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/patch) | デフォルトTTLの更新 | dpf_write
  DELETE | [/zones/{ZoneId}/default_ttl/changes](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1changes/delete) | 編集中デフォルトTTLの取消 | dpf_write
  GET | [/zones/{ZoneId}/default_ttl/diffs](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1diffs/get) | デフォルトTTLの編集差分の取得 | dpf_read

### dnssec
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/get) | DNSSEC情報の取得 | dpf_read
  PATCH | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/patch) | DNSSEC情報の更新 | dpf_write
  PATCH | [/zones/{ZoneId}/dnssec/ksk_rollover](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec~1ksk_rollover/patch) | KSKロールオーバーの開始 | dpf_write

### ds_records
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/ds_records](#tag/ds_records/paths/~1zones~1{ZoneId}~1ds_records/get) | DSレコードの一覧取得 | dpf_read

### logs (zones)
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/logs](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs/get) | ゾーン操作ログの一覧取得 | dpf_read
  GET | [/zones/{ZoneId}/logs/count](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs~1count/get) | ゾーン操作ログの件数取得 | dpf_read

### records
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/get) | レコードの一覧取得 | dpf_read
  POST | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/post) | レコードの作成 | dpf_write
  GET | [/zones/{ZoneId}/records/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1count/get) | レコードの件数取得 | dpf_read
  GET | [/zones/{ZoneId}/records/currents](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents/get) | DNS反映済レコードの一覧取得 | dpf_read
  GET | [/zones/{ZoneId}/records/currents/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents~1count/get) | DNS反映済レコードの件数取得 | dpf_read
  GET | [/zones/{ZoneId}/records/diffs](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs/get) | レコードの編集差分の一覧取得 | dpf_read
  GET | [/zones/{ZoneId}/records/diffs/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs~1count/get) | レコードの編集差分の件数取得 | dpf_read
  GET | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/get) | レコードの取得 | dpf_read
  PATCH | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/patch) | レコードの更新 | dpf_write
  DELETE | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/delete) | レコードの削除 | dpf_write
  DELETE | [/zones/{ZoneId}/records/{RecordId}/changes](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}~1changes/delete) | 編集中レコードの取消 | dpf_write

### zone_histories
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/zone_histories](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories/get) | ゾーン反映履歴の一覧取得 | dpf_read
  GET | [/zones/{ZoneId}/zone_histories/count](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1count/get) | ゾーン反映履歴の件数取得 | dpf_read
  GET | [/zones/{ZoneId}/zone_histories/{ZoneHistoryId}/text](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1{ZoneHistoryId}~1text/get) | ゾーン反映時のRFC1035形式のテキストの取得 | dpf_read

### zone_proxy
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/get) | ゾーンプロキシ設定の取得 | dpf_read
  PATCH | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/patch) | ゾーンプロキシ設定の更新 | dpf_write
  GET | [/zones/{ZoneId}/zone_proxy/health_check](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy~1health_check/get) | プライマリネームサーバのヘルスチェック結果の取得 | dpf_read

### zones
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/zones](#tag/zones/paths/~1zones/get) | ゾーンの一覧取得 | dpf_read
  GET | [/zones/count](#tag/zones/paths/~1zones~1count/get) | ゾーンの件数取得 | dpf_read
  GET | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/get) | ゾーンの取得 | dpf_read
  PATCH | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/patch) | ゾーンの更新 | dpf_write
  PATCH | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch) | 編集中レコードのゾーン反映 | dpf_write
  DELETE | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/delete) | 編集中レコードの一括取消 | dpf_write
  GET | [/zones/{ZoneId}/contract](#tag/zones/paths/~1zones~1{ZoneId}~1contract/get) | ゾーンに紐付くDPF契約情報の取得 | dpf_read
  GET | [/zones/{ZoneId}/managed_dns_servers](#tag/zones/paths/~1zones~1{ZoneId}~1managed_dns_servers/get) | マネージドDNSサーバの一覧取得 | dpf_read

## サービス共通

### delegations
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/delegations](#tag/delegations/paths/~1delegations/get) | ネームサーバ申請候補の一覧取得 | dpf_read
  POST | [/delegations](#tag/delegations/paths/~1delegations/post) | ネームサーバ申請 | dpf_write
  GET | [/delegations/count](#tag/delegations/paths/~1delegations~1count/get) | ネームサーバ申請候補の件数取得 | dpf_read

### jobs
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/jobs/{RequestId}](#tag/jobs/paths/~1jobs~1{RequestId}/get) | 非同期リクエストの状態確認 | dpf_read

### ping
  HTTPメソッド | API | 機能 | 許可するスコープ
  -----------|-----|-----|--------------
  GET | [/ping](#tag/ping/paths/~1ping/get) | API疎通確認 | dpf_read, dpf_write, dpf_contract


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import cc_primaries_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.get_cc_primaries import GetCcPrimaries
from openapi_client.model.get_cc_primary import GetCcPrimary
from openapi_client.model.id import Id
from openapi_client.model.patch_cc_primary import PatchCcPrimary
from openapi_client.model.post_cc_primary import PostCcPrimary
# Defining the host is optional and defaults to https://api.dns-platform.jp/dpf/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.dns-platform.jp/dpf/v1"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc_primaries_api.CcPrimariesApi(api_client)
    common_config_id = Id(1) # Id | ID
    cc_primary_id = Id(1) # Id | ID

    try:
        # プライマリネームサーバ設定の削除
        api_response = api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_delete(common_config_id, cc_primary_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CcPrimariesApi->common_configs_common_config_id_cc_primaries_cc_primary_id_delete: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.dns-platform.jp/dpf/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CcPrimariesApi* | [**common_configs_common_config_id_cc_primaries_cc_primary_id_delete**](docs/CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_cc_primary_id_delete) | **DELETE** /common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId} | プライマリネームサーバ設定の削除
*CcPrimariesApi* | [**common_configs_common_config_id_cc_primaries_cc_primary_id_get**](docs/CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_cc_primary_id_get) | **GET** /common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId} | プライマリネームサーバ設定の取得
*CcPrimariesApi* | [**common_configs_common_config_id_cc_primaries_cc_primary_id_patch**](docs/CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_cc_primary_id_patch) | **PATCH** /common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId} | プライマリネームサーバ設定の更新
*CcPrimariesApi* | [**common_configs_common_config_id_cc_primaries_get**](docs/CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_get) | **GET** /common_configs/{CommonConfigId}/cc_primaries | プライマリネームサーバ設定の一覧取得
*CcPrimariesApi* | [**common_configs_common_config_id_cc_primaries_post**](docs/CcPrimariesApi.md#common_configs_common_config_id_cc_primaries_post) | **POST** /common_configs/{CommonConfigId}/cc_primaries | プライマリネームサーバ設定の作成
*CcSecNotifiedServersApi* | [**common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete**](docs/CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_delete) | **DELETE** /common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId} | DNS NOTIFY設定の削除
*CcSecNotifiedServersApi* | [**common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get**](docs/CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId} | DNS NOTIFY設定の取得
*CcSecNotifiedServersApi* | [**common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch**](docs/CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_cc_sec_notified_server_id_patch) | **PATCH** /common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId} | DNS NOTIFY設定の更新
*CcSecNotifiedServersApi* | [**common_configs_common_config_id_cc_sec_notified_servers_get**](docs/CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_notified_servers | DNS NOTIFY設定の一覧取得
*CcSecNotifiedServersApi* | [**common_configs_common_config_id_cc_sec_notified_servers_post**](docs/CcSecNotifiedServersApi.md#common_configs_common_config_id_cc_sec_notified_servers_post) | **POST** /common_configs/{CommonConfigId}/cc_sec_notified_servers | DNS NOTIFY設定の作成
*CcSecTransferAclsApi* | [**common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete**](docs/CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_delete) | **DELETE** /common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId} | ゾーン転送ACLの削除
*CcSecTransferAclsApi* | [**common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get**](docs/CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId} | ゾーン転送ACLの取得
*CcSecTransferAclsApi* | [**common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch**](docs/CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_cc_sec_transfer_acl_id_patch) | **PATCH** /common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId} | ゾーン転送ACLの更新
*CcSecTransferAclsApi* | [**common_configs_common_config_id_cc_sec_transfer_acls_get**](docs/CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_get) | **GET** /common_configs/{CommonConfigId}/cc_sec_transfer_acls | ゾーン転送ACLの一覧取得
*CcSecTransferAclsApi* | [**common_configs_common_config_id_cc_sec_transfer_acls_post**](docs/CcSecTransferAclsApi.md#common_configs_common_config_id_cc_sec_transfer_acls_post) | **POST** /common_configs/{CommonConfigId}/cc_sec_transfer_acls | ゾーン転送ACLの作成
*CommonConfigsApi* | [**contracts_contract_id_common_configs_common_config_id_copy_post**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_copy_post) | **POST** /contracts/{ContractId}/common_configs/{CommonConfigId}/copy | 共通設定のコピー
*CommonConfigsApi* | [**contracts_contract_id_common_configs_common_config_id_delete**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_delete) | **DELETE** /contracts/{ContractId}/common_configs/{CommonConfigId} | 共通設定の削除
*CommonConfigsApi* | [**contracts_contract_id_common_configs_common_config_id_get**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_get) | **GET** /contracts/{ContractId}/common_configs/{CommonConfigId} | 共通設定の取得
*CommonConfigsApi* | [**contracts_contract_id_common_configs_common_config_id_managed_dns_patch**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_managed_dns_patch) | **PATCH** /contracts/{ContractId}/common_configs/{CommonConfigId}/managed_dns | マネージドDNSサーバの状態更新
*CommonConfigsApi* | [**contracts_contract_id_common_configs_common_config_id_patch**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_common_config_id_patch) | **PATCH** /contracts/{ContractId}/common_configs/{CommonConfigId} | 共通設定の更新
*CommonConfigsApi* | [**contracts_contract_id_common_configs_count_get**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_count_get) | **GET** /contracts/{ContractId}/common_configs/count | 共通設定の件数取得
*CommonConfigsApi* | [**contracts_contract_id_common_configs_default_patch**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_default_patch) | **PATCH** /contracts/{ContractId}/common_configs/default | 初期適用される共通設定の更新
*CommonConfigsApi* | [**contracts_contract_id_common_configs_get**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_get) | **GET** /contracts/{ContractId}/common_configs | 共通設定の一覧取得
*CommonConfigsApi* | [**contracts_contract_id_common_configs_post**](docs/CommonConfigsApi.md#contracts_contract_id_common_configs_post) | **POST** /contracts/{ContractId}/common_configs | 共通設定の作成
*ContractPartnersApi* | [**contracts_contract_id_contract_partners_get**](docs/ContractPartnersApi.md#contracts_contract_id_contract_partners_get) | **GET** /contracts/{ContractId}/contract_partners | DPF連携サービスの一覧取得
*ContractsApi* | [**contracts_contract_id_get**](docs/ContractsApi.md#contracts_contract_id_get) | **GET** /contracts/{ContractId} | DPF契約情報の取得
*ContractsApi* | [**contracts_contract_id_patch**](docs/ContractsApi.md#contracts_contract_id_patch) | **PATCH** /contracts/{ContractId} | DPF契約情報の更新
*ContractsApi* | [**contracts_count_get**](docs/ContractsApi.md#contracts_count_get) | **GET** /contracts/count | DPF契約情報の件数取得
*ContractsApi* | [**contracts_get**](docs/ContractsApi.md#contracts_get) | **GET** /contracts | DPF契約情報の一覧取得
*DefaultTtlApi* | [**zones_zone_id_default_ttl_changes_delete**](docs/DefaultTtlApi.md#zones_zone_id_default_ttl_changes_delete) | **DELETE** /zones/{ZoneId}/default_ttl/changes | 編集中デフォルトTTLの取消
*DefaultTtlApi* | [**zones_zone_id_default_ttl_diffs_get**](docs/DefaultTtlApi.md#zones_zone_id_default_ttl_diffs_get) | **GET** /zones/{ZoneId}/default_ttl/diffs | デフォルトTTLの編集差分の取得
*DefaultTtlApi* | [**zones_zone_id_default_ttl_get**](docs/DefaultTtlApi.md#zones_zone_id_default_ttl_get) | **GET** /zones/{ZoneId}/default_ttl | デフォルトTTLの取得
*DefaultTtlApi* | [**zones_zone_id_default_ttl_patch**](docs/DefaultTtlApi.md#zones_zone_id_default_ttl_patch) | **PATCH** /zones/{ZoneId}/default_ttl | デフォルトTTLの更新
*DelegationsApi* | [**delegations_count_get**](docs/DelegationsApi.md#delegations_count_get) | **GET** /delegations/count | ネームサーバ申請候補の件数取得
*DelegationsApi* | [**delegations_get**](docs/DelegationsApi.md#delegations_get) | **GET** /delegations | ネームサーバ申請候補の一覧取得
*DelegationsApi* | [**delegations_post**](docs/DelegationsApi.md#delegations_post) | **POST** /delegations | ネームサーバ申請
*DnssecApi* | [**zones_zone_id_dnssec_get**](docs/DnssecApi.md#zones_zone_id_dnssec_get) | **GET** /zones/{ZoneId}/dnssec | DNSSEC情報の取得
*DnssecApi* | [**zones_zone_id_dnssec_ksk_rollover_patch**](docs/DnssecApi.md#zones_zone_id_dnssec_ksk_rollover_patch) | **PATCH** /zones/{ZoneId}/dnssec/ksk_rollover | KSKロールオーバーの開始
*DnssecApi* | [**zones_zone_id_dnssec_patch**](docs/DnssecApi.md#zones_zone_id_dnssec_patch) | **PATCH** /zones/{ZoneId}/dnssec | DNSSEC情報の更新
*DsRecordsApi* | [**zones_zone_id_ds_records_get**](docs/DsRecordsApi.md#zones_zone_id_ds_records_get) | **GET** /zones/{ZoneId}/ds_records | DSレコードの一覧取得
*JobsApi* | [**jobs_request_id_get**](docs/JobsApi.md#jobs_request_id_get) | **GET** /jobs/{RequestId} | 非同期リクエストの状態確認
*LogsContractsApi* | [**contracts_contract_id_logs_count_get**](docs/LogsContractsApi.md#contracts_contract_id_logs_count_get) | **GET** /contracts/{ContractId}/logs/count | DPF契約操作ログの件数取得
*LogsContractsApi* | [**contracts_contract_id_logs_get**](docs/LogsContractsApi.md#contracts_contract_id_logs_get) | **GET** /contracts/{ContractId}/logs | DPF契約操作ログの一覧取得
*LogsZonesApi* | [**zones_zone_id_logs_count_get**](docs/LogsZonesApi.md#zones_zone_id_logs_count_get) | **GET** /zones/{ZoneId}/logs/count | ゾーン操作ログの件数取得
*LogsZonesApi* | [**zones_zone_id_logs_get**](docs/LogsZonesApi.md#zones_zone_id_logs_get) | **GET** /zones/{ZoneId}/logs | ゾーン操作ログの一覧取得
*PingApi* | [**ping_get**](docs/PingApi.md#ping_get) | **GET** /ping | API疎通確認
*QpsApi* | [**contracts_contract_id_qps_histories_get**](docs/QpsApi.md#contracts_contract_id_qps_histories_get) | **GET** /contracts/{ContractId}/qps/histories | 月別のQPSの一覧取得
*RecordsApi* | [**zones_zone_id_records_count_get**](docs/RecordsApi.md#zones_zone_id_records_count_get) | **GET** /zones/{ZoneId}/records/count | レコードの件数取得
*RecordsApi* | [**zones_zone_id_records_currents_count_get**](docs/RecordsApi.md#zones_zone_id_records_currents_count_get) | **GET** /zones/{ZoneId}/records/currents/count | DNS反映済レコードの件数取得
*RecordsApi* | [**zones_zone_id_records_currents_get**](docs/RecordsApi.md#zones_zone_id_records_currents_get) | **GET** /zones/{ZoneId}/records/currents | DNS反映済レコードの一覧取得
*RecordsApi* | [**zones_zone_id_records_diffs_count_get**](docs/RecordsApi.md#zones_zone_id_records_diffs_count_get) | **GET** /zones/{ZoneId}/records/diffs/count | レコードの編集差分の件数取得
*RecordsApi* | [**zones_zone_id_records_diffs_get**](docs/RecordsApi.md#zones_zone_id_records_diffs_get) | **GET** /zones/{ZoneId}/records/diffs | レコードの編集差分の一覧取得
*RecordsApi* | [**zones_zone_id_records_get**](docs/RecordsApi.md#zones_zone_id_records_get) | **GET** /zones/{ZoneId}/records | レコードの一覧取得
*RecordsApi* | [**zones_zone_id_records_post**](docs/RecordsApi.md#zones_zone_id_records_post) | **POST** /zones/{ZoneId}/records | レコードの作成
*RecordsApi* | [**zones_zone_id_records_record_id_changes_delete**](docs/RecordsApi.md#zones_zone_id_records_record_id_changes_delete) | **DELETE** /zones/{ZoneId}/records/{RecordId}/changes | 編集中レコードの取消
*RecordsApi* | [**zones_zone_id_records_record_id_delete**](docs/RecordsApi.md#zones_zone_id_records_record_id_delete) | **DELETE** /zones/{ZoneId}/records/{RecordId} | レコードの削除
*RecordsApi* | [**zones_zone_id_records_record_id_get**](docs/RecordsApi.md#zones_zone_id_records_record_id_get) | **GET** /zones/{ZoneId}/records/{RecordId} | レコードの取得
*RecordsApi* | [**zones_zone_id_records_record_id_patch**](docs/RecordsApi.md#zones_zone_id_records_record_id_patch) | **PATCH** /zones/{ZoneId}/records/{RecordId} | レコードの更新
*TsigsApi* | [**contracts_contract_id_tsigs_count_get**](docs/TsigsApi.md#contracts_contract_id_tsigs_count_get) | **GET** /contracts/{ContractId}/tsigs/count | TSIG鍵の件数取得
*TsigsApi* | [**contracts_contract_id_tsigs_get**](docs/TsigsApi.md#contracts_contract_id_tsigs_get) | **GET** /contracts/{ContractId}/tsigs | TSIG鍵の一覧取得
*TsigsApi* | [**contracts_contract_id_tsigs_post**](docs/TsigsApi.md#contracts_contract_id_tsigs_post) | **POST** /contracts/{ContractId}/tsigs | TSIG鍵の作成
*TsigsApi* | [**contracts_contract_id_tsigs_tsig_id_common_configs_count_get**](docs/TsigsApi.md#contracts_contract_id_tsigs_tsig_id_common_configs_count_get) | **GET** /contracts/{ContractId}/tsigs/{TsigId}/common_configs/count | TSIG鍵を利用している共通設定の件数取得
*TsigsApi* | [**contracts_contract_id_tsigs_tsig_id_common_configs_get**](docs/TsigsApi.md#contracts_contract_id_tsigs_tsig_id_common_configs_get) | **GET** /contracts/{ContractId}/tsigs/{TsigId}/common_configs | TSIG鍵を利用している共通設定の一覧取得
*TsigsApi* | [**contracts_contract_id_tsigs_tsig_id_delete**](docs/TsigsApi.md#contracts_contract_id_tsigs_tsig_id_delete) | **DELETE** /contracts/{ContractId}/tsigs/{TsigId} | TSIG鍵の削除
*TsigsApi* | [**contracts_contract_id_tsigs_tsig_id_get**](docs/TsigsApi.md#contracts_contract_id_tsigs_tsig_id_get) | **GET** /contracts/{ContractId}/tsigs/{TsigId} | TSIG鍵の取得
*TsigsApi* | [**contracts_contract_id_tsigs_tsig_id_patch**](docs/TsigsApi.md#contracts_contract_id_tsigs_tsig_id_patch) | **PATCH** /contracts/{ContractId}/tsigs/{TsigId} | TSIG鍵の更新
*ZoneHistoriesApi* | [**zones_zone_id_zone_histories_count_get**](docs/ZoneHistoriesApi.md#zones_zone_id_zone_histories_count_get) | **GET** /zones/{ZoneId}/zone_histories/count | ゾーン反映履歴の件数取得
*ZoneHistoriesApi* | [**zones_zone_id_zone_histories_get**](docs/ZoneHistoriesApi.md#zones_zone_id_zone_histories_get) | **GET** /zones/{ZoneId}/zone_histories | ゾーン反映履歴の一覧取得
*ZoneHistoriesApi* | [**zones_zone_id_zone_histories_zone_history_id_text_get**](docs/ZoneHistoriesApi.md#zones_zone_id_zone_histories_zone_history_id_text_get) | **GET** /zones/{ZoneId}/zone_histories/{ZoneHistoryId}/text | ゾーン反映時のRFC1035形式のテキストの取得
*ZoneProxyApi* | [**zones_zone_id_zone_proxy_get**](docs/ZoneProxyApi.md#zones_zone_id_zone_proxy_get) | **GET** /zones/{ZoneId}/zone_proxy | ゾーンプロキシ設定の取得
*ZoneProxyApi* | [**zones_zone_id_zone_proxy_health_check_get**](docs/ZoneProxyApi.md#zones_zone_id_zone_proxy_health_check_get) | **GET** /zones/{ZoneId}/zone_proxy/health_check | プライマリネームサーバのヘルスチェック結果の取得
*ZoneProxyApi* | [**zones_zone_id_zone_proxy_patch**](docs/ZoneProxyApi.md#zones_zone_id_zone_proxy_patch) | **PATCH** /zones/{ZoneId}/zone_proxy | ゾーンプロキシ設定の更新
*ZonesApi* | [**zones_count_get**](docs/ZonesApi.md#zones_count_get) | **GET** /zones/count | ゾーンの件数取得
*ZonesApi* | [**zones_get**](docs/ZonesApi.md#zones_get) | **GET** /zones | ゾーンの一覧取得
*ZonesApi* | [**zones_zone_id_changes_delete**](docs/ZonesApi.md#zones_zone_id_changes_delete) | **DELETE** /zones/{ZoneId}/changes | 編集中レコードの一括取消
*ZonesApi* | [**zones_zone_id_changes_patch**](docs/ZonesApi.md#zones_zone_id_changes_patch) | **PATCH** /zones/{ZoneId}/changes | 編集中レコードのゾーン反映
*ZonesApi* | [**zones_zone_id_contract_get**](docs/ZonesApi.md#zones_zone_id_contract_get) | **GET** /zones/{ZoneId}/contract | ゾーンに紐付くDPF契約情報の取得
*ZonesApi* | [**zones_zone_id_get**](docs/ZonesApi.md#zones_zone_id_get) | **GET** /zones/{ZoneId} | ゾーンの取得
*ZonesApi* | [**zones_zone_id_managed_dns_servers_get**](docs/ZonesApi.md#zones_zone_id_managed_dns_servers_get) | **GET** /zones/{ZoneId}/managed_dns_servers | マネージドDNSサーバの一覧取得
*ZonesApi* | [**zones_zone_id_patch**](docs/ZonesApi.md#zones_zone_id_patch) | **PATCH** /zones/{ZoneId} | ゾーンの更新
*ZonesContractsApi* | [**contracts_contract_id_zones_common_configs_patch**](docs/ZonesContractsApi.md#contracts_contract_id_zones_common_configs_patch) | **PATCH** /contracts/{ContractId}/zones/common_configs | DPF契約に紐付くゾーンの共通設定の更新
*ZonesContractsApi* | [**contracts_contract_id_zones_count_get**](docs/ZonesContractsApi.md#contracts_contract_id_zones_count_get) | **GET** /contracts/{ContractId}/zones/count | DPF契約に紐付くゾーンの件数取得
*ZonesContractsApi* | [**contracts_contract_id_zones_get**](docs/ZonesContractsApi.md#contracts_contract_id_zones_get) | **GET** /contracts/{ContractId}/zones | DPF契約に紐付くゾーンの一覧取得


## Documentation For Models

 - [AsyncResponse](docs/AsyncResponse.md)
 - [BadRequest](docs/BadRequest.md)
 - [CcPrimary](docs/CcPrimary.md)
 - [CcPrimaryEnabled](docs/CcPrimaryEnabled.md)
 - [CcSecTransferAcl](docs/CcSecTransferAcl.md)
 - [CommonConfig](docs/CommonConfig.md)
 - [CommonConfigDefault](docs/CommonConfigDefault.md)
 - [CommonConfigName](docs/CommonConfigName.md)
 - [Contract](docs/Contract.md)
 - [ContractFavorite](docs/ContractFavorite.md)
 - [ContractPlan](docs/ContractPlan.md)
 - [ContractState](docs/ContractState.md)
 - [ContractsLog](docs/ContractsLog.md)
 - [ContractsLogsLogType](docs/ContractsLogsLogType.md)
 - [ContractsLogsOperation](docs/ContractsLogsOperation.md)
 - [ContractsLogsStatus](docs/ContractsLogsStatus.md)
 - [DefaultTtl](docs/DefaultTtl.md)
 - [DefaultTtlState](docs/DefaultTtlState.md)
 - [DefaultTtlValue](docs/DefaultTtlValue.md)
 - [Delegation](docs/Delegation.md)
 - [DelegationsFavorite](docs/DelegationsFavorite.md)
 - [DelegationsRequested](docs/DelegationsRequested.md)
 - [Description](docs/Description.md)
 - [Dnssec](docs/Dnssec.md)
 - [DnssecDsState](docs/DnssecDsState.md)
 - [DnssecEnabled](docs/DnssecEnabled.md)
 - [DnssecState](docs/DnssecState.md)
 - [DsRecord](docs/DsRecord.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [GetCcPrimaries](docs/GetCcPrimaries.md)
 - [GetCcPrimary](docs/GetCcPrimary.md)
 - [GetCcSecNotifiedServer](docs/GetCcSecNotifiedServer.md)
 - [GetCcSecNotifiedServers](docs/GetCcSecNotifiedServers.md)
 - [GetCcSecTransferAcl](docs/GetCcSecTransferAcl.md)
 - [GetCcSecTransferAcls](docs/GetCcSecTransferAcls.md)
 - [GetCommonConfig](docs/GetCommonConfig.md)
 - [GetCommonConfigs](docs/GetCommonConfigs.md)
 - [GetContract](docs/GetContract.md)
 - [GetContractPartners](docs/GetContractPartners.md)
 - [GetContractPartnersResults](docs/GetContractPartnersResults.md)
 - [GetContracts](docs/GetContracts.md)
 - [GetContractsLogs](docs/GetContractsLogs.md)
 - [GetCount](docs/GetCount.md)
 - [GetCountResult](docs/GetCountResult.md)
 - [GetDefaultTtl](docs/GetDefaultTtl.md)
 - [GetDefaultTtlDiffs](docs/GetDefaultTtlDiffs.md)
 - [GetDefaultTtlDiffsResults](docs/GetDefaultTtlDiffsResults.md)
 - [GetDelegations](docs/GetDelegations.md)
 - [GetDnssec](docs/GetDnssec.md)
 - [GetDsRecords](docs/GetDsRecords.md)
 - [GetJobs](docs/GetJobs.md)
 - [GetManagedServers](docs/GetManagedServers.md)
 - [GetPing](docs/GetPing.md)
 - [GetQpsHistories](docs/GetQpsHistories.md)
 - [GetRecord](docs/GetRecord.md)
 - [GetRecords](docs/GetRecords.md)
 - [GetRecordsDiffs](docs/GetRecordsDiffs.md)
 - [GetRecordsDiffsResults](docs/GetRecordsDiffsResults.md)
 - [GetTsig](docs/GetTsig.md)
 - [GetTsigs](docs/GetTsigs.md)
 - [GetTsigsCommonConfigs](docs/GetTsigsCommonConfigs.md)
 - [GetZone](docs/GetZone.md)
 - [GetZoneHistories](docs/GetZoneHistories.md)
 - [GetZoneHistoriesText](docs/GetZoneHistoriesText.md)
 - [GetZoneProxy](docs/GetZoneProxy.md)
 - [GetZoneProxyHealth](docs/GetZoneProxyHealth.md)
 - [GetZones](docs/GetZones.md)
 - [GetZonesLogs](docs/GetZonesLogs.md)
 - [Id](docs/Id.md)
 - [KeywordsString](docs/KeywordsString.md)
 - [ManagedDnsEnabled](docs/ManagedDnsEnabled.md)
 - [NotifiedServer](docs/NotifiedServer.md)
 - [PatchCcPrimary](docs/PatchCcPrimary.md)
 - [PatchCcSecNotifiedServer](docs/PatchCcSecNotifiedServer.md)
 - [PatchCcSecTransferAcl](docs/PatchCcSecTransferAcl.md)
 - [PatchCommonConfig](docs/PatchCommonConfig.md)
 - [PatchContract](docs/PatchContract.md)
 - [PatchContractsZones](docs/PatchContractsZones.md)
 - [PatchDefaultCommonConfig](docs/PatchDefaultCommonConfig.md)
 - [PatchDefaultTtl](docs/PatchDefaultTtl.md)
 - [PatchDnssec](docs/PatchDnssec.md)
 - [PatchManagedDns](docs/PatchManagedDns.md)
 - [PatchRecord](docs/PatchRecord.md)
 - [PatchTsig](docs/PatchTsig.md)
 - [PatchZone](docs/PatchZone.md)
 - [PatchZoneCommit](docs/PatchZoneCommit.md)
 - [PatchZoneProxy](docs/PatchZoneProxy.md)
 - [PostCcPrimary](docs/PostCcPrimary.md)
 - [PostCcSecNotifiedServer](docs/PostCcSecNotifiedServer.md)
 - [PostCcSecTransferAcl](docs/PostCcSecTransferAcl.md)
 - [PostCommonConfig](docs/PostCommonConfig.md)
 - [PostDelegations](docs/PostDelegations.md)
 - [PostRecord](docs/PostRecord.md)
 - [PostTsig](docs/PostTsig.md)
 - [Qps](docs/Qps.md)
 - [QpsHistory](docs/QpsHistory.md)
 - [QpsValue](docs/QpsValue.md)
 - [Record](docs/Record.md)
 - [RecordsName](docs/RecordsName.md)
 - [RecordsRdata](docs/RecordsRdata.md)
 - [RecordsRrtype](docs/RecordsRrtype.md)
 - [RecordsState](docs/RecordsState.md)
 - [RecordsTtl](docs/RecordsTtl.md)
 - [RequestId](docs/RequestId.md)
 - [SearchLimit](docs/SearchLimit.md)
 - [SearchLogsLimit](docs/SearchLogsLimit.md)
 - [SearchLogsOffset](docs/SearchLogsOffset.md)
 - [SearchOffset](docs/SearchOffset.md)
 - [SearchOrder](docs/SearchOrder.md)
 - [SearchType](docs/SearchType.md)
 - [ServiceCode](docs/ServiceCode.md)
 - [SystemId](docs/SystemId.md)
 - [Tsig](docs/Tsig.md)
 - [TsigId](docs/TsigId.md)
 - [TsigsAlgorithm](docs/TsigsAlgorithm.md)
 - [TsigsPostName](docs/TsigsPostName.md)
 - [Zone](docs/Zone.md)
 - [ZoneHistory](docs/ZoneHistory.md)
 - [ZoneHistoryText](docs/ZoneHistoryText.md)
 - [ZoneProxy](docs/ZoneProxy.md)
 - [ZoneProxyEnabled](docs/ZoneProxyEnabled.md)
 - [ZoneProxyHealth](docs/ZoneProxyHealth.md)
 - [ZoneProxyStatus](docs/ZoneProxyStatus.md)
 - [ZonesEnabled](docs/ZonesEnabled.md)
 - [ZonesFavorite](docs/ZonesFavorite.md)
 - [ZonesLog](docs/ZonesLog.md)
 - [ZonesLogsOperation](docs/ZonesLogsOperation.md)
 - [ZonesLogsStatus](docs/ZonesLogsStatus.md)
 - [ZonesLogsType](docs/ZonesLogsType.md)
 - [ZonesName](docs/ZonesName.md)
 - [ZonesState](docs/ZonesState.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```

