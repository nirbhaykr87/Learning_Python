with open("sample.txt", "a+") as f:
    # f.write("\nThis is append line22")
    # f.seek(0)
    data = f.readline()
    print(data)