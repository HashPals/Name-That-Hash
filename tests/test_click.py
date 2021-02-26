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
    result = runner.invoke(main, ["-t", "NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk=", '--base64', '-g'])
    assert "MD5" in result.output

def test__b64():
    runner = CliRunner()
    result = runner.invoke(main, ["-t", "NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk=", '-b64'])
    assert "MD5" in result.output

def test_file_input():
    runner = CliRunner()
    result = runner.invoke(main, ["-f", "tests/mocks/hashes.txt", '-b64', '-g'])
    assert "SHA-1" in result.output
    assert "SHA-512" in result.output
