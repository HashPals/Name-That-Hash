import loguru

from name_that_hash import hash_info, HashTypeObj

class HashChecker:
    """
    Call this with an input to identify hashes
    """

    def __init__(self, kwargs, nth):
        self.kwargs = kwargs
        self.hashinfo_obj = hash_info.HashInformation()
        self.nth = nth
        self.output = []

    def file_input(self, f):
        for nr, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                logger.trace(f"Skipped empty line {nr}")
                continue
            self.single_hash(nr)
            
    def single_hash(self, chash: str):
        if self.kwargs["base64"]:
            logger.trace("decoding as base64")
            try:
                # b64decode returns Bytes obj
                chash = base64.b64decode(line).decode("utf-8")
            except:
                logger.trace("Failed to base64 decode")
            logger.trace(f"hash is now {line}")
        self.output.append(HashTypeObj.HashType(chash, self.nth, self.hashinfo_obj))
