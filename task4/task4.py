import sys


def find_min_moves_to_equal_elements(nums: list[int]) -> int:
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


if __name__ == '__main__':
    try:
        array = sys.argv[1]
        
        with open(array, 'r') as file:
            nums = [int(line.strip()) for line in file.readlines()]
        
        min_moves = find_min_moves_to_equal_elements(nums)
        print(f"Минимальное количество ходов: {min_moves}")
        
    except (FileNotFoundError, ValueError, IndexError) as e:
        print(f"Ошибка: {e}")