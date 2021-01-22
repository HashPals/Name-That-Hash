import re


class Name_That_Hash:
    """
    The main class which deals with hash identification
    """

    def __init__(self, prototypes: list):
        self.prototypes = list(prototypes)

    def identify(self, chash: str):
        chash = chash.strip()
        for prototype in self.prototypes:
            if prototype.regex.match(chash):
                for mode in prototype.modes:
                    yield mode
