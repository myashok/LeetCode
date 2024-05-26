class Solution:
    def exclusiveTime(self, n, logs):
        exclusive_times = [0] * n
        stack = []
        prev_timestamp = 0
        for log in logs:
            parts = log.split(":")
            function_id = int(parts[0])
            action = parts[1]
            timestamp = int(parts[2])
            
            if action == "start":
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_timestamp
                stack.append(function_id)
                prev_timestamp = timestamp
            else:
                exclusive_times[stack.pop()] += timestamp - prev_timestamp + 1
                prev_timestamp = timestamp + 1
        
        return exclusive_times

