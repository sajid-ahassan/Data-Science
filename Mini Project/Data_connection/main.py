import json;

def lod(filename):
    with open(filename,"r") as file:
        return json.load(file);
data = lod("data.json");

def read(name):
    id_name = {d["id"]:d["name"] for d in name["users"]}
    id_pages = {d["id"]:d["name"] for d in name["pages"]}
    for d in name["users"]:
        frnds = [id_name[da] for da in d["friends"]]
        page = [id_pages[da] for da in d["liked_pages"]]
        print(f"Name: {d["name"]}(ID: {d["id"]}) , Friends: {frnds}, Liked Pages: {page}")




read(data);
