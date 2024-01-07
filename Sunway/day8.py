f = open('File.txt', 'w')
f.write("""
HEloo! My name is Ayush Tamanga.
This is File Handling testo.
Using Python.
Date: 7 Jan 2024
Time: 9:01 am.
""")
f.close()

f = open('File.txt', 'r')
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# print(f.readline())

for x in f:
    print(x)

f.close()

f = open('File.txt', 'a')

f.write("Now, the txt has more content.")

f.close()

f = open('File.txt', 'r')
print(f.read())
f.close()

f = open('File.txt', 'w')
f.write("\nOh no! I over wrote the contents.\n")
f.close()

f = open('File.txt', 'r')
print(f.read())
f.close()

try:
    f = open("abc.txt", "r")
except FileNotFoundError:
    print("File not found.")
except:
    print("An error occured.")