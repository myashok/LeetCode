class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False

        # Set to store visited states
        visited = set()

        # Set the initial state with empty jars
        queue = {(0, 0)}
        
        while queue:
            a, b = queue.pop()
            
            if a + b == z:
                return True

            # Define possible next states
            states = [
                (x, b),     # Fill jar x
                (a, y),     # Fill jar y
                (0, b),     # Empty jar x
                (a, 0),     # Empty jar y
                (min(x, b + a), max(0, b - (x - a))),   # Pour jar y to x
                (max(0, a - (y - b)), min(b + a, y))    # Pour jar x to y
            ]

            for state in states:
                if state not in visited:
                    if sum(state) == z:
                        return True
                    queue.add(state)
                    visited.add(state)

        return False

