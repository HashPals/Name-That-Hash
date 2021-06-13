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


def test_kerberos7():
    hashes = [
        "$krb5pa$17$user1$EXAMPLE.COM$$c5461873dc13665771b98ba80be53939e906d90ae1ba79cf2e21f0395e50ee56379fbef4d0298cfccfd6cf8f907329120048fd05e8ae5df4"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 17, Pre-Auth (with salt)" in x


def test_monero():
    hashes = [
        "$monero$0*dbaa1db887689e76af0c5a8a7d71595983843c58bca382192e477262d820a98fcd12955335171a96670f8282d09ad4dc67bb66b3fc0590b028d53e574ef908d97cac8578878a6147112dff92cc322e8d86b34e96807f70f5ede43254454bdfe2c6216280d181b495ae24f49ab1aaaebaec4f856f3d160f1d2176b79dd6eb64fa3e192ecfa054be5bbb780364f7c444f23d62fba00d1e125b8b12e518102a48f8c4f7bcba2ca7fefe4e0acd0b61352e32bc821bcbbe211ce433204c08aced7766cfc20b5b2538ef269a91fc5e96d214a8b9cb9bc7c1cc87279164d64353450daaf4f2f8b964f051111ea49a9fbf358e8746cdf043460b975a1eb59e02f3960ab92b59ae5161158d4d0f4c982a4e744b7bcd0319210073ff17a8ca433bd4ff8fe0907882bc43371775ad2ad1beb0c551cebfb4ff9b0dae57d25ea530e5976f874e22a25ad8b79007ee89c9e1923e016f39bc1cd16ac1e34984a2e786896d235a7900a127acc1cf33cebdfba171eb2a36924363d86d98c29c93666ac7a779dfec08f87632fa1b25250ff93ba300b166618cfdd2415b8b3075a431cd785bc22846329111fcbd230375e8c145c76721e65e801948c756f7519add6b6f3ef82bd92f10c47a6d1c5cd45a196fb3a9345186ed1b676de850940ca735f5e81f74df8f54ae906f916b847cf666b74d3632cba2d8f6a2ae8eb8ff34ff1ede7d9a602026cf1f1392ab24491a14983875fd3a4eb2e93caa4de867fd78b1853af9134d866a2abf70a8ef13ada0cb0f49cefe622393219c6a54eaedf37673f1c09af47f884db063d432021a27cff463ef6bb90c9fa5db884b0673c7681eea38b17eb503dba448b406d27f76eaab7693a60ba5bb376167e25d9d37e44c0fc49a20cf082100697a7b053f85650d6515359fa0a9ed0b16c7ae2a699e82872487c54734b23a51b0811d18ea270008ac3634c8655d8c662efc6420c0d1d890e97a457924eb7f148c519955fd7bfcb319ae49bc64ac6fa9beba327b029116afeee7d1002c24c16e163cd15ccc7a964326e881c6b3085abfd49c253946bbacfd5eeb979365690fb281501bf1e88359f630cdff78244160fb129b8b2610e24ca117b74d9a4b2fcdbed0f59e9d71109d9b93661be7408ebd7aa3c7360bb0069eb553e5ee808b08aa330f9a91f1fa9075c1a1817dd0a4c06be756122597044a43a3b8b5722b169da0b97c8647ae478440f1ad588faf595f573d26e7e66110d70cbe78ef5efeab333f896daa04c3cd222dbfc705b5ab5b10ce46cca036ec4904e786ac91eb099fb2bc5a6d5b4492d6ec0d07e71c68ac6c2da39794e070f6454a4c4e2678dc9ece69785d4d3ae101f6ad0781b8a515a5059663ebd3a17c4bf5fa4dd56d6fbf387d4e7de3baef9e6da46e9a9ada6155514a29d30e1b334c892c9ad14c49cf63baf66cb2b12725c898e4ba6fc73939872b60c60976285d3727900a0b346d3ccf5bbd1c724daa98f4db3681f41f45d01e8022ca50b812269bf77f4d5d2ed2327d39d7e6d945907513604e1b42ffa88f2414952dbbe7cabdb8b9a14d95d832f455dd1affd16ddacc21d9a9bb9ea69a61e5d7a4df0db6eb7e11736f0955d096bb648ec5de392d57f80d60bfd139992f84cd3622faea5d77dd52ac16932f1d2dae353134ab195e5dc0af5c270553c6a09d11f6d95463ef5de483e529aa88644aaf709ba23f54309e5e9eed235017d674d1a5b11a2e189ea427dbe9151fbe78cc4a34644203ea424fc3016653a5e1d7c265df5a9f37ac5c67a04e0ed0f7df76fa4fd071b49cc7c5f08f80b4766a9b5359310f7efe7a5a694d1d5f875f0bb9367324f32736a84b02e1c042e4c016fc329522f7c31555c6b989ef43a9044474d99c58244d010ac6625be314ceb6e78a4bd3da98f106048d1b5f1fe34bef2edd7194f3e4ad3f6dc9cea7361a4817fbe78b99d0aa0db3dc8ce2299ba9049eed66f70f4feb6e69dfc7a7e7577d6559866abee9652ab6ef89009256105612a4a2b79fd11c55850e1b3c174137436d5c0baa2631db2911202e593b7d0f1d381f2f250fd732a98297dcc20a9a0c1a2c5b98d1482c182bb8d6c22f7cf9f400fd794ca8a1f58e0e790b34f168c39f0f514b918a0856d0621a66a83efc12fc3510ef1a833dc4147ebf23a1347d32355f085dcb0ab0d0206a3fa8858475391b5b47e24b4842c28c0e74044a190ae295aa305deb3dac453837bdcfac52ddd607564ddfd9fb76ee59f4ba"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Monero" in x


def test_blake2b256():
    hashes = ["87e402405c9c268532ba64e5130476237cfc1289e2e993d62c97f3b14febcbf0"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Blake2b-256" in x


def test_7zip():
    hashes = [
        "$7z$0$19$0$$16$c46ee87167606ba2cedbc7b61e970c63$3341692866$16$9$7f6b4ddc563d6481339775c52b653f00"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "7-zip" in x


def test_pdf4():
    hashes = [
        "$pdf$5*6*256*-4*1*16*381692e488413f5502fa7314a78c25db*48*e5bf81a2a23c88f3dccb44bc7da68bb5606b653b733bcf9adaa5eb2c8ccf53abba66539044eb1957eda68469b1d0b9b5*48*b222df06deb308bf919d13447e688775fdcab972faed2c866dc023a126cb4cd4bbffab3683ecde243cf8d88967184680"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "PDF 1.7 Level 8 (Acrobat 10 - 11)" in x
