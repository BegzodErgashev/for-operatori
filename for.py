# # for-8
# a = 2
# b = 10
# k = 1
# for i in range(a, b+1):
#     k *= i
#     print(k)
# print(k)

# # for - 9
# a = 2
# b = 10
# s = 0
# for i in range(a, b+1):
#     s +=i**2
#     print(s)
# print("natijaviy: ", s)

# # for -10
# n = 15
# s = 0
# for i in range(1, n+1):
#     s += 1/i
#     print(s)
# print("natijaviy:", s)

# # for 11
# n = 6
# s = 0
# for i in range(n, 2*n+1):
#     s += i**2
#     print(s)
# print("natijaviy:", s)

# # for 12
# n = 10
# k = 1
# for i in range(11, 11+n):
#     k *= i/10
#     print(k)
# print("natijaviy:", k)

# # for 13
# s = 0
# n = 10
# for i in range(11, 11+n):
#     x = (-1)**(i+1)*i/10
#     s += (-1)**(i+1)*i/10
#     print(x)
#     print(s)
# print("natijaviy:", s)

# # for 14
# s = 0
# n = 10

# for i in range(1, 2*n, 2):
#     s += i
#     print(s)

# # for 15
# n = 4
# a = 3
# k = 1
#
# for i in range(1,n+1):
#     k *=a
#     print(k)
#
# print("natijaviy :", k)

# # for 25
# n = 5
# x = 6
# s = 0
# for i in range(1, n+1):
#     s += (-1)**(i+1)*x/i
#     print(s)

# # for 31
# n = 6
# a = 2
# for i in  range(1, n):
#     a = 2+1/a
#     print(a)

# # for 27
#
# x = 2
# n = 5
# s = 0.0
# for i in range(1, n+1):
#     s += (2*i-1)*x**(2*i+1)/(2*n*(2*n+1))
#     print(s)




# # for 32
# a = 1
# n = 6
# for i in range(1,n):
#     a = (a+1)/i
#     print(a)



# # for 36
# k = 3
# n = 4
# s = 0
# for i in range(1, n+1):
#     s += i**k
#     print(s)

# # for 37
# n = 4
# s = 0
# for i in range(1, n+1):
#     s += i**i
#     print(s)

# # for 38
# n = 5
# s = 0
# for i in range(n, 0, -1):
# # for_23
# x = 3
# n = 2
# f = 1
# s = 0
# k = 0
# for i in range(1, 2*n):
#     f *= i
#     if i%2==1:
#         print("k=",k)
#         s += ((-1)**(k)*(x**i))/f
#         print("f", f)
#         print("s", s)
#         k += 1


# n = 6
# f = 1
# for i in range(1,n):
#     f *= (2*i-1)
#     print(f)

# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)


# # for 38
# n = 10
# s = 0
# for i in range(1, n+1):
#     s += i**n
#     print(s)
#     n -= 1


# for 39

# a = 3
# b = 7
# for i in range(a, b+1):
#     k = 1
#     while k <= i:
#             print("i", i)
#             k +=1

# for39:
# a=int(input('a: '))
# b=int(input('b: '))
# for i in range(a,b+1):
#     for j in range(1,i+1):
#         print(i)
