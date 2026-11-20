# mylist = [76,92,3,"hello",true,4,76]
#
# mylist.append("apple")
# mylist.append("76")
# mylist.insert(3,"cat")
# mylist.insert(0,99)
# print(mylist)
#
# print(mylist.index("hello"))
# print(mylist.count(76))
# mylist.remove(76)
# print(mylist)
# mylist.pop(mylist.index(true))
#
# print(mylist)


# def sum_of_squares(xs):
#     total = 0
#     for x in xs:
#         total += x ** 2
#     return total
#
# print(sum_of_squares([2, 3, 4]))
#
#
#
#
# def sum_even_numbers(xs):
#     total = 0
#     for x in xs:
#         if x % 2 == 0:
#             total += x
#     return total
#
# print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
#
#
#
#
# def count_length_five(words):
#     count = 0
#     for word in words:
#         if len(word) == 5:
#             count += 1
#     return count
#
# print(count_length_five(["apple", "cat", "hello", "world"]))
#
#
#
#
# def sum_until_even(xs):
#     total = 0
#     for x in xs:
#         if x % 2 == 0:
#             break
#         total += x
#     return total
#
# print(sum_until_even([1, 3, 5, 8, 9, 10]))
#
#
#
#
# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count += 1
#         if word == "sam":
#             break
#     return count
#
# print(count_until_sam(["tom", "jack", "sam", "alex"]))
#
#
#
#
# def replace(s, old, new):
#     return new.join(s.split(old))
#
# s = "I love spam! Spam is my favorite food."
#
# print(replace(s, "Spam", "ham"))
# print(replace(s, "a", "o"))
#
#
#
#
# def max_number(numbers):
#     largest = numbers[0]
#
#     for number in numbers:
#         if number > largest:
#             largest = number
#
#     return largest
#
# print(max_number([12, 45, 7, 89, 23]))
