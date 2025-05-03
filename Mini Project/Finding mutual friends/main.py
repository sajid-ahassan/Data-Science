import json

with open("data3.json", "r") as file:
    data = json.load(file)


def find_mutual(user_id, data):
    user_friends = {}
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])
    if user_id not in user_friends.keys():
        return []
    direct_friends = user_friends[user_id]
    frq = {}
    for user in direct_friends:
        for friend in user_friends[user]:
            if friend != user_id and friend not in direct_friends:
                frq[friend] = frq.get(friend, 0) + 1
    frq_sorted = (sorted(frq.items(), key=lambda x: x[1], reverse=True))
    return [users for users,_ in frq_sorted]


ids = 1
recommendations = find_mutual(ids, data)
print(f"People You May Know for User {ids}: {recommendations}")
