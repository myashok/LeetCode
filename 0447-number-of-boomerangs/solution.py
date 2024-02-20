class Solution:
    def numberOfBoomerangs(self, points):
        total_boomerangs = 0
        for p1 in points:
            distances = {}  # Store distances and their counts for each point
            for p2 in points:
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                if dist in distances:
                    # current point is can be place in the front or in the back of number
                    total_boomerangs += 2 * distances[dist]
                    distances[dist] += 1
                else:
                    distances[dist] = 1

        return total_boomerangs

