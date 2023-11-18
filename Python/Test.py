import copy
languages={
    "one"  :{"name":"C++","progress":"50%"},
    "two"  :{"name":"Python","progress":"80%"},
    "three":{"name":"R","progress":"30%"}
}
cplan =copy.deepcopy(languages)

print(id(languages["one"]["name"]))
print(id(cplan["one"]["name"]))