from ast import Pass, main
import os
import time
from setuptools import setup


banner = """
       _         ___ _             __        ___ _   _  
 |\ | / \ |\ |    | |_)  /\  |\ | (_  |   /\  | / \ |_) 
 | \| \_/ | \|    | | \ /--\ | \| __) |_ /--\ | \_/ | \  a NONDOS 2 Project
 Beta (Only Words) 
 Write NONTRANSLATOR.words to see all words

 The language of the Words you type is detected automatically.                                                    
"""

print(banner)
print("""
Languages ---> English, Turkish, German, French
""")

yourtext = input("Write Text To Translate ---> ")

if yourtext == "NONTRANSLATOR.words":
      print("""
English Words ---> Why, Hello
Turkish Words ---> Neden, Merhaba
German Words ---> Warum, Hallo
French Words ---> Pourquoi, Bonjour""")
      time.sleep(9999)

if yourtext == "Why":
      print("""
English ---> Why 
Turkish ---> Neden
German ---> Warum
French ---> Pourquoi
""")
      time.sleep(9999)

if yourtext == "Neden":
      print("""
English ---> Why 
Turkish ---> Neden
German ---> Warum
French ---> Pourquoi
""")
      time.sleep(9999)

if yourtext == "Warum":
      print("""
English ---> Why 
Turkish ---> Neden
German ---> Warum
French ---> Pourquoi
""")
      time.sleep(9999)

if yourtext == "Pourquoi":
      print("""
English ---> Why 
Turkish ---> Neden
German ---> Warum
French ---> Pourquoi
""")
      time.sleep(9999)

if yourtext == "Hello":
      print("""
English ---> Hello
Turkish ---> Merhaba
German ---> Hallo
French ---> Bonjour
""")
      time.sleep(9999)

if yourtext == "Merhaba":
      print("""
English ---> Hello 
Turkish ---> Merhaba
German ---> Hallo
French ---> Bonjour
""")
      time.sleep(9999)

if yourtext == "Hallo":
      print("""
English ---> Hello 
Turkish ---> Merhaba
German ---> Hallo
French ---> Bonjour
""")
      time.sleep(9999)

if yourtext == "Bonjour":
      print("""
English ---> Hello 
Turkish ---> Merhaba
German ---> Hallo
French ---> Bonjour
""")
      time.sleep(9999)




