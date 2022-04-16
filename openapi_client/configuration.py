"""
    DPF-APIリファレンスマニュアル

    # はじめに  ## DPF-APIについて IIJ DNSプラットフォームサービスでは、DNSレコードやゾーン情報などを、\\ お客様が用意したプログラムから自動的に操作するためのAPI機能を提供しています。\\ 以降、IIJ DNSプラットフォームサービスを「DPF」、DPFが提供するAPIを「DPF-API」あるいは単に「API」と表記します。\\ DPF-APIの利用には、DPFの契約とIIJ IDサービスの契約が必要となります。  本リファレンスマニュアルは**[OpenAPI](https://www.openapis.org/)**に準拠しています。  ## サポート範囲 DPF-APIを呼び出すためのプログラム、及びそのプログラムを稼働させるためのサーバは、お客様にてご用意ください。\\ お客様にご用意いただくプログラムの開発、利用、動作についてのお問い合わせは承ることができません。  以下の事項についてのお問い合わせは、弊社**[サポートセンター](https://help.iij.ad.jp/)**にて承ります。 - DPF-APIの挙動が本リファレンスマニュアルと異なる場合 - DPF-APIがシステムエラーを応答した場合  ## 参考資料 - IIJ DNSプラットフォームサービス オンラインマニュアル   - [https://manual.iij.jp/dpf/help/](https://manual.iij.jp/dpf/help/)  - IIJ IDサービス オンラインマニュアル   - [https://manual.iij.jp/iid/admin-help/](https://manual.iij.jp/iid/admin-help/)  # 利用方法 DPF-APIは、URLとHTTPリクエストヘッダ、HTTPリクエストボディでパラメータを指定して利用します。\\ また、IIJ IDサービスのアクセストークンと管理対象の権限設定が必要です。  ## リクエスト仕様  項目 | 規格 -----|----- プロトコル | HTTP/1.1、HTTP/2（https） HTTPメソッド | GET、PATCH、POST、DELETE フォーマット | JSON 文字コード | UTF-8 タイムアウト | 300秒  - httpでのリクエストは受け付けません。必ずhttpsを使用してください。 - DPF-APIを呼び出すプログラムは、リクエスト先が正当なものであることを確認するため、SSL証明書を検証することを推奨します。 - 短期間に極めて多数のリクエストが行われた場合、サービスの健全性を保つためにリクエストを制限する場合があります。  ### アクセストークン APIリクエストの際にIIJ IDサービスによって発行されたアクセストークンをAuthorizationヘッダに指定する必要があります。\\ 各APIにより必要となるアクセス権の範囲（許可するスコープ）が異なるのでご注意ください。  アクセストークン作成時に指定できる「許可するスコープ」は以下のとおりです。  許可するスコープ | 実行できるAPI -----------------|------------ dpf_read | 参照系API dpf_write | 更新系、及び参照系API dpf_contract | 契約系API  発行済のアクセストークンは、**[IIJ IDサービス](https://www.auth.iij.jp/console/)**の「アクセストークンの管理」より確認できます。\\ DPF-APIを利用する場合は「利用するリソースサーバ」の設定で「IIJ DNSサービスAPI」を選択してください。\\ アクセストークン管理方法のマニュアルは**[こちら](https://manual.iij.jp/iid/admin-help/9054382.html)**を参照してください。  ### 管理対象の権限設定 DPFでは、管理対象となるサービスやゾーン単位での参照、編集権限を細かく設定できます。\\ アクセストークンの許可するスコープが適切であっても、管理対象の権限が付与されていない場合はAPIを実行できません。\\ 管理対象の権限設定のマニュアルは**[こちら](https://manual.iij.jp/dpf/help/19004706.html#IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B-IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%B8%E7%AE%A1%E7%90%86%E6%A8%A9%E9%99%90%E3%82%92%E4%BB%98%E4%B8%8E%E3%81%99%E3%82%8B)**を参照してください。  ## HTTPリクエスト  ### 例 ``` <HTTPメソッド> /dpf/<version>/<APIパス> HTTP/1.1 Host: api.dns-platform.jp Authorization: Bearer <access_token> Content-Type: application/json; charset=UTF-8  <HTTPリクエストボディ: JSON形式のAPI固有のパラメータ> ```  ### リクエストパラメータ DPF-APIで指定するパラメータは以下のとおりです。\\ リクエストパラメータに同一のキーが含まれる場合の動作は保証されません。  共通 | 指定箇所 | パラメータ | 意味 -----|----------|------------|----- 共通 | HTTPメソッド | HTTPメソッド | HTTPメソッド（値：GET、PATCH、POST、DELETE） 共通 | URL | version | DPF-APIバージョン（値：v1） 個別 | URL | APIパス | API名称やAPI個別のパラメータの組み合わせ（参照：**[API一覧](#section/API)**） 共通 | HTTPヘッダー | access_token | IIJ IDアクセストークン（参照：**[IIJ IDサービス](https://www.auth.iij.jp/console/)**） 個別 | HTTPボディ | APIごとに異なる | JSON形式のパラメータ（参照：**[API一覧](#section/API)**）  ## HTTPレスポンス  ### 成功レスポンス APIごとにレスポンスが異なりますので、**[該当のAPI](#section/API)**を参照してください。  ### エラーレスポンス HTTPステータスコード、及びレスポンスボディによってクライアントプログラムにエラーを通知します。  #### 例：アクセストークンが誤っている ``` {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"error_type\": \"ParameterError\",   \"error_message\": \"There are invalid parameters.\",   \"error_details\": [     {       \"code\": \"invalid\",       \"attribute\": \"access_token\"     }   ] } ```  #### エラーコード一覧 HTTP Status Code | error_type | error_message | code | attribute | 説明 | 対処方法 -----------------|------------|---------------|------|-----------|------|--------- 400 | ParameterError | There are invalid parameters. | invalid | access_token | 指定したアクセストークンに誤りがあります | アクセストークンを確認してください 400 | ParameterError | JSON parse error occurred. | - | - | パラメータとして不正なJSON文字列が指定されました | リクエストのパラメータを確認してください 400 | ParameterError | There are invalid parameters. | （API個別） | （API個別） | 不正なパラメータが指定されました | 各APIのエラーコードを確認してください 404 | NotFound | Specified resource not found. | - | - | アクセスURLが正しくありません <br> 存在しないAPIが指定されました <br> 指定された以外のHTTPメソッドが指定されました | 左記の内容を確認してください 429 | TooManyRequests | Too many requests. | - | - | 大量のAPIリクエストが送信されました | 単位時間当たりのAPIリクエスト数を確認してください 500 | SystemError | System error occurred. | - | - | システム障害が発生しました | **[サポートセンター](https://help.iij.ad.jp/)**へお問い合わせください 504 | GatewayTimeout | Gateway timeout. | - | - | リクエストがタイムアウトしました | しばらく待ってから再度リクエストしてください  ## 非同期リクエスト  DPF-APIにおけるGET以外のAPIは全て非同期APIです。\\ 非同期APIはリクエストを受け付けると即座にレスポンスを返却しますが、\\ リクエストに対する実際の処理は非同期で行われます。  非同期リクエストの受け付けに成功した場合のHTTPステータスコードは202で、\\ 返却されたレスポンスボディには、処理進捗を確認するためのURL（jobs_url）が含まれます。\\ このjobs_urlに対してGETリクエストをすることで進捗状況を確認できます。  進捗状況を確認した際、非同期処理が正常に終了していた場合は、\\ 返却されたレスポンスボディには、対象リソースを取得するためのURL（resources_url）が含まれます。\\ このresources_urlに対してGETリクエストをすることで実行結果を確認できます。  ### 例 #### 非同期リクエストのレスポンス ``` HTTP/1.1 202 Accepted Date: Mon, 26 Mar 20XX hh:mm:dd GMT Content-Type: application/json; charset=utf-8 〜 略 〜  {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"jobs_url\": \"https://api.dns-platform.jp/dpf/<version>/jobs/<request_id>\" } ```  #### GETリクエスト ``` GET /dpf/<version>/jobs/<request_id> HTTP/1.1 Host: api.dns-platform.jp Authorization: Bearer <access_token> Content-Type: application/json; charset=UTF-8  {} ```  #### 進捗状況のレスポンス ``` HTTP/1.1 200 OK Date: Mon, 26 Mar 20XX hh:mm:dd GMT Content-Type: application/json; charset=utf-8 〜 略 〜  {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"resources_url\": <resources_url>,   \"status\": \"SUCCESSFUL\" } ```  # API一覧 DPF-APIではIIJ DNSプラットフォームサービスに関する以下の操作を行うことができます。  ## IIJ DNSプラットフォームサービス  ### cc_primaries   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/get) | プライマリネームサーバ設定の一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/post) | プライマリネームサーバ設定の作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/get) | プライマリネームサーバ設定の取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/patch) | プライマリネームサーバ設定の更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/delete) | プライマリネームサーバ設定の削除 | dpf_write  ### cc_sec_notified_servers   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/get) | DNS NOTIFY設定の一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/post) | DNS NOTIFY設定の作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/get) | DNS NOTIFY設定の取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/patch) | DNS NOTIFY設定の更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/delete) | DNS NOTIFY設定の削除 | dpf_write  ### cc_sec_transfer_acls   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/get) | ゾーン転送ACLの一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/post) | ゾーン転送ACLの作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/get) | ゾーン転送ACLの取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/patch) | ゾーン転送ACLの更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/delete) | ゾーン転送ACLの削除 | dpf_write  ### common_configs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/get) | 共通設定の一覧取得 | dpf_read   POST | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/post) | 共通設定の作成 | dpf_write   GET | [/contracts/{ContractId}/common_configs/count](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1count/get) | 共通設定の件数取得 | dpf_read   PATCH | [/contracts/{ContractId}/common_configs/default](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1default/patch) | 初期適用される共通設定の更新 | dpf_write   GET | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/get) | 共通設定の取得 | dpf_read   PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/patch) | 共通設定の更新 | dpf_write   DELETE | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/delete) | 共通設定の削除 | dpf_write   POST | [/contracts/{ContractId}/common_configs/{CommonConfigId}/copy](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1copy/post) | 共通設定のコピー | dpf_write   PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}/managed_dns](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1managed_dns/patch) | マネージドDNSサーバの状態更新 | dpf_write  ### contracts   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts](#tag/contracts/paths/~1contracts/get) | DPF契約情報の一覧取得 | dpf_read   GET | [/contracts/count](#tag/contracts/paths/~1contracts~1count/get) | DPF契約情報の件数取得 | dpf_read   GET | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/get) | DPF契約情報の取得 | dpf_read   PATCH | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/patch) | DPF契約情報の更新 | dpf_write  ### contract_partners   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/contract_partners](#tag/contract_partners/paths/~1contracts~1{ContractId}~1contract_partners/get) | DPF連携サービスの一覧取得 | dpf_read  ### logs (contracts)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/logs](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs/get) | DPF契約操作ログの一覧取得 | dpf_read   GET | [/contracts/{ContractId}/logs/count](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs~1count/get) | DPF契約操作ログの件数取得 | dpf_read  ### qps HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/qps/histories](#tag/qps/paths/~1contracts~1{ContractId}~1qps~1histories/get) | 月別のQPSの一覧取得 | dpf_read  ### tsigs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/get) | TSIG鍵の一覧取得 | dpf_read   POST | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/post) | TSIG鍵の作成 | dpf_write   GET | [/contracts/{ContractId}/tsigs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1count/get) | TSIG鍵の件数取得 | dpf_read   GET | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/get) | TSIG鍵の取得 | dpf_read   PATCH | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/patch) | TSIG鍵の更新 | dpf_write   DELETE | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/delete) | TSIG鍵の削除 | dpf_write   GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs/get) | TSIG鍵を利用している共通設定の一覧取得 | dpf_read   GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs~1count/get) | TSIG鍵を利用している共通設定の件数取得 | dpf_read  ### zones (contracts)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/zones](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones/get) | DPF契約に紐付くゾーンの一覧取得 | dpf_read   PATCH | [/contracts/{ContractId}/zones/common_configs](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1common_configs/patch) | DPF契約に紐付くゾーンの共通設定の更新 | dpf_write   GET | [/contracts/{ContractId}/zones/count](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1count/get) | DPF契約に紐付くゾーンの件数取得 | dpf_read  ## IIJマネージドDNSサービス  ### default_ttl   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/get) | デフォルトTTLの取得 | dpf_read   PATCH | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/patch) | デフォルトTTLの更新 | dpf_write   DELETE | [/zones/{ZoneId}/default_ttl/changes](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1changes/delete) | 編集中デフォルトTTLの取消 | dpf_write   GET | [/zones/{ZoneId}/default_ttl/diffs](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1diffs/get) | デフォルトTTLの編集差分の取得 | dpf_read  ### dnssec   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/get) | DNSSEC情報の取得 | dpf_read   PATCH | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/patch) | DNSSEC情報の更新 | dpf_write   PATCH | [/zones/{ZoneId}/dnssec/ksk_rollover](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec~1ksk_rollover/patch) | KSKロールオーバーの開始 | dpf_write  ### ds_records   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/ds_records](#tag/ds_records/paths/~1zones~1{ZoneId}~1ds_records/get) | DSレコードの一覧取得 | dpf_read  ### logs (zones)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/logs](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs/get) | ゾーン操作ログの一覧取得 | dpf_read   GET | [/zones/{ZoneId}/logs/count](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs~1count/get) | ゾーン操作ログの件数取得 | dpf_read  ### records   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/get) | レコードの一覧取得 | dpf_read   POST | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/post) | レコードの作成 | dpf_write   GET | [/zones/{ZoneId}/records/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1count/get) | レコードの件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/currents](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents/get) | DNS反映済レコードの一覧取得 | dpf_read   GET | [/zones/{ZoneId}/records/currents/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents~1count/get) | DNS反映済レコードの件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/diffs](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs/get) | レコードの編集差分の一覧取得 | dpf_read   GET | [/zones/{ZoneId}/records/diffs/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs~1count/get) | レコードの編集差分の件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/get) | レコードの取得 | dpf_read   PATCH | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/patch) | レコードの更新 | dpf_write   DELETE | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/delete) | レコードの削除 | dpf_write   DELETE | [/zones/{ZoneId}/records/{RecordId}/changes](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}~1changes/delete) | 編集中レコードの取消 | dpf_write  ### zone_histories   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/zone_histories](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories/get) | ゾーン反映履歴の一覧取得 | dpf_read   GET | [/zones/{ZoneId}/zone_histories/count](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1count/get) | ゾーン反映履歴の件数取得 | dpf_read   GET | [/zones/{ZoneId}/zone_histories/{ZoneHistoryId}/text](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1{ZoneHistoryId}~1text/get) | ゾーン反映時のRFC1035形式のテキストの取得 | dpf_read  ### zone_proxy   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/get) | ゾーンプロキシ設定の取得 | dpf_read   PATCH | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/patch) | ゾーンプロキシ設定の更新 | dpf_write   GET | [/zones/{ZoneId}/zone_proxy/health_check](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy~1health_check/get) | プライマリネームサーバのヘルスチェック結果の取得 | dpf_read  ### zones   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones](#tag/zones/paths/~1zones/get) | ゾーンの一覧取得 | dpf_read   GET | [/zones/count](#tag/zones/paths/~1zones~1count/get) | ゾーンの件数取得 | dpf_read   GET | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/get) | ゾーンの取得 | dpf_read   PATCH | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/patch) | ゾーンの更新 | dpf_write   PATCH | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch) | 編集中レコードのゾーン反映 | dpf_write   DELETE | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/delete) | 編集中レコードの一括取消 | dpf_write   GET | [/zones/{ZoneId}/contract](#tag/zones/paths/~1zones~1{ZoneId}~1contract/get) | ゾーンに紐付くDPF契約情報の取得 | dpf_read   GET | [/zones/{ZoneId}/managed_dns_servers](#tag/zones/paths/~1zones~1{ZoneId}~1managed_dns_servers/get) | マネージドDNSサーバの一覧取得 | dpf_read  ## サービス共通  ### delegations   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/delegations](#tag/delegations/paths/~1delegations/get) | ネームサーバ申請候補の一覧取得 | dpf_read   POST | [/delegations](#tag/delegations/paths/~1delegations/post) | ネームサーバ申請 | dpf_write   GET | [/delegations/count](#tag/delegations/paths/~1delegations~1count/get) | ネームサーバ申請候補の件数取得 | dpf_read  ### jobs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/jobs/{RequestId}](#tag/jobs/paths/~1jobs~1{RequestId}/get) | 非同期リクエストの状態確認 | dpf_read  ### ping   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/ping](#tag/ping/paths/~1ping/get) | API疎通確認 | dpf_read, dpf_write, dpf_contract   # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import copy
import logging
import multiprocessing
import sys
import urllib3

from http import client as http_client
from openapi_client.exceptions import ApiValueError


JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

class Configuration(object):
    """NOTE: This class is auto generated by OpenAPI Generator

    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param host: Base url
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer)
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication
    :param password: Password for HTTP basic authentication
    :param discard_unknown_keys: Boolean value indicating whether to discard
      unknown properties. A server may send a response that includes additional
      properties that are not known by the client in the following scenarios:
      1. The OpenAPI document is incomplete, i.e. it does not match the server
         implementation.
      2. The client was generated using an older version of the OpenAPI document
         and the server has been upgraded since then.
      If a schema in the OpenAPI document defines the additionalProperties attribute,
      then all undeclared properties received by the server are injected into the
      additional properties map. In that case, there are undeclared properties, and
      nothing to discard.
    :param disabled_client_side_validations (string): Comma-separated list of
      JSON schema validation keywords to disable JSON schema structural validation
      rules. The following keywords may be specified: multipleOf, maximum,
      exclusiveMaximum, minimum, exclusiveMinimum, maxLength, minLength, pattern,
      maxItems, minItems.
      By default, the validation is performed for data generated locally by the client
      and data received from the server, independent of any validation performed by
      the server side. If the input data does not satisfy the JSON schema validation
      rules specified in the OpenAPI document, an exception is raised.
      If disabled_client_side_validations is set, structural validation is
      disabled. This can be useful to troubleshoot data validation problem, such as
      when the OpenAPI document validation rules do not match the actual API data
      received by the server.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format

    """

    _default = None

    def __init__(self, host=None,
                 api_key=None, api_key_prefix=None,
                 access_token=None,
                 username=None, password=None,
                 discard_unknown_keys=False,
                 disabled_client_side_validations="",
                 server_index=None, server_variables=None,
                 server_operation_index=None, server_operation_variables=None,
                 ssl_ca_cert=None,
                 ):
        """Constructor
        """
        self._base_path = "https://api.dns-platform.jp/dpf/v1" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.access_token = access_token
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.discard_unknown_keys = discard_unknown_keys
        self.disabled_client_side_validations = disabled_client_side_validations
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("openapi_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy = None
        """Proxy URL
        """
        self.no_proxy = None
        """bypass proxy for host in the no_proxy list.
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        # Options to pass down to the underlying urllib3 socket
        self.socket_options = None

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == 'disabled_client_side_validations':
            s = set(filter(None, value.split(',')))
            for v in s:
                if v not in JSON_SCHEMA_VALIDATION_KEYWORDS:
                    raise ApiValueError(
                        "Invalid keyword: '{0}''".format(v))
            self._disabled_client_side_validations = s

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = copy.deepcopy(default)

    @classmethod
    def get_default_copy(cls):
        """Return new instance of configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration passed by the set_default method.

        :return: The configuration object.
        """
        if cls._default is not None:
            return copy.deepcopy(cls._default)
        return Configuration()

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on http_client debug
            http_client.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off http_client debug
            http_client.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://api.dns-platform.jp/dpf/v1",
                'description': "API endpoint",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None
