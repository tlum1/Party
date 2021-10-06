def count_teams(frst_index:int, scnd_index:int, teams:list, teams_count:int) -> tuple:
    """Функция считающая количество команд"""
    minimal = min(teams[frst_index], teams[scnd_index])
    teams_count+= minimal
    teams[frst_index] -= minimal
    teams[scnd_index] -= minimal
    
    return (teams, teams_count)

count = 0 # количество пати игроков

with open('party.txt') as f:
    count = sum(1 for _ in f)  #считаем количество пати
    
with open('party.txt') as f:
    teams_count = 0 #Счетчик собранных команд
    teams = [0, 0, 0, 0, 0] #список количество команд, где на месте с индексом i+1 стоит количество пати из i+1 человек
    
    #cчитаем количество пати для групп людей от 1 до 5
    for i in range(count):
        x = f.readline()
        teams[int(x.strip())-1]+=1

    #считаем пати из пяти людей
    teams_count+=teams[-1]
    teams[-1] = 0
    
    #считаем пати для групп из 1 и 4 человек
    teams, teams_count = (count_teams(0, 3, teams, teams_count))
    #считаем пати для групп из 2 и 3 человек
    teams, teams_count = (count_teams(1, 2, teams, teams_count))

    #формируем команды из пати из одного человека
    teams_count+= teams[0]//5
    
    print(f'Итог: составлено {teams_count} команд')
    
    
    
        
    
    