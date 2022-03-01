import pandas as pd
from finance.utils import Calculator
pip install mpl-finance
pip install --upgrade mplfinance

data = [['December, 2011', 44.89], ['January, 2012', 46.76],['February, 2012', 47.55],
['March, 2012', 54.73],['April, 2012', 56.17],['May, 2012', 53.91],
['June, 2012', 52.37],['July, 2012', 44.47],['August, 2012', 48.91],
['September, 2012', 50.00],['October, 2012', 45.26],['November, 2012', 51.36],
['December, 2012', 53.10]]

starbucks = pd.DataFrame(data, columns=['Date', 'Value']).set_index('Date')['Value']

#Question 1: Using the data in the table, what is the simple monthly return between the
#end of December 2004 and the end of January 2005?

Calculator.ret(starbucks, pos=1)
