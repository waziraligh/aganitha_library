# aganitha_library
Reusable Library for conversion of spoken english to written english

The .py file is Spoken2Writtenenglish.py which has the class Conversion which could be imported in any independent program and 
can be used for the desired purpose by passing the input paragraph from the program from which the class is called. The class 
conversion has the function convert which takes the input paragraph from the calling program and converts it into written english before
printing it. This py file can be imported in python3 environment using import command and the class conversion can be imported 
using the import Spoken2Writtenenglish.conversion command.

For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

E.g:-

#Put the Spoken2Writtenenglish.py in the same folder in which you are writing the program ABC.py, say.

#Import the class convert using the following
from Spoken2Writtenenglish import conversion

#Create an object of the class conversion
obj = conversion()

#Take the input paragraph of spoken english from the user
inp_para = input("Please enter your paragraph of SPoken English:\n\n")

#Call the method convert of the instance of the class conversion
obj.convert(inp_para)
