__version__ = "0.1.0"

# cli interface
from name_that_hash import runner

# script interface
from name_that_hash.runner import (
    api_return_hashes_as_json,
    api_return_hashes_identity
)

if __name__ == "__main__":
    runner.main()
