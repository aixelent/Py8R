def words_numbers_counter():
    entered_value = input("Enter string:")
    print("Words:", len(list(filter(lambda x: x.isalpha(), entered_value))))
    print("Numbers:", len(list(filter(lambda x: x.isdigit(), entered_value))))


words_numbers_counter()
