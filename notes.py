#100DaysofCode: DAY 12 - Namesspaces Local vs Global Scope

#Scope
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enimies inside the function: {enemies}")

# increase_enemies()
# print(f"eneimies outside the function {enemies}")

#Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)


#Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(f"The potions strength is: {potion_strength}")
#     drink_potion()


# game()


#The is no Block Scope
# game_level = 3
# enemies = ["Deliah", "Kim", "Joseph"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)


# game_level = 3
# def create_enemy():
#     enemies = ["Deliah", "Kim", "Joseph"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
# create_enemy()