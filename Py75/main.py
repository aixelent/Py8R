def capitalize(string):
    sttings_upper = string.title()

    for word in string.split():
        words = word[:-1] + word[0-1].upper() + " "
    return sttings_upper[:-1]


print(capitalize("GoLand is a new commercial IDE by JetBrains aimed at providing an ergonomic environment "
                  "for Go development. The new IDE extends the IntelliJ platform with coding assistance "
                  "and tool integrations specific for the Go language."))
