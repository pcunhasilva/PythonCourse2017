# Create the following functions: with exceptions, errors, and such
# Create a test for those functions

#Hello. to HELLO!
def shout(txt):
    try:
        txt = txt.replace(".", "!")
        txt = txt.upper()
        if txt[-1] != "!": txt = txt + "!"
    except:
        txt = str(txt)+ "!"
    finally:
        return txt

# Name to emaN
def reverse(txt):
    try:
        if len(txt) > 1: raise RuntimeError("Please insert only one word.")
    except TypeError:
        txt = str(txt)
    except AttributeError:
        txt = str(txt)
    finally:
        txt = txt[::-1]
        return txt


# Hello world! to !world Hello
def reversewords(txt):
    try:
        txt = str(txt)
        if len(txt.split()) == 1:
            raise RuntimeError("Please insert more than one word.")
    finally:
        return " ".join(txt.split()[ : : -1])

# Hello world! to !dlrow olleH
def reversewordletters(txt):
    try:
        txt = str(txt)
        if len(txt.split()) == 1:
            raise RuntimeError("Please insert more than one word.")
    finally:
        txt = txt[::-1]
        return txt

# # Take a word and transfer to pig latin
