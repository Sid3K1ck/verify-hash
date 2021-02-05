#!/usr/bin/env python3
""" verifyHash.py
----------------------------------------------------------------------------------------------------
@Program: Verify Hash of file
@Author:  Jamie R. Dayton
@Version: 1.21.02.05.001
----------------------------------------------------------------------------------------------------
@Summary: Run get-filehash on a file and compare the required value of the respective checksum type.
----------------------------------------------------------------------------------------------------
"""

# Imports
import os
import hashlib


fh = input("Enter file path to check >> ")
fd = ""
fn = ""

if os.path.isabs(fh):
    w = os.path.abspath(fh)
    fd = os.path.dirname(w)
    fn = os.path.basename(w)
    os.chdir(fd)

else:
    if os.path.exists(fh):
        fd = os.getcwd()
        fn = fh
    else:
        print("The file is not located in this directory.")
        exit()

ck = input("What is the checksum type >> ")
val = input("What is value to compare from download site >> ")

try:
    with open(fn, "rb") as f:
        b = f.read()
        if ck.lower() == 'sha256':
            h = hashlib.sha256(b).hexdigest()
        elif ck.lower() == 'md5':
            h = hashlib.md5(b).hexdigest()
        elif ck.lower() == 'sha1':
            h = hashlib.sha1(b).hexdigest()
        elif ck.lower() == 'sha224':
            h = hashlib.sha224(b).hexdigest()
        elif ck.lower() == 'sha384':
            h = hashlib.sha384(b).hexdigest()
        elif ck.lower() == 'sha512':
            h = hashlib.sha512(b).hexdigest()
        else:
            print("{} is not a supported checksum type, please try another".format(ck))
            exit()

    if h.lower() == val.lower():
        print("Congratulations, both hash values match.")
    else:
        print("DANGER! do not use this download, remove it from your system.")

except ValueError as e:
    print(e)
