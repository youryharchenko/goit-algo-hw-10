import random

from collections import Counter

class Coins():

    def __init__(self, nominals: list[int]) -> None:
        self.nominals = sorted(nominals, reverse=True)

    def find_coins_greedy(self, sum: int):
        
        nominals = sorted(self.nominals, reverse=True)

        result = {}
        total_coins = 0
        rest = sum
        while rest > 0:
            for c in nominals:
               if c <= rest:
                    count = result.get(c, 0)
                    result[c] = count + 1
                    rest -= c 
                    total_coins += 1
                    break
            else:
                raise ValueError("Нема монет з потрібним номіналом")
               
        return result, total_coins


    def find_min_coins(self, sum: int):
        infinity = 10000

        dp = {}
        dp[0] = 0

        used_coins = {}
        used_coins[0] = []

        for i in range(sum):
            best_count = infinity
            best_set = None
            
            for c in self.nominals:
                if (i+1) - c in dp:
                    # Якщо для попередньої суми вже є рішення
                    current_count = 1 + dp[(i+1) - c]
                    
                    if current_count < best_count:
                        # Якщо це кращий варіант
                        best_count = current_count
                        best_set = used_coins[(i+1) - c] + [c]

            if best_set:
                dp[i+1] = best_count
                used_coins[i+1] = best_set

        # Результат
        if sum in dp:
            return Counter(used_coins[sum]), dp[sum] 
        else:
            raise ValueError("Нема монет з потрібним номіналом")


            

def main():

    coins_nominals = [50, 25,  10, 5, 2, 1]
    random.shuffle(coins_nominals)

    print(f"Номінали монет в копійках: {coins_nominals}")

    coins = Coins(coins_nominals)

    #suma = 1234567890
    suma = 113
    print(f"Сума в копійках: {suma}")

    result, total = coins.find_coins_greedy(suma)
    print(f"Жадібний алгоритм: {result}, монет: {total}")
    
    result, total = coins.find_min_coins(113)
    print(f"Динамічне програмування: {result}, монет: {total}")

    print("") 
    




    

