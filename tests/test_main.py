from name_that_hash import name_that_hash


def test_it_works():

    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = name_that_hash.main.api_return_hashes_as_json(hashes)
    print(x)
    assert x is not None
