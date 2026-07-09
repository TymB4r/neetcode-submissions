class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if nums.count(0) >= 2:
            return [0] * n


        # czy inicjalizować zmienne zaraz przed tym, gdzie będą użyte czy wszystko na samym początku funkcji?
        prefix_product = [1] * n
        for i in range(n): # czy tu lepiej zrobić enumerate czy zrobić też range dla jednolitości?
            if i == 0:
                prefix_product[i] = nums[i]
            else:
                prefix_product[i] = prefix_product[i-1] * nums[i]
        
        suffix_product = [1] * n 
        for i in range(n - 1, -1, -1): 
            if i == n - 1:
                suffix_product[i] = nums[i]
            else:
                suffix_product[i] = suffix_product[i+1] * nums[i]
        
        res = [0] * n
        res[0] = suffix_product[1]
        res[-1] = prefix_product[-2]  # czy lepiej zrobić n - 1 i n - 2 czy -1 i -2 jak jest?


        # czy to lepiej zrobić tak jak teraz, czy zrobić if'y w środku pętli na sprawdzanie indeksów
        for i in range(1, n - 1):
            res[i] = prefix_product[i-1] * suffix_product[i+1]
        
        return res

