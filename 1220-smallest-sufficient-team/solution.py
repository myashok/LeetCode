class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_index = {skill:i for i, skill in enumerate(req_skills)}
        dp = defaultdict(list)
        dp[0] = []
        for i, p_skills in enumerate(people):
            skill_mask_of_people_i = 0
            for skill in p_skills:
                skill_mask_of_people_i |= (1 << skill_to_index[skill])
            
            for prev_skill_mask_of_people in list(dp.keys()):
                updated_skill_mask = prev_skill_mask_of_people | skill_mask_of_people_i
                if updated_skill_mask not in dp or len(dp[updated_skill_mask]) > len(dp[prev_skill_mask_of_people]) + 1:
                    dp[updated_skill_mask] = dp[prev_skill_mask_of_people] + [i]
    
        return dp[(1 << len(req_skills)) - 1]
