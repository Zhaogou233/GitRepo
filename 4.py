def cube_count(a):
    if is_number(a):
        return a**3
    else:
        print("非数字不能计算立方值")
    
def is_number(a):
    if not isinstance(a,(int,float)):
        print("输入的%s不是数字，请重新输入"%a)
        return False
    else:
        return True  
c = cube_count("abc")
print(c)


c=cube_count(10)
print(c)
