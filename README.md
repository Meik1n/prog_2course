##Лабараторная работа №2 
###Бинарное дерево
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
