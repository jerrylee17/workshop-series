# add vs multiply

## add case
arr_a = [1, 2, 3, 4, 5]
arr_b = [5, 4, 3, 2, 1]
count = 0
for elem_a in arr_a:
    count += 1 
    print(elem_a)

for elem_b in arr_b:
    count+= 1
    # print(elem_b)
print(count) 

## multiply case
arr_a = [1, 2, 3, 4, 5]
arr_b = [5, 4, 3, 2, 1]
count = 0
for elem_a in arr_a:
    for elem_b in arr_b:
        # print(elem_a, ",", elem_b)
        count += 1 
print(count)


# two sum two techniques
## brute force
my_arr = [5, 4, 1, 2, 7]
target = 5

two_nums_brute = []

for i in range(len(my_arr)-1):
    for j in range(i+1, len(my_arr)):
        if my_arr[i] + my_arr[j] == target:
            two_nums_brute.append(my_arr[i])
            two_nums_brute.append(my_arr[j])
print(two_nums_brute)

## set method
two_nums = []
check = set()
for i in range(len(my_arr)):
    if my_arr[i] in check:
        two_nums.append(my_arr[i])
        two_nums.append(target-my_arr[i])
    else:
        check.add(target-my_arr[i])
print(two_nums)

# print(two_nums)

## recursive multiplication
def multiplication(multiplicand, multiplier):
    if multiplier <= 0:
        return 0
    return multiplicand + multiplication(multiplicand, multiplier - 1) 
print(multiplication(2,3))

## printing numbers with a twist
arr_a = [1, 2, 3, 4, 5, 6, 7]
arr_store = []

for i in range(len(arr_a)):
    for j in range(len(arr_a) // 2):
        arr_store.append(arr_a[j] + arr_a[i])
        print(arr_a[i], arr_a[j] + arr_a[i]) 

print(arr_store)

def fib(number):
    if number <= 1:
        return 1
    return fib(number - 1) + fib(number - 2)

print(fib(5))


def factorial(number):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return factorial(n - 1) * n

print(factorial(4)) # 4! = 4 * 3 * 2 * 1 = 24

odd_arr= [1, 3, 5, 7, 9, 11, 13]


for element in odd_arr:
    for i in range(5):
        print(element * i)
    print("-----")