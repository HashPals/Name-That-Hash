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
