class HashType:
    """
    Every hash given to our program will be assiocated with one object
    This object contains the possible type of hash
    and provides ways to print that hash
    """

    def __init__(self, chash: str, nth, hash_info, kwargs):
        self.chash = chash
        self.nth = nth

        self.popular = hash_info.popular

        # prorotypes is given as a generator
        if "extreme" in kwargs and kwargs["extreme"]:
            self.prototypes = nth.identify_all(chash)
        else:
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
            else:
                to_ret.append(i.__dict__)
        return populars + to_ret
