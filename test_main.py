import main

def test_main():
    nums = [1, 2, 3]
    assert main.sum_numbers(nums) == sum(nums)
