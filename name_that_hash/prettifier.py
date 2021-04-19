import json
from typing import NamedTuple, List
from rich.console import Console
import logging

# we need a global console to control highlighting / printing
console = Console(highlighter=False)


class Prettifier:
    """
    This classes entire existence is to output stuff.
    """

    def __init__(self, kwargs, api=False):
        """
        Takes arguments as list so we can do A11Y stuff etc
        """
        if api is not True:
            self.a11y = kwargs["accessible"]
            self.john = kwargs["no_john"]
            self.hashcat = kwargs["no_hashcat"]

    def greppable_output(self, objs: List):
        logging.debug("Greppable output")
        logging.debug(f"Objects is {objs}")
        """
        takes the prototypes and turns it into json
        returns the json

        Doesn't print it, it prints in main
        """
        return json.dumps(self.turn_hash_objs_into_dict(objs), indent=2)

    def turn_hash_objs_into_dict(self, objs: List):
        outputs_as_dict = {}

        for y in objs:
            outputs_as_dict.update(y.hash_obj)
            logging.debug(f"Output_as_dicts is now {outputs_as_dict}")
        return outputs_as_dict

    def pretty_print(self, objs):
        logging.debug("In pretty printing")
        """
        prints it prettily in the format:
        most popular hashes
        1.
        2.
        3.
        4.


        then everything else on one line.
        """
        multi_print = True if len(objs) > 1 else False
        for i in objs:
            logging.debug(i)
            self.pretty_print_one(i, multi_print)

    def pretty_print_one(self, objs: List, multi_print: bool):
        out = f"\n[bold magenta]{objs.chash}[/bold magenta]\n"

        # It didn't find any hashes.
        if len(objs.prototypes) == 0:
            out += "[bold #FF0000]No hashes found.[/bold #FF0000]"
            console.print(out)
            return out

        out += "\n[bold underline #5f5fff]Most Likely[/bold underline #5f5fff] \n"
        start = objs.prototypes[0:4]
        rest = objs.prototypes[4:]

        for i in start:
            out += self.turn_named_tuple_pretty_print(i) + "\n"

        # It has hashes, but not many so don't print least likely.
        if len(objs.prototypes) <= 5:
            console.print(out)
            return out

        # return if accessible is on
        if not self.a11y:
            out += "\n[bold underline #5f5fff]Least Likely[/bold underline #5f5fff]\n"

            for i in rest:
                out += self.turn_named_tuple_pretty_print(i) + " "

        console.print(out)
        return out

    def turn_named_tuple_pretty_print(self, nt: NamedTuple):
        # This colours red
        out = f"[bold #ff5f00]{nt['name']}[/bold #ff5f00], "

        hc = nt["hashcat"]
        john = nt["john"]
        des = nt["description"]

        if not self.hashcat:
            if hc is not None and john:
                out += f"HC: {hc} "
            elif hc is not None:
                out += f"HC: {hc} "

        if not self.john:
            if john is not None and des:
                out += f"JtR: {john} "
            elif john is not None:
                out += f"JtR: {john}"
        if des:
            # Orange
            out += f"[#8787D7]Summary: {des}[/#8787D7]"

        return out
