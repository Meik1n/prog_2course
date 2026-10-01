# Лабораторная работа №1
### Решение в "лоб"

---
```python
def two_sum(lst,target):

    if len(lst)>1:
        for i in range(len(lst)-1):
            for a in range(i,len(lst)):
                if lst[i]+lst[a]==target:
                    return(i,a)
    return()

```
---

### Усложнение 2

---
```python
def two_sum_hashed1(lst,target):
    # for i in range(len(lst)):
    #     list.append([i,lst[i]])  #Создаем список с ключами
    list=[(i, lst[i]) for i in range(len(lst))]    #То же действее(строки 16-17), только в одну строчку с генератором списков
    key = dict(list)    #Объедениям в словарь
    for i in key.values():  #Перебор значений
        if i < target: #нахождение мин.пары
            if target - i in key.values(): #Проверка есть ли мин.пара
                return(get_key(key,i),get_key(key,target - i))
```
---

### Усложнение 3

---
```python
def get_key(dic,value):
    for key, val in dic.items():
        if val == value:
            return key
            
def two_sum_hashed2(lst,target):

    # for i in range(len(lst)):
    #     list.append([i,lst[i]])  #Создаем список с ключами
    
    list=[(i, lst[i]) for i in range(len(lst))]    #То же действее(стоки 28-29), только в одну строчку с генератором списков
    
    key = dict(list)    #Объедениям в словарь
    result = [] #Список с результатами
    
    for i in key.values():  #Перебор значений
        if i < target // 2: #нахождение мин.пары, //2 Чтобы не взять повторки и одинаковые индексы
            if target - i in key.values(): #Проверка есть ли мин.пара
                result.append(tuple([get_key(key,i),get_key(key,target - i)]))  #Добавление результатов в один список
                
    return result
```
---
[Смотри lab1]

# Лабараторная работа №2
## Бинарное дерево
----
```python
#root - корень = 11
#height - высота дерево, терминатор функции = 3
#leaf - "Листья" left_leaf=lambda x:x**2,right_leaf=lambda y:2+y**2

def gen_bin_tree(root,height)->dict:

    if height == 0: #Терминатор рекурсии 
        return {f"{root}":[{f"{(int(root)**2)}":[]},{f"{(2+int(root)**2)}":[]}]}

    else:
        height -= 1
        left_leaf,right_leaf = root**2,2+root**2 #Создание "листьев"
        return {f"{root}":[gen_bin_tree(left_leaf,height),gen_bin_tree(right_leaf,height)]}
  ```
[Смотри lab2]
