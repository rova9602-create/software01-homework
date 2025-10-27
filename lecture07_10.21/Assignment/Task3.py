
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def main():
    nums = [3, 7, 2, 8, 4]
    total = sum_list(nums)
    print("List:", nums)
    print("Sum:", total)

main()
