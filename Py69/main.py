def sep_url():
    sep = ["."]
    inp = input(str("Enter url with '_' :"))
    for s in inp:
        if s in sep:
            print(inp.split(s)[0])


# URL for testing: http://en.wikipedia.org/wiki/Clean_URL
# https://www.amazon.com/Lenovo-ThinkPad-T470p-i7-7700HQ-Professional/dp/B07BL559MQ/ref=sr_1_4?ie=UTF8&qid=1545335206&sr=8-4&keywords=thinkpad+t470p
sep_url()
