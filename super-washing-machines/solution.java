public class Solution {
    public int findMinMoves(int[] machines) {
        int n = machines.length;
        int sum = 0;
        for (int num : machines) {
            sum += num;
        }
        if (sum % n != 0) {
            return -1;
        }
        int avg = sum / n;
        int[] leftSums = new int[n];
        int[] rightSums = new int[n];        
        for (int i = 0; i < n; i++) {
            leftSums[i] = (i-1 >= 0 ? leftSums[i-1]: 0) + machines[i];
          //   System.out.println(leftSums[i]);
        }
        for (int i = n - 1; i >= 0; i--) {
            rightSums[i] = (i+1 <= n-1 ? rightSums[i+1] : 0) + machines[i];
           // System.out.println(rightSums[i]);
        }
        int move = 0;
        for (int i = 0; i < n; i ++) {
            int expLeft = i * avg;
            int expRight = (n - i - 1) * avg;
            int left = 0;
            int right = 0;
            leftSums[i] -= machines[i];
            rightSums[i] -= machines[i];
          //  System.out.println(leftSums[i] + " " + rightSums[i]);
            if (expLeft > leftSums[i]) {
                left = expLeft - leftSums[i];// - machines[i];
            } 
            if (expRight > rightSums[i]) {
                right = expRight - rightSums[i];// - machines[i];
            }
            move = Math.max(move, (left + right));
        }
        return move;
    }
}
