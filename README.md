<p align="center">

<img src="logo.gif">
</p>


# Name-That-Hash
Don't know what type of hash it is? Name That Hash will name that hash type!

# Features
* Reports most popular hashes first. No more Watt pad hash when MD5 is an option!
* Extremely fast.
* Easy to add more hashes to.

# Name-That-Hash vs HashID vs Hash-Identifier

| **Features** | Name-That-Hash | HashID | Hash-Identifier |
| ---- | ---- | ---- | ---- |
| **Last updated** | 13/01/2021 | 17/03/2015 | 30/09/2011 |


# ToDo

- [ ] Implement most popular first, so MD5 appears before Watt pad
- [ ] Remove logic of hashing from one big file, break it down into modules
- [ ] Use click + API keys


```
{'5d41402abc4b2a76b9719d911017c592': [{'name': 'MD5', 'hashcat': 0, 'john': 'raw-md5', 'extended': False, 'description': None}, {'name': 'NTLM', 'hashcat': 1000, 'john': 'nt', 'extended': False, 'descri
ption': 'Often used in Windows Active Directory.'}, {'name': 'Double MD5', 'hashcat': 2600, 'john': None, 'extended': False, 'description': None}, {'name': 'LM', 'hashcat': 3000, 'john': 'lm', 'extended
': False, 'description': None}, {'name': 'RIPEMD-128', 'hashcat': None, 'john': 'ripemd-128', 'extended': False, 'description': None}, {'name': 'Haval-128', 'hashcat': None, 'john': 'haval-128-4', 'exte
nded': False, 'description': None}, {'name': 'Tiger-128', 'hashcat': None, 'john': None, 'extended': False, 'description': None}, {'name': 'Skein-256(128)', 'hashcat': None, 'john': None, 'extended': Fa
lse, 'description': None}, {'name': 'Skein-512(128)', 'hashcat': None, 'john': None, 'extended': False, 'description': None}, {'name': 'Lotus Notes/Domino 5', 'hashcat': 8600, 'john': 'lotus5', 'extende
d': False, 'description': None}, {'name': 'Skype', 'hashcat': 23, 'john': None, 'extended': False, 'description': None}, {'name': 'ZipMonster', 'hashcat': None, 'john': None, 'extended': True, 'descript
ion': None}, {'name': 'PrestaShop', 'hashcat': 11000, 'john': None, 'extended': True, 'description': None}, {'name': 'md5(md5(md5($pass)))', 'hashcat': 3500, 'john': None, 'extended': True, 'description
': None}, {'name': 'md5(strtoupper(md5($pass)))', 'hashcat': 4300, 'john': None, 'extended': True, 'description': None}, {'name': 'md5(sha1($pass))', 'hashcat': 4400, 'john': None, 'extended': True, 'de
scription': None}, {'name': 'md5($pass.$salt)', 'hashcat': 10, 'john': None, 'extended': True, 'description': None}, {'name': 'md5($salt.$pass)', 'hashcat': 20, 'john': None, 'extended': True, 'descript
ion': None}, {'name': 'md5(unicode($pass).$salt)', 'hashcat': 30, 'john': None, 'extended': True, 'description': None}, {'name': 'md5($salt.unicode($pass))', 'hashcat': 40, 'john': None, 'extended': Tru
e, 'description': None}, {'name': 'HMAC-MD5 (key = $pass)', 'hashcat': 50, 'john': 'hmac-md5', 'extended': True, 'description': None}, {'name': 'HMAC-MD5 (key = $salt)', 'hashcat': 60, 'john': 'hmac-md5
', 'extended': True, 'description': None}, {'name': 'md5(md5($salt).$pass)', 'hashcat': 3610, 'john': None, 'extended': True, 'description': None}, {'name': 'md5($salt.md5($pass))', 'hashcat': 3710, 'jo
hn': None, 'extended': True, 'description': None}, {'name': 'md5($pass.md5($salt))', 'hashcat': 3720, 'john': None, 'extended': True, 'description': None}, {'name': 'md5($salt.$pass.$salt)', 'hashcat':
3810, 'john': None, 'extended': True, 'description': None}, {'name': 'md5(md5($pass).md5($salt))', 'hashcat': 3910, 'john': None, 'extended': True, 'description': None}, {'name': 'md5($salt.md5($salt.$p
ass))', 'hashcat': 4010, 'john': None, 'extended': True, 'description': None}, {'name': 'md5($salt.md5($pass.$salt))', 'hashcat': 4110, 'john': None, 'extended': True, 'description': None}, {'name': 'md
5($username.0.$pass)', 'hashcat': 4210, 'john': None, 'extended': True, 'description': None}, {'name': 'MD2', 'hashcat': None, 'john': 'md2', 'extended': False, 'description': None}, {'name': 'Snefru-12
8', 'hashcat': None, 'john': 'snefru-128', 'extended': False, 'description': None}, {'name': 'Domain Cached Credentials 2', 'hashcat': 2100, 'john': 'mscach2', 'extended': False, 'description': None}, {
'name': 'DNSSEC(NSEC3)', 'hashcat': 8300, 'john': None, 'extended': False, 'description': None}, {'name': 'RAdmin v2.x', 'hashcat': 9900, 'john': 'radmin', 'extended': False, 'description': None}, {'nam
e': 'Cisco Type 7', 'hashcat': None, 'john': None, 'extended': True, 'description': None}, {'name': 'BigCrypt', 'hashcat': None, 'john': 'bigcrypt', 'extended': True, 'description': None}]}
```
