# with open("./data.txt","r",encoding="utf-8") as dd:
#     content = dd.read()
#     print(content)
with open("./data.txt","r",encoding="utf-8") as dd:
    lines = dd.readlines()
    for line in lines:
        print(line)
