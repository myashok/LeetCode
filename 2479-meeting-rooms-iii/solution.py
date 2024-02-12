class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        room_min_heap = list(range(n))
        heapq.heapify(room_min_heap)
        scheduled_meet_min_heap = []
        freq_of_room_used = [0] * n       
        for meeting in meetings:
            while (
                scheduled_meet_min_heap and scheduled_meet_min_heap[0][0] <= meeting[0]
            ):
                _, room_no = heapq.heappop(scheduled_meet_min_heap)
                heapq.heappush(room_min_heap, room_no)

            if room_min_heap:
                room_no = heapq.heappop(room_min_heap)
                freq_of_room_used[room_no] += 1
                heapq.heappush(scheduled_meet_min_heap, (meeting[1], room_no))

            else:
                first_ending_meet, room_no = heapq.heappop(scheduled_meet_min_heap)
                freq_of_room_used[room_no] += 1
                heapq.heappush(
                    scheduled_meet_min_heap,
                    (meeting[1] - meeting[0] + first_ending_meet, room_no),
                )

        
        return max(enumerate(freq_of_room_used), key=lambda x: x[1])[0]

