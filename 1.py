def combinations(n, k):
    result = []
    
    def backtrack(start, current_comb):
        if len(current_comb) == k:
            result.append(current_comb.copy())
            return
        
        for i in range(start, n + 1):
            current_comb.append(i)
            backtrack(i + 1, current_comb)
            current_comb.pop()
    
    backtrack(1, [])
    return result

# Пример использования
n = 4
k = 2
print(f"Сочетания из {n} по {k}:")
for comb in combinations(n, k):
    print(comb)