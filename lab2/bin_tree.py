#root - корень = 11
#height - высота дерево, терминатор функции = 3
#leaf - "Листья" left_leaf(l_l)=lambda x:x**2,right_leaf(r_l)=lambda y:2+y**2
def l_l(root):
    return root**2
def r_l(root):
    return 2+root**2

def gen_bin_tree(root,height)->dict:
    if height == 0: #Терминатор рекурсии
        return {f"{root}":[{l_l(root):[]},{r_l(root):[]}]}
    else:
        height -= 1
        return {f"{root}":[gen_bin_tree(l_l(root),height),gen_bin_tree(r_l(root),height)]}