import easyquotation
import time as tt
import logging as log

# 命名py脚本时，不要与python预留字，模块名等相同
# 否则会报错AttributeError: module 'easyquotation' has no attribute 'PY_VERSION'

# logging模块配置 https://www.cnblogs.com/yyds/p/6901864.html
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
log.basicConfig(filename='common.log', level=log.DEBUG, format=LOG_FORMAT)
quotation = easyquotation.use("sina")
# quotation.market_snapshot(prefix=True)
平安银行 = quotation.real('000001')
detail = 平安银行.get('000001')
log.info("this is info log")
log.error("this is error log")

while 1:
    name = detail.get('name')
    time = detail.get('time')
    high = detail.get('high')
    now = detail.get('now')
    open = detail.get('open')
    low = detail.get('low')
    print(name+'----'+time)
    print('开盘：'+str(open))
    print('今日最高：'+str(high))
    print('今日最低：'+str(low))
    print('当前：'+str(now))
    print((now-high)/high)
    tt.sleep(10)
