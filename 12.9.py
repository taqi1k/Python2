#1863528
#taqi syed

result = []

while(1):
    string = input()
    if(string == "-1"):
        break
    try:
        result.append([string.split(' ')[0],int(string.split(' ')[1])+1])
    except ValueError:
        result.append([string.split(' ')[0],0])
for name, age in result:
    print(name,age)