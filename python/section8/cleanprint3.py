favthing = ["Truyện tranh","LOA","Sếp"]
print(*favthing, sep=", ")
favthing.append("Python")
print(*favthing, sep=" | ")
print(favthing[0].upper)
favlen = len(favthing)
print(favthing[favlen-1].upper())
print(favthing[favlen-2].upper())