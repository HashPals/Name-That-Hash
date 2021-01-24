from name_that_hash import runner


def test_it_works():

    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert x is not None


def test_it_identifieis_correctly():
    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "NTLM" in x
