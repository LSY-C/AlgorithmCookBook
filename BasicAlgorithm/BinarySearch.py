class BinarySearch:
    def run(self, test_nums, target):  # 升序列表
        left = 0
        right = len(test_nums) - 1
        while left <= right:
            middle = (right - left) // 2 + left
            if test_nums[middle] < target:
                left = middle + 1
            elif test_nums[middle] > target:
                right = middle - 1
            else:
                return 'Find it ! index:{}'.format(middle)
        return 'Can\' find target'

    def test(self):
        '''
        自动测试
        :return:
        '''
        test_nums = [1, 4, 6, 7, 8, 9, 10, 12, 14, 14, 16, 18, 20]
        test_nums = [1, 3]
        print("test:{}".format(test_nums))
        print("result:{}".format(self.run(test_nums, 3)))


if __name__ == '__main__':
    sol = BinarySearch()
    sol.test()
