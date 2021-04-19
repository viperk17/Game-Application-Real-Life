"""
Task

is a shoe shop owner. His shop has number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay

amount of money only if they get the shoe of their desired size.

Your task is to compute how much money

earned.

Input Format

The first line contains
, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next lines contain the space separated values of the desired by the customer and , the price of the shoe.

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

"""

from collections import Counter

n = int(input())
s = Counter(map(int, input().split()))
x = int(input())

total = []

for i in range(x):
    a, b = map(int, input().split())
    print(a, b)
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print(sum(total))
