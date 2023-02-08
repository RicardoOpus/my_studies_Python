while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("That was no valid number. Try again...")


# File exception:
try:
    file = open("file_that_not_exist")
except OSError:
    print("File not found")
else:
    print("File opened")
    file.close()
finally:
    print("File open called")


# Using o WITH (recomended)
with open("test_with.md", "w") as file:
    file.write("Test autoclose with")


print(file.closed)