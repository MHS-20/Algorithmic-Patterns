import java.util.*;

// CLASSIC INTERVAL SCHEDULING
// maximum number of pairwise disjoint intervals

public class DisjointIntervals {

    public static int disjoint(int[][] intervals) {
        if (intervals.length == 0) return 0;

        // Sort intervals by end time
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));

        // Initialize
        int count = 1;
        int prevEnd = intervals[0][1];

        // Greedy selection
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            if (start > prevEnd) {     // disjoint
                count++;
                prevEnd = end;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[][] intervals = {
            {1, 2},
            {2, 10},
            {4, 6}
        };
        System.out.println(disjoint(intervals));
    }
}

