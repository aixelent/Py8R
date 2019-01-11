def repeated_word(string):
    temp = set()

    for word in string.split():
        if word in temp:
            return word
        else:
            temp.add(word)
    return None


print(repeated_word("GoLand is a new commercial IDE by JetBrains aimed at providing an ergonomic environment "
                    "for Go development. The new IDE extends the IntelliJ platform with coding assistance "
                    "and tool integrations specific for the Go language."))
