Реализация алгоритма для генерации всех возможных сочетаний размера k из n элементов с использованием метода backtracking.





Python
python
def combinations(n, k):
    """
    Генерирует все сочетания размера k из n элементов
    """
    result = []
    
    def backtrack(start, current_comb):
        # Базовый случай: достигли нужного размера сочетания
        if len(current_comb) == k:
            result.append(current_comb.copy())
            return
        
        # Рекурсивный случай: добавляем новые элементы
        for i in range(start, n + 1):
            current_comb.append(i)
            backtrack(i + 1, current_comb)  # i+1 гарантирует уникальность
            current_comb.pop()  # backtracking
    
    backtrack(1, [])
    return result

# Пример использования
if __name__ == "__main__":
    n = 4
    k = 2
    print(f"Сочетания из {n} по {k}:")
    for comb in combinations(n, k):
        print(comb)






Java
java
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
        // Базовый случай: достигли нужного размера сочетания
        if (currentComb.size() == k) {
            result.add(new ArrayList<>(currentComb));
            return;
        }
        
        // Рекурсивный случай: добавляем новые элементы
        for (int i = start; i <= n; i++) {
            currentComb.add(i);
            backtrack(i + 1, n, k, currentComb, result);  // i+1 гарантирует уникальность
            currentComb.remove(currentComb.size() - 1);  // backtracking
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




C++
cpp
#include <iostream>
#include <vector>
using namespace std;

void backtrack(int start, int n, int k, vector<int>& currentComb, vector<vector<int>>& result) {
    // Базовый случай: достигли нужного размера сочетания
    if (currentComb.size() == k) {
        result.push_back(currentComb);
        return;
    }
    
    // Рекурсивный случай: добавляем новые элементы
    for (int i = start; i <= n; i++) {
        currentComb.push_back(i);
        backtrack(i + 1, n, k, currentComb, result);  // i+1 гарантирует уникальность
        currentComb.pop_back();  // backtracking
    }
}

vector<vector<int>> combinations(int n, int k) {
    vector<vector<int>> result;
    vector<int> currentComb;
    backtrack(1, n, k, currentComb, result);
    return result;
}

int main() {
    int n = 4;
    int k = 2;
    cout << "Сочетания из " << n << " по " << k << ":" << endl;
    vector<vector<int>> combs = combinations(n, k);
    for (auto comb : combs) {
        for (int num : comb) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}





Алгоритм работы
Принцип работы (на примере Python кода)

def combinations(n, k):
    result = []  # Создаем список для хранения всех найденных сочетаний
Инициализация результата - создаем пустой список, куда будем сохранять все валидные сочетания.


def backtrack(start, current_comb):
Рекурсивная функция backtrack - основная функция, которая строит сочетания:

start - номер, с которого начинаем добавлять элементы (гарантирует уникальность)

current_comb - текущее формируемое сочетание

if len(current_comb) == k:
    result.append(current_comb.copy())
    return
Базовый случай рекурсии - проверяем, достигли ли мы нужного размера сочетания:

Если current_comb содержит k элементов, сохраняем копию в результат

return завершает текущую ветвь рекурсии

for i in range(start, n + 1):
Цикл перебора элементов - перебираем все числа от start до n:

start гарантирует, что элементы будут в возрастающем порядке

Это предотвращает дубликаты типа [1,2] и [2,1]

current_comb.append(i)
Добавление элемента - добавляем текущее число i в формируемое сочетание

backtrack(i + 1, current_comb)
Рекурсивный вызов - вызываем функцию для следующего уровня:

i + 1 гарантирует, что следующие элементы будут больше текущего

Это обеспечивает уникальность и правильный порядок элементов

current_comb.pop()
Backtracking шаг - удаляем последний элемент перед переходом к следующей итерации:

"Откатываем" изменение, чтобы попробовать другой вариант

Позволяет исследовать альтернативные ветви перебора

backtrack(1, [])
Начальный вызов - запускаем рекурсию с начальными параметрами:
start = 1 - начинаем с первого элемента
[] - пустое начальное сочетание

Временная сложность
Общая сложность: O(C(n,k) × k)
Объяснение
Алгоритм генерирует все C(n,k) сочетаний
Каждое сочетание копируется за O(k) операций
Общая сложность: O(C(n,k) × k)


Примеры ввода-вывода
Пример 1
Ввод:
n = 4, k = 2
Вывод:
Сочетания из 4 по 2:
[1, 2]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
[3, 4]


Пример 2
Ввод:
n = 3, k = 1
Вывод:
Сочетания из 3 по 1:
[1]
[2]
[3]



Пример 3
Ввод:
n = 5, k = 3
Вывод:
Сочетания из 5 по 3:
[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 3, 4]
[1, 3, 5]
[1, 4, 5]
[2, 3, 4]
[2, 3, 5]
[2, 4, 5]
[3, 4, 5]
