"""
    DPF-APIリファレンスマニュアル

    # はじめに  ## DPF-APIについて IIJ DNSプラットフォームサービスでは、DNSレコードやゾーン情報などを、\\ お客様が用意したプログラムから自動的に操作するためのAPI機能を提供しています。\\ 以降、IIJ DNSプラットフォームサービスを「DPF」、DPFが提供するAPIを「DPF-API」あるいは単に「API」と表記します。\\ DPF-APIの利用には、DPFの契約とIIJ IDサービスの契約が必要となります。  本リファレンスマニュアルは**[OpenAPI](https://www.openapis.org/)**に準拠しています。  ## サポート範囲 DPF-APIを呼び出すためのプログラム、及びそのプログラムを稼働させるためのサーバは、お客様にてご用意ください。\\ お客様にご用意いただくプログラムの開発、利用、動作についてのお問い合わせは承ることができません。  以下の事項についてのお問い合わせは、弊社**[サポートセンター](https://help.iij.ad.jp/)**にて承ります。 - DPF-APIの挙動が本リファレンスマニュアルと異なる場合 - DPF-APIがシステムエラーを応答した場合  ## 参考資料 - IIJ DNSプラットフォームサービス オンラインマニュアル   - [https://manual.iij.jp/dpf/help/](https://manual.iij.jp/dpf/help/)  - IIJ IDサービス オンラインマニュアル   - [https://manual.iij.jp/iid/admin-help/](https://manual.iij.jp/iid/admin-help/)  # 利用方法 DPF-APIは、URLとHTTPリクエストヘッダ、HTTPリクエストボディでパラメータを指定して利用します。\\ また、IIJ IDサービスのアクセストークンと管理対象の権限設定が必要です。  ## リクエスト仕様  項目 | 規格 -----|----- プロトコル | HTTP/1.1、HTTP/2（https） HTTPメソッド | GET、PATCH、POST、DELETE フォーマット | JSON 文字コード | UTF-8 タイムアウト | 300秒  - httpでのリクエストは受け付けません。必ずhttpsを使用してください。 - DPF-APIを呼び出すプログラムは、リクエスト先が正当なものであることを確認するため、SSL証明書を検証することを推奨します。 - 短期間に極めて多数のリクエストが行われた場合、サービスの健全性を保つためにリクエストを制限する場合があります。  ### アクセストークン APIリクエストの際にIIJ IDサービスによって発行されたアクセストークンをAuthorizationヘッダに指定する必要があります。\\ 各APIにより必要となるアクセス権の範囲（許可するスコープ）が異なるのでご注意ください。  アクセストークン作成時に指定できる「許可するスコープ」は以下のとおりです。  許可するスコープ | 実行できるAPI -----------------|------------ dpf_read | 参照系API dpf_write | 更新系、及び参照系API dpf_contract | 契約系API  発行済のアクセストークンは、**[IIJ IDサービス](https://www.auth.iij.jp/console/)**の「アクセストークンの管理」より確認できます。\\ DPF-APIを利用する場合は「利用するリソースサーバ」の設定で「IIJ DNSサービスAPI」を選択してください。\\ アクセストークン管理方法のマニュアルは**[こちら](https://manual.iij.jp/iid/admin-help/9054382.html)**を参照してください。  ### 管理対象の権限設定 DPFでは、管理対象となるサービスやゾーン単位での参照、編集権限を細かく設定できます。\\ アクセストークンの許可するスコープが適切であっても、管理対象の権限が付与されていない場合はAPIを実行できません。\\ 管理対象の権限設定のマニュアルは**[こちら](https://manual.iij.jp/dpf/help/19004706.html#IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B-IIJID%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%B8%E7%AE%A1%E7%90%86%E6%A8%A9%E9%99%90%E3%82%92%E4%BB%98%E4%B8%8E%E3%81%99%E3%82%8B)**を参照してください。  ## HTTPリクエスト  ### 例 ``` <HTTPメソッド> /dpf/<version>/<APIパス> HTTP/1.1 Host: api.dns-platform.jp Authorization: Bearer <access_token> Content-Type: application/json; charset=UTF-8  <HTTPリクエストボディ: JSON形式のAPI固有のパラメータ> ```  ### リクエストパラメータ DPF-APIで指定するパラメータは以下のとおりです。\\ リクエストパラメータに同一のキーが含まれる場合の動作は保証されません。  共通 | 指定箇所 | パラメータ | 意味 -----|----------|------------|----- 共通 | HTTPメソッド | HTTPメソッド | HTTPメソッド（値：GET、PATCH、POST、DELETE） 共通 | URL | version | DPF-APIバージョン（値：v1） 個別 | URL | APIパス | API名称やAPI個別のパラメータの組み合わせ（参照：**[API一覧](#section/API)**） 共通 | HTTPヘッダー | access_token | IIJ IDアクセストークン（参照：**[IIJ IDサービス](https://www.auth.iij.jp/console/)**） 個別 | HTTPボディ | APIごとに異なる | JSON形式のパラメータ（参照：**[API一覧](#section/API)**）  ## HTTPレスポンス  ### 成功レスポンス APIごとにレスポンスが異なりますので、**[該当のAPI](#section/API)**を参照してください。  ### エラーレスポンス HTTPステータスコード、及びレスポンスボディによってクライアントプログラムにエラーを通知します。  #### 例：アクセストークンが誤っている ``` {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"error_type\": \"ParameterError\",   \"error_message\": \"There are invalid parameters.\",   \"error_details\": [     {       \"code\": \"invalid\",       \"attribute\": \"access_token\"     }   ] } ```  #### エラーコード一覧 HTTP Status Code | error_type | error_message | code | attribute | 説明 | 対処方法 -----------------|------------|---------------|------|-----------|------|--------- 400 | ParameterError | There are invalid parameters. | invalid | access_token | 指定したアクセストークンに誤りがあります | アクセストークンを確認してください 400 | ParameterError | JSON parse error occurred. | - | - | パラメータとして不正なJSON文字列が指定されました | リクエストのパラメータを確認してください 400 | ParameterError | There are invalid parameters. | （API個別） | （API個別） | 不正なパラメータが指定されました | 各APIのエラーコードを確認してください 404 | NotFound | Specified resource not found. | - | - | アクセスURLが正しくありません <br> 存在しないAPIが指定されました <br> 指定された以外のHTTPメソッドが指定されました | 左記の内容を確認してください 429 | TooManyRequests | Too many requests. | - | - | 大量のAPIリクエストが送信されました | 単位時間当たりのAPIリクエスト数を確認してください 500 | SystemError | System error occurred. | - | - | システム障害が発生しました | **[サポートセンター](https://help.iij.ad.jp/)**へお問い合わせください 504 | GatewayTimeout | Gateway timeout. | - | - | リクエストがタイムアウトしました | しばらく待ってから再度リクエストしてください  ## 非同期リクエスト  DPF-APIにおけるGET以外のAPIは全て非同期APIです。\\ 非同期APIはリクエストを受け付けると即座にレスポンスを返却しますが、\\ リクエストに対する実際の処理は非同期で行われます。  非同期リクエストの受け付けに成功した場合のHTTPステータスコードは202で、\\ 返却されたレスポンスボディには、処理進捗を確認するためのURL（jobs_url）が含まれます。\\ このjobs_urlに対してGETリクエストをすることで進捗状況を確認できます。  進捗状況を確認した際、非同期処理が正常に終了していた場合は、\\ 返却されたレスポンスボディには、対象リソースを取得するためのURL（resources_url）が含まれます。\\ このresources_urlに対してGETリクエストをすることで実行結果を確認できます。  ### 例 #### 非同期リクエストのレスポンス ``` HTTP/1.1 202 Accepted Date: Mon, 26 Mar 20XX hh:mm:dd GMT Content-Type: application/json; charset=utf-8 〜 略 〜  {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"jobs_url\": \"https://api.dns-platform.jp/dpf/<version>/jobs/<request_id>\" } ```  #### GETリクエスト ``` GET /dpf/<version>/jobs/<request_id> HTTP/1.1 Host: api.dns-platform.jp Authorization: Bearer <access_token> Content-Type: application/json; charset=UTF-8  {} ```  #### 進捗状況のレスポンス ``` HTTP/1.1 200 OK Date: Mon, 26 Mar 20XX hh:mm:dd GMT Content-Type: application/json; charset=utf-8 〜 略 〜  {   \"request_id\": \"782d746ac3cb46499b31708fa80e8660\",   \"resources_url\": <resources_url>,   \"status\": \"SUCCESSFUL\" } ```  # API一覧 DPF-APIではIIJ DNSプラットフォームサービスに関する以下の操作を行うことができます。  ## IIJ DNSプラットフォームサービス  ### cc_primaries   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/get) | プライマリネームサーバ設定の一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_primaries](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries/post) | プライマリネームサーバ設定の作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/get) | プライマリネームサーバ設定の取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/patch) | プライマリネームサーバ設定の更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_primaries/{CcPrimaryId}](#tag/cc_primaries/paths/~1common_configs~1{CommonConfigId}~1cc_primaries~1{CcPrimaryId}/delete) | プライマリネームサーバ設定の削除 | dpf_write  ### cc_sec_notified_servers   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/get) | DNS NOTIFY設定の一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_sec_notified_servers](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers/post) | DNS NOTIFY設定の作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/get) | DNS NOTIFY設定の取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/patch) | DNS NOTIFY設定の更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_sec_notified_servers/{CcSecNotifiedServerId}](#tag/cc_sec_notified_servers/paths/~1common_configs~1{CommonConfigId}~1cc_sec_notified_servers~1{CcSecNotifiedServerId}/delete) | DNS NOTIFY設定の削除 | dpf_write  ### cc_sec_transfer_acls   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/get) | ゾーン転送ACLの一覧取得 | dpf_read   POST | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls/post) | ゾーン転送ACLの作成 | dpf_write   GET | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/get) | ゾーン転送ACLの取得 | dpf_read   PATCH | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/patch) | ゾーン転送ACLの更新 | dpf_write   DELETE | [/common_configs/{CommonConfigId}/cc_sec_transfer_acls/{CcSecTransferAclId}](#tag/cc_sec_transfer_acls/paths/~1common_configs~1{CommonConfigId}~1cc_sec_transfer_acls~1{CcSecTransferAclId}/delete) | ゾーン転送ACLの削除 | dpf_write  ### common_configs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/get) | 共通設定の一覧取得 | dpf_read   POST | [/contracts/{ContractId}/common_configs](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs/post) | 共通設定の作成 | dpf_write   GET | [/contracts/{ContractId}/common_configs/count](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1count/get) | 共通設定の件数取得 | dpf_read   PATCH | [/contracts/{ContractId}/common_configs/default](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1default/patch) | 初期適用される共通設定の更新 | dpf_write   GET | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/get) | 共通設定の取得 | dpf_read   PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/patch) | 共通設定の更新 | dpf_write   DELETE | [/contracts/{ContractId}/common_configs/{CommonConfigId}](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}/delete) | 共通設定の削除 | dpf_write   POST | [/contracts/{ContractId}/common_configs/{CommonConfigId}/copy](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1copy/post) | 共通設定のコピー | dpf_write   PATCH | [/contracts/{ContractId}/common_configs/{CommonConfigId}/managed_dns](#tag/common_configs/paths/~1contracts~1{ContractId}~1common_configs~1{CommonConfigId}~1managed_dns/patch) | マネージドDNSサーバの状態更新 | dpf_write  ### contracts   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts](#tag/contracts/paths/~1contracts/get) | DPF契約情報の一覧取得 | dpf_read   GET | [/contracts/count](#tag/contracts/paths/~1contracts~1count/get) | DPF契約情報の件数取得 | dpf_read   GET | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/get) | DPF契約情報の取得 | dpf_read   PATCH | [/contracts/{ContractId}](#tag/contracts/paths/~1contracts~1{ContractId}/patch) | DPF契約情報の更新 | dpf_write  ### contract_partners   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/contract_partners](#tag/contract_partners/paths/~1contracts~1{ContractId}~1contract_partners/get) | DPF連携サービスの一覧取得 | dpf_read  ### logs (contracts)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/logs](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs/get) | DPF契約操作ログの一覧取得 | dpf_read   GET | [/contracts/{ContractId}/logs/count](#tag/logs-(contracts)/paths/~1contracts~1{ContractId}~1logs~1count/get) | DPF契約操作ログの件数取得 | dpf_read  ### qps HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/qps/histories](#tag/qps/paths/~1contracts~1{ContractId}~1qps~1histories/get) | 月別のQPSの一覧取得 | dpf_read  ### tsigs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/get) | TSIG鍵の一覧取得 | dpf_read   POST | [/contracts/{ContractId}/tsigs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs/post) | TSIG鍵の作成 | dpf_write   GET | [/contracts/{ContractId}/tsigs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1count/get) | TSIG鍵の件数取得 | dpf_read   GET | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/get) | TSIG鍵の取得 | dpf_read   PATCH | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/patch) | TSIG鍵の更新 | dpf_write   DELETE | [/contracts/{ContractId}/tsigs/{TsigId}](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}/delete) | TSIG鍵の削除 | dpf_write   GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs/get) | TSIG鍵を利用している共通設定の一覧取得 | dpf_read   GET | [/contracts/{ContractId}/tsigs/{TsigId}/common_configs/count](#tag/tsigs/paths/~1contracts~1{ContractId}~1tsigs~1{TsigId}~1common_configs~1count/get) | TSIG鍵を利用している共通設定の件数取得 | dpf_read  ### zones (contracts)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/contracts/{ContractId}/zones](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones/get) | DPF契約に紐付くゾーンの一覧取得 | dpf_read   PATCH | [/contracts/{ContractId}/zones/common_configs](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1common_configs/patch) | DPF契約に紐付くゾーンの共通設定の更新 | dpf_write   GET | [/contracts/{ContractId}/zones/count](#tag/zones-(contracts)/paths/~1contracts~1{ContractId}~1zones~1count/get) | DPF契約に紐付くゾーンの件数取得 | dpf_read  ## IIJマネージドDNSサービス  ### default_ttl   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/get) | デフォルトTTLの取得 | dpf_read   PATCH | [/zones/{ZoneId}/default_ttl](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl/patch) | デフォルトTTLの更新 | dpf_write   DELETE | [/zones/{ZoneId}/default_ttl/changes](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1changes/delete) | 編集中デフォルトTTLの取消 | dpf_write   GET | [/zones/{ZoneId}/default_ttl/diffs](#tag/default_ttl/paths/~1zones~1{ZoneId}~1default_ttl~1diffs/get) | デフォルトTTLの編集差分の取得 | dpf_read  ### dnssec   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/get) | DNSSEC情報の取得 | dpf_read   PATCH | [/zones/{ZoneId}/dnssec](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec/patch) | DNSSEC情報の更新 | dpf_write   PATCH | [/zones/{ZoneId}/dnssec/ksk_rollover](#tag/dnssec/paths/~1zones~1{ZoneId}~1dnssec~1ksk_rollover/patch) | KSKロールオーバーの開始 | dpf_write  ### ds_records   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/ds_records](#tag/ds_records/paths/~1zones~1{ZoneId}~1ds_records/get) | DSレコードの一覧取得 | dpf_read  ### logs (zones)   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/logs](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs/get) | ゾーン操作ログの一覧取得 | dpf_read   GET | [/zones/{ZoneId}/logs/count](#tag/logs-(zones)/paths/~1zones~1{ZoneId}~1logs~1count/get) | ゾーン操作ログの件数取得 | dpf_read  ### records   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/get) | レコードの一覧取得 | dpf_read   POST | [/zones/{ZoneId}/records](#tag/records/paths/~1zones~1{ZoneId}~1records/post) | レコードの作成 | dpf_write   GET | [/zones/{ZoneId}/records/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1count/get) | レコードの件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/currents](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents/get) | DNS反映済レコードの一覧取得 | dpf_read   GET | [/zones/{ZoneId}/records/currents/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1currents~1count/get) | DNS反映済レコードの件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/diffs](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs/get) | レコードの編集差分の一覧取得 | dpf_read   GET | [/zones/{ZoneId}/records/diffs/count](#tag/records/paths/~1zones~1{ZoneId}~1records~1diffs~1count/get) | レコードの編集差分の件数取得 | dpf_read   GET | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/get) | レコードの取得 | dpf_read   PATCH | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/patch) | レコードの更新 | dpf_write   DELETE | [/zones/{ZoneId}/records/{RecordId}](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}/delete) | レコードの削除 | dpf_write   DELETE | [/zones/{ZoneId}/records/{RecordId}/changes](#tag/records/paths/~1zones~1{ZoneId}~1records~1{RecordId}~1changes/delete) | 編集中レコードの取消 | dpf_write  ### zone_histories   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/zone_histories](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories/get) | ゾーン反映履歴の一覧取得 | dpf_read   GET | [/zones/{ZoneId}/zone_histories/count](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1count/get) | ゾーン反映履歴の件数取得 | dpf_read   GET | [/zones/{ZoneId}/zone_histories/{ZoneHistoryId}/text](#tag/zone_histories/paths/~1zones~1{ZoneId}~1zone_histories~1{ZoneHistoryId}~1text/get) | ゾーン反映時のRFC1035形式のテキストの取得 | dpf_read  ### zone_proxy   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/get) | ゾーンプロキシ設定の取得 | dpf_read   PATCH | [/zones/{ZoneId}/zone_proxy](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy/patch) | ゾーンプロキシ設定の更新 | dpf_write   GET | [/zones/{ZoneId}/zone_proxy/health_check](#tag/zone_proxy/paths/~1zones~1{ZoneId}~1zone_proxy~1health_check/get) | プライマリネームサーバのヘルスチェック結果の取得 | dpf_read  ### zones   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/zones](#tag/zones/paths/~1zones/get) | ゾーンの一覧取得 | dpf_read   GET | [/zones/count](#tag/zones/paths/~1zones~1count/get) | ゾーンの件数取得 | dpf_read   GET | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/get) | ゾーンの取得 | dpf_read   PATCH | [/zones/{ZoneId}](#tag/zones/paths/~1zones~1{ZoneId}/patch) | ゾーンの更新 | dpf_write   PATCH | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/patch) | 編集中レコードのゾーン反映 | dpf_write   DELETE | [/zones/{ZoneId}/changes](#tag/zones/paths/~1zones~1{ZoneId}~1changes/delete) | 編集中レコードの一括取消 | dpf_write   GET | [/zones/{ZoneId}/contract](#tag/zones/paths/~1zones~1{ZoneId}~1contract/get) | ゾーンに紐付くDPF契約情報の取得 | dpf_read   GET | [/zones/{ZoneId}/managed_dns_servers](#tag/zones/paths/~1zones~1{ZoneId}~1managed_dns_servers/get) | マネージドDNSサーバの一覧取得 | dpf_read  ## サービス共通  ### delegations   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/delegations](#tag/delegations/paths/~1delegations/get) | ネームサーバ申請候補の一覧取得 | dpf_read   POST | [/delegations](#tag/delegations/paths/~1delegations/post) | ネームサーバ申請 | dpf_write   GET | [/delegations/count](#tag/delegations/paths/~1delegations~1count/get) | ネームサーバ申請候補の件数取得 | dpf_read  ### jobs   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/jobs/{RequestId}](#tag/jobs/paths/~1jobs~1{RequestId}/get) | 非同期リクエストの状態確認 | dpf_read  ### ping   HTTPメソッド | API | 機能 | 許可するスコープ   -----------|-----|-----|--------------   GET | [/ping](#tag/ping/paths/~1ping/get) | API疎通確認 | dpf_read, dpf_write, dpf_contract   # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import io
import json
import logging
import re
import ssl
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.request import proxy_bypass_environment
import urllib3
import ipaddress

from openapi_client.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException, ServiceException, ApiValueError


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if configuration.retries is not None:
            addition_pool_args['retries'] = configuration.retries

        if configuration.socket_options is not None:
            addition_pool_args['socket_options'] = configuration.socket_options

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy and not should_bypass_proxies(configuration.host, no_proxy=configuration.no_proxy or ''):
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=configuration.ssl_ca_cert,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                proxy_headers=configuration.proxy_headers,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=configuration.ssl_ca_cert,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args
            )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, float)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple) and
                  len(_request_timeout) == 2):
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1])

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                # Only set a default Content-Type for POST, PUT, PATCH and OPTIONS requests
                if (method != 'DELETE') and ('Content-Type' not in headers):
                    headers['Content-Type'] = 'application/json'
                if query_params:
                    url += '?' + urlencode(query_params)
                if ('Content-Type' not in headers) or (re.search('json', headers['Content-Type'], re.IGNORECASE)):
                    request_body = None
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str) or isinstance(body, bytes):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            if r.status == 401:
                raise UnauthorizedException(http_resp=r)

            if r.status == 403:
                raise ForbiddenException(http_resp=r)

            if r.status == 404:
                raise NotFoundException(http_resp=r)

            if 500 <= r.status <= 599:
                raise ServiceException(http_resp=r)

            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

# end of class RESTClientObject
def is_ipv4(target):
    """ Test if IPv4 address or not
    """
    try:
       chk = ipaddress.IPv4Address(target)
       return True
    except ipaddress.AddressValueError:
       return False

def in_ipv4net(target, net):
    """ Test if target belongs to given IPv4 network
    """
    try:
        nw = ipaddress.IPv4Network(net)
        ip = ipaddress.IPv4Address(target)
        if ip in nw:
            return True
        return False
    except ipaddress.AddressValueError:
        return False
    except ipaddress.NetmaskValueError:
        return False

def should_bypass_proxies(url, no_proxy=None):
    """ Yet another requests.should_bypass_proxies
    Test if proxies should not be used for a particular url.
    """

    parsed = urlparse(url)

    # special cases
    if parsed.hostname in [None, '']:
        return True

    # special cases
    if no_proxy in [None , '']:
        return False
    if no_proxy == '*':
        return True

    no_proxy = no_proxy.lower().replace(' ','');
    entries = (
        host for host in no_proxy.split(',') if host
    )

    if is_ipv4(parsed.hostname):
        for item in entries:
           if in_ipv4net(parsed.hostname, item):
               return True
    return proxy_bypass_environment(parsed.hostname, {'no': no_proxy} )
