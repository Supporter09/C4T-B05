print("__________AVENGERS END GAME__________")
film ={
    "name" : "Avengers: End Game",
    "release year" : 2019,
    "actor" : ["Robert Downey Jr","Chris Evans","Mark Ruffalo","Chris Hemsworth","Scarlett Johansson","Jeremy Renner","Don Cheadle","Paul Rudd","Brie Larson","Karen Gillan","Danai Gurira","Bradley Cooper","Josh Brolin"],
    "director": ["Anthony Russo","Joe Russo"],
}
print(film)

actor = film["actor"]
print(actor)
for actors in range(len(actor)-1):
    print(actor[actors])