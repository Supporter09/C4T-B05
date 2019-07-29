score = [80,76,64,52,34,28]
score.sort(reverse=True)
print("Hign scores :")
for i,score in enumerate(score):
    print(i,'.',score)
score1=[80,76,64,52,34,28]
newscore = int(input("Enter your new score :"))
print(type(newscore))
score1.append(newscore)
score1.sort(reverse=True)
print("Hign scores :")

for n in range(5):
    print(score1[n])
newscore2 = int(input("Enter your new score :"))
score1.append(newscore2)
score1.sort(reverse=True)
print("NEW High scores:")
for n in range(5):
    print(score1[n])


