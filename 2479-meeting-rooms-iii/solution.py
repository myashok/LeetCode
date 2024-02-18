import heapq
from typing import List

class Solution:
    def mostBooked(self, num_rooms: int, meetings: List[List[int]]) -> int:
        # Sort meetings based on their starting times
        meetings.sort()
        
        # Initialize a min-heap to keep track of available rooms
        available_rooms_heap = list(range(num_rooms))
        heapq.heapify(available_rooms_heap)
        
        # Initialize a min-heap to schedule meetings based on their ending times
        scheduled_meetings_heap = []
        
        # Initialize a list to keep track of the frequency of room usage
        room_usage_frequency = [0] * num_rooms       
        
        # Iterate through each meeting
        for meeting in meetings:
            # Check if there are meetings scheduled and if the earliest ending meeting ends before the current meeting starts
            while scheduled_meetings_heap and scheduled_meetings_heap[0][0] <= meeting[0]:
                # Retrieve the room number of the meeting that ends earliest
                _, room_no = heapq.heappop(scheduled_meetings_heap)
                # Add the room back to the available rooms heap
                heapq.heappush(available_rooms_heap, room_no)

            # Check if there are available rooms
            if available_rooms_heap:
                # Allocate a room for the current meeting
                room_no = heapq.heappop(available_rooms_heap)
                # Increment the frequency of room usage
                room_usage_frequency[room_no] += 1
                # Schedule the current meeting
                heapq.heappush(scheduled_meetings_heap, (meeting[1], room_no))

            else:
                # If no available rooms, find the meeting that ends earliest
                earliest_ending_meeting, room_no = heapq.heappop(scheduled_meetings_heap)
                # Increment the frequency of room usage
                room_usage_frequency[room_no] += 1
                # Adjust the end time of the current meeting based on the earliest ending meeting
                heapq.heappush(
                    scheduled_meetings_heap,
                    (meeting[1] - meeting[0] + earliest_ending_meeting, room_no),
                )

        # Find the room with the maximum frequency of usage and return its index
        most_used_room_index = max(enumerate(room_usage_frequency), key=lambda x: x[1])[0]
        return most_used_room_index

