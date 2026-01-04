class Solution {
    public int sumFourDivisors(int[] nums) {
        int ans = 0;

        for (int n : nums) {
            for (int i = 2; i * i <= n; i++) {
                if (n % i == 0) {
                    int p = i;
                    int q = n / i;

                    if (p != q && isPrime(p) && isPrime(q)) {
                        ans += 1 + p + q + n;
                    }

                    else if (i * i * i == n && isPrime(i)) {
                        ans += 1 + i + i * i + n;
                    }
                    break;
                }
            }
        }
        return ans;
    }

    private boolean isPrime(int a) {
        if (a < 2) return false;
        for (int i = 2; i * i <= a; i++) {
            if (a % i == 0) return false;
        }
        return true;
    }
}
