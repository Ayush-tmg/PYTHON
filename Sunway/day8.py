f = open('/Users/ayushtamang/Documents/Python/Sunway/File.txt', 'w')
f.write("""
HEloo! My name is Ayush Tamanga.
This is File Handling testo.
Using Python.
Date: 7 Jan 2024
Time: 9:01 am.
""")
f.close()

f = open('/Users/ayushtamang/Documents/Python/Sunway/File.txt', 'r')
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())

for x in f:
    print(x)

f.close()

f = open('/Users/ayushtamang/Documents/Python/Sunway/File.txt', 'a')

f.write("Now, the txt has more content.")

f.close()

f = open('/Users/ayushtamang/Documents/Python/Sunway/File.txt', 'r')
print(f.read())
f.close()

f = open('/Users/ayushtamang/Documents/Python/Sunway/File.txt', 'w')
f.write("\nOh no! I over wrote the contents.")
f.close()

f = open('/Users/ayushtamang/Documents/Python/Sunway/File.txt', 'r')
print(f.read())
f.close()