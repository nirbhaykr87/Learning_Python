
f = open("Sample.txt","w+")
f.write("This is sample file use to demonstrate the input output file")
f.write("Nirbhay")

f.seek(0)
data = f.readline()
print(data)


