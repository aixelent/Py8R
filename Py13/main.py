def append_string(str):
    if len(str) >= 0 or str[:3] == "Py8R":
        return str
    return str + "Py8R"


print(append_string("Py8R"))
