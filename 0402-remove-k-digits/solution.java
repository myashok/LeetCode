public class Solution {
    public String removeKdigits(String num, int k) {
        Deque<Character> deque = new LinkedList<>();
        for (char digit : num.toCharArray()) {
            while (!deque.isEmpty() && k > 0 && deque.peekLast() > digit) {
                deque.pollLast();
                k--;
            }
            deque.offerLast(digit);
        }

        // Remove digits from the end if k is still positive
        while (k > 0 && !deque.isEmpty()) {
            deque.pollLast();
            k--;
        }

        // Remove leading zeros
        while (!deque.isEmpty() && deque.peek() == '0') {
            deque.pollFirst();
        }

        // If deque is empty, return "0"
        if (deque.isEmpty()) {
            return "0";
        }

        // Build the resulting string from deque
        StringBuilder result = new StringBuilder();
        for (char c : deque) {
            result.append(c);
        }
        return result.toString();
    }
}

