from collections import namedtuple
import re
from dataclasses import dataclass

Prototype = namedtuple("Prototype", ["regex", "modes"])
"""HashInfo = namedtuple(
    "HashInfo", ["name", "hashcat", "john", "extended", "description"]
)"""


@dataclass
class HashInfo:
    name: str
    hashcat: int
    john: str
    extended: bool
    description: str = None


prototypes = [
    Prototype(
        regex=re.compile(r"^[a-f0-9]{4}$", re.IGNORECASE),
        modes=[
            HashInfo(name="CRC-16", hashcat=None, john=None, extended=False),
            HashInfo(name="CRC-16-CCITT", hashcat=None, john=None, extended=False),
            HashInfo(name="FCS-16", hashcat=None, john=None, extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{8}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Adler-32", hashcat=None, john=None, extended=False),
            HashInfo(name="CRC-32B", hashcat=None, john=None, extended=False),
            HashInfo(name="FCS-32", hashcat=None, john=None, extended=False),
            HashInfo(name="GHash-32-3", hashcat=None, john=None, extended=False),
            HashInfo(name="GHash-32-5", hashcat=None, john=None, extended=False),
            HashInfo(name="FNV-132", hashcat=None, john=None, extended=False),
            HashInfo(name="Fletcher-32", hashcat=None, john=None, extended=False),
            HashInfo(name="Joaat", hashcat=None, john=None, extended=False),
            HashInfo(name="ELF-32", hashcat=None, john=None, extended=False),
            HashInfo(name="XOR-32", hashcat=None, john=None, extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{6}$", re.IGNORECASE),
        modes=[HashInfo(name="CRC-24", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^(\$crc32\$[a-f0-9]{8}.)?[a-f0-9]{8}$", re.IGNORECASE),
        modes=[HashInfo(name="CRC-32", hashcat=11500, john="crc32", extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^\+[a-z0-9\/.]{12}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Eggdrop IRC Bot", hashcat=None, john="bfegg", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9\/.]{13}$", re.IGNORECASE),
        modes=[
            HashInfo(name="DES(Unix)", hashcat=1500, john="descrypt", extended=False),
            HashInfo(
                name="Traditional DES", hashcat=1500, john="descrypt", extended=False
            ),
            HashInfo(name="DEScrypt", hashcat=1500, john="descrypt", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{16}$", re.IGNORECASE),
        modes=[
            HashInfo(name="MySQL323", hashcat=200, john="mysql", extended=False),
            HashInfo(name="DES(Oracle)", hashcat=3100, john=None, extended=False),
            HashInfo(name="Half MD5", hashcat=5100, john=None, extended=False),
            HashInfo(name="Oracle 7-10g", hashcat=3100, john=None, extended=False),
            HashInfo(name="FNV-164", hashcat=None, john=None, extended=False),
            HashInfo(name="CRC-64", hashcat=None, john=None, extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9\/.]{16}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Cisco-PIX(MD5)", hashcat=2400, john="pix-md5", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\([a-z0-9\/+]{20}\)$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Lotus Notes/Domino 6",
                hashcat=8700,
                john="dominosec",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^_[a-z0-9\/.]{19}$", re.IGNORECASE),
        modes=[
            HashInfo(name="BSDi Crypt", hashcat=None, john="bsdicrypt", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{24}$", re.IGNORECASE),
        modes=[HashInfo(name="CRC-96(ZIP)", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9\/.]{24}$", re.IGNORECASE),
        modes=[HashInfo(name="Crypt16", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}(:.+)?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="MD5",
                hashcat=0,
                john="raw-md5",
                extended=False,
                description="Used for Linux Shadow files.",
            ),
            HashInfo(name="MD4", hashcat=900, john="raw-md4", extended=False),
            HashInfo(name="Double MD5", hashcat=2600, john=None, extended=False),
            HashInfo(name="LM", hashcat=3000, john="lm", extended=False),
            HashInfo(
                name="RIPEMD-128", hashcat=None, john="ripemd-128", extended=False
            ),
            HashInfo(
                name="Haval-128", hashcat=None, john="haval-128-4", extended=False
            ),
            HashInfo(name="Tiger-128", hashcat=None, john=None, extended=False),
            HashInfo(name="Skein-256(128)", hashcat=None, john=None, extended=False),
            HashInfo(name="Skein-512(128)", hashcat=None, john=None, extended=False),
            HashInfo(
                name="Lotus Notes/Domino 5", hashcat=8600, john="lotus5", extended=False
            ),
            HashInfo(name="Skype", hashcat=23, john=None, extended=False),
            HashInfo(name="ZipMonster", hashcat=None, john=None, extended=True),
            HashInfo(name="PrestaShop", hashcat=11000, john=None, extended=True),
            HashInfo(
                name="md5(md5(md5($pass)))", hashcat=3500, john=None, extended=True
            ),
            HashInfo(
                name="md5(uppercase(md5($pass)))",
                hashcat=4300,
                john=None,
                extended=True,
            ),
            HashInfo(name="md5(sha1($pass))", hashcat=4400, john=None, extended=True),
            HashInfo(name="md5($pass.$salt)", hashcat=10, john=None, extended=True),
            HashInfo(name="md5($salt.$pass)", hashcat=20, john=None, extended=True),
            HashInfo(
                name="md5(unicode($pass).$salt)", hashcat=30, john=None, extended=True
            ),
            HashInfo(
                name="md5($salt.unicode($pass))", hashcat=40, john=None, extended=True
            ),
            HashInfo(
                name="HMAC-MD5 (key = $pass)",
                hashcat=50,
                john="hmac-md5",
                extended=True,
            ),
            HashInfo(
                name="HMAC-MD5 (key = $salt)",
                hashcat=60,
                john="hmac-md5",
                extended=True,
            ),
            HashInfo(
                name="md5(md5($salt).$pass)", hashcat=3610, john=None, extended=True
            ),
            HashInfo(
                name="md5($salt.md5($pass))", hashcat=3710, john=None, extended=True
            ),
            HashInfo(
                name="md5($pass.md5($salt))", hashcat=3720, john=None, extended=True
            ),
            HashInfo(
                name="md5($salt.$pass.$salt)", hashcat=3810, john=None, extended=True
            ),
            HashInfo(
                name="md5(md5($pass).md5($salt))",
                hashcat=3910,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="md5($salt.md5($salt.$pass))",
                hashcat=4010,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="md5($salt.md5($pass.$salt))",
                hashcat=4110,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="md5($username.0.$pass)", hashcat=4210, john=None, extended=True
            ),
            HashInfo(
                name="md5(utf16($pass))", hashcat=None, john="dynamic_29", extended=True
            ),
            HashInfo(
                name="md4($salt.$pass)", hashcat=None, john="dynamic_31", extended=True
            ),
            HashInfo(
                name="md4($pass.$salt)", hashcat=None, john="dynamic_32", extended=True
            ),
            HashInfo(
                name="md4(utf16($pass))", hashcat=None, john="dynamic_33", extended=True
            ),
            HashInfo(
                name="md5(md4($pass))", hashcat=None, john="dynamic_34", extended=True
            ),
            HashInfo(name="net-md5", hashcat=None, john="dynamic_39", extended=True),
            HashInfo(
                name="md5($salt.pad16($pass))",
                hashcat=None,
                john="dynamic_39",
                extended=True,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$md2\$)?[a-f0-9]{32}$", re.IGNORECASE),
        modes=[HashInfo(name="MD2", hashcat=None, john="md2", extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^(\$snefru\$)?[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Snefru-128", hashcat=None, john="snefru-128", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$NT\$)?[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="NTLM",
                hashcat=1000,
                john="nt",
                extended=False,
                description="Often used in Windows Active Directory.",
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r'^([^\\\/:*?"<>|]{1,20}:)?[a-f0-9]{32}(:[^\\\/:*?"<>|]{1,20})?$',
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Domain Cached Credentials",
                hashcat=1100,
                john="mscach",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r'^([^\\\/:*?"<>|]{1,20}:)?(\$DCC2\$10240#[^\\\/:*?"<>|]{1,20}#)?[a-f0-9]{32}$',
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Domain Cached Credentials 2",
                hashcat=2100,
                john="mscach2",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^{SHA}[a-z0-9\/+]{27}=$", re.IGNORECASE),
        modes=[
            HashInfo(name="SHA-1(Base64)", hashcat=101, john="nsldap", extended=False),
            HashInfo(
                name="Netscape LDAP SHA", hashcat=101, john="nsldap", extended=False
            ),
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$1\$[a-z0-9\/.]{0,8}\$[a-z0-9\/.]{22}(:.*)?$", re.IGNORECASE
        ),
        modes=[
            HashInfo(name="MD5 Crypt", hashcat=500, john="md5crypt", extended=False),
            HashInfo(
                name="Cisco-IOS(MD5)", hashcat=500, john="md5crypt", extended=False
            ),
            HashInfo(name="FreeBSD MD5", hashcat=500, john="md5crypt", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^0x[a-f0-9]{32}$", re.IGNORECASE),
        modes=[HashInfo(name="Lineage II C4", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^\$H\$[a-z0-9\/.]{31}$", re.IGNORECASE),
        modes=[
            HashInfo(name="phpBB v3.x", hashcat=400, john="phpass", extended=False),
            HashInfo(
                name="Wordpress v2.6.0/2.6.1",
                hashcat=400,
                john="phpass",
                extended=False,
            ),
            HashInfo(
                name="PHPass' Portable Hash", hashcat=400, john="phpass", extended=False
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$P\$[a-z0-9\/.]{31}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name=u"Wordpress ≥ v2.6.2", hashcat=400, john="phpass", extended=False
            ),
            HashInfo(
                name=u"Joomla ≥ v2.5.18", hashcat=400, john="phpass", extended=False
            ),
            HashInfo(
                name="PHPass' Portable Hash", hashcat=400, john="phpass", extended=False
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:[a-z0-9]{2}$", re.IGNORECASE),
        modes=[
            HashInfo(name="osCommerce", hashcat=21, john=None, extended=False),
            HashInfo(name="xt:Commerce", hashcat=21, john=None, extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$apr1\$[a-z0-9\/.]{0,8}\$[a-z0-9\/.]{22}$", re.IGNORECASE),
        modes=[
            HashInfo(name="MD5(APR)", hashcat=1600, john=None, extended=False),
            HashInfo(name="Apache MD5", hashcat=1600, john=None, extended=False),
            HashInfo(name="md5apr1", hashcat=1600, john=None, extended=True),
        ],
    ),
    Prototype(
        regex=re.compile(r"^{smd5}[a-z0-9$\/.]{31}$", re.IGNORECASE),
        modes=[
            HashInfo(name="AIX(smd5)", hashcat=6300, john="aix-smd5", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(name="WebEdition CMS", hashcat=3721, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:.{5}$", re.IGNORECASE),
        modes=[
            HashInfo(name=u"IP.Board ≥ v2+", hashcat=2811, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:.{8}$", re.IGNORECASE),
        modes=[HashInfo(name=u"MyBB ≥ v1.2+", hashcat=2811, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9]{34}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="CryptoCurrency(Adress)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{40}(:.+)?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SHA-1",
                hashcat=100,
                john="raw-sha1",
                extended=False,
                description="[link=https://en.wikipedia.org/wiki/SHA-1]Used for checksums.[/link]",
            ),
            HashInfo(name="Double SHA-1", hashcat=4500, john=None, extended=False),
            HashInfo(
                name="RIPEMD-160", hashcat=6000, john="ripemd-160", extended=False
            ),
            HashInfo(name="Haval-160", hashcat=None, john=None, extended=False),
            HashInfo(name="Tiger-160", hashcat=None, john=None, extended=False),
            HashInfo(name="HAS-160", hashcat=None, john=None, extended=False),
            HashInfo(
                name="LinkedIn", hashcat=190, john="raw-sha1-linkedin", extended=False
            ),
            HashInfo(name="Skein-256(160)", hashcat=None, john=None, extended=False),
            HashInfo(name="Skein-512(160)", hashcat=None, john=None, extended=False),
            HashInfo(
                name="MangosWeb Enhanced CMS", hashcat=None, john=None, extended=True
            ),
            HashInfo(
                name="sha1(sha1(sha1($pass)))", hashcat=4600, john=None, extended=True
            ),
            HashInfo(name="sha1(md5($pass))", hashcat=4700, john=None, extended=True),
            HashInfo(name="sha1($pass.$salt)", hashcat=110, john=None, extended=True),
            HashInfo(name="sha1($salt.$pass)", hashcat=120, john=None, extended=True),
            HashInfo(
                name="sha1(unicode($pass).$salt)", hashcat=130, john=None, extended=True
            ),
            HashInfo(
                name="sha1($salt.unicode($pass))", hashcat=140, john=None, extended=True
            ),
            HashInfo(
                name="HMAC-SHA1 (key = $pass)",
                hashcat=150,
                john="hmac-sha1",
                extended=True,
            ),
            HashInfo(
                name="HMAC-SHA1 (key = $salt)",
                hashcat=160,
                john="hmac-sha1",
                extended=True,
            ),
            HashInfo(
                name="sha1($salt.$pass.$salt)", hashcat=4710, john=None, extended=True
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^\*[a-f0-9]{40}$", re.IGNORECASE),
        modes=[
            HashInfo(name="MySQL5.x", hashcat=300, john="mysql-sha1", extended=False),
            HashInfo(name="MySQL4.1", hashcat=300, john="mysql-sha1", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9]{43}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Cisco-IOS(SHA-256)", hashcat=5700, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^{SSHA}[a-z0-9\/+]{38}==$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SSHA-1(Base64)", hashcat=111, john="nsldaps", extended=False
            ),
            HashInfo(
                name="Netscape LDAP SSHA", hashcat=111, john="nsldaps", extended=False
            ),
            HashInfo(name="nsldaps", hashcat=111, john="nsldaps", extended=True),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9=]{47}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Fortigate(FortiOS)",
                hashcat=7000,
                john="fortigate",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{48}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Haval-192", hashcat=None, john=None, extended=False),
            HashInfo(name="Tiger-192", hashcat=None, john="tiger", extended=False),
            HashInfo(name="SHA-1(Oracle)", hashcat=None, john=None, extended=False),
            HashInfo(name="OSX v10.4", hashcat=122, john="xsha", extended=False),
            HashInfo(name="OSX v10.5", hashcat=122, john="xsha", extended=False),
            HashInfo(name="OSX v10.6", hashcat=122, john="xsha", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{51}$", re.IGNORECASE),
        modes=[HashInfo(name="Palshop CMS", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9]{51}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="CryptoCurrency(PrivateKey)",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^{ssha1}[0-9]{2}\$[a-z0-9$\/.]{44}$", re.IGNORECASE),
        modes=[
            HashInfo(name="AIX(ssha1)", hashcat=6700, john="aix-ssha1", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^0x0100[a-f0-9]{48}$", re.IGNORECASE),
        modes=[
            HashInfo(name="MSSQL(2005)", hashcat=132, john="mssql05", extended=False),
            HashInfo(name="MSSQL(2008)", hashcat=132, john="mssql05", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^(\$md5,rounds=[0-9]+\$|\$md5\$rounds=[0-9]+\$|\$md5\$)[a-z0-9\/.]{0,16}(\$|\$\$)[a-z0-9\/.]{22}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(name="Sun MD5 Crypt", hashcat=3300, john="sunmd5", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{56}$", re.IGNORECASE),
        modes=[
            HashInfo(name="SHA-224", hashcat=None, john="raw-sha224", extended=False),
            HashInfo(name="Haval-224", hashcat=None, john=None, extended=False),
            HashInfo(name="SHA3-224", hashcat=17300, john=None, extended=False),
            HashInfo(name="Skein-256(224)", hashcat=None, john=None, extended=False),
            HashInfo(name="Skein-512(224)", hashcat=None, john=None, extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Blowfish(OpenBSD)",
                hashcat=3200,
                john="bcrypt",
                extended=False,
                description="Can be used in Linux Shadow Files.",
            ),
            HashInfo(
                name="Woltlab Burning Board 4.x",
                hashcat=None,
                john=None,
                extended=False,
            ),
            HashInfo(name="bcrypt", hashcat=3200, john="bcrypt", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{40}:[a-f0-9]{16}$", re.IGNORECASE),
        modes=[HashInfo(name="Android PIN", hashcat=5800, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^(S:)?[a-f0-9]{40}(:)?[a-f0-9]{20}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Oracle 11g/12c", hashcat=112, john="oracle11", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$bcrypt-sha256\$(2[axy]|2)\,[0-9]+\$[a-z0-9\/.]{22}\$[a-z0-9\/.]{31}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(name="bcrypt(SHA-256)", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:.{3}$", re.IGNORECASE),
        modes=[
            HashInfo(name="vBulletin < v3.8.5", hashcat=2611, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:.{30}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name=u"vBulletin ≥ v3.8.5", hashcat=2711, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$snefru\$)?[a-f0-9]{64}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Snefru-256", hashcat=None, john="snefru-256", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{64}(:.+)?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SHA-256",
                hashcat=1400,
                john="raw-sha256",
                extended=False,
                description="256-bit key and is a good partner-function for AES. Can be used in Shadow files.",
            ),
            HashInfo(name="RIPEMD-256", hashcat=None, john=None, extended=False),
            HashInfo(
                name="Haval-256", hashcat=None, john="haval-256-3", extended=False
            ),
            HashInfo(name="GOST R 34.11-94", hashcat=6900, john="gost", extended=False),
            HashInfo(
                name="GOST CryptoPro S-Box", hashcat=None, john=None, extended=False
            ),
            HashInfo(name="Blake2b-256", hashcat=None, john=None,extended=False),
            HashInfo(name="SHA3-256", hashcat=17400, john=None, extended=False),
            HashInfo(name="Skein-256", hashcat=None, john="skein-256", extended=False),
            HashInfo(name="Skein-512(256)", hashcat=None, john=None, extended=False),
            HashInfo(name="Ventrilo", hashcat=None, john=None, extended=True),
            HashInfo(
                name="sha256($pass.$salt)", hashcat=1410, john=None, extended=True
            ),
            HashInfo(
                name="sha256($salt.$pass)", hashcat=1420, john=None, extended=True
            ),
            HashInfo(
                name="sha256(unicode($pass).$salt)",
                hashcat=1430,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="sha256($salt.unicode($pass))",
                hashcat=1440,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="HMAC-SHA256 (key = $pass)",
                hashcat=1450,
                john="hmac-sha256",
                extended=True,
            ),
            HashInfo(
                name="HMAC-SHA256 (key = $salt)",
                hashcat=1460,
                john="hmac-sha256",
                extended=True,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:[a-z0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Joomla < v2.5.18", hashcat=11, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{32}:[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SAM(LM_Hash:NT_Hash)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^(\$chap\$0\*)?[a-f0-9]{32}[\*:][a-f0-9]{32}(:[0-9]{2})?$", re.IGNORECASE
        ),
        modes=[
            HashInfo(name="MD5(Chap)", hashcat=4800, john="chap", extended=False),
            HashInfo(
                name="iSCSI CHAP Authentication",
                hashcat=4800,
                john="chap",
                extended=False,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$episerver\$\*0\*[a-z0-9\/=+]+\*[a-z0-9\/=+]{27,28}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="EPiServer 6.x < v4", hashcat=141, john="episerver", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^{ssha256}[0-9]{2}\$[a-z0-9$\/.]{60}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="AIX(ssha256)", hashcat=6400, john="aix-ssha256", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{80}$", re.IGNORECASE),
        modes=[HashInfo(name="RIPEMD-320", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(
            r"^\$episerver\$\*1\*[a-z0-9\/=+]+\*[a-z0-9\/=+]{42,43}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name=u"EPiServer 6.x ≥ v4",
                hashcat=1441,
                john="episerver",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^0x0100[a-f0-9]{88}$", re.IGNORECASE),
        modes=[HashInfo(name="MSSQL(2000)", hashcat=131, john="mssql", extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{96}$", re.IGNORECASE),
        modes=[
            HashInfo(name="SHA-384", hashcat=10800, john="raw-sha384", extended=False),
            HashInfo(name="SHA3-384", hashcat=None, john=None, extended=False),
            HashInfo(name="Skein-512(384)", hashcat=None, john=None, extended=False),
            HashInfo(name="Skein-1024(384)", hashcat=None, john=None, extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^{SSHA512}[a-z0-9\/+]{96}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SSHA-512(Base64)", hashcat=1711, john="ssha512", extended=False
            ),
            HashInfo(
                name="LDAP(SSHA-512)", hashcat=1711, john="ssha512", extended=False
            ),
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^{ssha512}[0-9]{2}\$[a-z0-9\/.]{16,48}\$[a-z0-9\/.]{86}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="AIX(ssha512)", hashcat=6500, john="aix-ssha512", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{128}(:.+)?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SHA-512",
                hashcat=1700,
                john="raw-sha512",
                extended=False,
                description="Used in Bitcoin Blockchain and Shadow Files.",
            ),
            HashInfo(name="Keccak-512", hashcat=1800, john=None, extended=False),
            HashInfo(name="Whirlpool", hashcat=6100, john="whirlpool", extended=False),
            HashInfo(
                name="Salsa10",
                hashcat=None,
                john=None,
                extended=False,
                description="[link = https://bugs.php.net/bug.php?id=60783]Not considered a hash function.[/link]",
            ),
            HashInfo(
                name="Salsa20",
                hashcat=None,
                john=None,
                extended=False,
                description="[link = https://bugs.php.net/bug.php?id=60783]Not considered a hash function.[/link]",
            ),
            HashInfo(
                name="Blake2",
                hashcat=600,
                john="raw-blake2",
                extended=False,
                description="[link = https://en.wikipedia.org/wiki/BLAKE_(hash_function)#Users_of_BLAKE2]Used in Wireguard, Zcash, IPFS and more.[/link]",
            ),
            HashInfo(name="SHA3-512", hashcat=17600, john="raw-sha3", extended=False),
            HashInfo(name="Skein-512", hashcat=None, john="skein-512", extended=False),
            HashInfo(name="Skein-1024(512)", hashcat=None, john=None, extended=False),
            HashInfo(
                name="sha512($pass.$salt)", hashcat=1710, john=None, extended=True
            ),
            HashInfo(
                name="sha512($salt.$pass)", hashcat=1720, john=None, extended=True
            ),
            HashInfo(
                name="sha512(unicode($pass).$salt)",
                hashcat=1730,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="sha512($salt.unicode($pass))",
                hashcat=1740,
                john=None,
                extended=True,
            ),
            HashInfo(
                name="HMAC-SHA512 (key = $pass)",
                hashcat=1750,
                john="hmac-sha512",
                extended=True,
            ),
            HashInfo(name="Keccak-384", hashcat=17900, john=None, extended=False),
            HashInfo(name="Keccak-256", hashcat=17800, john=None, extended=False),
            HashInfo(name="Keccak-224", hashcat=17700, john=None, extended=False),
            HashInfo(
                name="HMAC-SHA512 (key = $salt)",
                hashcat=1760,
                john="hmac-sha512",
                extended=True,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{136}$", re.IGNORECASE),
        modes=[
            HashInfo(name="OSX v10.7", hashcat=1722, john="xsha512", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^0x0200[a-f0-9]{136}$", re.IGNORECASE),
        modes=[
            HashInfo(name="MSSQL(2012)", hashcat=1731, john="msql12", extended=False),
            HashInfo(name="MSSQL(2014)", hashcat=1731, john="msql12", extended=False),
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$ml\$[0-9]+\$[a-f0-9]{64}\$[a-f0-9]{128}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="OSX v10.8",
                hashcat=7100,
                john="pbkdf2-hmac-sha512",
                extended=False,
            ),
            HashInfo(
                name="OSX v10.9",
                hashcat=7100,
                john="pbkdf2-hmac-sha512",
                extended=False,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{256}$", re.IGNORECASE),
        modes=[HashInfo(name="Skein-1024", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(
            r"^grub\.pbkdf2\.sha512\.[0-9]+\.([a-f0-9]{128,2048}\.|[0-9]+\.)?[a-f0-9]{128}$",
            re.IGNORECASE,
        ),
        modes=[HashInfo(name="GRUB 2", hashcat=7200, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^sha1\$[a-z0-9]+\$[a-f0-9]{40}$", re.IGNORECASE),
        modes=[HashInfo(name="Django(SHA-1)", hashcat=124, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{49}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Citrix Netscaler",
                hashcat=8100,
                john="citrix_ns10",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$S\$[a-z0-9\/.]{52}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Drupal > v7.x", hashcat=7900, john="drupal7", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$5\$(rounds=[0-9]+\$)?[a-z0-9\/.]{0,16}\$[a-z0-9\/.]{43}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="SHA-256 Crypt", hashcat=7400, john="sha256crypt", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^0x[a-f0-9]{4}[a-f0-9]{16}[a-f0-9]{64}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Sybase ASE", hashcat=8000, john="sybasease", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$6\$(rounds=[0-9]+\$)?[a-z0-9\/.]{0,16}\$[a-z0-9\/.]{86}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="SHA-512 Crypt", hashcat=1800, john="sha512crypt", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$sha\$[a-z0-9]{1,16}\$([a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64}|[a-f0-9]{128}|[a-f0-9]{140})$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Minecraft(AuthMe Reloaded)",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^sha256\$[a-z0-9]+\$[a-f0-9]{64}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Django(SHA-256)", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^sha384\$[a-z0-9]+\$[a-f0-9]{96}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Django(SHA-384)", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^crypt1:[a-z0-9+=]{12}:[a-z0-9+=]{12}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Clavister Secure Gateway", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{112}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Cisco VPN Client(PCF-File)",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{1329}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Microsoft MSTSC(RDP-File)",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r'^[^\\\/:*?"<>|]{1,20}[:]{2,3}([^\\\/:*?"<>|]{1,20})?:[a-f0-9]{48}:[a-f0-9]{48}:[a-f0-9]{16}$',
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="NetNTLMv1-VANILLA / NetNTLMv1+ESS",
                hashcat=5500,
                john="netntlm",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r'^([^\\\/:*?"<>|]{1,20}\\)?[^\\\/:*?"<>|]{1,20}[:]{2,3}([^\\\/:*?"<>|]{1,20}:)?[^\\\/:*?"<>|]{1,20}:[a-f0-9]{32}:[a-f0-9]+$',
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(name="NetNTLMv2", hashcat=5600, john="netntlmv2", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$(krb5pa|mskrb5)\$(23)?\$.+\$[a-f0-9]{1,}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="Kerberos 5 AS-REQ Pre-Auth",
                hashcat=7500,
                john="krb5pa-md5",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$scram\$[0-9]+\$[a-z0-9\/.]{16}\$sha-1=[a-z0-9\/.]{27},sha-256=[a-z0-9\/.]{43},sha-512=[a-z0-9\/.]{86}$",
            re.IGNORECASE,
        ),
        modes=[HashInfo(name="SCRAM Hash", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{40}:[a-f0-9]{0,32}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Redmine Project Management Web App",
                hashcat=7600,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^(.+)?\$[a-f0-9]{16}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SAP CODVN B (BCODE)", hashcat=7700, john="sapb", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^(.+)?\$[a-f0-9]{40}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SAP CODVN F/G (PASSCODE)",
                hashcat=7800,
                john="sapg",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^(.+\$)?[a-z0-9\/.+]{30}(:.+)?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Juniper Netscreen/SSG(ScreenOS)",
                hashcat=22,
                john="md5ns",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^0x[a-f0-9]{60}\s0x[a-f0-9]{40}$", re.IGNORECASE),
        modes=[HashInfo(name="EPi", hashcat=123, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{40}:[^*]{1,25}$", re.IGNORECASE),
        modes=[HashInfo(name=u"SMF ≥ v1.1", hashcat=121, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(
            r"^(\$wbb3\$\*1\*)?[a-f0-9]{40}[:*][a-f0-9]{40}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="Woltlab Burning Board 3.x",
                hashcat=8400,
                john="wbb3",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{130}(:[a-f0-9]{40})?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="IPMI2 RAKP HMAC-SHA1", hashcat=7300, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^[a-f0-9]{32}:[0-9]+:[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$",
            re.IGNORECASE,
        ),
        modes=[HashInfo(name="Lastpass", hashcat=6800, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9\/.]{16}([:$].{1,})?$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Cisco-ASA(MD5)", hashcat=2410, john="asa-md5", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$vnc\$\*[a-f0-9]{32}\*[a-f0-9]{32}$", re.IGNORECASE),
        modes=[HashInfo(name="VNC", hashcat=None, john="vnc", extended=False)],
    ),
    Prototype(
        regex=re.compile(
            r"^[a-z0-9]{32}(:([a-z0-9-]+\.)?[a-z0-9-.]+\.[a-z]{2,7}:.+:[0-9]+)?$",
            re.IGNORECASE,
        ),
        modes=[HashInfo(name="DNSSEC(NSEC3)", hashcat=8300, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^(user-.+:)?\$racf\$\*.+\*[a-f0-9]{16}$", re.IGNORECASE),
        modes=[HashInfo(name="RACF", hashcat=8500, john="racf", extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^\$3\$\$[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="NTHash(FreeBSD Variant)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$sha1\$[0-9]+\$[a-z0-9\/.]{0,64}\$[a-z0-9\/.]{28}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(name="SHA-1 Crypt", hashcat=None, john="sha1crypt", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{70}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="hMailServer", hashcat=1421, john="hmailserver", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^[:\$][AB][:\$]([a-f0-9]{1,8}[:\$])?[a-f0-9]{32}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(name="MediaWiki", hashcat=3711, john="mediawiki", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{140}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Minecraft(xAuth)", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$pbkdf2(-sha1)?\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{27}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PBKDF2-SHA1(Generic)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$pbkdf2-sha256\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{43}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PBKDF2-SHA256(Generic)",
                hashcat=None,
                john="pbkdf2-hmac-sha256",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$pbkdf2-sha512\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{86}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PBKDF2-SHA512(Generic)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$p5k2\$[0-9]+\$[a-z0-9\/+=-]+\$[a-z0-9\/+-]{27}=$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PBKDF2(Cryptacular)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$p5k2\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{32}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PBKDF2(Dwayne Litzenberger)",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^{FSHP[0123]\|[0-9]+\|[0-9]+}[a-z0-9\/+=]+$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Fairly Secure Hashed Password",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$PHPS\$.+\$[a-f0-9]{32}$", re.IGNORECASE),
        modes=[HashInfo(name="PHPS", hashcat=2612, john="phps", extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[0-9]{4}:[a-f0-9]{16}:[a-f0-9]{2080}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="1Password(Agile Keychain)",
                hashcat=6600,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^[a-f0-9]{64}:[a-f0-9]{32}:[0-9]{5}:[a-f0-9]{608}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="1Password(Cloud Keychain)",
                hashcat=8200,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^[a-f0-9]{256}:[a-f0-9]{256}:[a-f0-9]{16}:[a-f0-9]{16}:[a-f0-9]{320}:[a-f0-9]{16}:[a-f0-9]{40}:[a-f0-9]{40}:[a-f0-9]{32}$",
            re.IGNORECASE,
        ),
        modes=[HashInfo(name="IKE-PSK MD5", hashcat=5300, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(
            r"^[a-f0-9]{256}:[a-f0-9]{256}:[a-f0-9]{16}:[a-f0-9]{16}:[a-f0-9]{320}:[a-f0-9]{16}:[a-f0-9]{40}:[a-f0-9]{40}:[a-f0-9]{40}$",
            re.IGNORECASE,
        ),
        modes=[HashInfo(name="IKE-PSK SHA1", hashcat=5400, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9\/+]{27}=$", re.IGNORECASE),
        modes=[HashInfo(name="PeopleSoft", hashcat=133, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^crypt\$[a-f0-9]{5}\$[a-z0-9\/.]{13}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Django(DES Crypt Wrapper)",
                hashcat=None,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^(\$django\$\*1\*)?pbkdf2_sha256\$[0-9]+\$[a-z0-9]+\$[a-z0-9\/+=]{44}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Django(PBKDF2-HMAC-SHA256)",
                hashcat=10000,
                john="django",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^pbkdf2_sha1\$[0-9]+\$[a-z0-9]+\$[a-z0-9\/+=]{28}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="Django(PBKDF2-HMAC-SHA1)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^bcrypt(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(name="Django(bcrypt)", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^md5\$[a-f0-9]+\$[a-f0-9]{32}$", re.IGNORECASE),
        modes=[HashInfo(name="Django(MD5)", hashcat=None, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^\{PKCS5S2\}[a-z0-9\/+]{64}$", re.IGNORECASE),
        modes=[
            HashInfo(name="PBKDF2(Atlassian)", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^md5[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(name="PostgreSQL MD5", hashcat=None, john=None, extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^\([a-z0-9\/+]{49}\)$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Lotus Notes/Domino 8", hashcat=9100, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^SCRYPT:[0-9]{1,}:[0-9]{1}:[0-9]{1}:[a-z0-9:\/+=]{1,}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="scrypt",
                hashcat=8900,
                john=None,
                extended=False,
                description="Used in Dogecoin and Litecoin.",
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$8\$[a-z0-9\/.]{14}\$[a-z0-9\/.]{43}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Cisco Type 8", hashcat=9200, john="cisco8", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$9\$[a-z0-9\/.]{14}\$[a-z0-9\/.]{43}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Cisco Type 9", hashcat=9300, john="cisco9", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$office\$\*2007\*[0-9]{2}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{40}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Microsoft Office 2007",
                hashcat=9400,
                john="office",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$office\$\*2010\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Microsoft Office 2010", hashcat=9500, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$office\$\*2013\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="Microsoft Office 2013", hashcat=9600, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$fde\$[0-9]{2}\$[a-f0-9]{32}\$[0-9]{2}\$[a-f0-9]{32}\$[a-f0-9]{3072}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name=u"Android FDE ≤ 4.3", hashcat=8800, john="fde", extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"\$krb5tgs\$23\$\*[^*]*\*\$[a-f0-9]{32}\$[a-f0-9]{64,40960}",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name=u"Kerberos 5 TGS-REP etype 23",
                hashcat=13100,
                john="krb5tgs",
                extended=False,
                description="Used in Windows Active Directory.",
            ),
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$oldoffice\$[01]\*[a-f0-9]{32}\*[a-f0-9]{32}\*[a-f0-9]{32}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name=u"Microsoft Office ≤ 2003 (MD5+RC4)",
                hashcat=9700,
                john="oldoffice",
                extended=False,
            ),
            HashInfo(
                name=u"Microsoft Office ≤ 2003 (MD5+RC4) collider-mode #1",
                hashcat=9710,
                john="oldoffice",
                extended=False,
            ),
            HashInfo(
                name=u"Microsoft Office ≤ 2003 (MD5+RC4) collider-mode #2",
                hashcat=9720,
                john="oldoffice",
                extended=False,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$oldoffice\$[34]\*[a-f0-9]{32}\*[a-f0-9]{32}\*[a-f0-9]{40}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name=u"Microsoft Office ≤ 2003 (SHA1+RC4)",
                hashcat=9800,
                john=None,
                extended=False,
            ),
            HashInfo(
                name=u"Microsoft Office ≤ 2003 (SHA1+RC4) collider-mode #1",
                hashcat=9810,
                john=None,
                extended=False,
            ),
            HashInfo(
                name=u"Microsoft Office ≤ 2003 (SHA1+RC4) collider-mode #2",
                hashcat=9820,
                john=None,
                extended=False,
            ),
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$radmin2\$)?[a-f0-9]{32}$", re.IGNORECASE),
        modes=[
            HashInfo(name="RAdmin v2.x", hashcat=9900, john="radmin", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^{x-issha,\s[0-9]{4}}[a-z0-9\/+=]+$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="SAP CODVN H (PWDSALTEDHASH) iSSHA-1",
                hashcat=10300,
                john="saph",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$cram_md5\$[a-z0-9\/+=-]+\$[a-z0-9\/+=-]{52}$", re.IGNORECASE
        ),
        modes=[HashInfo(name="CRAM-MD5", hashcat=10200, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{16}:2:4:[a-f0-9]{32}$", re.IGNORECASE),
        modes=[HashInfo(name="SipHash", hashcat=10100, john=None, extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^[a-f0-9]{4,}$", re.IGNORECASE),
        modes=[HashInfo(name="Cisco Type 7", hashcat=None, john=None, extended=True)],
    ),
    Prototype(
        regex=re.compile(r"^[a-z0-9\/.]{13,}$", re.IGNORECASE),
        modes=[HashInfo(name="BigCrypt", hashcat=None, john="bigcrypt", extended=True)],
    ),
    Prototype(
        regex=re.compile(r"^(\$cisco4\$)?[a-z0-9\/.]{43}$", re.IGNORECASE),
        modes=[
            HashInfo(name="Cisco Type 4", hashcat=None, john="cisco4", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^bcrypt_sha256\$\$(2[axy]|2)\$[0-9]+\$[a-z0-9\/.]{53}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="Django(bcrypt-SHA256)", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$postgres\$.[^\*]+[*:][a-f0-9]{1,32}[*:][a-f0-9]{32}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PostgreSQL Challenge-Response Authentication (MD5)",
                hashcat=11100,
                john="postgres",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$siemens-s7\$[0-9]{1}\$[a-f0-9]{40}\$[a-f0-9]{40}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(name="Siemens-S7", hashcat=None, john="siemens-s7", extended=False)
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$pst\$)?[a-f0-9]{8}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Microsoft Outlook PST", hashcat=None, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^sha256[:$][0-9]+[:$][a-z0-9\/+]+[:$][a-z0-9\/+]{32,128}$", re.IGNORECASE
        ),
        modes=[
            HashInfo(
                name="PBKDF2-HMAC-SHA256(PHP)", hashcat=10900, john=None, extended=False
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^(\$dahua\$)?[a-z0-9]{8}$", re.IGNORECASE),
        modes=[HashInfo(name="Dahua", hashcat=None, john="dahua", extended=False)],
    ),
    Prototype(
        regex=re.compile(r"^\$mysqlna\$[a-f0-9]{40}[:*][a-f0-9]{40}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="MySQL Challenge-Response Authentication (SHA1)",
                hashcat=11200,
                john=None,
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(
            r"^\$pdf\$[24]\*[34]\*128\*[0-9-]{1,5}\*1\*(16|32)\*[a-f0-9]{32,64}\*32\*[a-f0-9]{64}\*(8|16|32)\*[a-f0-9]{16,64}$",
            re.IGNORECASE,
        ),
        modes=[
            HashInfo(
                name="PDF 1.4 - 1.6 (Acrobat 5 - 8)",
                hashcat=10500,
                john="pdf",
                extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5asrep\$23\$[^:]+:[a-f0-9]{32,32}\$[a-f0-9]{64,40960}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5 AS-REP etype 23",
                hashcat=18200,
                john="krb5pa-sha1",
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5tgs\$17\$[^$]{1,512}\$[^$]{1,512}\$[^$]{1,4}?\$?[a-f0-9]{1,32}\$[a-f0-9]{64,40960}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5 TGS-REP etype 17 (AES128-CTS-HMAC-SHA1-96)",
                hashcat=19600,
                john=None,
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5tgs\$18\$[^$]{1,512}\$[^$]{1,512}\$[^$]{1,4}?\$?[a-f0-9]{1,32}\$[a-f0-9]{64,40960}", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5 TGS-REP etype 18 (AES256-CTS-HMAC-SHA1-96)",
                hashcat=19700,
                john=None,
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5pa\$17\$[^$]{1,512}\$[^$]{1,512}\$[a-f0-9]{104,112}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5, etype 17, Pre-Auth",
                hashcat=19800,
                john=None,
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5pa\$17\$[^$]{1,512}\$[^$]{1,512}\$[^$]{0,512}\$[a-f0-9]{104,112}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5, etype 17, Pre-Auth (with salt)",
                hashcat=None,
                john="krb5pa-sha1",
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5pa\$18\$[^$]{1,512}\$[^$]{1,512}\$[^$]{0,512}\$[a-f0-9]{104,112}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5, etype 18, Pre-Auth (with salt)",
                hashcat=None,
                john="krb5pa-sha1",
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$krb5pa\$18\$[^$]{1,512}\$[^$]{1,512}\$[a-f0-9]{104,112}$", re.IGNORECASE),
        modes=[
            HashInfo(
                name="Kerberos 5, etype 18, Pre-Auth",
                hashcat=19900,
                john=None,
                extended=False,
                description="Used for Windows Active Directory"
                )
        ],
    ),
    Prototype(
    regex=re.compile(r"\$bitcoin\$[0-9]{2,4}\$[a-fA-F0-9$]{250,350}", re.IGNORECASE),
    modes=[
        HashInfo(
            name="Bitcoin / Litecoin",
            hashcat=11300,
            john="bitcoin",
            extended=False,
            description="Use Bitcoin2John.py to extract the hash for cracking."
            )
        ],
    ),
    Prototype(
    regex=re.compile(r"\$ethereum\$[a-z0-9*]{150,250}", re.IGNORECASE),
    modes=[
        HashInfo(
            name="Ethereum Wallet, PBKDF2-HMAC-SHA256",
            hashcat=15600,
            john="ethereum-opencl",
            extended=False,
            description="Use ethereum2john.py to crack."
            ),
        HashInfo(
            name="Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256",
            hashcat=16300,
            john="ethereum-presale-opencl",
            extended=False,
            description="Use ethereum2john.py to crack."
        )
        ],
    ),
    Prototype(
    regex=re.compile(r"\$monero\$(0)\*[a-f0-9]{32,3196}", re.IGNORECASE),
    modes=[
        HashInfo(
            name="Monero",
            hashcat=None,
            john="monero",
            extended=False,
            description="Use monero2john.py to crack."
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$electrum\$[1-3]\*[a-f0-9]{32,32}\*[a-f0-9]{32,32}$", re.IGNORECASE),
        modes=[
        HashInfo(
            name="Electrum Wallet (Salt-Type 1-3)",
            hashcat=16600,
            john="electrum",
            extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$electrum\$4\*[a-f0-9]{1,66}\*[a-f0-9]{128,32768}\*[a-f0-9]{64,64}$", re.IGNORECASE),
        modes=[
        HashInfo(
            name="Electrum Wallet (Salt-Type 4)",
            hashcat=21700,
            john="electrum",
            extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"^\$electrum\$5\*[a-f0-9]{66,66}\*[a-f0-9]{2048,2048}\*[a-f0-9]{64,64}$", re.IGNORECASE),
        modes=[
        HashInfo(
            name="Electrum Wallet (Salt-Type 5)",
            hashcat=21800,
            john="electrum",
            extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"\$ab\$[0-9]{1}\*[0-9]{1}\*[0-9]{1,6}\*[a-f0-9]{128}\*[a-f0-9]{128}\*[a-f0-9]{32}\*[a-f0-9]{192}", re.IGNORECASE),
        modes=[
        HashInfo(
            name="Android Backup",
            hashcat=18900,
            john="androidbackup",
            extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"\$zip2\$\*[0-9]{1}\*[0-9]{1}\*[0-9]{1}\*[a-f0-9]{16,32}\*[a-f0-9]{1,6}\*[a-f0-9]{1,6}\*[a-f0-9]{0,16384}\*[a-f0-9]{20}\*\$\/zip2\$", re.IGNORECASE),
        modes=[
        HashInfo(
            name="WinZip",
            hashcat=13600,
            john="ZIP",
            extended=False,
            )
        ],
    ),
    Prototype(
        regex=re.compile(r"\$itunes_backup\$\*[0-9]{1,2}\*[a-f0-9]{80}\*[0-9]{1,6}\*[a-f0-9]{40}\*[0-9]{0,10}\*[a-f0-9]{0,40}", re.IGNORECASE),
        modes=[
        HashInfo(
            name="iTunes backup >= 10.0 11",
            hashcat=14800,
            john="itunes-backup",
            extended=False,
            )
        ],
    ),
]