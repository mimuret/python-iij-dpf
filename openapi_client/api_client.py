"""
    DPF-APIリファレンスマニュアル

    # はじめに  ## DPF-APIについて IIJ DNSプラットフォームサービスでは、DNSレコードやゾーン情報などを、\\ お客様が用意したプログラムから自動的に操作するためのAPI機能を提供しています。\\ 以降、IIJ DNSプラットフォームサービスを「DPF」、DPFが提供するAPIを「DPF-API」あるいは単に「API」と表記します。\\ DPF-APIの利用には、DPFの契約とIIJ IDサービスの契約が必要となります。  本リファレンスマニュアルは**[OpenAPI](https://www.openapis.org/)**に準拠しています。  ## サポート範囲 DPF-APIを呼び出すためのプログラム、及びそのプログラムを稼働させるためのサーバは、お客様にてご用意ください。\\ お客様にご用意いただくプログラムの開発、利用、動作についてのお問い合わせは承ることができません。  以下の事項についてのお問い合わせは、弊社**[サポートセンター](https://help.iij.ad.jp/)**にて承ります。 - DPF-APIの挙動が本リファレンスマニュアルと異なる場合 - DPF-APIがシステムエラーを応答した場合  ## 参考資料 - IIJ DNSプラットフォームサービス オンラインマニュアル   - [https://manual.iij.jp/dpf/help/](https://manual.iij.jp/dpf/help/)  - IIJ IDサービス オンラインマニュアル   - [https://manual.iij.jp/iid/admin-help/](https://manual.iij.jp/iid/admin-help/)  # 利用方法 DPF-APIは、URLとHTTPリクエストヘッダ、HTTPリクエストボディでパラメータを指定して利用します。\\ また、IIJ IDサービスのアクセストークンと管理対象の権限設定が必要です。  ## リクエスト仕様  項目 | 規格 -----|----- プロトコル | HTTP/1.1、HTTP/2（https） HTTPメソッド | GET、PATCH、POST、DELETE フォーマット | JSON 文字コード | UTF-8 タイムアウト | 300秒  - httpでのリクエストは受け付けません。必ずhttpsを使用してください。 - DPF-APIを呼び出すプログラムは、リクエスト先が正当なものであることを確認するため、SSL証明書を検証することを推奨します。 - 短期間に極めて多数のリクエストが行われた場合、サービスの健全性を保つためにリクエストを制限する場合があります。  ### アクセストークン APIリクエストの際にIIJ IDサービスによって発行されたアクセストークンをAuthorizationヘッダに指定する必要があります。\\ 各APIにより必要となるアクセス権の範囲（許可するスコープ）が異なるのでご注意ください。  アクセストークン作成時に指定できる「許可するスコープ」は以下のとおりです。  許可するスコープ | 実行できるAPI -----------------|------------ dpf_read | 参照系API dpf_write | 更新系、及び参照系API dpf_contract | 契約系API  発行済のアクセストークンは、**[IIJ IDサービス](https://www.auth.iij.jp/console/)**の「アクセストークンの管理」より確認できます。\\ DPF-APIを利用する場合は「利用するリソースサーバ」の設定で「IIJ DNSサービスAPI」を選択してください。\\ アクセストークン管理方法のマニュアルは**[こちら](https://manual.iij.jp/iid/admin-help/9054382.html)**を参照してください。  ### 管理対象の権限設定 DPFでは、管理対象となるサービスやゾーン単位での参照、編集権限を細かく設定できます。\\ アクセストークンの許可するスコープが適切であっても、管理対象の権限が付与されていない場合はAPIを実行できません。\\ 管理対象の権限設定のマニュアルは**[こちら](https://manual.iij.jp/dpf/help/19004706.html#IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B-IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%B8%E7%AE%A1%E7%90%86%E6%A8%A9%E9%99%90%E3%82%92%E4%BB%98%E4%B8%8E%E3%81%99%E3%82%8B)**を参照してください。  ## HTTPリクエスト  ### 例 ``` <HTTPメソッド> /dpf/<version>/<APIパス> HTTP/1.1 Host: api.dns-platform.jp Authorization: Bearer <access_token> Content-Type: application/json; charset=UTF-8  <HTTPリクエストボディ: JSON形式のAPI固有のパラメータ> ```  ### リクエストパラメータ DPF-APIで指定するパラメータは以下のとおりです。\\ リクエストパラメータに同一のキーが含まれる場合の動作は保証されません。  共通 | 指定箇所 | パラメータ | 意味 -----|----------|------------|----- 共通 | HTTPメソッド | HTTPメソッド | HTTPメソッド（値：GET、PATCH、POST、DELETE） 共通 | URL | version | DPF-APIバージョン（値：v1） 個別 | URL | APIパス | API名称やAPI個別のパラメータの組み合わせ（参照：**[API一覧](#section/API)**） 共通 | HTTPヘッダー | access_token | IIJ IDアクセストークン（参照：**[IIJ IDサービス](https://www.auth.iij.jp/console/)**） 個別 | HTTPボディ | APIごとに異なる | JSON形式のパラメータ（参照：**[API一覧](#section/API)**）  ## HTTPレスポンス  ### 成功レスポンス APIごとにレスポンスが異なりますので、**[該当のAPI](#section/API)**を参照してください。  ### エラーレスポンス HTTPステータスコード、及びレスポンスボディによってクライアントプログラムにエラーを通知します。  #### 例：アクセストークンが誤っている ``` {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"error_type\": \"ParameterError\",   \"error_message\": \"There are invalid parameters.\",   \"error_details\": [     {       \"code\": \"invalid\",       \"attribute\": \"access_token\"     }   ] } ```  #### エラーコード一覧 HTTP Status Code | error_type | error_message | code | attribute | 説明 | 対処方法 -----------------|------------|---------------|------|-----------|------|--------- 400 | ParameterError | There are invalid parameters. | invalid | access_token | 指定したアクセストークンに誤りがあります | アクセストークンを確認してください 400 | ParameterError | JSON parse error occurred. | - | - | パラメータとして不正なJSON文字列が指定されました | リクエストのパラメータを確認してください 400 | ParameterError | There are invalid parameters. | （API個別） | （API個別） | 不正なパラメータが指定されました | 各APIのエラーコードを確認してください 404 | NotFound | Specified resource not found. | - | - | アクセスURLが正しくありません <br> 存在しないAPIが指定されました <br> 指定された以外のHTTPメソッドが指定されました | 左記の内容を確認してください 429 | TooManyRequests | Too many requests. | - | - | 大量のAPIリクエストが送信されました | 単位時間当たりのAPIリクエスト数を確認してください 500 | SystemError | System error occurred. | - | - | システム障害が発生しました | **[サポートセンター](https://help.iij.ad.jp/)**へお問い合わせください 504 | GatewayTimeout | Gateway timeout. | - | - | リクエストがタイムアウトしました | しばらく待ってから再度リクエストしてください  ## 非同期リクエスト  DPF-APIにおけるGET以外のAPIは全て非同期APIです。\\ 非同期APIはリクエストを受け付けると即座にレスポンスを返却しますが、\\ リクエストに対する実際の処理は非同期で行われます。  非同期リクエストの受け付けに成功した場合のHTTPステータスコードは202で、\\ 返却されたレスポンスボディには、処理進捗を確認するためのURL（jobs_url）が含まれます。\\ このjobs_urlに対してGETリクエストをすることで進捗状況を確認できます。  進捗状況を確認した際、非同期処理が正常に終了していた場合は、\\ 返却されたレスポンスボディには、対象リソースを取得するためのURL（resources_url）が含まれます。\\ このresources_urlに対してGETリクエストをすることで実行結果を確認できます。  ### 例 #### 非同期リクエストのレスポンス ``` HTTP/1.1 202 Accepted Date: Mon, 26 Mar 20XX hh:mm:dd GMT Content-Type: application/json; charset=utf-8 〜 略 〜  {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"jobs_url\": \"https://api.dns-platform.jp/dpf/<version>/jobs/<request_id>\" } ```  #### GETリクエスト ``` GET /dpf/<version>/jobs/<request_id> HTTP/1.1 Host: api.dns-platform.jp Authorization: Bearer <access_token> Content-Type: application/json; charset=UTF-8  {} ```  #### 進捗状況のレスポンス ``` HTTP/1.1 200 OK Date: Mon, 26 Mar 20XX hh:mm:dd GMT Content-Type: application/json; charset=utf-8 〜 略 〜  {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"resources_url\": <resources_url>,   \"status\": \"SUCCESSFUL\" } ```  # API一覧 DPF-APIではIIJ DNSプラットフォームサービスに関する以下の操作を行うことができます。  ## IIJ DNSプラットフォームサービス  ### cc_primaries   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/get) | プライマリネームサーバ設定の一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/post) | プライマリネームサーバ設定の作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/get) | プライマリネームサーバ設定の取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/patch) | プライマリネームサーバ設定の更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/delete) | プライマリネームサーバ設定の削除 | dpf_write  ### cc_sec_notified_servers   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/get) | DNS NOTIFY設定の一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/post) | DNS NOTIFY設定の作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/get) | DNS NOTIFY設定の取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/patch) | DNS NOTIFY設定の更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/delete) | DNS NOTIFY設定の削除 | dpf_write  ### cc_sec_transfer_acls   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/get) | ゾーン転送ACLの一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/post) | ゾーン転送ACLの作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/get) | ゾーン転送ACLの取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/patch) | ゾーン転送ACLの更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/delete) | ゾーン転送ACLの削除 | dpf_write  ### common_configs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/get) | 共通設定の一覧取得 | dpf_read   POST | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/post) | 共通設定の作成 | dpf_write   GET | [/contracts/{ContractId}/common_configs/count](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1count/get) | 共通設定の件数取得 | dpf_read   PATCH | [/contracts/{ContractId}/common_configs/default](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1default/patch) | 初期適用される共通設定の更新 | dpf_write   GET | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/get) | 共通設定の取得 | dpf_read   PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/patch) | 共通設定の更新 | dpf_write   DELETE | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/delete) | 共通設定の削除 | dpf_write   POST | [/contracts/{ContractId}/common_configs/{CommonConfigId}/copy](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1copy/post) | 共通設定のコピー | dpf_write   PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}/managed_dns](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1managed_dns/patch) | マネージドDNSサーバの状態更新 | dpf_write  ### contracts   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts](#tag/contracts/paths/~1contracts/get) | DPF契約情報の一覧取得 | dpf_read   GET | [/contracts/count](#tag/contracts/paths/~1contracts~1count/get) | DPF契約情報の件数取得 | dpf_read   GET | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/get) | DPF契約情報の取得 | dpf_read   PATCH | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/patch) | DPF契約情報の更新 | dpf_write  ### contract_partners   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/contract_partners](#tag/contract_partners/paths/~1contracts~1{ContractId}~1contract_partners/get) | DPF連携サービスの一覧取得 | dpf_read  ### logs (contracts)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/logs](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs/get) | DPF契約操作ログの一覧取得 | dpf_read   GET | [/contracts/{ContractId}/logs/count](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs~1count/get) | DPF契約操作ログの件数取得 | dpf_read  ### qps HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/qps/histories](#tag/qps/paths/~1contracts~1{ContractId}~1qps~1histories/get) | 月別のQPSの一覧取得 | dpf_read  ### tsigs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/get) | TSIG鍵の一覧取得 | dpf_read   POST | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/post) | TSIG鍵の作成 | dpf_write   GET | [/contracts/{ContractId}/tsigs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1count/get) | TSIG鍵の件数取得 | dpf_read   GET | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/get) | TSIG鍵の取得 | dpf_read   PATCH | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/patch) | TSIG鍵の更新 | dpf_write   DELETE | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/delete) | TSIG鍵の削除 | dpf_write   GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs/get) | TSIG鍵を利用している共通設定の一覧取得 | dpf_read   GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs~1count/get) | TSIG鍵を利用している共通設定の件数取得 | dpf_read  ### zones (contracts)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/zones](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones/get) | DPF契約に紐付くゾーンの一覧取得 | dpf_read   PATCH | [/contracts/{ContractId}/zones/common_configs](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1common_configs/patch) | DPF契約に紐付くゾーンの共通設定の更新 | dpf_write   GET | [/contracts/{ContractId}/zones/count](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1count/get) | DPF契約に紐付くゾーンの件数取得 | dpf_read  ## IIJマネージドDNSサービス  ### default_ttl   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/get) | デフォルトTTLの取得 | dpf_read   PATCH | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/patch) | デフォルトTTLの更新 | dpf_write   DELETE | [/zones/{ZoneId}/default_ttl/changes](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1changes/delete) | 編集中デフォルトTTLの取消 | dpf_write   GET | [/zones/{ZoneId}/default_ttl/diffs](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1diffs/get) | デフォルトTTLの編集差分の取得 | dpf_read  ### dnssec   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/get) | DNSSEC情報の取得 | dpf_read   PATCH | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/patch) | DNSSEC情報の更新 | dpf_write   PATCH | [/zones/{ZoneId}/dnssec/ksk_rollover](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec~1ksk_rollover/patch) | KSKロールオーバーの開始 | dpf_write  ### ds_records   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/ds_records](#tag/ds_records/paths/~1zones~1{ZoneId}~1ds_records/get) | DSレコードの一覧取得 | dpf_read  ### logs (zones)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/logs](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs/get) | ゾーン操作ログの一覧取得 | dpf_read   GET | [/zones/{ZoneId}/logs/count](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs~1count/get) | ゾーン操作ログの件数取得 | dpf_read  ### records   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/get) | レコードの一覧取得 | dpf_read   POST | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/post) | レコードの作成 | dpf_write   GET | [/zones/{ZoneId}/records/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1count/get) | レコードの件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/currents](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents/get) | DNS反映済レコードの一覧取得 | dpf_read   GET | [/zones/{ZoneId}/records/currents/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents~1count/get) | DNS反映済レコードの件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/diffs](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs/get) | レコードの編集差分の一覧取得 | dpf_read   GET | [/zones/{ZoneId}/records/diffs/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs~1count/get) | レコードの編集差分の件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/get) | レコードの取得 | dpf_read   PATCH | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/patch) | レコードの更新 | dpf_write   DELETE | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/delete) | レコードの削除 | dpf_write   DELETE | [/zones/{ZoneId}/records/{RecordId}/changes](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}~1changes/delete) | 編集中レコードの取消 | dpf_write  ### zone_histories   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/zone_histories](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories/get) | ゾーン反映履歴の一覧取得 | dpf_read   GET | [/zones/{ZoneId}/zone_histories/count](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1count/get) | ゾーン反映履歴の件数取得 | dpf_read   GET | [/zones/{ZoneId}/zone_histories/{ZoneHistoryId}/text](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1{ZoneHistoryId}~1text/get) | ゾーン反映時のRFC1035形式のテキストの取得 | dpf_read  ### zone_proxy   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/get) | ゾーンプロキシ設定の取得 | dpf_read   PATCH | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/patch) | ゾーンプロキシ設定の更新 | dpf_write   GET | [/zones/{ZoneId}/zone_proxy/health_check](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy~1health_check/get) | プライマリネームサーバのヘルスチェック結果の取得 | dpf_read  ### zones   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones](#tag/zones/paths/~1zones/get) | ゾーンの一覧取得 | dpf_read   GET | [/zones/count](#tag/zones/paths/~1zones~1count/get) | ゾーンの件数取得 | dpf_read   GET | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/get) | ゾーンの取得 | dpf_read   PATCH | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/patch) | ゾーンの更新 | dpf_write   PATCH | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch) | 編集中レコードのゾーン反映 | dpf_write   DELETE | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/delete) | 編集中レコードの一括取消 | dpf_write   GET | [/zones/{ZoneId}/contract](#tag/zones/paths/~1zones~1{ZoneId}~1contract/get) | ゾーンに紐付くDPF契約情報の取得 | dpf_read   GET | [/zones/{ZoneId}/managed_dns_servers](#tag/zones/paths/~1zones~1{ZoneId}~1managed_dns_servers/get) | マネージドDNSサーバの一覧取得 | dpf_read  ## サービス共通  ### delegations   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/delegations](#tag/delegations/paths/~1delegations/get) | ネームサーバ申請候補の一覧取得 | dpf_read   POST | [/delegations](#tag/delegations/paths/~1delegations/post) | ネームサーバ申請 | dpf_write   GET | [/delegations/count](#tag/delegations/paths/~1delegations~1count/get) | ネームサーバ申請候補の件数取得 | dpf_read  ### jobs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/jobs/{RequestId}](#tag/jobs/paths/~1jobs~1{RequestId}/get) | 非同期リクエストの状態確認 | dpf_read  ### ping   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/ping](#tag/ping/paths/~1ping/get) | API疎通確認 | dpf_read, dpf_write, dpf_contract   # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import json
import atexit
import mimetypes
from multiprocessing.pool import ThreadPool
import io
import os
import re
import typing
from urllib.parse import quote
from urllib3.fields import RequestField


from openapi_client import rest
from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiTypeError, ApiValueError, ApiException
from openapi_client.model_utils import (
    ModelNormal,
    ModelSimple,
    ModelComposed,
    check_allowed_values,
    check_validations,
    date,
    datetime,
    deserialize_file,
    file_type,
    model_to_dict,
    none_type,
    validate_and_convert_types
)


class ApiClient(object):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    _pool = None

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1):
        if configuration is None:
            configuration = Configuration.get_default_copy()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)

    @property
    def pool(self):
        """Create thread pool on first request
         avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
        _content_type: typing.Optional[str] = None,
        _request_auths: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    ):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
            post_params.extend(self.files_parameters(files))
            if header_params['Content-Type'].startswith("multipart"):
                post_params = self.parameters_to_multipart(post_params,
                                                          (dict) )

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # auth setting
        self.update_params_for_auth(header_params, query_params,
                                    auth_settings, resource_path, method, body,
                                    request_auths=_request_auths)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        try:
            # perform request and return response
            response_data = self.request(
                method, url, query_params=query_params, headers=header_params,
                post_params=post_params, body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout)
        except ApiException as e:
            e.body = e.body.decode('utf-8')
            raise e

        self.last_response = response_data

        return_data = response_data

        if not _preload_content:
            return (return_data)
            return return_data

        # deserialize response data
        if response_type:
            if response_type != (file_type,):
                encoding = "utf-8"
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s\;]?", content_type)
                    if match:
                        encoding = match.group(1)
                response_data.data = response_data.data.decode(encoding)

            return_data = self.deserialize(
                response_data,
                response_type,
                _check_type
            )
        else:
            return_data = None

        if _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def parameters_to_multipart(self, params, collection_types):
        """Get parameters as list of tuples, formatting as json if value is collection_types

        :param params: Parameters as list of two-tuples
        :param dict collection_types: Parameter collection types
        :return: Parameters as list of tuple or urllib3.fields.RequestField
        """
        new_params = []
        if collection_types is None:
            collection_types = (dict)
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if isinstance(v, collection_types): # v is instance of collection_type, formatting as application/json
                 v = json.dumps(v, ensure_ascii=False).encode("utf-8")
                 field = RequestField(k, v)
                 field.make_multipart(content_type="application/json; charset=utf-8")
                 new_params.append(field)
            else:
                 new_params.append((k, v))
        return new_params

    @classmethod
    def sanitize_for_serialization(cls, obj):
        """Prepares data for transmission before it is sent with the rest client
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.
        If obj is io.IOBase, return the bytes
        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if isinstance(obj, (ModelNormal, ModelComposed)):
            return {
                key: cls.sanitize_for_serialization(val) for key, val in model_to_dict(obj, serialize=True).items()
            }
        elif isinstance(obj, io.IOBase):
            return cls.get_file_data_and_close_file(obj)
        elif isinstance(obj, (str, int, float, none_type, bool)):
            return obj
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, ModelSimple):
            return cls.sanitize_for_serialization(obj.value)
        elif isinstance(obj, (list, tuple)):
            return [cls.sanitize_for_serialization(item) for item in obj]
        if isinstance(obj, dict):
            return {key: cls.sanitize_for_serialization(val) for key, val in obj.items()}
        raise ApiValueError('Unable to prepare type {} for serialization'.format(obj.__class__.__name__))

    def deserialize(self, response, response_type, _check_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param _check_type: boolean, whether to check the types of the data
            received from the server
        :type _check_type: bool

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == (file_type,):
            content_disposition = response.getheader("Content-Disposition")
            return deserialize_file(response.data, self.configuration,
                                    content_disposition=content_disposition)

        # fetch data from response object
        try:
            received_data = json.loads(response.data)
        except ValueError:
            received_data = response.data

        # store our data under the key of 'received_data' so users have some
        # context if they are deserializing a string and the data type is wrong
        deserialized_data = validate_and_convert_types(
            received_data,
            response_type,
            ['received_data'],
            True,
            _check_type,
            configuration=self.configuration
        )
        return deserialized_data

    def call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        async_req: typing.Optional[bool] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
        _request_auths: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    ):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param files: key -> field name, value -> a list of open file
            objects for `multipart/form-data`.
        :type files: dict
        :param async_req bool: execute request asynchronously
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :type collection_formats: dict, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _check_type: boolean describing if the data back from the server
            should have its type checked.
        :type _check_type: bool, optional
        :param _request_auths: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auths: list, optional
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings,
                                   _return_http_data_only, collection_formats,
                                   _preload_content, _request_timeout, _host,
                                   _check_type, _request_auths=_request_auths)

        return self.pool.apply_async(self.__call_api, (resource_path,
                                                       method, path_params,
                                                       query_params,
                                                       header_params, body,
                                                       post_params, files,
                                                       response_type,
                                                       auth_settings,
                                                       _return_http_data_only,
                                                       collection_formats,
                                                       _preload_content,
                                                       _request_timeout,
                                                       _host, _check_type, None, _request_auths))

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    @staticmethod
    def get_file_data_and_close_file(file_instance: io.IOBase) -> bytes:
        file_data = file_instance.read()
        file_instance.close()
        return file_data

    def files_parameters(self, files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None):
        """Builds form parameters.

        :param files: None or a dict with key=param_name and
            value is a list of open file objects
        :return: List of tuples of form parameters with file data
        """
        if files is None:
            return []

        params = []
        for param_name, file_instances in files.items():
            if file_instances is None:
                # if the file field is nullable, skip None values
                continue
            for file_instance in file_instances:
                if file_instance is None:
                    # if the file field is nullable, skip None values
                    continue
                if file_instance.closed is True:
                    raise ApiValueError(
                        "Cannot read a closed file. The passed in file_type "
                        "for %s must be open." % param_name
                    )
                filename = os.path.basename(file_instance.name)
                filedata = self.get_file_data_and_close_file(file_instance)
                mimetype = (mimetypes.guess_type(filename)[0] or
                            'application/octet-stream')
                params.append(
                    tuple([param_name, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types, method=None, body=None):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :param method: http method (e.g. POST, PATCH).
        :param body: http body to send.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        content_types = [x.lower() for x in content_types]

        if (method == 'PATCH' and
                'application/json-patch+json' in content_types and
                isinstance(body, list)):
            return 'application/json-patch+json'

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, queries, auth_settings,
                               resource_path, method, body, request_auths=None):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :param resource_path: A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method.
        :param body: A object representing the body of the HTTP request.
            The object type is the return value of _encoder.default().
        :param request_auths: if set, the provided settings will
            override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auths:
            for auth_setting in request_auths:
                self._apply_auth_params(headers, queries, resource_path, method, body, auth_setting)
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                self._apply_auth_params(headers, queries, resource_path, method, body, auth_setting)

    def _apply_auth_params(self, headers, queries, resource_path, method, body, auth_setting):
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (tuple/None): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only',
            '_check_input_type',
            '_check_return_type',
            '_content_type',
            '_spec_property_naming',
            '_request_auths'
        ])
        self.params_map['nullable'].extend(['_request_timeout'])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        extra_types = {
            'async_req': (bool,),
            '_host_index': (none_type, int),
            '_preload_content': (bool,),
            '_request_timeout': (none_type, float, (float,), [float], int, (int,), [int]),
            '_return_http_data_only': (bool,),
            '_check_input_type': (bool,),
            '_check_return_type': (bool,),
            '_spec_property_naming': (bool,),
            '_content_type': (none_type, str),
            '_request_auths': (none_type, list)
        }
        self.openapi_types.update(extra_types)
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param]
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param],
                    configuration=self.api_client.configuration
                )

        if kwargs['_check_input_type'] is False:
            return

        for key, value in kwargs.items():
            fixed_val = validate_and_convert_types(
                value,
                self.openapi_types[key],
                [key],
                kwargs['_spec_property_naming'],
                kwargs['_check_input_type'],
                configuration=self.api_client.configuration
            )
            kwargs[key] = fixed_val

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in kwargs.items():
            param_location = self.location_map.get(param_name)
            if param_location is None:
                continue
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == (file_type,)):
                    params['file'][base_name] = [param_value]
                elif (param_location == 'form' and
                        self.openapi_types[param_name] == ([file_type],)):
                    # param_value is already a list
                    params['file'][base_name] = param_value
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:

        api_instance = CcPrimariesApi()
        api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_delete  # this is an instance of the class Endpoint
        api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_delete()  # this invokes api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_delete.__call__()
        which then invokes the callable functions stored in that endpoint at
        api_instance.common_configs_common_config_id_cc_primaries_cc_primary_id_delete.callable or self.callable in this class

        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        try:
            index = self.api_client.configuration.server_operation_index.get(
                self.settings['operation_id'], self.api_client.configuration.server_index
            ) if kwargs['_host_index'] is None else kwargs['_host_index']
            server_variables = self.api_client.configuration.server_operation_variables.get(
                self.settings['operation_id'], self.api_client.configuration.server_variables
            )
            _host = self.api_client.configuration.get_host_from_settings(
                index, variables=server_variables, servers=self.settings['servers']
            )
        except IndexError:
            if self.settings['servers']:
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s" %
                    len(self.settings['servers'])
                )
            _host = None

        for key, value in kwargs.items():
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    " to method `%s`" %
                    (key, self.settings['operation_id'])
                )
            # only throw this nullable ApiValueError if _check_input_type
            # is False, if _check_input_type==True we catch this case
            # in self.__validate_inputs
            if (key not in self.params_map['nullable'] and value is None
                    and kwargs['_check_input_type'] is False):
                raise ApiValueError(
                    "Value may not be None for non-nullable parameter `%s`"
                    " when calling `%s`" %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    "Missing the required parameter `%s` when calling "
                    "`%s`" % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        if kwargs.get('_content_type'):
            params['header']['Content-Type'] = kwargs['_content_type']
        else:
            content_type_headers_list = self.headers_map['content_type']
            if content_type_headers_list:
                if params['body'] != "":
                    content_types_list = self.api_client.select_header_content_type(
                        content_type_headers_list, self.settings['http_method'],
                        params['body'])
                    if content_types_list:
                        params['header']['Content-Type'] = content_types_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs['async_req'],
            _check_type=kwargs['_check_return_type'],
            _return_http_data_only=kwargs['_return_http_data_only'],
            _preload_content=kwargs['_preload_content'],
            _request_timeout=kwargs['_request_timeout'],
            _host=_host,
            _request_auths=kwargs['_request_auths'],
            collection_formats=params['collection_format'])
