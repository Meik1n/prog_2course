def get_key(dic,value):
    for key, val in dic.items():
        if val == value:
            return key

def two_sum(lst,target):
    if len(lst)>1:
        for i in range(len(lst)-1):
            for a in range(i,len(lst)):
                if lst[i]+lst[a]==target:
                    return(i,a)
    return()

def two_sum_hashed1(lst,target):
    
    # for i in range(len(lst)):
    #     list.append([i,lst[i]])  #Создаем список с ключами
    list=[(i, lst[i]) for i in range(len(lst))]    #То же действее(строки 16-17), только в одну строчку с генератором списков
    key = dict(list)    #Объедениям в словарь
    
    for i in key.values():  #Перебор значений
        if i < target: #нахождение мин.пары
            if target - i in key.values(): #Проверка есть ли мин.пара 
                return(get_key(key,i),get_key(key,target - i))

def two_sum_hashed2(lst,target):
    
    # for i in range(len(lst)):
    #     list.append([i,lst[i]])  #Создаем список с ключами
    list=[(i, lst[i]) for i in range(len(lst))]    #То же действее(стоки 28-29), только в одну строчку с генератором списков
    key = dict(list)    #Объедениям в словарь
    result = [] #Список с результатами
    for i in key.values():  #Перебор значений
        if i < target // 2: #нахождение мин.пары, //2 Чтобы не взять повторки и одинаковые индексы
            if target - i in key.values(): #Проверка есть ли мин.пара 
                result.append(tuple([get_key(key,i),get_key(key,target - i)]))  #Добавление результатов в один список
    return result

        
        
    
    