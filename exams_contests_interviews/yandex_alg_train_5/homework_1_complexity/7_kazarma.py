soldiers = int(input())
kazarma_hp = int(input())
new_enemies = int(input())
enemies = 0

kazarma_hp -= soldiers
rounds = 1

if soldiers > new_enemies:
    while True:
        s = soldiers
        s -= new_enemies
        kazarma_hp -= s
        rounds += 1
        if kazarma_hp <= 0:
            break
elif soldiers <= new_enemies:
    enemies = new_enemies
    s = soldiers
    s -= kazarma_hp
    if s <= 0:
        rounds = -1
    elif enemies - s >= s:
        rounds = -1
    elif kazarma_hp > 0:
        enemies -= s
        soldiers -= enemies
        rounds += 1
        while enemies > 0:
            rounds += 1
            enemies -= soldiers
            if soldiers <= enemies:
                rounds = -1
                break
            soldiers -= enemies


print(rounds)
