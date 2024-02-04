# How to Raise a Exception

try:
    with open("NewFile.txt",mode='r') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(e)



