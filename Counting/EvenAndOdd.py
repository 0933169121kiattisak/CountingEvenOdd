def findNumber(number1,number2,number3):
  countOdd = 0
  countEven = 0

  numbers = str(number1) + str(number2) + str(number3)
  for i in numbers:
    if int(i) % 2 == 0:
      countEven += 1
    else:
      countOdd += 1
  print(f"even: {countEven}\nodd: {countOdd}")
findNumber(1,2,3)



numbers = list(map(int, input().split()))
print(numbers)

even_count = 0
odd_count = 0


for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print(f"even {even_count}")
print(f"odd {odd_count}")




numbers = list(map(int, input().split()))


even_count = len([num for num in numbers if num % 2 == 0])
odd_count = len([num for num in numbers if num % 2 != 0])


print(f"even {even_count}")
print(f"odd {odd_count}")




numbers = list(map(int, input().split()))


even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))


print(f"even {even_count}")
print(f"odd {odd_count}")




even_count = 0
odd_count = 0


for _ in range(3):
    number = int(input())  
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print(f"even {even_count}")
print(f"odd {odd_count}")




numbers = list(map(int, input().split()))


counts = {'even': 0, 'odd': 0}


for number in numbers:
    if number % 2 == 0:
        counts['even'] += 1
    else:
        counts['odd'] += 1


print(f"even {counts['even']}")
print(f"odd {counts['odd']}")



numbers = list(map(int, input().split()))


counts = {'even': 0, 'odd': 0}


for number in numbers:
    if number % 2 == 0:
        counts['even'] += 1
    else:
        counts['odd'] += 1


print(f"even {counts['even']}")
print(f"odd {counts['odd']}")
