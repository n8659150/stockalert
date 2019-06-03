
# coding: utf-8
import stockAlert
# gbkEncode 用于解决中文字符在windows平台的cmd下显示为乱码的问题
stockId = raw_input(stockAlert.gbkEncode('请输入股票代码：'))

priceLine = raw_input(stockAlert.gbkEncode('请输入提醒股价：'))

timeout = input(stockAlert.gbkEncode('请输入查询间隔（秒）'))

print (stockAlert.gbkEncode('当 股票' + stockId + '每股价格大于' + priceLine + '时，将会弹窗提醒'))

stockAlert.stockAlert(stockId,priceLine,timeout)




