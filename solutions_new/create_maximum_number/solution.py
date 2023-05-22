class Solution:
    def merge(self, max_numl1, max_numl2):
        max_merge = []
        while max_numl1 and max_numl2:
            if max_numl1 > max_numl2:
                max_merge.append(max_numl1[0])
                max_numl1 = max_numl1[1:]
            else:
                max_merge.append(max_numl2[0])
                max_numl2 = max_numl2[1:]
        return max_merge + max_numl1 + max_numl2

    def max_number_in_list_of_size_s(self, l1, s):
        picked_index = -1
        to_select = s
        l1_size = len(l1)
        ans = []
        while to_select:
            start = picked_index + 1
            end = l1_size - (to_select - 1)
            picked_index = max(range(start, end), key=l1.__getitem__)
            ans.append(l1[picked_index])
            to_select -= 1

        return ans

    def maxNumber(self, l1: List[int], l2: List[int], k: int) -> List[int]:
        final_ans = [0]*k
        l1_length = len(l1)
        l2_length = len(l2)
        for i in range(1, k + 1):
            j = k - i
            if i > l1_length or j > l2_length:
                continue
            max_l1 = self.max_number_in_list_of_size_s(l1, i)
            max_l2 = self.max_number_in_list_of_size_s(l2, j)
            max_merge = self.merge(max_l1, max_l2)
            print(max_l1, max_l2)
            final_ans = final_ans if final_ans > max_merge else max_merge
        return final_ans