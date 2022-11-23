from itertools import combinations

from django.test import TestCase

# Create your tests here.
a = list(range(2))
print(a)
c = combinations(a, 3)
for i in c:
    print(str(i))