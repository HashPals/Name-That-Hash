from click.testing import CliRunner
from name_that_hash.runner import main


def test_it_runs():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "-t",
            "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86",
        ],
    )
    assert result.exit_code == 0
    assert "SHA-512" in result.output


def test_greppable():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "-t",
            "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86",
            "-g",
        ],
    )
    assert result.exit_code == 0
    assert "Twitter" not in result.output


def test_greppable_no_text():
    runner = CliRunner()
    result = runner.invoke(main, ["-t", "", "-g"])
    assert "Usage" not in result.output


def test_greppable_b64():
    runner = CliRunner()
    result = runner.invoke(
        main, ["-t", "NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk=", "--base64", "-g"]
    )
    assert "MD5" in result.output


def test__b64():
    runner = CliRunner()
    result = runner.invoke(
        main, ["-t", "NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk=", "-b64"]
    )
    assert "MD5" in result.output


def test_file_input():
    runner = CliRunner()
    result = runner.invoke(main, ["-f", "tests/mocks/hashes.txt", "-b64", "-g"])
    assert "SHA-1" in result.output
    assert "SHA-512" in result.output


def test_kerberos_works():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "-t",
            "$krb5tgs$23$*user$realm$test/spn*$63386d22d359fe42230300d56852c9eb$891ad31d09ab89c6b3b8c5e5de6c06a7f49fd559d7a9a3c32576c8fedf705376cea582ab5938f7fc8bc741acf05c5990741b36ef4311fe3562a41b70a4ec6ecba849905f2385bb3799d92499909658c7287c49160276bca0006c350b0db4fd387adc27c01e9e9ad0c20ed53a7e6356dee2452e35eca2a6a1d1432796fc5c19d068978df74d3d0baf35c77de12456bf1144b6a750d11f55805f5a16ece2975246e2d026dce997fba34ac8757312e9e4e6272de35e20d52fb668c5ed",
        ],
    )
    assert "Kerberos" in result.output
