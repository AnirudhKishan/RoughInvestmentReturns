from __future__ import division

import math, numpy

invested = int(input("Invested: "))
current = int(input("Current: "))
months = int(input("Months: "))

values = []

for i in range(months):
	values.append(-(invested/months))

values.append(current)

irr_monthly = numpy.irr(values)

irr_annual = ((1 + irr_monthly) ** 12) - 1

print("{0:.2%}".format(irr_annual))
