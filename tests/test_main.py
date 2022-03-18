import re

import click.testing

from name_that_hash import runner


def test_it_works():
    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert x is not None


def test_it_identifies_correctly_correctly():
    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "NTLM" in x


def test_for_popular():
    hashes = ["5f4dcc3b5aa765d61d8327deb882cf99"]

    x = runner.api_return_hashes_as_json(hashes, {"popular_only": True})
    assert "ZipMonster" not in x


def test_for_popular_2():
    hashes = ["5f4dcc3b5aa765d61d8327deb882cf99"]

    x = runner.api_return_hashes_as_json(hashes, {"popular_only": True})
    assert "MD5" in x


def test_main_succeeds():
    runn = click.testing.CliRunner()
    result = runn.invoke(runner.main)
    assert result.exit_code == 0


def test_if_no_hashes_found():
    hashes = ["abc"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "[]" in x


def test_bcrypt_dollar():
    hashes = ["$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "bcrypt" in x


def test_base64_works():
    hashes = ["NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk="]

    x = runner.api_return_hashes_as_json(hashes, {"base64": True})
    assert "MD5" in x


def test_scrypt_succeeds():
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "scrypt" in x


def test_kerberos1():
    hashes = [
        "$krb5pa$23$user$realm$salt$4e751db65422b2117f7eac7b721932dc8aa0d9966785ecd958f971f622bf5c42dc0c70b532363138363631363132333238383835"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 AS-REQ Pre-Auth" in x


def test_kerberos2():
    hashes = [
        "$krb5tgs$23$*user$realm$test/spn*$63386d22d359fe42230300d56852c9eb$891ad31d09ab89c6b3b8c5e5de6c06a7f49fd559d7a9a3c32576c8fedf705376cea582ab5938f7fc8bc741acf05c5990741b36ef4311fe3562a41b70a4ec6ecba849905f2385bb3799d92499909658c7287c49160276bca0006c350b0db4fd387adc27c01e9e9ad0c20ed53a7e6356dee2452e35eca2a6a1d1432796fc5c19d068978df74d3d0baf35c77de12456bf1144b6a750d11f55805f5a16ece2975246e2d026dce997fba34ac8757312e9e4e6272de35e20d52fb668c5ed"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 TGS-REP etype 23" in x


def test_kerberos3():
    hashes = [
        "$krb5asrep$23$user@domain.com:3e156ada591263b8aab0965f5aebd837$007497cb51b6c8116d6407a782ea0e1c5402b17db7afa6b05a6d30ed164a9933c754d720e279c6c573679bd27128fe77e5fea1f72334c1193c8ff0b370fadc6368bf2d49bbfdba4c5dccab95e8c8ebfdc75f438a0797dbfb2f8a1a5f4c423f9bfc1fea483342a11bd56a216f4d5158ccc4b224b52894fadfba3957dfe4b6b8f5f9f9fe422811a314768673e0c924340b8ccb84775ce9defaa3baa0910b676ad0036d13032b0dd94e3b13903cc738a7b6d00b0b3c210d1f972a6c7cae9bd3c959acf7565be528fc179118f28c679f6deeee1456f0781eb8154e18e49cb27b64bf74cd7112a0ebae2102ac"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 AS-REP etype 23" in x


def test_kerberos4():
    hashes = [
        "$krb5tgs$17$user$realm$ae8434177efd09be5bc2eff8$90b4ce5b266821adc26c64f71958a475cf9348fce65096190be04f8430c4e0d554c86dd7ad29c275f9e8f15d2dab4565a3d6e21e449dc2f88e52ea0402c7170ba74f4af037c5d7f8db6d53018a564ab590fc23aa1134788bcc4a55f69ec13c0a083291a96b41bffb978f5a160b7edc828382d11aacd89b5a1bfa710b0e591b190bff9062eace4d26187777db358e70efd26df9c9312dbeef20b1ee0d823d4e71b8f1d00d91ea017459c27c32dc20e451ea6278be63cdd512ce656357c942b95438228e"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 TGS-REP etype 17 (AES128-CTS-HMAC-SHA1-96)" in x


def test_kerberos5():
    hashes = [
        "$krb5tgs$18$user$realm$8efd91bb01cc69dd07e46009$7352410d6aafd72c64972a66058b02aa1c28ac580ba41137d5a170467f06f17faf5dfb3f95ecf4fad74821fdc7e63a3195573f45f962f86942cb24255e544ad8d05178d560f683a3f59ce94e82c8e724a3af0160be549b472dd83e6b80733ad349973885e9082617294c6cbbea92349671883eaf068d7f5dcfc0405d97fda27435082b82b24f3be27f06c19354bf32066933312c770424eb6143674756243c1bde78ee3294792dcc49008a1b54f32ec5d5695f899946d42a67ce2fb1c227cb1d2004c0"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 TGS-REP etype 18 (AES256-CTS-HMAC-SHA1-96)" in x


def test_kerberos6():
    hashes = [
        "$krb5pa$17$hashcat$HASHCATDOMAIN.COM$a17776abe5383236c58582f515843e029ecbff43706d177651b7b6cdb2713b17597ddb35b1c9c470c281589fd1d51cca125414d19e40e333"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 17, Pre-Auth" in x


def test_kerberos7():
    hashes = [
        "$krb5pa$17$user1$EXAMPLE.COM$$c5461873dc13665771b98ba80be53939e906d90ae1ba79cf2e21f0395e50ee56379fbef4d0298cfccfd6cf8f907329120048fd05e8ae5df4"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 17, Pre-Auth (with salt)" in x


def test_kerberos8():
    hashes = [
        "$krb5pa$18$hashcat$HASHCATDOMAIN.COM$96c289009b05181bfd32062962740b1b1ce5f74eb12e0266cde74e81094661addab08c0c1a178882c91a0ed89ae4e0e68d2820b9cce69770"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 18, Pre-Auth" in x


def test_scrypt_python_dict():
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]

    x = runner.api_return_hashes_as_dict(hashes)
    assert (
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
        in x
    )


def test_etherum():
    hashes = [
        "$ethereum$p*262144*3238383137313130353438343737383736323437353437383831373034343735*06eae7ee0a4b9e8abc02c9990e3730827396e8531558ed15bb733faf12a44ce1*e6d5891d4f199d31ec434fe25d9ecc2530716bc3b36d5bdbc1fab7685dda3946"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Ethereum" in x


def test_bitcoin():
    hashes = [
        "$bitcoin$96$d011a1b6a8d675b7a36d0cd2efaca32a9f8dc1d57d6d01a58399ea04e703e8bbb44899039326f7a00f171a7bbc854a54$16$1563277210780230$158555$96$628835426818227243334570448571536352510740823233055715845322741625407685873076027233865346542174$66$625882875480513751851333441623702852811440775888122046360561760525"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Bitcoin / Litecoin" in x


def test_monero():
    hashes = [
        "$monero$0*dbaa1db887689e76af0c5a8a7d71595983843c58bca382192e477262d820a98fcd12955335171a96670f8282d09ad4dc67bb66b3fc0590b028d53e574ef908d97cac8578878a6147112dff92cc322e8d86b34e96807f70f5ede43254454bdfe2c6216280d181b495ae24f49ab1aaaebaec4f856f3d160f1d2176b79dd6eb64fa3e192ecfa054be5bbb780364f7c444f23d62fba00d1e125b8b12e518102a48f8c4f7bcba2ca7fefe4e0acd0b61352e32bc821bcbbe211ce433204c08aced7766cfc20b5b2538ef269a91fc5e96d214a8b9cb9bc7c1cc87279164d64353450daaf4f2f8b964f051111ea49a9fbf358e8746cdf043460b975a1eb59e02f3960ab92b59ae5161158d4d0f4c982a4e744b7bcd0319210073ff17a8ca433bd4ff8fe0907882bc43371775ad2ad1beb0c551cebfb4ff9b0dae57d25ea530e5976f874e22a25ad8b79007ee89c9e1923e016f39bc1cd16ac1e34984a2e786896d235a7900a127acc1cf33cebdfba171eb2a36924363d86d98c29c93666ac7a779dfec08f87632fa1b25250ff93ba300b166618cfdd2415b8b3075a431cd785bc22846329111fcbd230375e8c145c76721e65e801948c756f7519add6b6f3ef82bd92f10c47a6d1c5cd45a196fb3a9345186ed1b676de850940ca735f5e81f74df8f54ae906f916b847cf666b74d3632cba2d8f6a2ae8eb8ff34ff1ede7d9a602026cf1f1392ab24491a14983875fd3a4eb2e93caa4de867fd78b1853af9134d866a2abf70a8ef13ada0cb0f49cefe622393219c6a54eaedf37673f1c09af47f884db063d432021a27cff463ef6bb90c9fa5db884b0673c7681eea38b17eb503dba448b406d27f76eaab7693a60ba5bb376167e25d9d37e44c0fc49a20cf082100697a7b053f85650d6515359fa0a9ed0b16c7ae2a699e82872487c54734b23a51b0811d18ea270008ac3634c8655d8c662efc6420c0d1d890e97a457924eb7f148c519955fd7bfcb319ae49bc64ac6fa9beba327b029116afeee7d1002c24c16e163cd15ccc7a964326e881c6b3085abfd49c253946bbacfd5eeb979365690fb281501bf1e88359f630cdff78244160fb129b8b2610e24ca117b74d9a4b2fcdbed0f59e9d71109d9b93661be7408ebd7aa3c7360bb0069eb553e5ee808b08aa330f9a91f1fa9075c1a1817dd0a4c06be756122597044a43a3b8b5722b169da0b97c8647ae478440f1ad588faf595f573d26e7e66110d70cbe78ef5efeab333f896daa04c3cd222dbfc705b5ab5b10ce46cca036ec4904e786ac91eb099fb2bc5a6d5b4492d6ec0d07e71c68ac6c2da39794e070f6454a4c4e2678dc9ece69785d4d3ae101f6ad0781b8a515a5059663ebd3a17c4bf5fa4dd56d6fbf387d4e7de3baef9e6da46e9a9ada6155514a29d30e1b334c892c9ad14c49cf63baf66cb2b12725c898e4ba6fc73939872b60c60976285d3727900a0b346d3ccf5bbd1c724daa98f4db3681f41f45d01e8022ca50b812269bf77f4d5d2ed2327d39d7e6d945907513604e1b42ffa88f2414952dbbe7cabdb8b9a14d95d832f455dd1affd16ddacc21d9a9bb9ea69a61e5d7a4df0db6eb7e11736f0955d096bb648ec5de392d57f80d60bfd139992f84cd3622faea5d77dd52ac16932f1d2dae353134ab195e5dc0af5c270553c6a09d11f6d95463ef5de483e529aa88644aaf709ba23f54309e5e9eed235017d674d1a5b11a2e189ea427dbe9151fbe78cc4a34644203ea424fc3016653a5e1d7c265df5a9f37ac5c67a04e0ed0f7df76fa4fd071b49cc7c5f08f80b4766a9b5359310f7efe7a5a694d1d5f875f0bb9367324f32736a84b02e1c042e4c016fc329522f7c31555c6b989ef43a9044474d99c58244d010ac6625be314ceb6e78a4bd3da98f106048d1b5f1fe34bef2edd7194f3e4ad3f6dc9cea7361a4817fbe78b99d0aa0db3dc8ce2299ba9049eed66f70f4feb6e69dfc7a7e7577d6559866abee9652ab6ef89009256105612a4a2b79fd11c55850e1b3c174137436d5c0baa2631db2911202e593b7d0f1d381f2f250fd732a98297dcc20a9a0c1a2c5b98d1482c182bb8d6c22f7cf9f400fd794ca8a1f58e0e790b34f168c39f0f514b918a0856d0621a66a83efc12fc3510ef1a833dc4147ebf23a1347d32355f085dcb0ab0d0206a3fa8858475391b5b47e24b4842c28c0e74044a190ae295aa305deb3dac453837bdcfac52ddd607564ddfd9fb76ee59f4ba"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Monero" in x


def test_electrum1():
    hashes = [
        "$electrum$1*44358283104603165383613672586868*c43a6632d9f59364f74c395a03d8c2ea"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Electrum Wallet (Salt-Type 1-3)" in x


def test_electrum2():
    hashes = [
        "$electrum$4*03eae309d8bda5dcbddaae8145469193152763894b7260a6c4ba181b3ac2ed5653*8c594086a64dc87a9c1f8a69f646e31e8d3182c3c722def4427aa20684776ac26092c6f60bf2762e27adfa93fe1e952dcb8d6362224b9a371953aa3a2edb596ce5eb4c0879c4353f2cc515ec6c9e7a6defa26c5df346d18a62e9d40fcc606bc8c34322bf2212f77770a683788db0baf4cb43595c2a27fe5ff8bdcb1fd915bcd725149d8ee8f14c71635fecb04da5dde97584f4581ceb7d907dceed80ae5daa8352dda20b25fd6001e99a96b7cf839a36cd3f5656304e6998c18e03dd2fb720cb41386c52910c9cb83272c3d50f3a6ff362ab8389b0c21c75133c971df0a75b331796371b060b32fe1673f4a041d7ae08bbdeffb45d706eaf65f99573c07972701c97766b4d7a8a03bba0f885eb3845dfd9152286e1de1f93e25ce04c54712509166dda80a84c2d34652f68e6c01e662f8b1cc7c15103a4502c29332a4fdbdda470c875809e15aab3f2fcb061ee96992ad7e8ab9da88203e35f47d6e88b07a13b0e70ef76de3be20dc06facbddc1e47206b16b44573f57396265116b4d243e77d1c98bc2b28aa3ec0f8d959764a54ecdd03d8360ff2823577fe2183e618aac15b30c1d20986841e3d83c0bfabcedb7c27ddc436eb7113db927e0beae7522b04566631a090b214660152a4f4a90e19356e66ee7309a0671b2e7bfde82667538d193fc7e397442052c6c611b6bf0a04f629a1dc7fa9eb44bfad1bfc6a0bce9f0564c3b483737e447720b7fd038c9a961a25e9594b76bf8c8071c83fcacd689c7469f698ee4aee4d4f626a73e21ce4967e705e4d83e1145b4260330367d8341c84723a1b02567ffbab26aac3afd1079887b4391f05d09780fc65f8b4f68cd51391c06593919d7eafd0775f83045b8f5c2e59cef902ff500654ea29b7623c7594ab2cc0e05ffe3f10abc46c9c5dac824673c307dcbff5bc5f3774141ff99f6a34ec4dd8a58d154a1c72636a2422b8fafdef399dec350d2b91947448582d52291f2261d264d29399ae3c92dc61769a49224af9e7c98d74190f93eb49a44db7587c1a2afb5e1a4bec5cdeb8ad2aac9728d5ae95600c52e9f063c11cdb32b7c1d8435ce76fcf1fa562bd38f14bf6c303c70fb373d951b8a691ab793f12c0f3336d6191378bccaed32923bba81868148f029e3d5712a2fb9f610997549710716db37f7400690c8dfbed12ff0a683d8e4d0079b380e2fd856eeafb8c6eedfac8fb54dacd6bd8a96e9f8d23ea87252c1a7c2b53efc6e6aa1f0cc30fbaaf68ee7d46666afc15856669cd9baebf9397ff9f322cce5285e68a985f3b6aadce5e8f14e9f9dd16764bc4e9f62168aa265d8634ab706ed40b0809023f141c36717bd6ccef9ec6aa6bfd2d00bda9375c2fee9ebba49590a166*1b0997cf64bb2c2ff88cb87bcacd9729d404bd46db18117c20d94e67c946fedc"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Electrum Wallet (Salt-Type 4)" in x


def test_electrum3():
    hashes = [
        "$electrum$5*02170fee7c35f1ef3b229edc90fbd0793b688a0d6f41137a97aab2343d315cce16*94cf72d8f5d774932b414a3344984859e43721268d2eb35fa531de5a2fc7024b463c730a54f4f46229dd9fede5034b19ac415c2916e9c16b02094f845795df0c397ff76d597886b1f9e014ad1a8f64a3f617d9900aa645b3ba86f16ce542251fc22c41d93fa6bc118be96d9582917e19d2a299743331804cfc7ce2c035367b4cbcfb70adfb1e10a0f2795769f2165d8fd13daa8b45eeac495b5b63e91a87f63b42e483f84a881e49adecacf6519cb564694b42dd9fe80fcbc6cdb63cf5ae33f35255266f5c2524dd93d3cc15eba0f2ccdc3c109cc2d7e8f711b8b440f168caf8b005e8bcdfe694148e94a04d2a738f09349a96600bd8e8edae793b26ebae231022f24e96cb158db141ac40400a9e9ef099e673cfe017281537c57f82fb45c62bdb64462235a6eefb594961d5eb2c46537958e4d04250804c6e9f343ab7a0db07af6b8a9d1a6c5cfcd311b8fb8383ac9ed9d98d427d526c2f517fc97473bd87cb59899bd0e8fb8c57fa0f7e0d53daa57c972cf92764af4b1725a5fb8f504b663ec519731929b3caaa793d8ee74293eee27d0e208a60e26290bc546e6fa9ed865076e13febfea249729218c1b5752e912055fbf993fbac5df2cca2b37c5e0f9c30789858ceeb3c482a8db123966775aeed2eee2fc34efb160d164929f51589bff748ca773f38978bff3508d5a7591fb2d2795df983504a788071f469d78c88fd7899cabbc5804f458653d0206b82771a59522e1fa794d7de1536c51a437f5d6df5efd6654678e5794ca429b5752e1103340ed80786f1e9da7f5b39af628b2212e4d88cd36b8a7136d50a6b6e275ab406ba7c57cc70d77d01c4c16e9363901164fa92dc9e9b99219d5376f24862e775968605001e71b000e2c7123b4b43f3ca40db17efd729388782e46e64d43ccb947db4eb1473ff1a3836b74fe312cd1a33b73b8b8d80c087088932277773c329f2f66a01d6b3fc1e651c56959ebbed7b14a21b977f3acdedf1a0d98d519a74b50c39b3052d840106da4145345d86ec0461cddafacc2a4f0dd646457ad05bf04dcbcc80516a5c5ed14d2d639a70e77b686f19cbfb63f546d81ae19cc8ba35cce3f3b5b9602df25b678e14411fecec87b8347f5047513df415c6b1a3d39871a6bcb0f67d9cf8311596deae45fd1d84a04fd58f1fd55c5156b7309af09094c99a53674809cb87a45f95a2d69f9997a38085519cb4e056f9efd56672a2c1fe927d5ea8eec25b8aff6e56f9a2310f1a481daf407b8adf16201da267c59973920fd21bb087b88123ef98709839d6a3ee34efb8ccd5c15ed0e46cff3172682769531164b66c8689c35a26299dd26d09233d1f64f9667474141cf9c6a6de7f2bc52c3bb44cfe679ff4b912c06df406283836b3581773cb76d375304f46239da5996594a8d03b14c02f1b35a432dc44a96331242ae31174*33a7ee59d6d17ed1ee99dc0a71771227e6f3734b17ba36eb589bdced56244135"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Electrum Wallet (Salt-Type 5)" in x


def test_itunes():
    hashes = [
        "$itunes_backup$*10*8b715f516ff8e64442c478c2d9abb046fc6979ab079007d3dbcef3ddd84217f4c3db01362d88fa68*10000*2353363784073608264337337723324886300850*10000000*425b4bb4e200b5fd4c66979c9caca31716052063"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "iTunes backup >= 10.0" in x


def test_winzip():
    hashes = [
        "$zip2$*0*3*0*e3222d3b65b5a2785b192d31e39ff9de*1320*e*19648c3e063c82a9ad3ef08ed833*3135c79ecb86cd6f48fc*$/zip2$"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "WinZip" in x


def test_androidbackup():
    hashes = [
        "$ab$5*0*10000*b8900e4885ff9cad8f01ee1957a43bd633fea12491440514ae27aa83f2f5c006ec7e7fa0bce040add619919b4eb60608304b7d571a2ed87fd58c9ad6bc5fcf4c*7d254d93e16be9312fb1ccbfc6265c40cb0c5eab7b605a95a116e2383fb1cf12b688223f96221dcd2bf5410d4ca6f90e0789ee00157fa91658b42665d6b6844c*fc9f6be604d1c59ac32664ec2c5b9b30*00c4972149af3adcc235899e9d20611ea6e8de2212afcb9fcfefde7e35b691c2d0994eb47e4f9a260526ba47f4caea71af9c7fadcd5685d50126276f6acdd59966528b13ccc26036a0eaba2f2451aa64b05766d0edd03c988dcf87e2a9eec52d"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Android Backup" in x


def test_blake2b256():
    hashes = ["87e402405c9c268532ba64e5130476237cfc1289e2e993d62c97f3b14febcbf0"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Blake2b-256" in x


def test_telegram():
    hashes = [
        "$telegram$0*518c001aeb3b4ae96c6173be4cebe60a85f67b1e087b045935849e2f815b5e41*25184098058621950709328221838128"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Telegram Mobile App Passcode (SHA256)" in x


def test_blake2():
    hashes = [
        "$BLAKE2$296c269e70ac5f0095e6fb47693480f0f7b97ccd0307f5c3bfa4df8f5ca5c9308a0e7108e80a0a9c0ebb715e8b7109b072046c6cd5e155b4cfd2f27216283b1e"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "BLAKE2b-512" in x


def test_office():
    hashes = [
        "$oldoffice$0*55045061647456688860411218030058*e7e24d163fbd743992d4b8892bf3f2f7*493410dbc832557d3fe1870ace8397e2:91b2e062b9"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert re.findall(r"MS Office [^#]+ MD5 \+ RC4[^#]+ #2", x)


def test_office2():
    hashes = [
        "$oldoffice$3*83328705222323020515404251156288*2855956a165ff6511bc7f4cd77b9e101*941861655e73a09c40f7b1e9dfd0c256ed285acd:b8f63619ca"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert re.findall(r"MS Office [^#]+ SHA1 \+ RC4[^#]+ #2", x)


def test_office3():
    hashes = [
        "$office$2016$0$100000$876MLoKTq42+/DLp415iZQ==$TNDvpvYyvlSUy97UOLKNhXynhUDDA7H8kLql0ISH5SxcP6hbthdjaTo4Z3/MU0dcR2SAd+AduYb3TB5CLZ8+ow=="
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "MS Office 2016 - SheetProtection" in x


def test_7zip():
    hashes = [
        "$7z$0$19$0$$16$c46ee87167606ba2cedbc7b61e970c63$3341692866$16$9$7f6b4ddc563d6481339775c52b653f00"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "7-zip" in x


def test_securezip():
    hashes = [
        "$zip3$*0*1*256*0*39bff47df6152a0214d7a967*65ff418ffb3b1198cccdef0327c03750f328d6dd5287e00e4c467f33b92a6ef40a74bb11b5afad61a6c3c9b279d8bd7961e96af7b470c36fc186fd3cfe059107021c9dea0cf206692f727eeca71f18f5b0b6ee1f702b648bba01aa21c7b7f3f0f7d547838aad46868155a04214f22feef7b31d7a15e1abe6dba5e569c62ee640783bb4a54054c2c69e93ece9f1a2af9d*0*0*0*file.txt"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "SecureZIP AES-256" in x


def test_pkzipMasterKey():
    hashes = ["f1eff5c0368d10311dcfc419"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "PKZIP Master Key" in x


def test_pdf1():
    hashes = [
        "$pdf$1*2*40*-1*0*16*51726437280452826511473255744374*32*9b09be05c226214fa1178342673d86f273602b95104f2384b6c9b709b2cbc058*32*0000000000000000000000000000000000000000000000000000000000000000"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "PDF 1.1 - 1.3 (Acrobat 2 - 4)" in x


def test_pdf2():
    hashes = [
        "$pdf$1*2*40*-1*0*16*01221086741440841668371056103222*32*27c3fecef6d46a78eb61b8b4dbc690f5f8a2912bbb9afc842c12d79481568b74*32*0000000000000000000000000000000000000000000000000000000000000000:6a8aedccb7"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2" in x


def test_pdf3():
    hashes = [
        "$pdf$5*5*256*-1028*1*16*20583814402184226866485332754315*127*f95d927a94829db8e2fbfbc9726ebe0a391b22a084ccc2882eb107a74f7884812058381440218422686648533275431500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*127*00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "PDF 1.7 Level 3 (Acrobat 9)" in x


def test_pdf4():
    hashes = [
        "$pdf$5*6*256*-4*1*16*381692e488413f5502fa7314a78c25db*48*e5bf81a2a23c88f3dccb44bc7da68bb5606b653b733bcf9adaa5eb2c8ccf53abba66539044eb1957eda68469b1d0b9b5*48*b222df06deb308bf919d13447e688775fdcab972faed2c866dc023a126cb4cd4bbffab3683ecde243cf8d88967184680"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "PDF 1.7 Level 8 (Acrobat 10 - 11)" in x


def test_argon2i():
    hashes = [
        "$argon2i$v=19$m=200,t=5,p=10$MDk4NzZ0NGdmcmhzZGs$YO+KtnzglyaX52PL0WfoY4JfAOxhwNSmokYh+TWU"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Argon2i" in x


def test_argon2id():
    hashes = [
        "$argon2id$v=19$m=150,t=9,p=5$MDk4NzZ0NGdmcmhzZGs$mS34N/lEqBpGWQDGI1/Ztp7QEvDgvMoqPOsdXQB7dsDlGdAAamxncg"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Argon2id" in x


def test_argon2d():
    hashes = [
        "$argon2d$v=19$m=300,t=15,p=2$MDk4NzZ0NGdmcmhzZGs$yqcjojxf8O/plrwApyAhkpojnwuZW9UPp7DgCXoHtkGPUN1nhLZYB2FtzPjcrQC4sFXRauCjwZed6NUmoZc1mcoigTfgyQ"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Argon2d" in x
