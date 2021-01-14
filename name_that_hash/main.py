import click

import name_that_hash
import hashes


class prettifier:
    def __init__(self, prototypes):
        self.popular = set(["MD5", "NTLM", "SHA256", "SHA515"])
        # prorotypes is given as a generator
        self.prototypes = list(prototypes)

    def greppable_output(self):
        import pprint

        pprint.pprint(self.prototypes)

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
