#!/usr/bin/python3
from urllib.parse import unquote
from os import environ
from sys import exit

if not unquote(environ["QUERY_STRING"]):
    print("10 Please enter your name",end="\r\n")
    exit()
name = unquote(environ["QUERY_STRING"])

print("20 text/gemini",end="\r\n")
print(f"Hello {name}!")
