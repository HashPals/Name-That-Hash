import click
import json
from rich import print

import name_that_hash
import hashes


class HashObj:
    """
    Every hash given to our program will be assiocated with one object
    This object contains the possible type of hash
    and provides ways to print that hash

    """

    def __init__(self, chash, nth):
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
    def greppable_output(self, objs):
        """
        takes the prototypes and turns it into json
        returns the json
        """
        json_obj = json.dumps(objs.hash_obj, indent=4)
        return json_obj

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
        out = "[bold underline]Most Likely[/bold underline] \n"
        start = objs.prototypes[0:4]
        rest = objs.prototypes[4:]

        for i in start:
            out += self.turn_named_tuple_pretty_print(i) + "\n"

        out += "\n[bold underline]Least Likely[/bold underline]\n"

        for i in rest:
            out += self.turn_named_tuple_pretty_print(i) + " "

        print(out)
        return out

    def turn_named_tuple_pretty_print(self, nt):
        out = f"[bold red]{nt['name']}[/bold red], "

        hc = nt["hashcat"]
        john = nt["john"]
        des = nt["description"]

        if hc and john:
            out += f"Hashcat Mode: {hc}, "
        elif hc:
            out += f"Hashcat Mode: {hc}."
        if john and des:
            out += f"John Name: {john}, "
        elif john:
            out += f"John Name: {john}."
        if des:
            out += f"[magenta]Summary: {des}[/magenta]"

        return out


def banner():
    text = """
  _   _                           _____ _           _          _   _           _     
 | \ | |                         |_   _| |         | |        | | | |         | |    
 |  \| | __ _ _ __ ___   ___ ______| | | |__   __ _| |_ ______| |_| | __ _ ___| |__  
 | . ` |/ _` | '_ ` _ \ / _ \______| | | '_ \ / _` | __|______|  _  |/ _` / __| '_ \ 
 | |\  | (_| | | | | | |  __/      | | | | | | (_| | |_       | | | | (_| \__ \ | | |
  \_| \_/\__,_|_| |_| |_|\___| |_| \_/ |_| |_|\__,_|\__|      \_| |_/\__,_|___/_| |_|
https://twitter.com/bee_sec_san
https://github.com/HashPals/Name-That-Hash
    """
    print(text)


@click.command()
@click.option(
    "-g",
    "--greppable",
    is_flag=True,
    type=bool,
    help="Are you going to grep this output?",
)
@click.option("-t", "--text", help="Check one hash")
@click.option(
    "-a",
    "--accessible",
    is_flag=True,
    help="Turn on accessible mode, does not print ASCII art.",
)
@click.argument("file", type=click.File("rb"), required=False)
def main(**kwargs):
    """Name That Hash - Instantly name the type of any hash!

    Github:
    https://github.com/hashpals/name-that-hash

    """

    if not kwargs["accessible"]:
        banner()

    nth = name_that_hash.Name_That_Hash(hashes.prototypes)
    prettifier = Prettifier()

    if kwargs["text"]:
        output_obj = HashObj(kwargs["text"], nth)
    else:
        pass

    if kwargs["greppable"]:
        prettifier.greppable_output(output_obj)
    else:
        prettifier.pretty_print(output_obj)


if __name__ == "__main__":
    main()
