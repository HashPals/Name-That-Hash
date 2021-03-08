__version__ = "0.1.0"

# cli interface
from name_that_hash import runner

# script interface
from name_that_hash.runner import (
    identify_hash,
    identify_hashes
)

if __name__ == "__main__":
    runner.main()
