list=input()
result=re.findall(r'\b\w+\b',list) 
print(result[-1])
