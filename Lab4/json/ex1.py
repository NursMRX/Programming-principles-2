import json

with open("file.json", "r") as json_file:
    json_data = json.load(json_file)
    
interfaces = json_data["imdata"]

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

def data(n):
    print(n["dn"], end = "       ")
    print(n["descr"], end= "                        ")
    print(n["speed"], end = "  ")
    print(n["mtu"])
for i in interfaces:
    data1 = i["l1PhysIf"]
    data2 = data1["attributes"]
    if data2["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/33]":
        data(data2)
    if data2["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/34]":
        data(data2)
    if data2["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/35]":
        data(data2)