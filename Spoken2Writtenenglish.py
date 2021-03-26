# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 03:09:08 2021

@author: Wazir
"""

def conversion_rules():
    # Defining a dictionary of dictionary with keys reprsenting the type of conversion
    rules = {"General":{                
                         "zero":0,
                          "one":1,
                          "two":2,
                          "three":3,
                          "four":4,
                          "five":5,
                          "six":6,
                          "seven":7,
                          "eight":8,
                          "nine":9,
                          "ten":10,
                          "eleven":11,
                          "twelve":12,
                          "thirteen":13,
                          "fourteen":14,
                          "fifteen":15,
                          "sixteen":16,
                          "seventeen":17,
                          "eighteen":18,
                          "nineteen":19,
                          "twenty":20,
                          "twenty one":21,
                          "twenty two":22,
                          "twenty three":23,
                          "twenty four":24,
                          "twenty five":25,
                          "twenty six":26,
                          "twenty seven":27,
                          "twenty eight":28,
                          "twenty nine":29,
                          "thirty":30,
                          "thrity one":31,
                          "thirty two":32,
                          "thirty three":33,
                          "thirty four":34,
                          "thirty five":35,
                          "thirty six":36,
                          "thirty seven":37,
                          "thirty eight":38,
                          "thirty nine":39,
                          "fourty":40,
                          "fourty one":41,
                          "fourty two":42,
                          "fourty three":43,
                          "fourty four":44,
                          "fourty five":45,
                          "fourty six":46,
                          "fourty seven":47,
                          "fourty eight":48,
                          "fourty nine":49,
                          "fifty":50,
                          "fifty one":51,
                          "fifty two":52,
                          "fifty three":53,
                          "fifty four":54,
                          "fifty five":55,
                          "fifty six":56,
                          "fifty seven":57,
                          "fifty eight":58,
                          "fifty nine":59,
                          "sixty":60,
                          "sixty one":61,
                          "sixty two":62,
                          "sixty three":63,
                          "sixty four":64,
                          "sixty five":65,
                          "sixty six":66,
                          "sixty seven":67,
                          "sixty eight":68,
                          "sixty nine":69,
                          "seventy":70,
                          "seventy one":71,
                          "seventy two":72,
                          "seventy three":73,
                          "seventy four":74,
                          "seventy five":75,
                          "seventy six":76,
                          "seventy seven":77,
                          "seventy eight":78,
                          "seventy nine":79,
                          "eighty":80,
                          "eighty one":81,
                          "eighty two":82,
                          "eighty three":83,
                          "eighty four":84,
                          "eighty five":85,
                          "eighty six":86,
                          "eighty seven":87,
                          "eighty eight":88,
                          "eighty nine":89,
                          "ninety":90,
                          "ninety one":91,
                          "ninety two":92,
                          "ninety three":93,
                          "ninety four":94,
                          "ninety five":95,
                          "ninety six":96,
                          "ninety seven":97,
                          "ninety eight":98,
                          "ninety nine":99,
                          "hundred":100,
                          "C M":"CM",
                          "P M":"PM",
                          "D M":"DM",
                          "A M":"AM"
                        },
             "Tuples": {
                          "single":1,
                          "double":2,
                          "triple":3,
                          "quadruple":4,
                          "quintuple":5,
                          "sextuple":6,
                          "septuple":7,
                          "octuple":8,
                          "nonuple":9,
                          "decuple":10
                        }
          }
    return rules

# Checking if the word starts with a comma and/or ends with a full stop to extract the word from that
# excluding the comma and the full-stop.

def word_check(word):
    first_char = ""
    last_char = ""
    if len(word)>1:
        if word[-1] == "," or word[-1] == ".":
            last_char = word[-1]
            word = word[:-1]
        if word[0] == "," or word[0] == ".":
            first_char = word[0]
            word = word[1:]
        elif word[0] == "," and word[-1] == ".":
            first_char = word[0]
            word = word[1:-1]
            last_char = word[-1]
    return first_char,word,last_char

class conversion:
    
    def __init__(self):
        
        self.rules = conversion_rules()
        self.inp_para = ""        
        
    def convert(self, inp_para):
        
        # Taking the input from the user
        self.inp_para = inp_para
        self.out_para = ""
        
        if self.inp_para == "":
            raise ValueError("Please enter something")
        
        # Splitting the sentences into words on whitespaces
        words_of_inp_para = self.inp_para.split()
        i=0
        while i < len(words_of_inp_para):
            # Getting the first_char, word and last_char of the ith word
            first_char, word, last_char = word_check(words_of_inp_para[i])
            
            if i+1 != len(words_of_inp_para):
                # Getting the first_char, word and last_char of the (i+1)th word
                first_char_next, next_word, last_char_next = word_check(words_of_inp_para[i+1])
                # When we encounter two dollars or three dollars
                if word.lower() in self.rules["General"].keys() and (next_word.lower() == "dollars" or next_word.lower() == "dollar"):
                    self.out_para += " " + first_char + "$" + str(self.rules["General"][word.lower()]) + last_char
                    i+=2
                # When we encounter triple A or triple B
                elif word.lower() in self.rules["Tuples"].keys() and (len(next_word.lower()) == 1):
                    self.out_para += " " + first_char_next + (next_word*self.rules["Tuples"][word.lower()]) + last_char_next
                    i+=2
                # When we encounter words like A M or P M or C M
                elif (word + " " + next_word) in self.rules["General"].keys():
                    self.out_para += " " + first_char + self.rules["General"][word+" "+next_word] + last_char_next
                    i+=2
                # When we encounter words like two, three, four
                elif word.lower() in self.rules["General"].keys():
                    self.out_para += " " + first_char + str(self.rules["General"][word.lower()]) + last_char
                    i+=1
                else:
                    self.out_para += " " + words_of_inp_para[i]
                    i+=1
            else:
                self.out_para += " " + words_of_inp_para[i]
                i+=1
                
        print("The input paragraph of spoken english was \n {}".format(self.inp_para))
        print("The converted paragraph of written english is \n {}".format(self.out_para))
