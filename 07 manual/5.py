dict1 = dict2 = dict3 = dict4 = {}
dict1={'a':5,'c':2,'s':76,'t':1,'n':4}
dict2={'z':12,'p':13,'b':14,'o':15}
dict3={'g':9,'h':31,'l':29,'k':36,'i':3}
dict4={**dict1,**dict2,**dict3}
print(dict4)
