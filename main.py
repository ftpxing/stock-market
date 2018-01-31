import easyquotation
import time as tt
import logging as log
import requests

# 命名py脚本时，不要与python预留字，模块名等相同
# 否则会报错AttributeError: module 'easyquotation' has no attribute 'PY_VERSION'
# logging模块配置 https://www.cnblogs.com/yyds/p/6901864.html
# 股市行情获取API https://github.com/shidenggui/easyquotation
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
log.basicConfig(filename='common.log', level=log.INFO, format=LOG_FORMAT)
apiKey = 'c457e4828891683f47ec6ae646330dbe'
mobile = '15613105771'
sms_api = 'https://sms.yunpian.com/v2/sms/single_send.json'


def cycle_check():
    quotation = easyquotation.use('sina')
    # 000651格力电器 000040东旭蓝天 002230科大讯飞
    codes = ['000651', '000040', '002230']
    while 1:
        sys_time = tt.strftime("%H:%M:%S", tt.localtime())
        for code in codes:
            detail = quotation.real(code).get(code)
            name = detail.get('name')
            high = detail.get('high')
            low = detail.get('low')
            time = detail.get('time')
            if (high-low)/high >= 0.03:
                log.error(name+code+'下跌了，发送预警短信')
                send_message(name=name, code=code)
                codes.remove(code)
                log.info(name+code+'被移出关注列表')
        if sys_time > time :
            log.info('<-- 交易关闭了，停止监控')
            break
        tt.sleep(5)


def send_message(name, code):
    text = '【星空科技】名称'+name+' 代码'+code+'价格异常，请及时处理'
    param = {'apikey':apiKey,'text':text,'mobile':mobile}
    headers = {'user-agent': 'my-app/0.0.1','Content-Type':'application/x-www-form-urlencoded'}
    resp = requests.post(url=sms_api,data=param,headers=headers)
    log.info('调用云片短信API回执:'+resp.text)

if __name__ == '__main__':
    log.info('开始监控 -->')
    cycle_check()
