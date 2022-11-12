import re

from name_that_hash import runner


def test_if_all_tests_exist():
    with open("name_that_hash/hashes.py", "r", encoding="utf8") as file:
        database = file.read()

    with open("tests/test_hashcat.py", "r", encoding="utf8") as file:
        tests = file.read()

    database = re.findall(r"hashcat=(\d+)", database)
    tests = re.findall(r"test_hashcat_(\d+)", tests)

    for mode in database:
        assert mode in tests, "No test for this hash type found"


def test_hashcat_0():
    hashes = [
        '8743b52063cd84097a65d1633f5c74f5'
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 0,' in x

def test_hashcat_10():
    hashes = [
        "01dfae6e5d4d90d9892622325959afbe:7050461"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10,' in x

def test_hashcat_20():
    hashes = [
        "f0fda58630310a6dd91a7d8f0a4ceda2:4225637426"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20,' in x

def test_hashcat_30():
    hashes = [
        "b31d032cfdcf47a399990a71e43c5d2a:144816"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 30,' in x

def test_hashcat_40():
    hashes = [
        "d63d0e21fdc05f618d55ef306c54af82:13288442151473"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 40,' in x

def test_hashcat_50():
    hashes = [
        "fc741db0a2968c39d9c2a5cc75b05370:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 50,' in x

def test_hashcat_60():
    hashes = [
        "bfd280436f45fa38eaacac3b00518f29:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 60,' in x

def test_hashcat_100():
    hashes = [
        "b89eaac7e61417341b710b727768294d0e6a277b"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 100,' in x

def test_hashcat_110():
    hashes = [
        "2fc5a684737ce1bf7b3b239df432416e0dd07357:2014"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 110,' in x

def test_hashcat_120():
    hashes = [
        "cac35ec206d868b7d7cb0b55f31d9425b075082b:5363620024"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 120,' in x

def test_hashcat_130():
    hashes = [
        "c57f6ac1b71f45a07dbd91a59fa47c23abcd87c2:631225"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 130,' in x

def test_hashcat_140():
    hashes = [
        "5db61e4cd8776c7969cfd62456da639a4c87683a:8763434884872"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 140,' in x

def test_hashcat_150():
    hashes = [
        "c898896f3f70f61bc3fb19bef222aa860e5ea717:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 150,' in x

def test_hashcat_160():
    hashes = [
        "d89c92b4400b15c39e462a8caa939ab40c3aeeea:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 160,' in x

def test_hashcat_200():
    hashes = [
        "7196759210defdc0"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 200,' in x

def test_hashcat_300():
    hashes = [
        "fcf7c1b8749cf99d88e5f34271d636178fb5d130"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 300,' in x

def test_hashcat_400():
    hashes = [
        "$P$984478476IagS59wHZvyQMArzfx58u."
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 400,' in x

def test_hashcat_400():
    hashes = [
        "$H$984478476IagS59wHZvyQMArzfx58u."
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 400,' in x

def test_hashcat_500():
    hashes = [
        "$1$28772684$iEwNOgGugqO9.bIz5sk8k/"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 500,' in x

def test_hashcat_600():
    hashes = [
        "$BLAKE2$296c269e70ac5f0095e6fb47693480f0f7b97ccd0307f5c3bfa4df8f5ca5c9308a0e7108e80a0a9c0ebb715e8b7109b072046c6cd5e155b4cfd2f27216283b1e"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 600,' in x

def test_hashcat_900():
    hashes = [
        "afe04867ec7a3845145579a95f72eca7"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 900,' in x

def test_hashcat_1000():
    hashes = [
        "b4b9b02e6f09a9bd760f388b67351e2b"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1000,' in x

def test_hashcat_1100():
    hashes = [
        "4dd8965d1d476fa0d026722989a6b772:3060147285011"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1100,' in x

def test_hashcat_1400():
    hashes = [
        "127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1400,' in x

def test_hashcat_1410():
    hashes = [
        "c73d08de890479518ed60cf670d17faa26a4a71f995c1dcc978165399401a6c4:53743528"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1410,' in x

def test_hashcat_1420():
    hashes = [
        "eb368a2dfd38b405f014118c7d9747fcc97f4f0ee75c05963cd9da6ee65ef498:560407001617"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1420,' in x

def test_hashcat_1430():
    hashes = [
        "4cc8eb60476c33edac52b5a7548c2c50ef0f9e31ce656c6f4b213f901bc87421:890128"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1430,' in x

def test_hashcat_1440():
    hashes = [
        "a4bd99e1e0aba51814e81388badb23ecc560312c4324b2018ea76393ea1caca9:12345678"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1440,' in x

def test_hashcat_1450():
    hashes = [
        "abaf88d66bf2334a4a8b207cc61a96fb46c3e38e882e6f6f886742f688b8588c:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1450,' in x

def test_hashcat_1460():
    hashes = [
        "8efbef4cec28f228fa948daaf4893ac3638fbae81358ff9020be1d7a9a509fc6:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1460,' in x

def test_hashcat_1500():
    hashes = [
        "48c/R8JAv757A"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1500,' in x

def test_hashcat_1600():
    hashes = [
        "$apr1$71850310$gh9m4xcAn3MGxogwX/ztb."
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1600,' in x

def test_hashcat_1700():
    hashes = [
        "82a9dda829eb7f8ffe9fbe49e45d47d2dad9664fbb7adf72492e3c81ebd3e29134d9bc12212bf83c6840f10e8246b9db54a4859b7ccd0123d86e5872c1e5082f"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1700,' in x

def test_hashcat_1710():
    hashes = [
        "e5c3ede3e49fb86592fb03f471c35ba13e8d89b8ab65142c9a8fdafb635fa2223c24e5558fd9313e8995019dcbec1fb584146b7bb12685c7765fc8c0d51379fd:6352283260"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1710,' in x

def test_hashcat_1720():
    hashes = [
        "976b451818634a1e2acba682da3fd6efa72adf8a7a08d7939550c244b237c72c7d42367544e826c0c83fe5c02f97c0373b6b1386cc794bf0d21d2df01bb9c08a:2613516180127"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1720,' in x

def test_hashcat_1730():
    hashes = [
        "13070359002b6fbb3d28e50fba55efcf3d7cc115fe6e3f6c98bf0e3210f1c6923427a1e1a3b214c1de92c467683f6466727ba3a51684022be5cc2ffcb78457d2:341351589"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1730,' in x

def test_hashcat_1740():
    hashes = [
        "bae3a3358b3459c761a3ed40d34022f0609a02d90a0d7274610b16147e58ece00cd849a0bd5cf6a92ee5eb5687075b4e754324dfa70deca6993a85b2ca865bc8:1237015423"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1740,' in x

def test_hashcat_1750():
    hashes = [
        "94cb9e31137913665dbea7b058e10be5f050cc356062a2c9679ed0ad6119648e7be620e9d4e1199220cd02b9efb2b1c78234fa1000c728f82bf9f14ed82c1976:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1750,' in x

def test_hashcat_1760():
    hashes = [
        "7cce966f5503e292a51381f238d071971ad5442488f340f98e379b3aeae2f33778e3e732fcc2f7bdc04f3d460eebf6f8cb77da32df25500c09160dd3bf7d2a6b:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1760,' in x

def test_hashcat_1800():
    hashes = [
        "$6$52450745$k5ka2p8bFuSmoVT1tzOyyuaREkkKBcCNqoDKzYiJL9RaE8yMnPgh2XzzF0NDrUhgrcLwg78xs1w5pJiypEdFX/"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1800,' in x

def test_hashcat_2100():
    hashes = [
        "$DCC2$10240#tom#e4e938d12fe5974dc42a90120bd9c90f "
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2100,' in x

def test_hashcat_2400():
    hashes = [
        "dRRVnUmUHXOTt9nk"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2400,' in x

def test_hashcat_2410():
    hashes = [
        "02dMBMYkTdC5Ziyp:36"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2410,' in x

def test_hashcat_2600():
    hashes = [
        "a936af92b0ae20b1ff6c3347a72e5fbe"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2600,' in x

def test_hashcat_3000():
    hashes = [
        "299bd128c1101fd6"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3000,' in x

def test_hashcat_3100():
    hashes = [
        "7A963A529D2E3229:3682427524"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3100,' in x

def test_hashcat_3200():
    hashes = [
        "$2a$05$LhayLxezLhK1LhWvKxCyLOj0j1u.Kj0jZ0pEmm134uzrQlFvQJLF6"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3200,' in x

def test_hashcat_3710():
    hashes = [
        "95248989ec91f6d0439dbde2bd0140be:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3710,' in x

def test_hashcat_3800():
    hashes = [
        "2e45c4b99396c6cb2db8bda0d3df669f:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3800,' in x

def test_hashcat_3910():
    hashes = [
        "250920b3a5e31318806a032a4674df7e:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3910,' in x

def test_hashcat_4010():
    hashes = [
        "30d0cf4a5d7ed831084c5b8b0ba75b46:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4010,' in x

def test_hashcat_4110():
    hashes = [
        "b4cb5c551a30f6c25d648560408df68a:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4110,' in x

def test_hashcat_4300():
    hashes = [
        "b8c385461bb9f9d733d3af832cf60b27"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4300,' in x

def test_hashcat_4400():
    hashes = [
        "288496df99b33f8f75a7ce4837d1b480"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4400,' in x

def test_hashcat_4500():
    hashes = [
        "3db9184f5da4e463832b086211af8d2314919951"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4500,' in x

def test_hashcat_4700():
    hashes = [
        "92d85978d884eb1d99a51652b1139c8279fa8663"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4700,' in x

def test_hashcat_4710():
    hashes = [
        "53c724b7f34f09787ed3f1b316215fc35c789504:hashcat1"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4710,' in x

def test_hashcat_4800():
    hashes = [
        "afd09efdd6f8ca9f18ec77c5869788c3:01020304050607080910111213141516:01"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4800,' in x

def test_hashcat_5100():
    hashes = [
        "8743b52063cd8409"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5100,' in x

def test_hashcat_5500():
    hashes = [
        "u4-netntlm::kNS:338d08f8e26de93300000000000000000000000000000000:9526fb8c23a90751cdd619b6cea564742e1e4bf33006ba41:cb8086049ec4736c"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5500,' in x

def test_hashcat_5600():
    hashes = [
        "admin::N46iSNekpT:08ca45b7d7ea58ee:88dcbe4446168966a153a0064958dac6:5c7830315c7830310000000000000b45c67103d07d7b95acd12ffa11230e0000000052920b85f78d013c31cdb3b92f5d765c783030"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5600,' in x

def test_hashcat_5700():
    hashes = [
        "2btjjy78REtmYkkW0csHUbJZOstRXoWdX1mGrmmfeHI"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5700,' in x

def test_hashcat_5800():
    hashes = [
        "0223b799d526b596fe4ba5628b9e65068227e68e:f6d45822728ddb2c"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5800,' in x

def test_hashcat_6000():
    hashes = [
        "012cb9b334ec1aeb71a9c8ce85586082467f7eb6"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6000,' in x

def test_hashcat_6100():
    hashes = [
        "7ca8eaaaa15eaa4c038b4c47b9313e92da827c06940e69947f85bc0fbef3eb8fd254da220ad9e208b6b28f6bb9be31dd760f1fdb26112d83f87d96b416a4d258"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6100,' in x

def test_hashcat_6300():
    hashes = [
        "{smd5}a5/yTL/u$VfvgyHx1xUlXZYBocQpQY0"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6300,' in x

def test_hashcat_6400():
    hashes = [
        "{ssha256}06$aJckFGJAB30LTe10$ohUsB7LBPlgclE3hJg9x042DLJvQyxVCX.nZZLEz.g2"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6400,' in x

def test_hashcat_6700():
    hashes = [
        "{ssha1}06$bJbkFGJAB30L2e23$dCESGOsP7jaIIAJ1QAcmaGeG.kr"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6700,' in x

def test_hashcat_6800():
    hashes = [
        "a2d1f7b7a1862d0d4a52644e72d59df5:500:lp@trash-mail.com"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6800,' in x

def test_hashcat_6900():
    hashes = [
        "df226c2c6dcb1d995c0299a33a084b201544293c31fc3d279530121d36bbcea9"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6900,' in x

def test_hashcat_7000():
    hashes = [
        "AK1AAECAwQFBgcICRARNGqgeC3is8gv2xWWRony9NJnDgE="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7000,' in x

def test_hashcat_7100():
    hashes = [
        "$ml$35460$93a94bd24b5de64d79a5e49fa372827e739f4d7b6975c752c9a0ff1e5cf72e05$752351df64dd2ce9dc9c64a72ad91de6581a15c19176266b44d98919dfa81f0f96cbcb20a1ffb400718c20382030f637892f776627d34e021bad4f81b7de8222"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7100,' in x

def test_hashcat_7200():
    hashes = [
        "grub.pbkdf2.sha512.10000.7d391ef48645f626b427b1fae06a7219b5b54f4f02b2621f86b5e36e83ae492bd1db60871e45bc07925cecb46ff8ba3db31c723c0c6acbd4f06f60c5b246ecbf.26d59c52b50df90d043f070bd9cbcd92a74424da42b3666fdeb08f1a54b8f1d2f4f56cf436f9382419c26798dc2c209a86003982b1e5a9fcef905f4dfaa4c524"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7200,' in x

def test_hashcat_7300():
    hashes = [
        "b7c2d6f13a43dce2e44ad120a9cd8a13d0ca23f0414275c0bbe1070d2d1299b1c04da0f1a0f1e4e2537300263a2200000000000000000000140768617368636174:472bdabe2d5d4bffd6add7b3ba79a291d104a9ef"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7300,' in x

def test_hashcat_7400():
    hashes = [
        "$5$rounds=5000$GX7BopJZJxPc/KEK$le16UF8I2Anb.rOrn22AUPWvzUETDGefUmAV8AZkGcD"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7400,' in x

def test_hashcat_7500():
    hashes = [
        "$krb5pa$23$user$realm$salt$4e751db65422b2117f7eac7b721932dc8aa0d9966785ecd958f971f622bf5c42dc0c70b532363138363631363132333238383835"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7500,' in x

def test_hashcat_7700():
    hashes = [
        "USER$C8B48F26B87B7EA7"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7700,' in x

def test_hashcat_7800():
    hashes = [
        "USER$ABCAD719B17E7F794DF7E686E563E9E2D24DE1D0"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7800,' in x

def test_hashcat_7900():
    hashes = [
        "$S$C33783772bRXEx1aCsvY.dqgaaSu76XmVlKrW9Qu8IQlvxHlmzLf"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 7900,' in x

def test_hashcat_8000():
    hashes = [
        "0xc00778168388631428230545ed2c976790af96768afa0806fe6c0da3b28f3e132137eac56f9bad027ea2"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8000,' in x

def test_hashcat_8100():
    hashes = [
        "1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8100,' in x

def test_hashcat_8300():
    hashes = [
        "7b5n74kq8r441blc2c5qbbat19baj79r:.lvdsiqfj.net:33164473:1"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8300,' in x

def test_hashcat_8400():
    hashes = [
        "8084df19a6dc81e2597d051c3d8b400787e2d5a9:6755045315424852185115352765375338838643"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8400,' in x

def test_hashcat_8500():
    hashes = [
        "$racf$*USER*FC2577C6EBE6265B"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8500,' in x

def test_hashcat_8600():
    hashes = [
        "3dd2e1e5ac03e230243d58b8c5ada076"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8600,' in x

def test_hashcat_8700():
    hashes = [
        "(GDpOtD35gGlyDksQRxEU)"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8700,' in x

def test_hashcat_8900():
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8900,' in x

def test_hashcat_9100():
    hashes = [
        "(HsjFebq0Kh9kH7aAZYc7kY30mC30mC3KmC30mCluagXrvWKj1)"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9100,' in x

def test_hashcat_9200():
    hashes = [
        "$8$TnGX/fE4KGHOVU$pEhnEvxrvaynpi8j4f.EMHr6M.FzU8xnZnBr/tJdFWk "
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9200,' in x

def test_hashcat_9300():
    hashes = [
        "$9$2MJBozw/9R3UsU$2lFhcKvpghcyw8deP25GOfyZaagyUOGBymkryvOdfo6 "
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9300,' in x

def test_hashcat_9400():
    hashes = [
        "$office$*2007*20*128*16*411a51284e0d0200b131a8949aaaa5cc*117d532441c63968bee7647d9b7df7d6*df1d601ccf905b375575108f42ef838fb88e1cde"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9400,' in x

def test_hashcat_9500():
    hashes = [
        "$office$*2010*100000*128*16*77233201017277788267221014757262*b2d0ca4854ba19cf95a2647d5eee906c*e30cbbb189575cafb6f142a90c2622fa9e78d293c5b0c001517b3f5b82993557 "
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9500,' in x

def test_hashcat_9600():
    hashes = [
        "$office$*2013*100000*256*16*7dd611d7eb4c899f74816d1dec817b3b*948dc0b2c2c6c32f14b5995a543ad037*0b7ee0e48e935f937192a59de48a7d561ef2691d5c8a3ba87ec2d04402a94895 "
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9600,' in x

def test_hashcat_9700():
    hashes = [
        "$oldoffice$1*04477077758555626246182730342136*b1b72ff351e41a7c68f6b45c4e938bd6*0d95331895e99f73ef8b6fbc4a78ac1a"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9700,' in x

def test_hashcat_9710():
    hashes = [
        "$oldoffice$0*55045061647456688860411218030058*e7e24d163fbd743992d4b8892bf3f2f7*493410dbc832557d3fe1870ace8397e2"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9710,' in x

def test_hashcat_9720():
    hashes = [
        "$oldoffice$0*55045061647456688860411218030058*e7e24d163fbd743992d4b8892bf3f2f7*493410dbc832557d3fe1870ace8397e2:91b2e062b9"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9720,' in x

def test_hashcat_9800():
    hashes = [
        "$oldoffice$3*83328705222323020515404251156288*2855956a165ff6511bc7f4cd77b9e101*941861655e73a09c40f7b1e9dfd0c256ed285acd"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9800,' in x

def test_hashcat_9810():
    hashes = [
        "$oldoffice$3*83328705222323020515404251156288*2855956a165ff6511bc7f4cd77b9e101*941861655e73a09c40f7b1e9dfd0c256ed285acd"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9810,' in x

def test_hashcat_9820():
    hashes = [
        "$oldoffice$3*83328705222323020515404251156288*2855956a165ff6511bc7f4cd77b9e101*941861655e73a09c40f7b1e9dfd0c256ed285acd:b8f63619ca"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9820,' in x

def test_hashcat_9900():
    hashes = [
        "22527bee5c29ce95373c4e0f359f079b"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 9900,' in x

def test_hashcat_10000():
    hashes = [
        "pbkdf2_sha256$20000$H0dPx8NeajVu$GiC4k5kqbbR9qWBlsRgDywNqC2vd9kqfk7zdorEnNas="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10000,' in x

def test_hashcat_10100():
    hashes = [
        "ad61d78c06037cd9:2:4:81533218127174468417660201434054"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10100,' in x

def test_hashcat_10200():
    hashes = [
        "$cram_md5$PG5vLXJlcGx5QGhhc2hjYXQubmV0Pg==$dXNlciA0NGVhZmQyMmZlNzY2NzBmNmIyODc5MDgxYTdmNWY3MQ=="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10200,' in x

def test_hashcat_10300():
    hashes = [
        "{x-issha, 1024}C0624EvGSdAMCtuWnBBYBGA0chvqAflKY74oEpw/rpY="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10300,' in x

def test_hashcat_10400():
    hashes = [
        "$pdf$1*2*40*-1*0*16*51726437280452826511473255744374*32*9b09be05c226214fa1178342673d86f273602b95104f2384b6c9b709b2cbc058*32*0000000000000000000000000000000000000000000000000000000000000000"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10400,' in x

def test_hashcat_10410():
    hashes = [
        "$pdf$1*2*40*-1*0*16*01221086741440841668371056103222*32*27c3fecef6d46a78eb61b8b4dbc690f5f8a2912bbb9afc842c12d79481568b74*32*0000000000000000000000000000000000000000000000000000000000000000"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10410,' in x

def test_hashcat_10420():
    hashes = [
        "$pdf$1*2*40*-1*0*16*01221086741440841668371056103222*32*27c3fecef6d46a78eb61b8b4dbc690f5f8a2912bbb9afc842c12d79481568b74*32*0000000000000000000000000000000000000000000000000000000000000000:6a8aedccb7"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10420,' in x

def test_hashcat_10500():
    hashes = [
        "$pdf$2*3*128*-1028*1*16*da42ee15d4b3e08fe5b9ecea0e02ad0f*32*c9b59d72c7c670c42eeb4fca1d2ca15000000000000000000000000000000000*32*c4ff3e868dc87604626c2b8c259297a14d58c6309c70b00afdfb1fbba10ee571"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10500,' in x

def test_hashcat_10600():
    hashes = [
        "$pdf$5*5*256*-1028*1*16*20583814402184226866485332754315*127*f95d927a94829db8e2fbfbc9726ebe0a391b22a084ccc2882eb107a74f7884812058381440218422686648533275431500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*127*00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10600,' in x

def test_hashcat_10700():
    hashes = [
        "$pdf$5*6*256*-1028*1*16*21240790753544575679622633641532*127*2d1ecff66ea354d3d34325a6503da57e03c199c21b13dd842f8d515826054d8d2124079075354457567962263364153200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*127*00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10700,' in x

def test_hashcat_10800():
    hashes = [
        "07371af1ca1fca7c6941d2399f3610f1e392c56c6d73fddffe38f18c430a2817028dae1ef09ac683b62148a2c8757f42"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10800,' in x

def test_hashcat_10900():
    hashes = [
        "sha256:1000:MTc3MTA0MTQwMjQxNzY=:PYjCU215Mi57AYPKva9j7mvF4Rc5bCnt"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 10900,' in x

def test_hashcat_11000():
    hashes = [
        "810e3d12f0f10777a679d9ca1ad7a8d9:M2uZ122bSHJ4Mi54tXGY0lqcv1r28mUluSkyw37ou5oia4i239ujqw0l"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11000,' in x

def test_hashcat_11100():
    hashes = [
        "$postgres$postgres*f0784ea5*2091bb7d4725d1ca85e8de6ec349baf6"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11100,' in x

def test_hashcat_11200():
    hashes = [
        "$mysqlna$1c24ab8d0ee94d70ab1f2e814d8f0948a14d10b9*437e93572f18ae44d9e779160c2505271f85821d"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11200,' in x

def test_hashcat_11300():
    hashes = [
        "$bitcoin$96$d011a1b6a8d675b7a36d0cd2efaca32a9f8dc1d57d6d01a58399ea04e703e8bbb44899039326f7a00f171a7bbc854a54$16$1563277210780230$158555$96$628835426818227243334570448571536352510740823233055715845322741625407685873076027233865346542174$66$625882875480513751851333441623702852811440775888122046360561760525"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11300,' in x

def test_hashcat_11500():
    hashes = [
        "c762de4a:00000000"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11500,' in x

def test_hashcat_11600():
    hashes = [
        "$7z$0$19$0$salt$8$f6196259a7326e3f0000000000000000$185065650$112$98$f3bc2a88062c419a25acd40c0c2d75421cf23263f69c51b13f9b1aada41a8a09f9adeae45d67c60b56aad338f20c0dcc5eb811c7a61128ee0746f922cdb9c59096869f341c7a9cb1ac7bb7d771f546b82cf4e6f11a5ecd4b61751e4d8de66dd6e2dfb5b7d1022d2211e2d66ea1703f96"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11600,' in x

def test_hashcat_12400():
    hashes = [
        "_9G..8147mpcfKT8g0U."
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 12400,' in x

def test_hashcat_13400_1():
    hashes = [
        "$keepass$*1*50000*0*375756b9e6c72891a8e5645a3338b8c8*82afc053e8e1a6cfa39adae4f5fe5e59f545a54d6956593d1709b39cacd7f796*c698fbfc7d1b71431d10611e2216ab21*24a63140f4eb3bfd7d59b7694eea38d1d93a43bc3af989755d2b326286c4d510*1*192*1a65072f436e9da0c9e832eca225a04ab78821b55d9f550860ade2ef8126a2c4050cf4d033374abd3dac6d0c5907c6cbb033643b203825c12e6c9853b5ac17a4809559fe723e01b4a2ab87cc83c8ba7ee4a757b8a0cf1674106f21f6675cba12064443d65436650df10ea0923c4cadfd4bfe341a6f4fa23a1a67f7d12a489fc5410ef6db9f6607905de491d3b3b915852a1b6c231c96366cbdee5ea9bd7f73ffd2f7a579215528ae1bf0ea540947ebfe39ca84bc6cbeded4f8e8fb6ed8f32dd5"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 13400,' in x

def test_hashcat_13400_2():
    hashes = [
        "$keepass$*2*6000*222*a279e37c38b0124559a83fa452a0269d56dc4119a5866d18e76f1f3fd536d64d*7ec7a06bc975ea2ae7c8dcb99e826a308564849b6b25d858cbbc78475af3733f*d477c849bf2278b7a1f626c81e343553*38c8ec186141c2705f2bcb334a730933ed3b0ee11391e1100fbaf429f6c99078*1ada85fe78cf36ab0537562a787dd83e446f13cd3d9a60fd495003de3537b702"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 13400,' in x

def test_hashcat_13400_3():
    hashes = [
        "$keepass$*1*6000*1*31c087828b0bb76362c10cae773aacdf*6d6c78b4f82ecbcd3b96670cf490914c25ea8c31bc3aeb3fc56e65fac16d721f*a735ec88c01816bc66200c8e17ee9110*08334be8523f4b69bd4e2328db854329bfc81e2ea5a46d8ccf3bccf7c03d879d*1*1360*f1e2c6c47f88c2abf4e79dbe73339b77778233a6c7d7f49f6b7d5db6a4885ff33585e221f5e94e8f7cc84ddcbe9c61a3d40c4f503a4ec7e91edca5745454588eebb4f0dc4d251c0d88eb5fae5d5b651d16e56ef830f412cb7fccf643de4963b66852d3a775489b5abb394b6fa325c3dbb4a55dd06d44c5fc911f1305e55accf0dc0eb172788f5400aab3c867cc6c5ddb7cd3e57bb78a739416985a276825171f5a19750dede055aa3e5fca9b11e3606beae97d68e593631a2efd88cdeb9f43b5ac1d1d9f0164f0fb022ea44a4a48061629c83d8f5bc594e3655ee684102fe706d1e96178bb805105fe1c5326c951401a6e7c9a0b8b572e7b74c3fb25e8700a2e0e70b4621ae3878805397ea1b873ea5218fdaa4fc5d11cdf7ea3579601eca3750fa347edc08569b1f51606d35920253f85f33e6a757a585adf079173161af919f7ea0d78ca6ca1513d01855057373c4f9fe22aba1fc4b18708d329500c127b865a528435e9e00d0a80554ae6eaf4d58bf85a959f37d0854b36c782991c36120b41ee2d9905b18d525b6bffef310e90dbfbe9be853614e6559737f1141f725902f59ee02789c6490c16adf0957e36dc4101c57ba35acb4ca9ec60f5585b60e74342921bbc7e56df5ad942b6deb7936532439b1dae39b9709cf282239c57b434d6f65ba277012ccddce32a217964f974c16f96d8b078ceaad43de9f3d5309279843f2f347ad8ae6eab3a998bb99a421b22b806e2f2302f9dcf3ba54e3d3f1ee64ef3b202194912eec202c2f44847ad5293b03b6b22df35f505670a79219efc399c6a4fa3fd4be7953e5df9baf94101c0a7036b82b6950ab2b722e38aec47bf1c7ffb4e82f43b9ca18d2a8b0b2a7b92015b01d07a429d2660902185cf143f871ff49dde73acf7c3bfd9c124733bd90ffe0fd1cc9090d56dd70bd62f9df1bfa4748ea3438f669d5691c61ec7fbc9d53ab4d8c2dda2cf203f7a5a7fac72eb2efe1d9a27b8c5b14e07a55c530dfd7b7c69dcf478590b7b364f5379f92a0762be0005c4cbc5285d7828248159286fe6d29c02c7de04e96e737a2d30ce75ff774982433f75ca16f09ad668e5b13f0a2e84886773d8fff67f71c1a9dab13f78e5b2da9b1eed9ab2208934a6da7eab32b3e8da1599d6cfa7e9c19ad8efc85dd9a2a4b95832c435381c2fe7e44c58045ce91e40d58c36924b38b19cbafd696bac8761229de9099ce31ee1c93a98aa0cb2a7c60b71b7f1998690e5eae623827727cfe7e8eed94ffc927a1e15aac32292daccda4f0d35383ce87f7e872fc3fe8f01f4a44de4f7b76257abc9c056ab8ae0d96d2dc3a154408c28a2e7befbd515cb5013cbfed31af456ac2b596b5d8095420c411b981d48741dc7ed1e8de4e428bd5e5a553348e2890b1ed12b7dc88261ab921a12da43e6344bbb4a0e0ce2b84c2d1d6c1f51b88202743433ac24340ae00cf27d43346240f4dc5e35ec29fcf1bf6de3bcc09ee8db3f49c3b6615bd8796bbe2cf4b914766779408e772123d9e51cc92ed5dedafa427fd767198cb97674eded4e4df84716aec75cbe7a54620c283fa60780be3cd66ea4167f46cdea1506be92a5102317c8ab8be097c993d82bd831818fe7cb1fbfecc3432d93e0f6d36da8a65ed15c78e623d59980be7ff54bdb1786de2ca9e7a11f0fe067db9ec42ade3bbaad10adae5ea77ba76fa2d0723a35891bde91da540a58e343c23afa9e22b38a66171eb9dbbd55f9e0f014e9de3943388fe0990cc801bbb978c02bf680b3c63a747e22a6317440c40e6844987e936c88c25f49e601ec3486ab080165b5e01dbee47a0a385dfba22ec5ed075f94052bdddabde761bbcc79852402c5b22ded89af4c602922099e37d71b7f87f4ffa614b4ca106fca6b062cba350be1fd12c6812db82f3e02a81e42*1*64*bbc3babf62557aa4dfba705e24274e1aebf43907fe12f52eaf5395066f7cbdba"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 13400,' in x

def test_hashcat_13400_4():
    hashes = [
        "$keepass$*1*50000*0*375756b9e6c72891a8e5645a3338b8c8*82afc053e8e1a6cfa39adae4f5fe5e59f545a54d6956593d1709b39cacd7f796*c698fbfc7d1b71431d10611e2216ab21*24a63140f4eb3bfd7d59b7694eea38d1d93a43bc3af989755d2b326286c4d510*1*192*1a65072f436e9da0c9e832eca225a04ab78821b55d9f550860ade2ef8126a2c4050cf4d033374abd3dac6d0c5907c6cbb033643b203825c12e6c9853b5ac17a4809559fe723e01b4a2ab87cc83c8ba7ee4a757b8a0cf1674106f21f6675cba12064443d65436650df10ea0923c4cadfd4bfe341a6f4fa23a1a67f7d12a489fc5410ef6db9f6607905de491d3b3b915852a1b6c231c96366cbdee5ea9bd7f73ffd2f7a579215528ae1bf0ea540947ebfe39ca84bc6cbeded4f8e8fb6ed8f32dd5"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 13400,' in x

def test_hashcat_13100():
    hashes = [
        "$krb5tgs$23$*user$realm$test/spn*$63386d22d359fe42230300d56852c9eb$891ad31d09ab89c6b3b8c5e5de6c06a7f49fd559d7a9a3c32576c8fedf705376cea582ab5938f7fc8bc741acf05c5990741b36ef4311fe3562a41b70a4ec6ecba849905f2385bb3799d92499909658c7287c49160276bca0006c350b0db4fd387adc27c01e9e9ad0c20ed53a7e6356dee2452e35eca2a6a1d1432796fc5c19d068978df74d3d0baf35c77de12456bf1144b6a750d11f55805f5a16ece2975246e2d026dce997fba34ac8757312e9e4e6272de35e20d52fb668c5ed"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 13100,' in x

def test_hashcat_13600():
    hashes = [
        "$zip2$*0*3*0*e3222d3b65b5a2785b192d31e39ff9de*1320*e*19648c3e063c82a9ad3ef08ed833*3135c79ecb86cd6f48fc*$/zip2$"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 13600,' in x

def test_hashcat_14800():
    hashes = [
        "$itunes_backup$*10*8b715f516ff8e64442c478c2d9abb046fc6979ab079007d3dbcef3ddd84217f4c3db01362d88fa68*10000*2353363784073608264337337723324886300850*10000000*425b4bb4e200b5fd4c66979c9caca31716052063"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 14800,' in x

def test_hashcat_15100():
    hashes = [
        "$sha1$15100$jiJDkz0E$E8C7RQAD3NetbSDz7puNAY.5Y2jr"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 15100,' in x

def test_hashcat_15600():
    hashes = [
        "$ethereum$p*262144*3238383137313130353438343737383736323437353437383831373034343735*06eae7ee0a4b9e8abc02c9990e3730827396e8531558ed15bb733faf12a44ce1*e6d5891d4f199d31ec434fe25d9ecc2530716bc3b36d5bdbc1fab7685dda3946"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 15600,' in x

def test_hashcat_16300():
    hashes = [
        "$ethereum$w*e94a8e49deac2d62206bf9bfb7d2aaea7eb06c1a378cfc1ac056cc599a569793c0ecc40e6a0c242dee2812f06b644d70f43331b1fa2ce4bd6cbb9f62dd25b443235bdb4c1ffb222084c9ded8c719624b338f17e0fd827b34d79801298ac75f74ed97ae16f72fccecf862d09a03498b1b8bd1d984fc43dd507ede5d4b6223a582352386407266b66c671077eefc1e07b5f42508bf926ab5616658c984968d8eec25c9d5197a4a30eed54c161595c3b4d558b17ab8a75ccca72b3d949919d197158ea5cfbc43ac7dd73cf77807dc2c8fe4ef1e942ccd11ec24fe8a410d48ef4b8a35c93ecf1a21c51a51a08f3225fbdcc338b1e7fdafd7d94b82a81d88c2e9a429acc3f8a5974eafb7af8c912597eb6fdcd80578bd12efddd99de47b44e7c8f6c38f2af3116b08796172eda89422e9ea9b99c7f98a7e331aeb4bb1b06f611e95082b629332c31dbcfd878aed77d300c9ed5c74af9cd6f5a8c4a261dd124317fb790a04481d93aec160af4ad8ec84c04d943a869f65f07f5ccf8295dc1c876f30408eac77f62192cbb25842470b4a5bdb4c8096f56da7e9ed05c21f61b94c54ef1c2e9e417cce627521a40a99e357dd9b7a7149041d589cbacbe0302db57ddc983b9a6d79ce3f2e9ae8ad45fa40b934ed6b36379b780549ae7553dbb1cab238138c05743d0103335325bd90e27d8ae1ea219eb8905503c5ad54fa12d22e9a7d296eee07c8a7b5041b8d56b8af290274d01eb0e4ad174eb26b23b5e9fb46ff7f88398e6266052292acb36554ccb9c2c03139fe72d3f5d30bd5d10bd79d7cb48d2ab24187d8efc3750d5a24980fb12122591455d14e75421a2074599f1cc9fdfc8f498c92ad8b904d3c4307f80c46921d8128*f3abede76ac15228f1b161dd9660bb9094e81b1b*d201ccd492c284484c7824c4d37b1593"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 16300,' in x

def test_hashcat_16600():
    hashes = [
        "$electrum$1*44358283104603165383613672586868*c43a6632d9f59364f74c395a03d8c2ea"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 16600,' in x

def test_hashcat_17300():
    hashes = [
        "412ef78534ba6ab0e9b1607d3e9767a25c1ea9d5e83176b4c2817a6c"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 17300,' in x

def test_hashcat_17400():
    hashes = [
        "d60fcf6585da4e17224f58858970f0ed5ab042c3916b76b0b828e62eaf636cbd"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 17400,' in x

def test_hashcat_17600():
    hashes = [
        "7c2dc1d743735d4e069f3bda85b1b7e9172033dfdd8cd599ca094ef8570f3930c3f2c0b7afc8d6152ce4eaad6057a2ff22e71934b3a3dd0fb55a7fc84a53144e"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 17600,' in x

def test_hashcat_17700():
    hashes = [
        "e1dfad9bafeae6ef15f5bbb16cf4c26f09f5f1e7870581962fc84636"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 17700,' in x

def test_hashcat_17800():
    hashes = [
        "203f88777f18bb4ee1226627b547808f38d90d3e106262b5de9ca943b57137b6"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 17800,' in x

def test_hashcat_17900():
    hashes = [
        "5804b7ada5806ba79540100e9a7ef493654ff2a21d94d4f2ce4bf69abda5d94bf03701fe9525a15dfdc625bfbd769701"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 17900,' in x

def test_hashcat_18200():
    hashes = [
        "$krb5asrep$23$user@domain.com:3e156ada591263b8aab0965f5aebd837$007497cb51b6c8116d6407a782ea0e1c5402b17db7afa6b05a6d30ed164a9933c754d720e279c6c573679bd27128fe77e5fea1f72334c1193c8ff0b370fadc6368bf2d49bbfdba4c5dccab95e8c8ebfdc75f438a0797dbfb2f8a1a5f4c423f9bfc1fea483342a11bd56a216f4d5158ccc4b224b52894fadfba3957dfe4b6b8f5f9f9fe422811a314768673e0c924340b8ccb84775ce9defaa3baa0910b676ad0036d13032b0dd94e3b13903cc738a7b6d00b0b3c210d1f972a6c7cae9bd3c959acf7565be528fc179118f28c679f6deeee1456f0781eb8154e18e49cb27b64bf74cd7112a0ebae2102ac"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 18200,' in x

def test_hashcat_18900():
    hashes = [
        "$ab$5*0*10000*b8900e4885ff9cad8f01ee1957a43bd633fea12491440514ae27aa83f2f5c006ec7e7fa0bce040add619919b4eb60608304b7d571a2ed87fd58c9ad6bc5fcf4c*7d254d93e16be9312fb1ccbfc6265c40cb0c5eab7b605a95a116e2383fb1cf12b688223f96221dcd2bf5410d4ca6f90e0789ee00157fa91658b42665d6b6844c*fc9f6be604d1c59ac32664ec2c5b9b30*00c4972149af3adcc235899e9d20611ea6e8de2212afcb9fcfefde7e35b691c2d0994eb47e4f9a260526ba47f4caea71af9c7fadcd5685d50126276f6acdd59966528b13ccc26036a0eaba2f2451aa64b05766d0edd03c988dcf87e2a9eec52d"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 18900,' in x

def test_hashcat_19600():
    hashes = [
        "$krb5tgs$17$user$realm$ae8434177efd09be5bc2eff8$90b4ce5b266821adc26c64f71958a475cf9348fce65096190be04f8430c4e0d554c86dd7ad29c275f9e8f15d2dab4565a3d6e21e449dc2f88e52ea0402c7170ba74f4af037c5d7f8db6d53018a564ab590fc23aa1134788bcc4a55f69ec13c0a083291a96b41bffb978f5a160b7edc828382d11aacd89b5a1bfa710b0e591b190bff9062eace4d26187777db358e70efd26df9c9312dbeef20b1ee0d823d4e71b8f1d00d91ea017459c27c32dc20e451ea6278be63cdd512ce656357c942b95438228e"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 19600,' in x

def test_hashcat_19700():
    hashes = [
        "$krb5tgs$18$user$realm$8efd91bb01cc69dd07e46009$7352410d6aafd72c64972a66058b02aa1c28ac580ba41137d5a170467f06f17faf5dfb3f95ecf4fad74821fdc7e63a3195573f45f962f86942cb24255e544ad8d05178d560f683a3f59ce94e82c8e724a3af0160be549b472dd83e6b80733ad349973885e9082617294c6cbbea92349671883eaf068d7f5dcfc0405d97fda27435082b82b24f3be27f06c19354bf32066933312c770424eb6143674756243c1bde78ee3294792dcc49008a1b54f32ec5d5695f899946d42a67ce2fb1c227cb1d2004c0"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 19700,' in x

def test_hashcat_19800():
    hashes = [
        "$krb5pa$17$hashcat$HASHCATDOMAIN.COM$a17776abe5383236c58582f515843e029ecbff43706d177651b7b6cdb2713b17597ddb35b1c9c470c281589fd1d51cca125414d19e40e333"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 19800,' in x

def test_hashcat_19900():
    hashes = [
        "$krb5pa$18$hashcat$HASHCATDOMAIN.COM$96c289009b05181bfd32062962740b1b1ce5f74eb12e0266cde74e81094661addab08c0c1a178882c91a0ed89ae4e0e68d2820b9cce69770"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 19900,' in x

def test_hashcat_20200():
    hashes = [
        "$pbkdf2-sha512$25000$LyWE0HrP2RsjZCxlDGFMKQ$1vC5Ohk2mCS9b6akqsEfgeb4l74SF8XjH.SljXf3dMLHdlY1GK9ojcCKts6/asR4aPqBmk74nCDddU3tvSCJvw"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20200,' in x

def test_hashcat_20300():
    hashes = [
        "$pbkdf2-sha256$29000$x9h7j/Ge8x6DMEao1VqrdQ$kra3R1wEnY8mPdDWOpTqOTINaAmZvRMcYd8u5OBQP9A"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20300,' in x

def test_hashcat_20400():
    hashes = [
        "$pbkdf2$131000$r5WythYixPgfQ2jt3buXcg$8Kdr.QQEOaZIXNOrrru36I/.6Po"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20400,' in x

def test_hashcat_20500():
    hashes = [
        "f1eff5c0368d10311dcfc419"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20500,' in x

def test_hashcat_21700():
    hashes = [
        "$electrum$4*03eae309d8bda5dcbddaae8145469193152763894b7260a6c4ba181b3ac2ed5653*8c594086a64dc87a9c1f8a69f646e31e8d3182c3c722def4427aa20684776ac26092c6f60bf2762e27adfa93fe1e952dcb8d6362224b9a371953aa3a2edb596ce5eb4c0879c4353f2cc515ec6c9e7a6defa26c5df346d18a62e9d40fcc606bc8c34322bf2212f77770a683788db0baf4cb43595c2a27fe5ff8bdcb1fd915bcd725149d8ee8f14c71635fecb04da5dde97584f4581ceb7d907dceed80ae5daa8352dda20b25fd6001e99a96b7cf839a36cd3f5656304e6998c18e03dd2fb720cb41386c52910c9cb83272c3d50f3a6ff362ab8389b0c21c75133c971df0a75b331796371b060b32fe1673f4a041d7ae08bbdeffb45d706eaf65f99573c07972701c97766b4d7a8a03bba0f885eb3845dfd9152286e1de1f93e25ce04c54712509166dda80a84c2d34652f68e6c01e662f8b1cc7c15103a4502c29332a4fdbdda470c875809e15aab3f2fcb061ee96992ad7e8ab9da88203e35f47d6e88b07a13b0e70ef76de3be20dc06facbddc1e47206b16b44573f57396265116b4d243e77d1c98bc2b28aa3ec0f8d959764a54ecdd03d8360ff2823577fe2183e618aac15b30c1d20986841e3d83c0bfabcedb7c27ddc436eb7113db927e0beae7522b04566631a090b214660152a4f4a90e19356e66ee7309a0671b2e7bfde82667538d193fc7e397442052c6c611b6bf0a04f629a1dc7fa9eb44bfad1bfc6a0bce9f0564c3b483737e447720b7fd038c9a961a25e9594b76bf8c8071c83fcacd689c7469f698ee4aee4d4f626a73e21ce4967e705e4d83e1145b4260330367d8341c84723a1b02567ffbab26aac3afd1079887b4391f05d09780fc65f8b4f68cd51391c06593919d7eafd0775f83045b8f5c2e59cef902ff500654ea29b7623c7594ab2cc0e05ffe3f10abc46c9c5dac824673c307dcbff5bc5f3774141ff99f6a34ec4dd8a58d154a1c72636a2422b8fafdef399dec350d2b91947448582d52291f2261d264d29399ae3c92dc61769a49224af9e7c98d74190f93eb49a44db7587c1a2afb5e1a4bec5cdeb8ad2aac9728d5ae95600c52e9f063c11cdb32b7c1d8435ce76fcf1fa562bd38f14bf6c303c70fb373d951b8a691ab793f12c0f3336d6191378bccaed32923bba81868148f029e3d5712a2fb9f610997549710716db37f7400690c8dfbed12ff0a683d8e4d0079b380e2fd856eeafb8c6eedfac8fb54dacd6bd8a96e9f8d23ea87252c1a7c2b53efc6e6aa1f0cc30fbaaf68ee7d46666afc15856669cd9baebf9397ff9f322cce5285e68a985f3b6aadce5e8f14e9f9dd16764bc4e9f62168aa265d8634ab706ed40b0809023f141c36717bd6ccef9ec6aa6bfd2d00bda9375c2fee9ebba49590a166*1b0997cf64bb2c2ff88cb87bcacd9729d404bd46db18117c20d94e67c946fedc"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 21700,' in x

def test_hashcat_21800():
    hashes = [
        "$electrum$5*02170fee7c35f1ef3b229edc90fbd0793b688a0d6f41137a97aab2343d315cce16*94cf72d8f5d774932b414a3344984859e43721268d2eb35fa531de5a2fc7024b463c730a54f4f46229dd9fede5034b19ac415c2916e9c16b02094f845795df0c397ff76d597886b1f9e014ad1a8f64a3f617d9900aa645b3ba86f16ce542251fc22c41d93fa6bc118be96d9582917e19d2a299743331804cfc7ce2c035367b4cbcfb70adfb1e10a0f2795769f2165d8fd13daa8b45eeac495b5b63e91a87f63b42e483f84a881e49adecacf6519cb564694b42dd9fe80fcbc6cdb63cf5ae33f35255266f5c2524dd93d3cc15eba0f2ccdc3c109cc2d7e8f711b8b440f168caf8b005e8bcdfe694148e94a04d2a738f09349a96600bd8e8edae793b26ebae231022f24e96cb158db141ac40400a9e9ef099e673cfe017281537c57f82fb45c62bdb64462235a6eefb594961d5eb2c46537958e4d04250804c6e9f343ab7a0db07af6b8a9d1a6c5cfcd311b8fb8383ac9ed9d98d427d526c2f517fc97473bd87cb59899bd0e8fb8c57fa0f7e0d53daa57c972cf92764af4b1725a5fb8f504b663ec519731929b3caaa793d8ee74293eee27d0e208a60e26290bc546e6fa9ed865076e13febfea249729218c1b5752e912055fbf993fbac5df2cca2b37c5e0f9c30789858ceeb3c482a8db123966775aeed2eee2fc34efb160d164929f51589bff748ca773f38978bff3508d5a7591fb2d2795df983504a788071f469d78c88fd7899cabbc5804f458653d0206b82771a59522e1fa794d7de1536c51a437f5d6df5efd6654678e5794ca429b5752e1103340ed80786f1e9da7f5b39af628b2212e4d88cd36b8a7136d50a6b6e275ab406ba7c57cc70d77d01c4c16e9363901164fa92dc9e9b99219d5376f24862e775968605001e71b000e2c7123b4b43f3ca40db17efd729388782e46e64d43ccb947db4eb1473ff1a3836b74fe312cd1a33b73b8b8d80c087088932277773c329f2f66a01d6b3fc1e651c56959ebbed7b14a21b977f3acdedf1a0d98d519a74b50c39b3052d840106da4145345d86ec0461cddafacc2a4f0dd646457ad05bf04dcbcc80516a5c5ed14d2d639a70e77b686f19cbfb63f546d81ae19cc8ba35cce3f3b5b9602df25b678e14411fecec87b8347f5047513df415c6b1a3d39871a6bcb0f67d9cf8311596deae45fd1d84a04fd58f1fd55c5156b7309af09094c99a53674809cb87a45f95a2d69f9997a38085519cb4e056f9efd56672a2c1fe927d5ea8eec25b8aff6e56f9a2310f1a481daf407b8adf16201da267c59973920fd21bb087b88123ef98709839d6a3ee34efb8ccd5c15ed0e46cff3172682769531164b66c8689c35a26299dd26d09233d1f64f9667474141cf9c6a6de7f2bc52c3bb44cfe679ff4b912c06df406283836b3581773cb76d375304f46239da5996594a8d03b14c02f1b35a432dc44a96331242ae31174*33a7ee59d6d17ed1ee99dc0a71771227e6f3734b17ba36eb589bdced56244135"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 21800,' in x

def test_hashcat_22941():
    hashes = [
        "$sshng$4$16$01684556100059289727957814500256$1232$b04d45fdfdf02a9ca91cbc9c53f9e59956822c72c718929aca9251cffd9ac48e48c490b7b6b6043df3a70cf5fbcc2f358b0e8b70d39155c93032b0fd79ec68f6cb8b7de8422ec95cb027a9eaacc453b0b99b5d3f8d6771d6b95b0242a1d8664de8598e8d6b6d6ee360fda5ae0106061a79e88ef2eef98a000b638f8fdc367155ec2d1120b366f74f0933efe5d174e7107db29dc8fb592b22b9837114415d78036c116b2d31b2080c7159442f2d1a61900f5ae4913548c8e7fc716dd4f812bc7e57b2dd5d3f56c6ae0e91c3bc2897d9341cb282d86b915d43cf20ad16fbd2056104529576142354a430281f5e458923ef8014ff9950351798bfcbbcb66cb98bb2cccea48c134b0e05e978d4308c82617869b207f0ed7b227893f2cdde2d6b6a98246de8a2494d5e018a84724780fbe8d1fa91c922908d18ccffbbbbc81e6578fe8bb5c8596a8cf689f3f12b810dee95887e12439e487313229a37913e3cd12bddba3bac94fab03aad8607f6034fa87f7a7a2ac74d0c0a6e6bc905f569221861e1e388cf379cda799d7b56eac58440d17fe97fa68a537d34317376c00dfa9a99e04725a0d2fcf27ee50463e725813c96fe2eed16de59e8a6944d903e11f7923d57ae6d4a1f8085ce19f4d180f13027806f3965fdf875ea092f103f28a5f42f356254958fa7eb0bca2389a6ad4e305640cc64501e6b16330b063037b1cf6fe64131f308e50d9d1dc687ffa487681941084ff21cb54c1b5903b7a78d9913595fa0124f1dde49b1bee2ea83837efe34e2cd6051a4a7a1437eaa84ad332ffd9946b952ed634948789d9541820a0f9c6f44ab6d3cad645743c76c54e79bfdc4fb8e43a0fd7d871baea98e78131bc530b6d736fa1ec5ac70438609497ab2ff8d516146b4b1b3488791cb84dccc0096b570e2ffb3a93cccefec0af7ce616a64466d2d4196941ba9e051dc00ed05e963a7b4a286973ee0b5df4fd92dfb0b229b10730d454832d945c6a596862212d109ce78ac14ffb5d775548b2f3e2ae4be059a24465cc10b7c810f8cc3db7cb327619cc104ebea575ac097d20701dc623f7aa893b785cc20851f3972390e00ab3355655f7d5bea323832c17d8e078e917843ef7fcaca349366092b6743bf7511d5fceb2d992fbd18574be532365be41ad80a114704a64a7aefdf98c907aa10e4d5c547dd8d21647ea9d5c975fe1b24525d94c3eb03e071742fd5f09f22da669b649fac9f87d8cf16c475d006421f69a9b2d5c4037ccc9bf9f0aa0e7df8ac5fcb0d88a528833f9640799026d2fe8694fa1a0307c5f24002172464b290bedd85667800edbff2f1de7119e5b65730a24922e42d53ef28b0a59817a298426dc72e29a85e59e3d777b19eb934bcd620a903aff72927cdbe7253f77694ab0ef970378b4347f6166ca2a40b23cc31970f0cbefd08d2d72bf2c3961d67c73a5a24f75a65e540dc5735520b0d81250af8980ddca3e22a9b25773afd27c76e564ff437d4208df14d802f1d0848390f45924cdd6ced3c9ffb726bb358b334ea0e0481acdd103f2db05f508f62588621d0b8fa274a69eba0d418d85086d9139391f7e28dc54fe9bab801f1fea854f27ad2e5907ae6f9a4b4527d16a8af3c8cbe2c6d82209dc6c7da060da58294eb00380598330c4c19d45581d09e04c0153a8559700b3a8ceab9b8124f84d397356cd9e38e3916afc1f63a3e1dfbc7df8dd0a7d0704e38a0ea523dfc2b9defd5"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 22941,' in x

def test_hashcat_23700():
    hashes = [
        "$RAR3$*1*e54a73729887cb53*49b0a846*16*14*1*34620bcca8176642a210b1051901921e*30"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 23700,' in x

def test_hashcat_6600():
    hashes = [
        "1000:9e55bd14cb90f5e1:99a89704bc67d6921ab393ca46ee7973e0d5227938a6d669cdc920ad7ae857eb4163dcccf6770190f80d3478c62904827c59d5c97f2a0f16ea9f3aee6992d921b0244617e309a8283c91a21c524561923658dee0d4d304465bac5f766ef26b02534e44a7d1506088f95f9610dbfaf1ace6cf4368921a28367415e7d76938faf3d7a27750eaf74c1855a671ad7b2e4fdb30734022c37565ec8e30681db367ad8be49ce3927232ccd8e0d8a4e726acf88fa8dedf32c24ba771a3f5eb2aae13180ca4c29e2b7fccec4bc4e4d32eb01c6b12405a5a2b8d3aea44d7745be76bec9068ec2dd13d227b3bdb4962143dfc74496e00e228465b6f214428243b3fca652c3f8661915fcae0a5db919f87f9e9202ae7e0a4080849dc5003d7618585746ec637dd9d17cb97be9f2eb550fd539d51ae4a6d07c63903c83c780bb8520ba6462bae6f1dec54fee0707e82345b39c46befd3eefe0c33e30adb13cafe7dc4f18b53bee60dccf92c80cfae1671f9e3c6b0cf0ed278bfbdbd69ee910130554d8348287c9372e0f437194018355f71b5236114f03b7a58036b85ac8f089b7eaa72ab8997c9e26c40a095014b64d5c3b9221e59f5b9e7dd1d730420875b73a6ad841f68c2004e5622400905000c977edb625d54c6a42cecfc9009bb4489ebb4d1e339e0d014a972364e378441c761aad8c8929f753917b9a1e1a316831cb9d6ba92354a47202b78ab2f42f2c99284c12d3e212ebf8ea8ec683aeb62c0e5d588cca9cc08aac3ead97831bfa1f698dac9f857e8cdd9ec4b15cffb5900f2f951c657f831689ac6199033b13cecf4b29d84fb06f422acd3db566d7ec6b664325c4331ff35963553c26e94af6eb5b36fe79f14bf3a30f4964ded7991ef5d859ebbb0e98c821b21f9620fca9086f9b3b2a7ad8360c4a635c481f1ef4990f7f0ec4fde37723b4639ee633bdb32be6bf31298a4574381d95831d65b3e8e6352b1207a684401a0f3fcff65e0ed1e6ec714c07526896468daeb056cbe49d82b87092e53ac40cfba049983ce8923bed2de773d15a5e87a88041f72c34d8c0436f95368ec73abfdd1d21897f649e1de9e7198e9db342c93b3b8b0d3af6c4867d63fed394674e5b02c92b7698d5457d2cca773abaad69c4a0a36e468a40d14b8bd73fa1d9074c8881158e10e4243045ab254775bda1e7e89a68005d91bb67044ed407f221d1028d034aedcfea3b527725607bd5c3f880557cfc6c2c0bb3361ae131261b8a5ebf3b53521fdd731ec2413c61bc78a1ab7f78057abd1c5459250fba0e0d57c1f4ebd3e1871ce0f5bfd44d2790d946936eef03e14e81f33f5484eec0a76910c253bf2777232be1a3593678f27225b035999d9ffb675685457b48928db1f1be6c3f206ad2efc764f8ba77a38b439f1e28318a1b077fe0c9e36fa6ed0df0f052d9aadd56b1514b5d01a44161fcea20f6326fab1ee3d7f79"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6600,' in x

def test_hashcat_8200():
    hashes = [
        "92407e964bb9a368e86bcd52273e3f6b86181ab1204a9ed709bbe97667e7f67c:c1b981dd8e36340daf420badbfe38ca9:40000:991a0942a91889409a70b6622caf779a00ba472617477883394141bd6e23e38d8e2f5a69f5b30aa9dc28ebf6ecedcb679224e29af1123889a947576806536b831cc1d159a6d9135194671719adf86324ce6c6cbc64069c4210e748dde5400f7da738016a6b3c35c843f740008b0282581b52ea91d46a9600bfa8b79270d1ce8e4326f9fc9afa97082096eaf0ce1270eb030f53e98e3654d6fd38a313777b182051d95d582f67675628202dab60f120d4146250fa9ade4d0112aa873b5eb56425380e7b1220f6284ed1fa7d913a595aedfc0159ba2c95719d3c33646372098dc49037018885ed5d79e3479fee47fbe69076ea94852672f04f10e63fe3f53366fd61f7afd41831150cf24a49e837d72d656a1906943117252ab1f3889261ce09c3d832a4d583cfc82a049cee99cf62d4ec"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8200,' in x

def test_hashcat_5300():
    hashes = [
        "e957a6a0f53ce06a56e4d82e96bc925ffa3cf7b79f6500b667edad5a1d7bad4619efa734f75cca9c4222fbb169f71d4240aced349eb7126f35cf94772b4af373ddf9b3f1ab3a9ff8cd2705417dca7e36dd9026bd0d472459cea7ad245ce57e4bf7d36efdea2a782978c6161eae98f01eac1ee05578f8e524a0d7748c5a1ec2de:647c051436ee84b39a514fd5f2da24fd3bdbb245ef3ed05cb362c58916bbb2cb93a93e3ec33da27404b82125cfd354c0114a3d10dfca26fab139f91046f2ad996f6091ac7a729305272696ac1769991b81a30826e24cee586f3f383b5e035820e17d9715db433ac75f204f20153a12cf7ee4fa7d11b2823e424c26cb513eb26b:fb3678377967e4db:708993a01df48348:00000001000000010000009801010004030000240101000080010005800200028003000180040002800b0001000c000400007080030000240201000080010005800200018003000180040002800b0001000c000400007080030000240301000080010001800200028003000180040002800b0001000c000400007080000000240401000080010001800200018003000180040002800b0001000c000400007080:01110000c0a83965:19004c6aa04dba354599f0d6afbc866970d751e4:6074841c25c83a0c1abfa348fee2d133399595f2:19a3428d90eb5045363a58dc33f51941"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5300,' in x

def test_hashcat_5400():
    hashes = [
        "7a1115b74a1b9d63de62627bdd029aa7a50df83ddbaba88c47d3e51833d21984fb463a2604ba0c82611a11edee7406e1826b2c70410d2797487d1220a4f716d7532fcd73e82b2fd6304f9af5dd1bc0a5dc1eb58bee978f95ffc8b6dc4401d4d2720978f4b0e69ae4dd96e61a1f23a347123aa242f893b33ac74fa234366dc56c:7e599b0168b56608f8a512b68bc7ea47726072ca8e66ecb8792a607f926afc2c3584850773d91644a3186da80414c5c336e07d95b891736f1e88eb05662bf17659781036fa03b869cb554d04689b53b401034e5ea061112066a89dcf8cbe3946e497feb8c5476152c2f8bc0bef4c2a05da51344370682ffb17ec664f8bc07855:419011bd5632fe07:169168a1ac421e4d:00000001000000010000009801010004030000240101000080010005800200028003000180040002800b0001000c000400007080030000240201000080010005800200018003000180040002800b0001000c000400007080030000240301000080010001800200028003000180040002800b0001000c000400007080000000240401000080010001800200018003000180040002800b0001000c000400007080:01110000c0a83965:ee4e517ba0f721798209d04dfcaf965758c4857e:48aada032ae2523815f4ec86758144fa98ad533c:e65f040dad4a628df43f3d1253f821110797a106"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 5400,' in x

def test_hashcat_8800():
    hashes = [
        "$fde$16$ca56e82e7b5a9c2fc1e3b5a7d671c2f9$16$7c124af19ac913be0fc137b75a34b20d$eac806ae7277c8d48243d52a8644fa57a817317bd3457f94dca727964cbc27c88296954f289597a9de3314a4e9d9f28dce70cf9ce3e1c3c0c6fc041687a0ad3cb333d4449bc9da8fcc7d5f85948a7ac3bc6d34f505e9d0d91da4396e35840bde3465ad11c5086c89ee6db68d65e47a2e5413f272caa01e02224e5ff3dc3bed3953a702e85e964e562e62f5c97a2df6c47547bfb5aeeb329ff8f9c9666724d399043fe970c8b282b45e93d008333f3b4edd5eb147bd023ed18ac1f9f75a6cd33444b507694c64e1e98a964b48c0a77276e9930250d01801813c235169a7b1952891c63ce0d462abc688bd96c0337174695a957858b4c9fd277d04abe8a0c2c5def4b352ba29410f8dbec91bcb2ca2b8faf26d44f02340b3373bc94e7487ce014e6adfbf7edfdd2057225f8aeb324c9d1be877c6ae4211ae387e07bf2a056984d2ed2815149b3e9cf9fbfae852f7dd5906c2b86e7910c0d7755ef5bcc39f0e135bf546c839693dc4af3e50b8382c7c8c754d4ee218fa85d70ee0a5707a9f827209a7ddb6c2fb9431a61c9775112cc88aa2a34f97c2f53dfce082aa0758917269a5fc30049ceab67d3efd721fee021ffca979f839b4f052e27f5c382c0dd5c02fd39fbc9b26e04bf9e051d1923eff9a7cde3244902bb8538b1b9f11631def5aad7c21d2113bcdc989b771ff6bf220f94354034dd417510117b55a669e969fc3bc6c5dcd4741b8313bf7d999dc94d4949f27eec0cd06f906c17a80d09f583a5dd601854832673b78d125a2c5ad0352932be7b93c611fee8c6049670442d8c532674f3d21d45d3d009211d2a9e6568252ac4682982172cb43e7c6b05e85851787ad90e25b77cce3f7968d455f92653a1d3790bc50e5f6e1f743ac47275ffa8e81bbe832a8d7d78d5d5a7c73f95703aebb355849ae566492093bd9cb51070f39c69bb4e22b99cc0e60e96d048385bb69f1c44a3b79547fbc19a873a632f43f05fa2d8a6f9155e59d153e2851b739c42444018b8c4e09a93be43570834667d0b5a5d2a53b1572dab3e750b3f9e641e303559bace06612fbd451a5e822201442828e79168c567a85d8c024cd8ce32bf650105b1af98cc5428675f4f4bbede37a0ef98d1533a8a6dcb27d87a2b799f18706f4677edaa0411becac4c591ede83993aedba660d1dd67f6c4a5c141ad3e6e0c77730cb0ecbf4f4bd8ef6067e05ca3bc563d9e1554a893fea0050bdd1733c883f533f87eac39cceee0ccf817fc1f19bcfdd13e9f241b89bfb149b509e9a0747658438536b6705514cc6d6bb3c64c903e4710435d8bebc35297d1ebbdff8074b203f37d1910d8b4637e4d3dab997f4aa378a7a67c79e698a11e83d0d7e759d0e7969c4f5408168b282fe28d3279ec1d4cc6f85a0f8e5d01f21c7508a69773c44167ff8d467d0801f9ec54f9ee2496d4e7e470214abc1ca11355bb18cd23273aac6b05b47f9e301b42b137a2455758c24e2716dcd2e55bbeb780f592e664e7392bf6eccb80959f24c8800816c84f2575e82e1f3559c33a5be7a3a0c843c2989f486b113d5eeada007caf6b5a0f6d71e2f5c09a4def57c7057168051868317a9ec790d570d76a0d21a45ad951c475db5a66101475871147c5a5907ec4e6b14128ed6695bb73c1c97952e96826eeb6003aa13462093e4afc209627241f03b0247e110fbab983640423b7cdf112e01579fed68c80ac7df7449d9d2114b9ae5539c03c2037be45c5f74e7357b25c6a24b7bd503864437147e50d7ac4ccc4bbd0cabecdc6bac60a362285fe450e2c2d0a446578c8880dc957e6e8061e691b83eb8062d1aad476e0c7b25e4d5454f1288686eb525f37fe649637b235b7828366b0219a9c63d6ddbb696dc3585a2ebfbd5f5e4c170d6784ab9993e15142535e194d2bee3dc9477ef8b8e1b07605e0c04f49edf6d42be3a9dabbc592dde78ce8b7dd9684bfcf4ca2f5a44b1872abe18fb6fa67a79390f273a9d12f9269389629456d71b9e7ed3447462269a849ce83e1893f253c832537f850b1acce5b11d2ba6b7c2f99e8e7c8085f390c21f69e1ce4bbf85b4e1ad86c0d6706432766978076f4cada9ca6f28d395d9cc5e74b2a6b46eb9d1de79eeecff7dc97ec2a8d8870e3894e1e4e26ccb98dd2f88c0229bbd3152fa149f0cc132561f"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8800,' in x

def test_hashcat_23001():
    hashes = [
        "$zip3$*0*1*128*0*b4630625c92b6e7848f6fd86*df2f62611b3d02d2c7e05a48dad57c7d93b0bac1362261ab533807afb69db856676aa6e350320130b5cbf27c55a48c0f75739654ac312f1cf5c37149557fc88a92c7e3dde8d23edd2b839036e88092a708b7e818bf1b6de92f0efb5cce184cceb11db6b3ca0527d0bdf1f1137ee6660d9890928cd80542ac1f439515519147c14d965b5ba107c6227f971e3e115170bf*0*0*0*file.txt"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 23001,' in x

def test_hashcat_23002():
    hashes = [
        "$zip3$*0*1*192*0*53ff2de8c280778e1e0ab997*603eb37dbab9ea109e2c405e37d8cae1ec89e1e0d0b9ce5bf55d1b571c343b6a3df35fe381c30249cb0738a9b956ba8e52dfc5552894296300446a771032776c811ff8a71d9bb3c4d6c37016c027e41fea2d157d5b0ce17804b1d7c1606b7c1121d37851bd705e001f2cd755bbf305966d129a17c1d48ff8e87cfa41f479090cd456527db7d1d43f9020ad8e73f851a5*0*0*0*file.txt"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 23002,' in x

def test_hashcat_23003():
    hashes = [
        "$zip3$*0*1*256*0*39bff47df6152a0214d7a967*65ff418ffb3b1198cccdef0327c03750f328d6dd5287e00e4c467f33b92a6ef40a74bb11b5afad61a6c3c9b279d8bd7961e96af7b470c36fc186fd3cfe059107021c9dea0cf206692f727eeca71f18f5b0b6ee1f702b648bba01aa21c7b7f3f0f7d547838aad46868155a04214f22feef7b31d7a15e1abe6dba5e569c62ee640783bb4a54054c2c69e93ece9f1a2af9d*0*0*0*file.txt"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 23003,' in x

def test_hashcat_25300():
    hashes = [
        "$office$2016$0$100000$876MLoKTq42+/DLp415iZQ==$TNDvpvYyvlSUy97UOLKNhXynhUDDA7H8kLql0ISH5SxcP6hbthdjaTo4Z3/MU0dcR2SAd+AduYb3TB5CLZ8+ow=="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 25300,' in x

def test_hashcat_11():
    hashes = [
        "19e0e8d91c722e7091ca7a6a6fb0f4fa:54718031842521651757785603028777"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 11,' in x

def test_hashcat_21():
    hashes = [
        "374996a5e8a5e57fd97d893f7df79824:36"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 21,' in x

def test_hashcat_22():
    hashes = [
        "nNxKL2rOEkbBc9BFLsVGG6OtOUO/8n:user"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 22,' in x

def test_hashcat_23():
    hashes = [
        "3af0389f093b181ae26452015f4ae728:user"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 23,' in x

def test_hashcat_101():
    hashes = [
        "{SHA}uJ6qx+YUFzQbcQtyd2gpTQ5qJ3s="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 101,' in x

def test_hashcat_111():
    hashes = [
        "{SSHA}AZKja92fbuuB9SpRlHqaoXxbTc43Mzc2MDM1Ng=="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 111,' in x

def test_hashcat_112():
    hashes = [
        "ac5f1e62d21fd0529428b84d42e8955b04966703:38445748184477378130"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 112,' in x

def test_hashcat_121():
    hashes = [
        "ecf076ce9d6ed3624a9332112b1cd67b236fdd11:17782686"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 121,' in x

def test_hashcat_122():
    hashes = [
        "1430823483d07626ef8be3fda2ff056d0dfd818dbfe47683"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 122,' in x

def test_hashcat_124():
    hashes = [
        "sha1$fe76b$02d5916550edf7fc8c886f044887f4b1abf9b013"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 124,' in x

def test_hashcat_131():
    hashes = [
        "0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 131,' in x

def test_hashcat_132():
    hashes = [
        "0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 132,' in x

def test_hashcat_133():
    hashes = [
        "uXmFVrdBvv293L9kDR3VnRmx4ZM="
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 133,' in x

def test_hashcat_141():
    hashes = [
        "$episerver$*0*bEtiVGhPNlZpcUN4a3ExTg==*utkfN0EOgljbv5FoZ6+AcZD5iLk"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 141,' in x

def test_hashcat_1421():
    hashes = [
        "8fe7ca27a17adc337cd892b1d959b4e487b8f0ef09e32214f44fb1b07e461c532e9ec3"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1421,' in x

def test_hashcat_1441():
    hashes = [
        "$episerver$*1*MDEyMzQ1Njc4OWFiY2RlZg==*lRjiU46qHA7S6ZE7RfKUcYhB85ofArj1j7TrCtu3u6Y"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1441,' in x

def test_hashcat_1711():
    hashes = [
        "{SSHA512}ALtwKGBdRgD+U0fPAy31C28RyKYx7+a8kmfksccsOeLknLHv2DBXYI7TDnTolQMBuPkWDISgZr2cHfnNPFjGZTEyNDU4OTkw"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1711,' in x

def test_hashcat_1722():
    hashes = [
        "648742485c9b0acd786a233b2330197223118111b481abfa0ab8b3e8ede5f014fc7c523991c007db6882680b09962d16fd9c45568260531bdb34804a5e31c22b4cfeb32d"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1722,' in x

def test_hashcat_1731():
    hashes = [
        "0x0200F733058A07892C5CACE899768F89965F6BD1DED7955FE89E1C9A10E27849B0B213B5CE92CC9347ECCB34C3EFADAF2FD99BFFECD8D9150DD6AACB5D409A9D2652A4E0AF16"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1731,' in x

def test_hashcat_2611():
    hashes = [
        "16780ba78d2d5f02f3202901c1b6d975:568"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2611,' in x

def test_hashcat_2612():
    hashes = [
        "$PHPS$247824$ad14afbbf0e16d4ad8c8985263a3d051"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2612,' in x

def test_hashcat_2711():
    hashes = [
        "bf366348c53ddcfbd16e63edfdd1eee6:181264250056774603641874043270"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2711,' in x

def test_hashcat_2811():
    hashes = [
        "8d2129083ef35f4b365d5d87487e1207:47204"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 2811,' in x

def test_hashcat_3711():
    hashes = [
        "$B$56668501$0ce106caa70af57fd525aeaf80ef2898"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3711,' in x

def test_hashcat_4521():
    hashes = [
        "1fb46a8f81d8838f46879aaa29168d08aa6bf22d:3290afd193d90e900e8021f81409d7a9"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4521,' in x

def test_hashcat_20711():
    hashes = [
        "$SHA$7218532375810603$bfede293ecf6539211a7305ea218b9f3f608953130405cda9eaba6fb6250f824"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20711,' in x

def test_hashcat_22301():
    hashes = [
        "$telegram$0*518c001aeb3b4ae96c6173be4cebe60a85f67b1e087b045935849e2f815b5e41*25184098058621950709328221838128"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 22301,' in x

def test_hashcat_6500():
    hashes = [
        "{ssha512}06$bJbkFGJAB30L2e23$bXiXjyH5YGIyoWWmEVwq67nCU5t7GLy9HkCzrodRCQCx3r9VvG98o7O3V0r9cVrX3LPPGuHqT5LLn0oGCuI1.."
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 6500,' in x

def test_hashcat_20510():
    hashes = [
        "f1eff5c0368d10311dcfc419"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 20510,' in x

def test_hashcat_1300():
    hashes = [
        "e4fa1555ad877bf0ec455483371867200eee89550a93eff2f95a6198"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 1300,' in x

def test_hashcat_14700():
    hashes = [
        "$itunes_backup$*9*b8e3f3a970239b22ac199b622293fe4237b9d16e74bad2c3c3568cd1bd3c471615a6c4f867265642*10000*4542263740587424862267232255853830404566**"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 14700,' in x

def test_hashcat_3500():
    hashes = [
        "9882d0778518b095917eb589f6998441"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3500,' in x

def test_hashcat_4210():
    hashes = [
        "09ea048c345ad336ebe38ae5b6c4de24:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4210,' in x

def test_hashcat_3610():
    hashes = [
        "7b57255a15958ef898543ea6cc3313bc:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3610,' in x

def test_hashcat_3720():
    hashes = [
        "10ce488714fdbde9453670e0e4cbe99c:1234"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3720,' in x

def test_hashcat_3721():
    hashes = [
        "fa01af9f0de5f377ae8befb03865178e:5678"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3721,' in x

def test_hashcat_123():
    hashes = [
        "0x326C6D7B4E4F794B79474E36704F35723958397163735263516265456E31"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 123,' in x

    hashes = [
        "0xAFC55E260B8F45C0C6512BCE776C1AD8312B56E6"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 123,' in x

def test_hashcat_4600():
    hashes = [
        "dc57f246485e62d99a5110afc9264b4ccbfcf3cc"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 4600,' in x

def test_hashcat_3300():
    hashes = [
        "$md5$rounds=904$iPPKEBnEkp3JV8uX$0L6m7rOFTVFn.SGqo2M9W1"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 3300,' in x

def test_hashcat_190():
    hashes = [
        "b89eaac7e61417341b710b727768294d0e6a277b"
    ]
    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 190,' in x

def test_hashcat_22100():
    hashes = [
        "$bitlocker$1$16$6f972989ddc209f1eccf07313a7266a2$1048576$12$3a33a8eaff5e6f81d907b591$60$316b0f6d4cb445fb056f0e3e0633c413526ff4481bbf588917b70a4e8f8075f5ceb45958a800b42cb7ff9b7f5e17c6145bf8561ea86f52d3592059fb"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 22100,' in x

def test_hashcat_8500():
    hashes = [
        "$racf$*USER*FC2577C6EBE6265B"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert '"hashcat": 8500,' in x
