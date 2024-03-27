class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_positive_satisfaction = 0
        prev_sum = 0
        n = len(satisfaction)
        i = 0
        while i < n:
            if satisfaction[i] < 0:
                break
            max_positive_satisfaction += prev_sum + satisfaction[i]
            prev_sum += satisfaction[i]
            i += 1
        while i < n:
            curr_positive_satisfaction = prev_sum + satisfaction[i] + max_positive_satisfaction
            if curr_positive_satisfaction < max_positive_satisfaction:
                break
            max_positive_satisfaction = curr_positive_satisfaction
            prev_sum += satisfaction[i]
            i += 1
            
        return max_positive_satisfaction



