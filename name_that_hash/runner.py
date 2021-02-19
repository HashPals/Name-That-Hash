import click
import sys
from typing import NamedTuple, List
import base64

from rich import print, text
from loguru import logger

from name_that_hash import hash_namer, hashes, prettifier

from name_that_hash import check_hashes

# Lets you import as an API
# or run as a package

def banner():
    text = r"""[bold blue]
  _   _                           _____ _           _          _   _           _     
 | \ | |                         |_   _| |         | |        | | | |         | |    
 |  \| | __ _ _ __ ___   ___ ______| | | |__   __ _| |_ ______| |_| | __ _ ___| |__  
 | . ` |/ _` | '_ ` _ \ / _ \______| | | '_ \ / _` | __|______|  _  |/ _` / __| '_ \ 
 | |\  | (_| | | | | | |  __/      | | | | | | (_| | |_       | | | | (_| \__ \ | | |
 \_| \_/\__,_|_| |_| |_|\___|      \_/ |_| |_|\__,_|\__|      \_| |_/\__,_|___/_| |_|

https://twitter.com/bee_sec_san
https://github.com/HashPals/Name-That-Hash [/bold blue]
    """
    print(text)


@click.command()
@click.option("-t", "--text", help="Check one hash, use single quotes ' as inverted commas \" messes up on Linux.", type=str)
@click.option(
    "-f",
    "--file",
    type=click.File("r", encoding="utf-8"),
    help="Checks every hash in a newline separated file.",
)
@click.option(
    "-g",
    "--greppable",
    is_flag=True,
    type=bool,
    help="Are you going to grep this output? Prints in JSON format.",
)
@click.option("-b64", "--base64", is_flag=True, help="Decodes hashes in Base64 before identification. For files with mixed Base64 & non-encoded it attempts base64 first and then falls back to normal hash identification per hash.")
@click.option(
    "-a",
    "--accessible",
    is_flag=True,
    help="Turn on accessible mode, does not print ASCII art. Also dooes not print very large blocks of text, as this can cause some pains with screenreaders. This reduces the information you get. If you want the least likely feature but no banner, use --no-banner. ",
)
@click.option("--no-banner", is_flag=True, help="Removes banner from startup.")
@click.option(
    "--no-john", is_flag=True, help="Don't print John The Ripper Information."
)
@click.option("--no-hashcat", is_flag=True, help="Don't print Hashcat Information.")
@click.option(
    "-v",
    "--verbose",
    count=True,
    type=int,
    help="Turn on debugging logs. -vvv for maximum logs.",
)
def main(**kwargs):
    """Name That Hash - Instantly name the type of any hash!

    Github:\n
    https://github.com/hashpals/name-that-hash

    From the creator of RustScan and Ciphey. Follow me on Twitter!\n
    https://twitter.com/bee_sec_san

    Example usage:\n
        nth --text '5f4dcc3b5aa765d61d8327deb882cf99'\n
        nth --file hash\n
        nth --text '5f4dcc3b5aa765d61d8327deb882cf99' --greppable\n
        Note: Use single quotes ' as inverted commas " do not work well on Linux.\n
    """
    
    if not len(sys.argv) > 1:
        with click.Context(main) as ctx:
            click.echo(ctx.get_help())
            ctx.exit()
            exit(0)
            
    # Load the verbosity, so that we can start logging
    set_logger(kwargs)
    logger.debug(kwargs)

    # Banner handling
    if not kwargs["accessible"] and not kwargs["no_banner"] and not kwargs["greppable"]:
        logger.info("Running the banner.")
        banner()

    # nth = the object which names the hash types
    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    # prettifier print things :)
    pretty_printer = prettifier.Prettifier(kwargs)

    hashChecker = check_hashes.HashChecker(kwargs, nth)

    logger.trace("Initialised the hash_info, nth, and pretty_printer objects.")

    output = []

    if kwargs["text"]:
        hashChecker.single_hash(kwargs["text"])
        output = hashChecker.output
    elif kwargs["file"]:
        hashChecker.file_input(kwargs["file"])
        output = hashChecker.output

    if kwargs["greppable"]:
        print(pretty_printer.greppable_output([output]))
    else:
        pretty_printer.pretty_print(output)


def set_logger(kwargs):
    try:
        logger_dict = {1: "WARNING", 2: "DEBUG", 3: "TRACE"}
        level = logger_dict[kwargs["verbose"]]
        logger.add(sink=sys.stderr, level=level, colorize=sys.stderr.isatty())
        logger.debug("TEST")
        logger.opt(colors=True)
    except Exception as e:
        logger.remove()


def api_return_hashes_as_json(chash: [str], args: dict = {}):
    """
    Using name-that-hash as an API? Call this function!

    Given a list of hashes of strings
    return a list of json of all hashes in the same order as the input
    """
    # nth = the object which names the hash types

    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    # prettifier print things :)
    pretty_printer = prettifier.Prettifier(args, api=True)
    hashChecker = check_hashes.HashChecker(args, nth)

    output = []
    for i in chash:
        hashChecker.single_hash(i)
        output.append(hashChecker.output)
    return pretty_printer.greppable_output(output)


if __name__ == "__main__":
    main()
