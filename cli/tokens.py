import re

def convertCommandToTokens(command):
    commandInLowerCase = command.strip().lower()
    tokenizedCommand = re.split(r"\s+", commandInLowerCase)
    return tokenizedCommand