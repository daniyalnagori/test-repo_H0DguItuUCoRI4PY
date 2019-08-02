import main

def test_base_url():
    assert main.BASE_URL == 'https://google.com'

def test_sum():
    nums = [7, 8]
    assert main.main._sum(nums) == sum(nums)

def test_create_user():
    assert main.main.create_user('admin')

def test_best_name():
    assert main.main.best_name('ali')

