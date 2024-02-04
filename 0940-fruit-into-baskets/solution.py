class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l , ans, picked_type = 0, 1, dict() 
        for i, fruit in enumerate(fruits):
            if fruit in picked_type:
                ans = max(ans, i - l + 1)
            else:
                if len(picked_type) < 2:
                    ans = max(ans, i - l + 1)
                else:
                    (key1, value1), (key2, value2) = picked_type.items()
                    if value1 < value2:
                        value_of_jump = value1
                        picked_type.pop(key1)
                    else:
                        value_of_jump = value2
                        picked_type.pop(key2)
                    l = value_of_jump + 1
            picked_type[fruit] = i

        return ans

            

