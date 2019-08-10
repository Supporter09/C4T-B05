import random
character_skill ={
    "skill1" : {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3,
    },
    "skill2" : {
        "Name": "Quick attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5,
    },
    "skill3" : {
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2,
    },
}
for i in character_skill.items():
    print(i)


level = random.randrange(5)
hit_rate = random.uniform(0,1)
print(hit_rate)
print(level)
def check_level(level_need,result):
    if level_need == level:
        result = "O"
        return result
    else:
        result = "X"
        return result
def print_in(result,damage):
    if result == "O":
        print("Damage :",damage)
    else:
        print("You don't have enough level.")
def check_hit_rate(skill_hit_rate,hit_rate,result,damage):
    if hit_rate < skill_hit_rate:
        print_in(result,damage)
    elif hit_rate>skill_hit_rate:
        print("Skill đánh ko trúng mục tiêu.")

def skill_option(level):
    user_choice = int(input("Enter your choice : "))
    if user_choice == 1:
        skill = character_skill["skill1"]

        level_need = skill["Minimum level"]

        damage = skill["Damage"]

        skill_hit_rate = skill["Hit rate"]

        result=0
        check_level(level_need,result)
        result = check_level(level_need,result)
        check_hit_rate(skill_hit_rate,hit_rate,result,damage)
    elif user_choice == 2:
        skill = character_skill["skill2"]

        level_need = skill["Minimum level"]

        damage = skill["Damage"]

        skill_hit_rate = skill["Hit rate"]

        result=0
        check_level(level_need,result)
        result = check_level(level_need,result)
        check_hit_rate(skill_hit_rate,hit_rate,result,damage)
    elif user_choice == 3:
        skill = character_skill["skill3"]

        level_need = skill["Minimum level"]

        damage = skill["Damage"]

        skill_hit_rate = skill["Hit rate"]

        result=0
        check_level(level_need,result)
        result = check_level(level_need,result)
        check_hit_rate(skill_hit_rate,hit_rate,result,damage)
    else:
        print("try again")
        return user_choice
skill_option(level)


