class Solution {
    public int minimumCardPickup(int[] cards) {
        Map<Integer, Integer> last_seen = new HashMap<>();
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < cards.length; ++i) {
            if (last_seen.containsKey(cards[i])) {
                ans = Math.min(ans, i - last_seen.get(cards[i]) + 1);
            }
            last_seen.put(cards[i], i);
        }
        return ans == Integer.MAX_VALUE ? -1: ans;
    }
}
