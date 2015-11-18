#! python3

# phoneEmailExtraction.py
# =======================
# Extracts phone numbers and emails from chunks of text.
# It also formats the phone numbers although at some point I may opt to
# make something that returns raw phone numbers.

# Regex cheat sheet: http://regexpal.com/


import re
import pyperclip


# Regex pattern for phone numbers (ignores case for ext vs EXT, etc.)
phoneRegex = re.compile(r"""(
    (\d{3})?                    # Group 1: Area code (3 digits)
    (\))?                       # First delimiter: )
    (\s|-|\.)?                  # Second delimiter: " ", -, .
    (\d{3})                     # Group 4: Phone number first 3 digits
    (\s|-|\.)?                  # Third delimiter: " ", -, .
    (\d{4})                     # Group 6: Phone number last 4 digits
    (\s*(ext|x)?(:|\.)?\s*)?    # Optional extension text and delimiters
    (\s*(\d{2,5}))?             # Group 11: Optional extension numbers
    )""", re.VERBOSE | re.IGNORECASE)


# Regex pattern for email addresses (ignores case)
emailRegex = re.compile(r"""(
    [a-z0-9._-]+        # Username
    @                   # at
    [a-z0-9._-]+        # Domain
    \.                  # dot
    [a-z]{2,4}          # Top-level domain
    )""", re.VERBOSE | re.IGNORECASE)


# Copied text from pyperclip.
text = str(pyperclip.paste())


# Collect phone numbers.
def phone_collector(text):
    phoneNumbers = []
    # Go through all the groups in the regex match object.
    for groups in phoneRegex.findall(text):
        # Raw numbers for area code and extension for readability.
        rawAreaCode = groups[1]
        rawExtension = groups[11]
        # Formatted area code, core phone number, and extension.
        areaCode = "(" + groups[1] + ") "
        coreNumber = "-".join([groups[4], groups[6]])
        extension = "  ext. " + groups[11]
        # Only prints the () and ext. if an area code and/or extension
        # are found.
        # Both area code and extension.
        if rawAreaCode != "" and rawExtension != "":
            foundNumber = areaCode + coreNumber + extension
        # Just area code.
        elif rawAreaCode != "":
            foundNumber = areaCode + coreNumber
        # Just extension.
        elif rawExtension != "":
            foundNumber = coreNumber + extension
        # (Lonely phone number)
        else:
            foundNumber = coreNumber
        # Add to list of phone numbers and return.
        phoneNumbers.append(foundNumber)
    return phoneNumbers


# def email_collector(text)


# Demonstration
print("Phone numbers found:")
for i in phone_collector(text):
    print(i)

