# NTLM Generator - Python3

A short python script to generate an NTLM hash for password testing. 
Useful for making sure that the NTLM generation process stays local to your machine for increased security.

## Use

- Call the script `./generate_ntlm.py` (for Linux). Here is a link to installing Python for a Windows or MacOS computer. https://www.python.org/downloads/
- It will prompt you for a string of characters (password) to convert to an NTLM hash.
- Profit.

## Troubleshooting

If running on an Ubuntu machine you may need to add these three lines to your /etc/ssl/openssl.cnf to 're-enable' md4 to hashlib.

`[provider_sect]
default = default_sect
legacy = legacy_sect`

`[default_sect]
activate = 1`

`[legacy_sect]
activate = 1`
