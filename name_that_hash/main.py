import click
import json

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
        populars = []
        for i in self.prototypes:
            if i.name in self.popular:
                populars.append(i)
                self.prototypes.remove(i)
        return populars + self.prototypes


class Prettifier:
    def greppable_output(self, objs):
        """
        takes the prototypes and turns it into json
        returns the json
        """
        import pprint

        pprint.pprint(objs.hash_obj)
        json_obj = json.dumps(objs.hash_obj, indent=4)
        print(json_obj)

    def pretty_print(self):
        """
        prints it prettily in the format:
        most popular hashe
        1.
        2.
        3.
        4.


        then everything else on one line.
        """
        out = "Most Likely \n"
        start = prototypes[0:4]
        rest = prototypes[4:]

        for i in start:
            out += self.turn_named_tuple_pretty_print(i) + "\n"

        out += "\nLeast Likely\n"

        for i in rest:
            out += self.turn_named_tuple_pretty_print(i)

        print(out)
        return out

    def turn_named_tuple_pretty_print(self, nt):
        return f"- {nt.name}, Hashcat mode {nt.hashcat}, John Name {nt.john}"


@click.command()
@click.option("-g", "--greppable", type=bool, help="Are you going to grep this output?")
@click.option("-t", "--text", help="Check one hash")
@click.argument("file", type=click.File("rb"), required=False)
def main(**kwargs):
    """Name That Hash - Instantly name the type of any hash!

    Github:
    https://github.com/hashpals/name-that-hash

    """
    nth = name_that_hash.Name_That_Hash(hashes.prototypes)
    prettifier = Prettifier()

    if kwargs["text"]:
        output_obj = HashObj(kwargs["text"], nth)

    if kwargs["greppable"]:
        prettifier.greppable_output(output_obj)
    else:
        output_obj.pretty_print()


if __name__ == "__main__":
    main()
