a = ["default","test1","test2","test3"]
b=0
for i in a:
    if "default" in a:
        a.remove("default")
        b +=1
        print(b)
print(a)