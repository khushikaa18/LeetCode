class Solution {
    public double separateSquares(int[][] squares) {

        double totalArea = 0;
        double low = Double.MAX_VALUE;
        double high = Double.MIN_VALUE;

        // Step 1: total area + search bounds
        for (int[] sq : squares) {
            int y = sq[1];
            int l = sq[2];

            totalArea += (double) l * l;
            low = Math.min(low, y);
            high = Math.max(high, y + l);
        }

        double target = totalArea / 2.0;

        // Step 2: Binary Search on y
        for (int i = 0; i < 100; i++) { // enough for 1e-5 precision
            double mid = (low + high) / 2.0;
            double areaBelow = 0;

            // Step 3: calculate area below mid
            for (int[] sq : squares) {
                int y = sq[1];
                int l = sq[2];

                if (mid <= y) {
                    // no area below
                    continue;
                } 
                else if (mid >= y + l) {
                    // full square below
                    areaBelow += (double) l * l;
                } 
                else {
                    // partial square below
                    areaBelow += (mid - y) * l;
                }
            }

            // Step 4: adjust binary search
            if (areaBelow < target) {
                low = mid;
            } else {
                high = mid;
            }
        }

        return low;
    }
}
