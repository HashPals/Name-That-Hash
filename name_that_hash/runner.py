import click
import sys
from typing import NamedTuple, List


from rich import print, text


# Lets you import as an API
# or run as a package
try:
    import hashes, hash_namer, prettifier
except ModuleNotFoundError:
    from name_that_hash import hash_namer, hashes, prettifier


class HashObj:
    """
    Every hash given to our program will be assiocated with one object
    This object contains the possible type of hash
    and provides ways to print that hash
    """

    def __init__(self, chash: str, nth, hash_info):
        self.chash = chash
        self.nth = nth

        self.popular = hash_info.popular

        # prorotypes is given as a generator
        self.prototypes = nth.identify(chash)
        self.prototypes = self.sort_by_popular()

        self.hash_obj = {self.chash: self.prototypes}

    def get_prototypes(self):
        return self.prototypes

    def sort_by_popular(self):
        """Sorts the list by popular + everything else

        we do this using the self.popular set. Sets have O(1) lookup, so it's cheap.
        If on named_tuple is in the popular set, we add it to the populars list and remove it from prototypes.

        we then return populars list + prototypes.
        """
        to_ret = []
        populars = []
        for i in self.prototypes:
            if i.name in self.popular:
                populars.append(i.__dict__)
                self.prototypes.remove(i)
            else:
                to_ret.append(i.__dict__)
        return populars + to_ret

class hash_information:
    def __init__(self):
        self.popular = set(["MD5", "NTLM", "SHA-256", "SHA-515", "Keccak-256", "Keccak-512", "Blake2"])

def print_help(ctx):
    click.echo(ctx.get_help())
    ctx.exit()


def banner():
    text = r"""[bold blue]
  _   _                           _____ _           _          _   _           _     
 | \ | |                         |_   _| |         | |        | | | |         | |    
 |  \| | __ _ _ __ ___   ___ ______| | | |__   __ _| |_ ______| |_| | __ _ ___| |__  
 | . ` |/ _` | '_ ` _ \ / _ \______| | | '_ \ / _` | __|______|  _  |/ _` / __| '_ \ 
 | |\  | (_| | | | | | |  __/      | | | | | | (_| | |_       | | | | (_| \__ \ | | |
  \_| \_/\__,_|_| |_| |_|\___|     \_/ |_| |_|\__,_|\__|      \_| |_/\__,_|___/_| |_|
https://twitter.com/bee_sec_san
https://github.com/HashPals/Name-That-Hash [/bold blue]
    """
    print(text)


@click.command()
@click.option("-t", "--text", help="Check one hash")
@click.option(
    "-f", "--file", type=click.File("rb"), help="Newline separated hash file input"
)
@click.option(
    "-g",
    "--greppable",
    is_flag=True,
    type=bool,
    help="Are you going to grep this output? Prints in JSON format.",
)
@click.option(
    "-a",
    "--accessible",
    is_flag=True,
    help="Turn on accessible mode, does not print ASCII art. Also dooes not print very large blocks of text, as this can cause some pains with screenreaders. This reduces the information you get. If you want the least likely feature but no banner, use --no-banner. ",
)
@click.option("--no-john", is_flag=True, help="Does not print John The Ripper Information.")
@click.option("--no-hashcat", is_flag=True, help="Does not print Hashcat Information.")
@click.option("--no-banner", is_flag=True, help="Removes banner from startup.")
def main(**kwargs):
    """Name That Hash - Instantly name the type of any hash!

    Github:\n
    https://github.com/hashpals/name-that-hash

    From the creator of RustScan and Ciphey. Follow me on Twitter!\n
    https://twitter.com/bee_sec_san

    Example usage:\n
        nth --text 5f4dcc3b5aa765d61d8327deb882cf99\n
        nth --file hash\n
        nth --text 5f4dcc3b5aa765d61d8327deb882cf99 --greppable\n
    """
    no_args = True
    for i in kwargs.values():
        if i:
            no_args = False
            break
    if no_args:
        with click.Context(main) as ctx:
            click.echo(main.get_help(ctx))
            exit(0)

    # Banner handling
    if not kwargs["accessible"] and not kwargs["no_banner"] and not kwargs["greppable"]:
        banner()

    hash_info = hash_information()
    # nth = the object which names the hash types
    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    # prettifier print things :)
    pretty_printer = prettifier.Prettifier(kwargs)

    output = []

    if kwargs["text"]:
        output.append(HashObj(kwargs["text"], nth, hash_info))
    elif kwargs["file"]:
        # else it must be a file
        for i in kwargs["file"].read().splitlines():
            # for every hash in the file, put it into the output list
            # we have to decode it as its bytes str
            output.append(HashObj(i.decode("utf-8"), nth, hash_info))

    if kwargs["greppable"]:
        print(pretty_printer.greppable_output(output))
    else:
        pretty_printer.pretty_print(output)


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
    # for most popular hashes etc
    hash_info = hash_information()

    output = []
    for i in chash:
        output.append(HashObj(i, nth, hash_info))

    return pretty_printer.greppable_output(output)


#     if kwargs["text"]:
#         output.append(HashObj(kwargs["text"], nth))
#     elif kwargs["file"]:
#         # else it must be a file
#         for i in kwargs["file"].read().splitlines():
#             # for every hash in the file, put it into the output list
#             # we have to decode it as its bytes str
#             output.append(HashObj(i.decode("utf-8"), nth))

#     if kwargs["greppable"]:
#         print(prettifier.greppable_output(output))


if __name__ == "__main__":
    main()