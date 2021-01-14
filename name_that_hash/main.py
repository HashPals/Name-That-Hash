import click
import json

import name_that_hash
import hashes


class prettifier:
    def __init__(self, prototypes):
        self.popular = set(["MD5", "NTLM", "SHA256", "SHA515"])
        # prorotypes is given as a generator
        self.prototypes = list(prototypes)
        self.prototypes = self.sort_by_popular()

    def greppable_output(self):
        """
        takes the prototypes and turns it into json
        returns the json
        """
        json_obj = json.dumps(self.prototypes, indent=4)
        print(json_obj)

    def pretty_print(self):
        """
        prints it prettily in the format:
        most popular hashes
        1.
        2.
        3.
        4.

        And then everything else on one line.
        """
        out = "Most Likely \n"
        start = self.prototypes[0:4]
        rest = self.prototypes[4:]

        for i in start:
            out += self.turn_named_tuple_pretty_print(i) + "\n"

        out += "\nLeast Likely\n"

        for i in rest:
            out += self.turn_named_tuple_pretty_print(i)

        print(out)
        return out

    def turn_named_tuple_pretty_print(self, nt):
        return f"- {nt.name}, Hashcat mode {nt.hashcat}, John Name {nt.john}"

    def get_prototypes(self):
        return self.prototypes

    def sort_by_popular(self):
        """Sorts the list by popular + everything else

        we do this using the self.popular set. Sets have O(1) lookup, so it's cheap.
        If one named_tuple is in the popular set, we add it to the populars list and remove it from prototypes.

        we then return populars list + prototypes.
        """
        populars = []
        for i in self.prototypes:
            if i.name in self.popular:
                populars.append(i)
                self.prototypes.remove(i)
        return populars + self.prototypes


@click.command()
@click.option("-g", "--greppable", help="Are you going to grep this output?")
@click.option("-t", "--text", help="Check one hash")
@click.argument("file", type=click.File("rb"), required=False)
def main(**kwargs):
    """Name That Hash - Instantly name the type of any hash!

    Github:
    https://github.com/hashpals/name-that-hash

    """
    print(kwargs)

    nth = name_that_hash.Name_That_Hash(hashes.prototypes)

    output = nth.identify(kwargs["text"])
    import pprint

    ptfy = prettifier(output)

    pprint.pprint(ptfy.sort_by_popular())


main()
