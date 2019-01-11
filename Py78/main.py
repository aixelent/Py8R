def duplicate_chars(string):
    temp = ""
    for duplicated in string:
        if not duplicated in temp:
            temp += duplicated
        else:
            pass
    return temp


print(duplicate_chars("GoLand is a new commercial IDE by JetBrains aimed at providing an ergonomic environment "
                      "for Go development. The new IDE extends the IntelliJ platform with coding assistance "
                      "and tool integrations specific for the Go language."))
