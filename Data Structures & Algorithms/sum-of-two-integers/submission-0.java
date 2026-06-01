class Solution {
    public int getSum(int a, int b) {
        // b is for the carry value
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return  a;
        
    }
}
