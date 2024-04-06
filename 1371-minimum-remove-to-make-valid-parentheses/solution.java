class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> st = new Stack<>();
        boolean[] flag = new boolean[s.length()];
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                st.push(i);
            } else if(s.charAt(i) == ')') {
                if (!st.isEmpty()) {
                    st.pop();
                } else {
                    flag[i] = true;
                }
            }
        }
        while (!st.isEmpty()) {
            flag[st.pop()] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!flag[i]) {
                sb.append(s.charAt(i));
            }
        }

        return sb.toString();
    }
}
