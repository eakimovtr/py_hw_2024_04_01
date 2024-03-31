def search(arr: list, value, type="linear") -> int:
    if type == "linear":
        for i, num in enumerate(arr):
            if num == value:
                return i
    
    if type == "binary":
        l: int = 0
        r: int = len(arr) - 1
        while True:
            median = (r + l) // 2
            if value == arr[median]:
                return median
            if l == r:
                return None
            if value < arr[median]:
                r = median - 1
            else:
                l = median + 1
            
    return None


arr = [1,2,3,4,5,7,9,12,16,58,950]
print(search(arr, 58, type="binary"))