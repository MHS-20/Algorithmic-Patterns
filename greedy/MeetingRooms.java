import java.util.*;

// CLASSIC OVERLAPPING INTERVALS
// maximum number of overlapping intervals

public class MeetingRooms {

    public static int meetingRooms(int[][] meetings) {
        List<int[]> data = new ArrayList<>();

        // Convert each meeting into two events: start (+1), end (-1)
        for (int[] m : meetings) {
            data.add(new int[]{m[0], 1});
            data.add(new int[]{m[1], -1});
        }

        // Sort by time; if same time, process "end" (-1) before "start" (+1)
        data.sort((a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });

        int curr = 0;
        int ans = 0;

        for (int[] e : data) {
            curr += e[1];
            ans = Math.max(ans, curr);
        }
        return ans;
    }

    public static void main(String[] args) {
        int[][] meetings = {
            {0, 30},
            {5, 10},
            {15, 20}
        };
        System.out.println(meetingRooms(meetings));
    }
}

