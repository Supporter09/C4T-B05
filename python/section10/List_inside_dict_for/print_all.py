print("__________AVENGERS END GAME__________")
film ={
    "name" : "Avengers: End Game",
    "release year" : 2019,
    "actor" : ["Robert Downey Jr","Chris Evans","Mark Ruffalo","Chris Hemsworth","Scarlett Johansson","Jeremy Renner","Don Cheadle","Paul Rudd","Brie Larson","Karen Gillan","Danai Gurira","Bradley Cooper","Josh Brolin"],
    "director": ["Anthony Russo","Joe Russo"],
}
print(film)

for keys,values in film.items():
    print(keys,":",values)