class HashInformation:
    def __init__(self):
        self.popular = set(
            [
                "MD5",
                "MD4",
                "NTLM",
                "SHA-256",
                "SHA-512",
                "Keccak-256",
                "Keccak-512",
                "Blake2",
                "bcrypt",
                "SHA-1",
                "HMAC-SHA1 (key = $salt)",
                "CryptoCurrency(PrivateKey)",
                "SHA-338",
                "Domain Cached Credentials",
                "Domain Cached Credentials 2",
            ]
        )
