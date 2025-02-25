class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #exponentiation by squaring

        #edge cases
        if x == 0: 
            return 0 if n > 0 else float('inf')
        if n == 0:
            return 1

        negative_power = (n < 0)
        
        n = abs(n)

        result = 1.0
        current_product = x

        while n > 0: 
            if n % 2 == 1:
                result *= current_product
                n -= 1
            
            current_product *= current_product

            #divide n by 2 (floor division)
            n //= 2
        
        if negative_power:
            return 1.0/ result
        else:
            return result 

   
        while n > 0: 
            if n % 2 == 1:
                result *= x - 1
        