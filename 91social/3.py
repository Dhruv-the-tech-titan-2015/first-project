import json
j_str={"4":5,'6':7,'1':3,'2':4}#storing dictionary
k=json.dumps(j_str,sort_keys=True,indent=4)#dumping dictionary in a json instance
print(k)