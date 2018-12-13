import sys

str_obj = "Five words"
int_obj = 315
fl_obj = 3.493

print("String object size:", sys.getsizeof(str_obj))
print("Int object size", sys.getsizeof(int_obj))
print("Float object size", sys.getsizeof(fl_obj))