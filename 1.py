!ls /home/aistudio/data/
def sumStartToEnd(start,end):
    sum = 0
    for n in range(start,end+1,1):
        sum = sum + n
    return sum
    
#if __name__ == '__main__' :
print(sumStartToEnd(1,10000))
