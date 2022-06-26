def toString():
    ?

flag_array = [["M",0],["C",0],["L",0],["{",0],[15,6],[14,2],["M",0],["_",0],[60,3],[40,1],["_",0],[20,1],[0,3],[4,3],[100,3],[7,0],["}",0]]

def print_flag():
    flag =""
    for letter in flag_array:
        flag += toString(letter[0])[letter[1]]  
    print(flag)

print_flag()