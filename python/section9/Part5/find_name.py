name = ["ST","BĐ","BTL","CG","ĐĐ","HBT"]
population = [150300,247100,333300,266800,420900,318000]
max_pop=max(population)
min_pop=min(population)
max_index = population.index(max_pop)
min_index = population.index(min_pop)
print("Quận có số dân lớn nhất là : ",name[max_index])
print("Quận có số dân ít nhất là: ",name[min_index])