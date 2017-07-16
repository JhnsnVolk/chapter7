import os


def run(**args):
    print "[*] In dirlisten module."
    files = os.listdir(".")

    return str(files)

