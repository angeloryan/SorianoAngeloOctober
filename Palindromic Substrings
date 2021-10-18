class Solution {
    public int countSubstrings(String s) {
        int sum = 0;
        
        for (int i = 0; i < s.length(); i++) {
            sum += check(s, i, i);
            sum+= check(s, i, i + 1);
        }
        
        return sum;
        
    }
    
    public int check(String s, int i, int j) {
        int left = i;
        int right = j;
        int sum = 0;
        
        while (left >= 0 && right < s.length()) {
            if (s.charAt(left) != s.charAt(right))
                return sum;
            
            sum++;
            left--;
            right++;
        }
        
        return sum;
    }
}
