


'''s="Python is easy to learn and int ex 123456"
print("The no.Spaces are:",s.count(" "))
alpha= sum(1 for char in s if char.isalpha())
print("The no. of alphabets are:", alpha)
digits = sum(1 for char in s if char.isdigit())
print("The no. of numbers are:", digits)'''

'''S="Python is easy to learn and int ex 123456"
w=0
s=0
n=0
l=0
u=0
c=0
for i in range (len(S)):
    if S[i].isalpha():
        w=w+1
    elif S[i].isspace():
        s=s+1
    elif S[i].isdigit():
        n=n+1
    elif S[i].islower():
        l=l+1
    elif S[i].isupper():
        u=u+1
    elif S[i].isascii():
        c=c+1
print("Words", w)
print("Space",s)
print("Number",n)
print("Lower case:",l)
print("Upper case:",u)
print("ascii:",c)'''

'''a=1,2,3,4,5,6,7,8,9
even= sum(1 for num in a if num%2==0)
print("The no. of even are:", even)
odd = sum(1 for num in a if num%2!=0)
print("The no. of odd are:", odd)'''

a=1,2,3,4,5,6
even=0
odd=0
for i in range (a):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)
            
    



