# Kiran Vuksanaj & Connor Oh - TonyTop40
# Softdev2 pd9
# K10_xtra - kevin bacon number
# 2020-03-04

from pymongo import MongoClient

client = MongoClient()
db = client.TobyTop40
movie_coll = db.movies
actor_coll = db.performers



def costars(name):
    movies_starring = movie_coll.find({"cast": {"$in": [ name ]} })
    adjacent_stars = []
    for movie in movies_starring:
        for performer in movie['cast']:
            if not performer in adjacent_stars:
                adjacent_stars.append(performer)
    adjacent_stars.remove(name)
    return adjacent_stars

def gen_actornumber(name,data):
    if not name in data:
        # if the name isnt in the dictionary yet, this is the start
        print('generating bacon graph for actor', name)
        data[name] = [0,'source']
    n = data[name][0]
    print('| '*n,'evaluating for actor', name)
    adjacent_stars = costars(name)
    next_layer = []
    print(len(adjacent_stars))
    for actor in adjacent_stars:
        if actor in data:
            print(actor,'already in dataset')
        else:
            print(actor,'added to dataset')
            data[actor] = [n+1,name]
            next_layer.append(actor)
    print(len(adjacent_stars))
    print(data)
    for actor in next_layer:
        gen_actornumber(actor,data)

if __name__ == "__main__":
    gen_actornumber("Kevin Bacon",{})
        
