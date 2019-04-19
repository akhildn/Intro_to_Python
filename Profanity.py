import urllib


def read_text():
    quotes = open("hello.txt", "r")
    contents_of_file = quotes.read()
    check_profanity(contents_of_file)


# WDYL is down doesn't work
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
