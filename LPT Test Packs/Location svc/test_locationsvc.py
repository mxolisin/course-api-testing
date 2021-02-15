import pytest

test_list = ["dsfdfsdf.rar", "books.docx", "numbers.xlsx", "my.foto.png", "dddddddd.file"]

for i in test_list:
    index = i.rfind(".")
    print(i[index:])   # string slicing

# start the list from the back
file_name = "my.foto.png"