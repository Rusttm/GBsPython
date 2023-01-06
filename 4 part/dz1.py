# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import decimal
import math

d = 0.001
x = math.pi

D = decimal.Decimal
result = D(f"{x}").quantize(D(f"{d}"), decimal.ROUND_DOWN)
print(f'При {d=} pi={result}')