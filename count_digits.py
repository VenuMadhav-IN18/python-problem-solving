n=89765

def count_digits(n):
    cnt=0
    while n!=0:
        
        cnt+=1
        n=n//10
    return cnt
print(count_digits(n))

