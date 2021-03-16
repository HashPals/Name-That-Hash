from name_that_hash import runner
import click.testing


def test_it_works():

    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert x is not None


def test_it_identifieis_correctly():
    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "NTLM" in x


def test_main_succeeds():
    runn = click.testing.CliRunner()
    result = runn.invoke(runner.main)
    assert result.exit_code == 0


def test_if_no_hashes_found():
    hashes = ["abc"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "[]" in x


def test_bcrypt_dollar():
    # for issue #23
    hashes = ["$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "bcrypt" in x


def test_base64_works():
    # for issue #23
    hashes = ["NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk="]

    x = runner.api_return_hashes_as_json(hashes, {"base64": True})
    assert "MD5" in x


def test_scrypt_succeeds():
    # for issue #23
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "scrypt" in x

def test_kerberos():
    hashes = [
        "$krb5pa$23$user$realm$salt$4e751db65422b2117f7eac7b721932dc8aa0d9966785ecd958f971f622bf5c42dc0c70b532363138363631363132333238383835"
        "$krb5tgs$23$*user$realm$test/spn*$63386d22d359fe42230300d56852c9eb$891ad31d09ab89c6b3b8c5e5de6c06a7f49fd559d7a9a3c32576c8fedf705376cea582ab5938f7fc8bc741acf05c5990741b36ef4311fe3562a41b70a4ec6ecba849905f2385bb3799d92499909658c7287c49160276bca0006c350b0db4fd387adc27c01e9e9ad0c20ed53a7e6356dee2452e35eca2a6a1d1432796fc5c19d068978df74d3d0baf35c77de12456bf1144b6a750d11f55805f5a16ece2975246e2d026dce997fba34ac8757312e9e4e6272de35e20d52fb668c5ed"
        "$krb5asrep$23$user@domain.com:3e156ada591263b8aab0965f5aebd837$007497cb51b6c8116d6407a782ea0e1c5402b17db7afa6b05a6d30ed164a9933c754d720e279c6c573679bd27128fe77e5fea1f72334c1193c8ff0b370fadc6368bf2d49bbfdba4c5dccab95e8c8ebfdc75f438a0797dbfb2f8a1a5f4c423f9bfc1fea483342a11bd56a216f4d5158ccc4b224b52894fadfba3957dfe4b6b8f5f9f9fe422811a314768673e0c924340b8ccb84775ce9defaa3baa0910b676ad0036d13032b0dd94e3b13903cc738a7b6d00b0b3c210d1f972a6c7cae9bd3c959acf7565be528fc179118f28c679f6deeee1456f0781eb8154e18e49cb27b64bf74cd7112a0ebae2102ac"
        "$krb5tgs$17$user$realm$ae8434177efd09be5bc2eff8$90b4ce5b266821adc26c64f71958a475cf9348fce65096190be04f8430c4e0d554c86dd7ad29c275f9e8f15d2dab4565a3d6e21e449dc2f88e52ea0402c7170ba74f4af037c5d7f8db6d53018a564ab590fc23aa1134788bcc4a55f69ec13c0a083291a96b41bffb978f5a160b7edc828382d11aacd89b5a1bfa710b0e591b190bff9062eace4d26187777db358e70efd26df9c9312dbeef20b1ee0d823d4e71b8f1d00d91ea017459c27c32dc20e451ea6278be63cdd512ce656357c942b95438228e"
        "$krb5tgs$18$user$realm$8efd91bb01cc69dd07e46009$7352410d6aafd72c64972a66058b02aa1c28ac580ba41137d5a170467f06f17faf5dfb3f95ecf4fad74821fdc7e63a3195573f45f962f86942cb24255e544ad8d05178d560f683a3f59ce94e82c8e724a3af0160be549b472dd83e6b80733ad349973885e9082617294c6cbbea92349671883eaf068d7f5dcfc0405d97fda27435082b82b24f3be27f06c19354bf32066933312c770424eb6143674756243c1bde78ee3294792dcc49008a1b54f32ec5d5695f899946d42a67ce2fb1c227cb1d2004c0"
        "$krb5pa$17$hashcat$HASHCATDOMAIN.COM$a17776abe5383236c58582f515843e029ecbff43706d177651b7b6cdb2713b17597ddb35b1c9c470c281589fd1d51cca125414d19e40e333"
        "$krb5pa$17$user1$EXAMPLE.COM$$c5461873dc13665771b98ba80be53939e906d90ae1ba79cf2e21f0395e50ee56379fbef4d0298cfccfd6cf8f907329120048fd05e8ae5df4"
        "$krb5pa$18$hashcat$HASHCATDOMAIN.COM$96c289009b05181bfd32062962740b1b1ce5f74eb12e0266cde74e81094661addab08c0c1a178882c91a0ed89ae4e0e68d2820b9cce69770"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "kerberos" in x

def test_scrypt_python_dict():
    # for issue #23
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]

    x = runner.api_return_hashes_as_dict(hashes)
    assert "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo=" in x
