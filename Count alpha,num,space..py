

# First Method
s="Python is easy to learn and int ex 123456"
print("The no.Spaces are:",s.count(" "))
alpha= sum(1 for char in s if char.isalpha())
print("The no. of alphabets are:", alpha)
digits = sum(1 for char in s if char.isdigit())
print("The no. of numbers are:", digits)


#Second Method
S="Python is easy to learn and int ex 123456"
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
print("ascii:",c)


            
    



