evgen_o=input()
dict={}
for key in range(len(evgen_o)):
    dict[evgen_o[key]] = evgen_o.count(evgen_o[key])
print(dict)
