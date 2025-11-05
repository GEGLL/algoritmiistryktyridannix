import java.util.ArrayList;
import java.util.List;

public class Combinations {
    public static List<List<Integer>> combinations(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>(), result);
        return result;
    }
    
    private static void backtrack(int start, int n, int k, 
                                 List<Integer> currentComb, 
                                 List<List<Integer>> result) {
        if (currentComb.size() == k) {
            result.add(new ArrayList<>(currentComb));
            return;
        }
        
        for (int i = start; i <= n; i++) {
            currentComb.add(i);
            backtrack(i + 1, n, k, currentComb, result);
            currentComb.remove(currentComb.size() - 1);
        }
    }
    
    public static void main(String[] args) {
        int n = 4;
        int k = 2;
        System.out.println("Сочетания из " + n + " по " + k + ":");
        List<List<Integer>> combs = combinations(n, k);
        for (List<Integer> comb : combs) {
            System.out.println(comb);
        }
    }
}