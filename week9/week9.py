# def is_oddHayır:
# return n % 2 == 1
#
# print(is_odd(13))

# def is_leapyear(year):
# if year % 400 == 0:
# return True
# elif year % 100 == 0:
# return False
# elif year % 4 == 0:
# return True
# else:
# return False
#
# print(is_leapyear(2000))


# def print_triangular_numbersHayır:
# total = 0
# for i in range(1, n+1):
# total = total + i
# print(i, total)
# print_triangular_numbers(5)


# def is_primeHayır:
# if n < 2:
# return False
# for i in range(2, n):
# if n % i == 0:
# return False
# return True
#
# print(is_prime(10))


# def reverse(s):
# result = ""
# for ch in s:
# result = ch + result
# return result

# def remove_all_occurrences(sab, s):
# return s.replace(sab, '')
# print(remove_all_occurrences("ll", "hello world"))

# def substitute(message,key):
#     alphabet = "abcçdefgğhıijklmnoöprştuüvyz"
#     result = ""
#     for ch  in message:
#         index = alphabet.find(ch.lower())
#         if index != -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
# key = "abcçdefgğhıijklmnoöprştuüvyz"
# print(substitute("hello world",key))

# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if ch.lower() not in result.lower():
#             result = result + ch
#     return result
#
# print(remove_dups("hello world"))


