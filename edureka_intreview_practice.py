# ------factorial of number
# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n* fact(n-1)
#
# print(fact(4))

# ------fibbonacci series 0 1 1 2 3 5 8
# a=int(input('enter first no'))
# b=int(input('enter 2nd no'))
# n=int(input('enter no till which u want fibbonacci series'))
# print(a,b,end=' ')
# while n-2:
#     c=a+b
#     a=b
#     b=c
#     print(c,end=' ')
#     n-=1

#-----check number is armstrong no or not, 153-->1*3 + 5*3 + 3*3==>153
# n='153'
# l=len(n)
# new=0
# for i in n:
#     new+=int(i)**l
#
# if new==int(n):
#     print('this is armstrong number')
# else:
#     print('not an armstrong number')

#-------pattern programs
# n=5
# for i in range(n):
#     for j in range(n - i):
#         print(end=' ')
#     for j in range(i):
#
#         print('+',end=' ')
#     print()

#-----leap year check

# year=int(input('enter year:'))
# result='leap year' if year%400==0 else 'leap year' if year%4==0 and year%100!=0 else 'non leap year'
# print(result)

#-----prime number check
# n=int(input('enter number:'))
# for i in range(2,n):
#     if n%i==0:
#         print('not prime')
#         break
#     else:
#         print('prime')
#         break

