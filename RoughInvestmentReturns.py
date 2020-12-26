from __future__ import division

import math, numpy
from datetime import date

def get_months(start_date, end_date):
    '''
    Gets the monthes between two dates
    '''
    start_month, start_year = start_date.split(":")
    end_month, end_year = end_date.split(":")
    return (int(end_year)-int(start_year))*12 + (int(end_month)-int(start_month))

invested = int(input("Invested: "))
current = int(input("Current: "))
months = input("Enter either Number of Months or A Start Date (MM:YYYY): ")

if ":" in months:
    # Create an object of the datetime module
    today = date.today()
    # Set the format to be MM:YYYY
    date = today.strftime("%m:%Y")
    months = get_months(start_date= months, end_date= date)
else:
    months = int(months)


values = []

for i in range(months):
    values.append(-(invested/months))

values.append(current)

irr_monthly = numpy.irr(values)

irr_annual = ((1 + irr_monthly) ** 12) - 1

print("{0:.2%}".format(irr_annual))
