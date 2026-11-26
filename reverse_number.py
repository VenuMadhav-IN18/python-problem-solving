n=89045

def reverse_number(n):
    rev_n=0
    while n!=0:
        rem=n%10
        rev_n=rev_n*10+rem
        n=n//10

    return rev_n
print(reverse_number(n))