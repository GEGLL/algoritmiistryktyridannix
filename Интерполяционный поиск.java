public class InterpolationSearch {
    public static int interpolationSearch(int[] arr, int x) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
            if (lo == hi) return arr[lo] == x ? lo : -1;
            int pos = lo + ((hi - lo) * (x - arr[lo])) / (arr[hi] - arr[lo]);
            if (arr[pos] == x) return pos;
            if (arr[pos] < x) lo = pos + 1;
            else hi = pos - 1;
        }
        return -1;
    }
}
