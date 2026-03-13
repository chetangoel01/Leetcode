class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i remmeber this, this is a prefix sum type of question where i need left and right product
        # if i skip the middle, the product at i will be left of i * right of i
        # i need to calculate all left of i and right of i

        left_product = [1]
        for i in range(len(nums)):
            left_product.append(left_product[-1] * nums[i])

        # nums = [1, 2, 3, 4]
        right_product = [1]
        for i in range(len(nums)-1, -1, -1):
            right_product.append(right_product[-1] * nums[i])
        right_product.reverse()

        result = []
        for i in range(len(nums)):
            result.append(left_product[i] * right_product[i+1])
        
        return result