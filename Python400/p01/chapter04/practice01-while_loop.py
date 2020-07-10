#!/usr/bin/env python
# -*- coding: utf-8 -*-

sum1 = 0  # 所有和
sum2 = 0  # 奇数和
sum3 = 0  # 偶数和
n = 1

while n <= 100:
    sum1 += n
    if n % 2 == 0:
        sum3 += n
    else:
        sum2 += n
    n += 1

print("1-100的所有数字的累加和为{0}, 所有奇数的和为{1}， 所有偶数的和为{2}。"\
      .format(sum1, sum2, sum3))
