def word_occur(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_occur("GoLand is a new commercial IDE by JetBrains aimed at providing an ergonomic environment "
                 "for Go development. The new IDE extends the IntelliJ platform with coding assistance "
                 "and tool integrations specific for the Go language."))
