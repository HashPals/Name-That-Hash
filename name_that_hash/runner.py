import click
import json
import sys
from typing import NamedTuple, List


from rich import print, text
from rich.console import Console

# we need a global console to control highlighting / printing
console = Console(highlighter=False)

# Lets you import as an API
# or run as a package
try:
    import hashes, hash_namer
except ModuleNotFoundError:
    from name_that_hash import hash_namer, hashes


class HashObj:
    """
    Every hash given to our program will be assiocated with one object
    This object contains the possible type of hash
    and provides ways to print that hash

    """

    def __init__(self, chash: str, nth):
        self.popular = set(["MD5", "NTLM", "SHA256", "SHA515"])
        self.chash = chash
        self.nth = nth

        # prorotypes is given as a generator
        self.prototypes = list(nth.identify(chash))
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


class Prettifier:
    def __init__(self, kwargs, api=False):
        """
        Takes arguments as list so we can do A11Y stuff etc
        """
        if api is not True:
            self.a11y = kwargs["accessible"]

    def greppable_output(self, objs: List):
        """
        takes the prototypes and turns it into json
        returns the json

        Doesn't print it, it prints in main
        """
        outputs_as_dict = {}
        for i in objs:
            outputs_as_dict.update(i.hash_obj)
        return json.dumps(outputs_as_dict, indent=2)

    def pretty_print(self, objs):
        """
        prints it prettily in the format:
        most popular hashe
        1.
        2.
        3.
        4.


        then everything else on one line.
        """
        multi_print = True if len(objs) > 1 else False
        for i in objs:
            self.pretty_print_one(i, multi_print)

    def pretty_print_one(self, objs: List, multi_print: bool):
        out = f"\n[bold #011627 on #ff9f1c]{objs.chash}[/bold #011627 on #ff9f1c]\n"
        out += "\n[bold underline #2ec4b6]Most Likely[/bold underline #2ec4b6] \n"
        start = objs.prototypes[0:4]
        rest = objs.prototypes[4:]

        for i in start:
            out += self.turn_named_tuple_pretty_print(i) + "\n"

        # return if accessible is on
        if not self.a11y:
            out += "\n[bold underline #2ec4b6]Least Likely[/bold underline #2ec4b6]\n"

            for i in rest:
                out += self.turn_named_tuple_pretty_print(i) + " "

        console.print(out)
        return out

    def turn_named_tuple_pretty_print(self, nt: NamedTuple):
        # This colours red
        out = f"[bold #e71d36]{nt['name']}[/bold #e71d36], "

        hc = nt["hashcat"]
        john = nt["john"]
        des = nt["description"]

        if hc is not None and john:
            out += f"Hashcat Mode: {hc}, "
        elif hc is not None:
            out += f"Hashcat Mode: {hc}."
        if john is not None and des:
            out += f"John Name: {john}, "
        elif john is not None:
            out += f"John Name: {john}."
        if des:
            # Orange
            out += f"[#ff9f1c]Summary: {des}[/#ff9f1c]"

        return out


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

    # nth = the object which names the hash types
    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    # prettifier print things :)
    prettifier = Prettifier(kwargs)

    output = []

    if kwargs["text"]:
        output.append(HashObj(kwargs["text"], nth))
    elif kwargs["file"]:
        # else it must be a file
        for i in kwargs["file"].read().splitlines():
            # for every hash in the file, put it into the output list
            # we have to decode it as its bytes str
            output.append(HashObj(i.decode("utf-8"), nth))

    if kwargs["greppable"]:
        print(prettifier.greppable_output(output))
    else:
        prettifier.pretty_print(output)


def api_return_hashes_as_json(chash: [str], args: dict = {}):
    """
    Using name-that-hash as an API? Call this function!

    Given a list of hashes of strings
    return a list of json of all hashes in the same order as the input
    """
    # nth = the object which names the hash types
    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    # prettifier print things :)
    prettifier = Prettifier(args, api=True)
    # prettifier print things :)

    output = []
    for i in chash:
        output.append(HashObj(i, nth))

    return prettifier.greppable_output(output)


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