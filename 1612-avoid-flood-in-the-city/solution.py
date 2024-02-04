from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = dict()
        drying_days = SortedList()
        ans = [-1] * (len(rains))
        for i, rain in enumerate(rains):
            if rain:
                if rain in full_lakes and not drying_days:
                    return []

                if rain in full_lakes:
                    drying_day_after_lake_is_fulled = drying_days.bisect_left(full_lakes[rain])
                    if drying_day_after_lake_is_fulled == len(drying_days):
                        return []

                    else:
                        ans[drying_days[drying_day_after_lake_is_fulled]] = rain
                        drying_days.pop(drying_day_after_lake_is_fulled)
                        full_lakes[rain] = i
                else:
                    full_lakes[rain] = i
                    ans[i] = -1

            else:
                drying_days.add(i)
                ans[i] = 1

        return ans

