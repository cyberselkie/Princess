import os
import random
import sys

import requests
from PIL import Image, ImageDraw

#   Made by TheOddFireFox/Theo/0xr4t
#
#   Made for a game i want to run and shared since its neat i think
#
#   feel free to improve but credit me

### DICTIONARIES
spell_buffer = "#':'#"

spl_nm_dict = {
    "A": [255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 255, 0],
    "B": [255, 0, 0, 255, 255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 0, 0],
    "C": [255, 255, 0, 0, 255, 0, 255, 255, 255, 0, 255, 255, 255, 255, 0, 0],
    "D": [255, 0, 0, 255, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 255],
    "E": [255, 0, 0, 0, 255, 0, 0, 255, 255, 0, 255, 255, 255, 0, 0, 0],
    "F": [255, 0, 0, 0, 255, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255],
    "G": [255, 255, 0, 0, 255, 0, 255, 255, 255, 0, 255, 0, 255, 255, 0, 0],
    "H": [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 255, 0],
    "I": [255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 0, 0],
    "J": [255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 0, 255],
    "K": [255, 0, 255, 0, 255, 0, 0, 255, 255, 0, 255, 0, 255, 0, 255, 0],
    "L": [255, 0, 255, 255, 255, 0, 255, 255, 255, 0, 255, 255, 255, 0, 0, 0],
    "M": [255, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 255, 0],
    "N": [255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0],
    "O": [255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 255, 0, 255, 255, 0, 255],
    "P": [255, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 255, 255, 0, 255, 255],
    "Q": [255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 255, 0, 255, 255, 0, 0],
    "R": [255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255, 0, 255, 0],
    "S": [255, 255, 0, 0, 255, 0, 255, 255, 255, 255, 0, 0, 255, 0, 0, 255],
    "T": [255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 255, 0, 255],
    "U": [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0],
    "V": [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 255, 0, 255],
    "W": [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0],
    "X": [255, 0, 255, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 255, 0],
    "Y": [255, 0, 255, 0, 255, 0, 255, 0, 255, 255, 0, 255, 255, 255, 0, 255],
    "Z": [255, 0, 0, 0, 255, 255, 255, 0, 255, 0, 0, 255, 255, 0, 0, 0],
    "`": [255, 0, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    ".": [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 255],
    '"': [255, 0, 255, 0, 255, 0, 255, 0, 255, 255, 255, 0, 255, 255, 255, 255],
    ":": [255, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 255, 255],
    ";": [255, 0, 255, 255, 255, 255, 255, 255, 255, 0, 255, 255, 255, 0, 255, 255],
    "!": [255, 0, 255, 255, 255, 0, 255, 255, 255, 255, 255, 255, 255, 0, 255, 255],
    "^": [255, 255, 0, 255, 255, 0, 255, 0, 255, 255, 255, 255, 255, 255, 255, 255],
    "/": [255, 255, 255, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 255, 255],
    "(": [255, 255, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 255, 255, 0, 255],
    ")": [255, 0, 255, 255, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 255, 255],
    "_": [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0],
    "-": [255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 255, 255, 255, 255],
    "+": [255, 255, 255, 255, 255, 255, 0, 255, 255, 0, 0, 0, 255, 255, 0, 255],
    "?": [255, 0, 0, 0, 255, 255, 255, 0, 255, 255, 255, 255, 255, 255, 0, 255],
    "*": [255, 0, 255, 0, 255, 255, 0, 255, 255, 0, 255, 0, 255, 255, 255, 255],
    "[": [255, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 255, 0, 0, 255],
    "]": [255, 0, 0, 255, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 0, 255],
    "{": [255, 0, 0, 255, 0, 0, 255, 255, 255, 0, 255, 255, 255, 0, 0, 255],
    "}": [255, 0, 0, 255, 255, 255, 0, 0, 255, 255, 0, 255, 255, 0, 0, 255],
    ",": [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 255, 255, 0, 255, 255],
    "'": [255, 255, 0, 255, 255, 255, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    "<": [255, 255, 255, 255, 255, 255, 0, 255, 255, 0, 255, 255, 255, 255, 0, 255],
    ">": [255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 0, 255, 255, 0, 255, 255],
    "=": [255, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0, 255, 255, 255, 255],
    "1": [255, 255, 0, 255, 255, 0, 0, 255, 255, 255, 0, 255, 255, 0, 0, 0],
    "2": [255, 0, 0, 0, 255, 255, 255, 0, 255, 255, 0, 255, 255, 0, 0, 0],
    "3": [255, 0, 0, 0, 255, 255, 0, 0, 255, 255, 255, 0, 255, 0, 0, 0],
    "4": [255, 0, 255, 0, 255, 0, 0, 0, 255, 255, 255, 0, 255, 255, 255, 0],
    "5": [255, 0, 0, 0, 255, 0, 255, 255, 255, 255, 0, 0, 255, 0, 0, 0],
    "6": [255, 255, 0, 0, 255, 0, 255, 255, 255, 0, 0, 0, 255, 0, 0, 0],
    "7": [255, 0, 0, 0, 255, 255, 255, 0, 255, 255, 0, 255, 255, 0, 255, 255],
    "8": [255, 0, 0, 0, 255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 0],
    "9": [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0, 255, 0, 0, 255],
    "0": [255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0],
    "#": [255, 255, 255, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 255, 255, 255],
    "&": [0, 0, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0],
    " ": [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
}

spl_ct_dict = {
    "1": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        0,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "2": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        0,
        0,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "3": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "4": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "5": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "6": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "7": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        0,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "8": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "9": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "0": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        255,
        0,
        0,
        255,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    " ": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
}

spl_sk_dict = {
    "Magic": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        0,
        0,
        255,
        0,
        0,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "Dreams": [
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        255,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        255,
        255,
        255,
        0,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
    ],
    "Misc.": [
        255,
        255,
        0,
        0,
        0,
        0,
        255,
        255,
        255,
        0,
        0,
        0,
        0,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        255,
        255,
        0,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        255,
        0,
        0,
        255,
        255,
        255,
    ],
}


### FUNCTIONS ###
def help_message():
    print("[i] You need to supply arguments to the script.")
    print("[i] '-t <file_path>' to translate spell card into text")
    print("[i] '-c \"<spell_name>|<spell_effects>|<cost>|<skill>\"' to create a spell card from text")
    print("[i]      <spell_name> limited to 36 characters")
    print("[i]      <spell_effects> limited to 128 characters")
    print("[i]      <cost> limited to 3 digits")
    print("[i]      <skill> limited to Magic, Dreams, or Misc.")
    print("[i]      Invalid <skill> input will be Misc.")
    exit()


# creates a string of text from a spell card png
#
# @param file_path - a path to the spell card png
#
# @return spell_text - decoded text from spell card
def card_read_text(file_path):
    spell_text = ""

    spell_name = ""
    spell_desc = ""
    spell_cost = ""
    spell_skil = ""

    with Image.open(file_path, formats=["PNG", "JPEG"]) as sc:
        chnk_shft = 0
        col_shft = 0
        col_fix = 0

        if sc.size[0] > 64 or sc.size[1] > 96:
            sc = sc.resize((64, 96), resample=Image.Resampling.NEAREST)

        # NAME
        ltrs = [0, 0, 0, 0]
        # Iterate over the 2 columns and read the text from them
        i = 0
        while i < 9:
            # shift column and read properly
            if chnk_shft == 40 or (chnk_shft + 16 == 48 and col_fix == 0):
                col_shft += 8
                col_fix = 8
                chnk_shft = 0

            # Grab values for each quarter
            ltrs[0] = list(
                sc.crop((8 + col_shft, 16 + chnk_shft - col_fix, 12 + col_shft, 20 + chnk_shft - col_fix))
                .convert("1")
                .getdata()
            )
            ltrs[1] = list(
                sc.crop((12 + col_shft, 16 + chnk_shft - col_fix, 16 + col_shft, 20 + chnk_shft - col_fix))
                .convert("1")
                .getdata()
            )
            ltrs[2] = list(
                sc.crop((8 + col_shft, 20 + chnk_shft - col_fix, 12 + col_shft, 24 + chnk_shft - col_fix))
                .convert("1")
                .getdata()
            )
            ltrs[3] = list(
                sc.crop((12 + col_shft, 20 + chnk_shft - col_fix, 16 + col_shft, 24 + chnk_shft - col_fix))
                .convert("1")
                .getdata()
            )

            # Decode to a value from the list
            for ltr in ltrs:
                if ltr not in spl_nm_dict.values() or ltr == spl_nm_dict["&"] or ltr == spl_nm_dict["#"]:
                    spell_name += ""
                else:
                    spell_name += list(spl_nm_dict.keys())[list(spl_nm_dict.values()).index(ltr)]

            # Move iteration and chunk down
            chnk_shft += 8
            i += 1
        # WHILE END

        # COST + SKILL
        cost = [0, 0, 0]
        skill = []

        cost[0] = list(sc.crop((40, 8, 48, 16)).convert("1").getdata())
        cost[1] = list(sc.crop((40, 16, 48, 24)).convert("1").getdata())
        cost[2] = list(sc.crop((48, 16, 56, 24)).convert("1").getdata())
        skill = list(sc.crop((48, 8, 56, 16)).convert("1").getdata())

        # Decode to a value from the list
        for c in cost:
            if c not in spl_ct_dict.values():
                spell_cost += "#"
            else:
                spell_cost += list(spl_ct_dict.keys())[list(spl_ct_dict.values()).index(c)]

        # Decode to a value from the list
        if skill not in spl_sk_dict.values():
            spell_skil += "Misc."
        else:
            spell_skil += list(spl_sk_dict.keys())[list(spl_sk_dict.values()).index(skill)]

        # DESCRIPTION
        desc_sqr = [0, 0, 0, 0, 0, 0, 0, 0]

        chnk_shft = 0
        row_shft = 0

        # TOP AREA BEFORE THE REST
        i = 0
        while i < 4:
            if i == 2:
                chnk_shft = 0
                row_shft += 8

            for x in range(8):
                desc_sqr[x] = list(
                    sc.crop((24 + x + chnk_shft, 8 + row_shft, 25 + x + chnk_shft, 16 + row_shft))
                    .convert("1")
                    .getdata()
                )
                desc_sqr[x] = list(map(lambda d: "1" if d == 0 else "0", desc_sqr[x]))
                spell_desc += chr(int("".join(desc_sqr[x]), 2))

            chnk_shft += 8
            i += 1
        # WHILE END

        # THE REST
        chnk_shft = 0
        row_shft = 0

        i = 0
        while i < 12:
            if i % 4 == 0 and i != 0:
                chnk_shft = 0
                row_shft += 8

            for x in range(8):
                desc_sqr[x] = list(
                    sc.crop((24 + x + chnk_shft, 24 + row_shft, 25 + x + chnk_shft, 32 + row_shft))
                    .convert("1")
                    .getdata()
                )
                desc_sqr[x] = list(map(lambda d: "1" if d == 0 else "0", desc_sqr[x]))
                spell_desc += chr(int("".join(desc_sqr[x]), 2))

            chnk_shft += 8
            i += 1
        # WHILE END

        spell_text = "|".join([spell_name, spell_desc.split(spell_buffer)[0], spell_cost, spell_skil])

    return spell_text


# creates a png of a spell card from a string of text
#
# @param spell_text - a string detailing the properties of the spell like so
#                     <spell_name>:<spell_effects>:<cost>:<skill>
#
# @return sc - completed spell card
def card_create_spell(spell_text):
    sc = Image.new("RGB", (64, 96), (255, 255, 255))

    draw = ImageDraw.Draw(sc)
    draw.rectangle((6, 6, 57, 89), fill=None, outline=0)

    # Corner design
    draw.rectangle((8, 8, 15, 15), fill=None, outline=0)
    draw.rectangle((10, 10, 13, 13), fill=0, outline=0)

    # Process text
    if len(spell_text) > 4:
        spell_strings = spell_text.split("|")
    else:
        spell_strings = spell_text

    # NAME
    # Set all uppercase
    spell_name = spell_strings[0].upper()

    # buffer
    flip = 0
    while len(spell_name) < 36:
        if flip < 1:
            spell_name += "&"
            flip += 1
        elif flip < 3:
            spell_name += "#"
            flip += 1
        else:
            spell_name += "&"
            flip = 0

    # print(spell_name)

    # Draw spell name
    i = 0
    chnk_shft = 0
    col_shft = 0
    col_fix = 0
    while i < 9:
        ltr_chnk = spell_name[i * 4 : i * 4 + 4]

        # shift column and read properly
        if chnk_shft == 40 or (chnk_shft + 16 == 48 and col_fix == 0):
            col_shft += 8
            col_fix = 8
            chnk_shft = 0

        # Grab values for each quarter
        ltr1 = Image.new("1", (4, 4), 255)
        ltr1.putdata(spl_nm_dict.get(ltr_chnk[0]))
        ltr2 = Image.new("1", (4, 4), 255)
        ltr2.putdata(spl_nm_dict.get(ltr_chnk[1]))
        ltr3 = Image.new("1", (4, 4), 255)
        ltr3.putdata(spl_nm_dict.get(ltr_chnk[2]))
        ltr4 = Image.new("1", (4, 4), 255)
        ltr4.putdata(spl_nm_dict.get(ltr_chnk[3]))

        sc.paste(ltr1, (8 + col_shft, 16 + chnk_shft - col_fix))
        sc.paste(ltr2, (12 + col_shft, 16 + chnk_shft - col_fix))
        sc.paste(ltr3, (8 + col_shft, 20 + chnk_shft - col_fix))
        sc.paste(ltr4, (12 + col_shft, 20 + chnk_shft - col_fix))

        # Move iteration and chunk down
        chnk_shft += 8
        i += 1
    # WHILE END

    # Description
    # START DESC ENCODE
    spell_desc = spell_strings[1]

    # buffer
    spell_desc += spell_buffer
    random.seed()
    while len(spell_desc) < 128:
        spell_desc += str(random.randint(0, 9))

    # print(spell_desc)
    # TOP AREA BEFORE THE REST - 32 chars max
    chnk_shft = 0
    row_shft = 0
    for chunk in range(4):
        chnk_i = chunk * 8
        if chunk % 2 == 0 and chunk != 0:
            chnk_shft = 0
            row_shft += 8

        cur_chunk = spell_desc[chnk_i : chnk_i + 8]

        lti = 0
        for ltr in cur_chunk:
            bar = Image.new("1", (1, 8), 255)
            bar_data = list(bin(int.from_bytes(ltr.encode(), "big"))[2:])

            # because its a piece of shit and wont encode correctly
            # so manual buffer for later decoding
            while len(bar_data) < 8:
                bar_data.insert(0, "0")

            bar_data = list(map(lambda d: 0 if d == "1" else 255, bar_data))
            bar.putdata(bar_data)

            sc.paste(bar, (24 + lti + chnk_shft, 8 + row_shft, 25 + lti + chnk_shft, 16 + row_shft))
            lti += 1

        chnk_shft += 8

    # THE REST
    chnk_shft = 0
    row_shft = 0
    for chunk in range(12):
        chnk_i = chunk * 8 + 32
        if chunk % 4 == 0 and chunk != 0:
            chnk_shft = 0
            row_shft += 8

        cur_chunk = spell_desc[chnk_i : chnk_i + 8]

        lti = 0
        for ltr in cur_chunk:
            bar = Image.new("1", (1, 8), 255)
            bar_data = list("0" + bin(int.from_bytes(ltr.encode(), "big"))[2:])

            # because its a piece of shit and wont encode correctly
            # so manual buffer for later decoding
            while len(bar_data) < 8:
                bar_data.insert(0, "0")

            bar_data = list(map(lambda d: 0 if d == "1" else 255, bar_data))
            bar.putdata(bar_data)

            sc.paste(bar, (24 + lti + chnk_shft, 24 + row_shft, 25 + lti + chnk_shft, 32 + row_shft))
            lti += 1

        chnk_shft += 8
    # END DESC ENCODE

    # COST + SKILL
    spell_cost = list(spell_strings[2])
    while len(spell_cost) < 3:
        spell_cost.insert(0, "0")

    spell_skil = spell_strings[3]
    if spell_skil not in spl_sk_dict.keys():
        spell_skil = "Misc."

    dig1 = Image.new("1", (8, 8), 255)
    dig1.putdata(spl_ct_dict.get(spell_cost[0]))
    dig2 = Image.new("1", (8, 8), 255)
    dig2.putdata(spl_ct_dict.get(spell_cost[1]))
    dig3 = Image.new("1", (8, 8), 255)
    dig3.putdata(spl_ct_dict.get(spell_cost[2]))
    skil = Image.new("1", (8, 8), 255)
    skil.putdata(spl_sk_dict.get(spell_skil))

    sc.paste(dig1, (40, 8, 48, 16))
    sc.paste(dig2, (40, 16, 48, 24))
    sc.paste(dig3, (48, 16, 56, 24))
    sc.paste(skil, (48, 8, 56, 16))

    # Flip design
    sct = sc.crop((0, 0, 64, 48)).rotate(180)
    sc.paste(sct, (0, 48))

    # sc.show()
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/" + spell_strings[0].lower().replace(" ", "_")
    sc.save(format="PNG", fp=file_path + ".png")

    # BIGGER
    height, width = sc.size
    scb = sc.resize((height * 10, width * 10), resample=Image.Resampling.NEAREST)
    scb.save(format="PNG", fp=file_path + "x10.png")

    print("[+] SpellCodes saved to:\n[i] " + file_path)


def save_file(url, image_name):
    response = requests.get(url)
    with open(image_name, "wb") as file:
        file.write(response.content)
    return image_name


def delete_file(image_name):
    os.remove(image_name)
