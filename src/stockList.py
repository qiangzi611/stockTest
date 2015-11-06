import tushare as ts
 
stock_list = ts.get_stock_basics()

stock_list.to_csv('E:\stock\data\stocklist.csv')
 
print 'finished!'