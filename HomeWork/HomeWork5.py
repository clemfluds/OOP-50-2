class BinarySearch:
    def __init__(self, sorted_list):
        self.sorted_list = sorted_list

    def search(self, target):
        left, right = 0, len(self.sorted_list) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.sorted_list[mid] == target:
                return mid
            elif self.sorted_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
binary_search = BinarySearch(arr)

result = binary_search.search(9)
if result != -1:
    print(f"Элемент найден на индексе {result}")
else:
    print("Элемент не найден")
