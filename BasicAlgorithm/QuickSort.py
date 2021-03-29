class QuickSort:
    def quick(self, nums, left, right):
        if left >= right:
            return
        flag = nums[left]
        i = left
        j = right
        while i < j:
            while nums[j] >= flag and i < j:
                j -= 1
            nums[i] = nums[j]
            while nums[i] <= flag and i < j:
                i += 1
            nums[j] = nums[i]
        nums[i] = flag
        self.quick(nums, left, i - 1)
        self.quick(nums, i + 1, right)

    def quick_nodigui(self,nums):

    def run(self, test_list):
        self.quick(test_list, 0, len(test_list) - 1)

    def test(self):
        test_list = [4, 6, 9, 2, 3, 4, 0, 10, 7, 8, 5, 1]
        test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        test_list = [5, 5, 5, 5, 5]
        test_list = [2, 1]
        self.run(test_list)
        print(test_list)


if __name__ == '__main__':
    sol = QuickSort()
    sol.test()
