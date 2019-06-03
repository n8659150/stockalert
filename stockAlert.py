
# coding: utf-8
import win32api
import win32con
import tushare
import win32serviceutil
import win32service
import win32event
import time

# gbk转码，为防止在WINDOWS系统的cmd中输出中文乱码
def gbkEncode(text):
    return text.decode('utf-8').encode('gbk')
def unicode2GBK(text):
    return text.encode('gbk')

def stockAlert(stockId,priceLine,timeout):
    while 1:

        stockInfo = tushare.get_realtime_quotes([stockId])

        stockName = stockInfo.iloc[0,0]
        stockPrice = float(stockInfo.iloc[0,2])

        stockPriceStr = '%.2f'%stockPrice
        print (stockId + "---" + unicode2GBK(stockName) + gbkEncode(' 目前股价:') + stockPriceStr)

        if (stockPrice - float(priceLine)) >= 0:

            msg = stockName + ':' + stockPriceStr

            win32api.MessageBox(0,msg,u'股价提醒',win32con.MB_OK)

            break
        # 每2分钟查询一次
        time.sleep(timeout)




