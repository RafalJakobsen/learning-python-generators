from time import time
from contextlib import contextmanger

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"

@contextmanger
def new_log_file(name):
    try:
        logname = name
        f = open(logname, "w")
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print("logfile created")
        f.close()

with new_log_file("logfile") as file:
    file.write("this is the body")

