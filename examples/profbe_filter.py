
from gosec_filter import ProfbeGosecWarning

the_gosec_filter = set([

ProfbeGosecWarning(error="G402: TLS InsecureSkipVerify set true. (Confidence: HIGH, Severity: HIGH)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/notifications/email.go:71",
             code="InsecureSkipVerify: true")


ProfbeGosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/logging/config.go:32",
             code="DEFAULT_MYSQL_DBPASS          = "awazza_pr_pass"")


ProfbeGosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/config/config.go:1492",
             code="DEFAULT_MYSQL_DBPASS          = "awazza_pr_pass"")


ProfbeGosecWarning(error="G402: TLS InsecureSkipVerify set true. (Confidence: HIGH, Severity: HIGH)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/oauth2/consumer.go:52",
             code="InsecureSkipVerify: true")


ProfbeGosecWarning(error="G402: TLS InsecureSkipVerify set true. (Confidence: HIGH, Severity: HIGH)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/notifications/notifications_commons.go:313",
             code="InsecureSkipVerify: true")


ProfbeGosecWarning(error="G501: Blacklisted import crypto/md5: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/api/api_filters.go:14",
             code=""crypto/md5"")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/split-sku-niji-sw/split_sku_niji_sw.go:97",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/split-sku-niji-sw/split_sku_niji_sw.go:121",
             code="os.Open(inputFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/unprovision-bulk-hgu/unprovision_bulk_hgu.go:73",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/unprovision-bulk-hgu/unprovision_bulk_hgu.go:82",
             code="os.Open(inputFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/retry_async_prov/retry_async_prov.go:87",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/commands/run_nt.go:34",
             code="ioutil.ReadFile(cfgFile)")


ProfbeGosecWarning(error="G501: Blacklisted import crypto/md5: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/notifications/parlayx.go:16",
             code=""crypto/md5"")


ProfbeGosecWarning(error="G401: Use of weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/notifications/parlayx.go:150",
             code="md5.Sum([]byte(p.Config.Id + p.Config.Password + timeStamp))")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/commands/run_be.go:47",
             code="ioutil.ReadFile(cfgFile)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/parlayx/parlayx.go:69",
             code="ioutil.ReadFile(sms_file)")


ProfbeGosecWarning(error="G501: Blacklisted import crypto/md5: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/whitelist/whitelist_commons.go:11",
             code=""crypto/md5"")


ProfbeGosecWarning(error="G401: Use of weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/whitelist/whitelist_commons.go:578",
             code="md5.New()")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/config/config.go:1457",
             code="os.Open(fullPath)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/commands/run_be.go:38",
             code="ioutil.ReadFile(cfgFile)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/config/elem-list.go:37",
             code="os.Open(fullPath)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/aes/aestool/encrypt/encrypt_aes.go:66",
             code="os.Open(fileName)")


ProfbeGosecWarning(error="G505: Blacklisted import crypto/sha1: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/sso/sso.go:5",
             code=""crypto/sha1"")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/smpp/smpp.go:171",
             code="ioutil.ReadFile(sms_file)")


ProfbeGosecWarning(error="G505: Blacklisted import crypto/sha1: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/api/v2/mobile_connect.go:13",
             code=""crypto/sha1"")


ProfbeGosecWarning(error="G505: Blacklisted import crypto/sha1: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/api/v2/session.go:12",
             code=""crypto/sha1"")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/provision-bulk-hgu/provision_bulk_hgu.go:83",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/provision-bulk-hgu/provision_bulk_hgu.go:92",
             code="os.Open(inputFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/email/email.go:64",
             code="ioutil.ReadFile(emailFile)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/mcafee/mcafee_sms.go:72",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/mcafee/mcafee_sms.go:82",
             code="ioutil.ReadFile(messageFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/mcafee/mcafee_sms.go:86",
             code="os.Open(mcafeeFileName)")


ProfbeGosecWarning(error="G201: SQL string formatting (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/utils/test_utils.go:87",
             code="fmt.Sprintf("DELETE FROM `profile_test_temp`.%s", t)")


ProfbeGosecWarning(error="G201: SQL string formatting (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/utils/test_utils.go:132",
             code="fmt.Sprintf("INSERT INTO `profile_test_temp`.%[1]s SELECT * FROM `profile_test`.%[1]s", t)")


ProfbeGosecWarning(error="G202: SQL string concatenation (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/migrate_hgu/migrate_hgu.go:145-146",
             code="`")


ProfbeGosecWarning(error="G202: SQL string concatenation (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/migrate_hgu/migrate_hgu.go:227-228",
             code="`")


ProfbeGosecWarning(error="G202: SQL string concatenation (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/migrate_hgu/migrate_hgu.go:269-270",
             code="`")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/mcafee_sms/mcafee_sms.go:89",
             code="os.Open(mcafeeFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/aes/aestool/decrypt/decrypt_aes.go:56",
             code="os.Open(fileName)")


ProfbeGosecWarning(error="G401: Use of weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/aes/aestool/decrypt/decrypt_aes.go:102",
             code="md5.New()")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/check-router-data/check_router_data.go:69",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/check-router-data/check_router_data.go:89",
             code="os.Open(inputFile)")


ProfbeGosecWarning(error="G401: Use of weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/api/api_filters.go:208",
             code="md5.New()")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/sms_pcm/sms_pcm.go:67",
             code="ioutil.ReadFile(sms_file)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/mcafee_sms/mcafee_sms.go:75",
             code="ioutil.ReadFile(configFileName)")


ProfbeGosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/mcafee_sms/mcafee_sms.go:85",
             code="ioutil.ReadFile(messageFileName)")


ProfbeGosecWarning(error="G501: Blacklisted import crypto/md5: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/aes/aestool/decrypt/decrypt_aes.go:9",
             code=""crypto/md5"")


ProfbeGosecWarning(error="G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/fiorix/go-smpp/smpp/transmitter.go:270",
             code="f.Set(pdufield.ValidityPeriod, convertValidity(sm.Validity))")


ProfbeGosecWarning(error="G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/tools/sso/sso.go:53",
             code="hash.Write([]byte(rawQuery))")


ProfbeGosecWarning(error="G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)",
             location="/home/mlg/go/src/niji-profile/src/awazza-profile-be/commands/run_nt.go:49",
             code="docopt.Parse(usage, argv, true, "", false)")


])


