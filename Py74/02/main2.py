def remove_spaces(string):
    string = "".join(string.split())
    return string


print(remove_spaces("GoLand is a new commercial IDE by JetBrains aimed at providing an ergonomic environment "
                    "for Go development. The new IDE extends the IntelliJ platform with coding assistance "
                    "and tool integrations specific for the Go language."))
