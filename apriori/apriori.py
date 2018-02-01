from collections import Counter
from itertools import combinations
import pickle as cp
# Agnihotra Bhattacharya


def input_transactions():
    trans_list = []
    max_len = -1
    for trans in range(n):
        x = list(map(int, input("Enter items in the transaction (space-separated) >> ").strip().split()))
        trans_list.append(x)
        if len(x) > max_len:
            max_len = len(x)
    cp.dump(trans_list, open("save.p", "wb"))
    return trans_list, max_len


def load_transactions():
    max_len = -1
    trans_list = cp.load(open("save.p", "rb"))
    for i in trans_list:
        if len(i) > max_len:
            max_len = len(i)
    return trans_list, max_len


def apriori(trans_list, max_len, ms):
    # Consider i-item sets
    final = []
    for i in range(1, max_len):                         # Iterates for each level of item-sets
        cnt = Counter()
        for j in trans_list:                            # Iterates for each transaction
            trans_item_set = combinations(j, i)         # Generates i-item subsets/candidates for each transaction
            for k in trans_item_set:                    # Iterates for each i-item subset in the transaction
                cnt[k] += 1                             # Increment
        print("\n=== ", str(i) + "-Item Set === ")
        for z in cnt:                                   # Iterates over each candidate
            if cnt[z] != 0:                             # Ignores zero-count candidates
                print(z, cnt[z])                        # Prints candidate, and its count
                if cnt[z] >= ms:                        # Prunes candidates with support < min support
                    final.append(z)                     # Adds to the final subset
    return final


n = int(input("Number of transactions >> "))
min_support = int(input("Minimum support >> "))
transactions, max_trans_len = load_transactions()
final_set = apriori(transactions, max_trans_len, min_support)
print("Frequent Items: ", final_set)
