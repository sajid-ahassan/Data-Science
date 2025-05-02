import json

with open("data.json","r") as file:
    data = json.load(file);

def modi(data):
    data["users"] = [user for user in data["users"] if user["name"].strip()];
    data["users"] = [user for user in data["users"] if user["friends"] and user["liked_pages"]];

    for user in data["users"]:
        user["friends"] = list(set(user["friends"]));
    for user in data["users"]:
        user["liked_pages"] = list(set(user["liked_pages"]));
    p ={};
    for page in data["pages"]:
        p[page["id"]] = page;
    data["pages"] = list(p.values());
    
    return data;


with open("data2.json","w") as f:
    json.dump(modi(data),f);

