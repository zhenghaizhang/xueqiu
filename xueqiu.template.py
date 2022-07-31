import requests
import time
import sys

time.sleep(2)

# 输入持有的票的代码和股数
codes = {
    "SZ000591": 0,
    "SH600893": 0,
}

daystart = 0 # 截止到昨天月收益
daydelta = 0  # 当天修正数

# 每个月的盈亏，后续计算年度盈亏
monthall = [
            -0.20,
            -123.00,  # month1
            +123.00,   # month2
            -123.00,  # month3
            -123.00, # month4
            +123.00,   # month5
            +123.00,   # month6
            +123.00,   # month7
]

# 填写自己账户的cookie
Cookie = 'xxxxxx'
UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'

headers = {
    'Cookie': Cookie,
    'User-Agent': UserAgent
}

timeformat = time.strftime("%H:%M:%S", time.localtime()) # 格式化当前时间
datetimeformat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if (timeformat > '09:15:00' and timeformat < '11:32:00')  or (timeformat > '13:00:00' and timeformat < '15:02:00'):
    print('-'*30)
    sumall = {} 
    # print(datetimeformat)
    # session = requests.Sesson()
    
    for code in codes.keys():
        url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol='+code+'&extend=detail'
        # print(url)
        r = requests.get(url, headers=headers).json()
        # print(r)
        rdata = r.get('data').get('quote')
        result = {}
        result['code'] = rdata.get('code')
    #    result['name'] = rdata.get('name')
        result['last_close'] = rdata.get('last_close')
        result['current'] = rdata.get('current')
        result['high'] = rdata.get('high')
        result['low'] = rdata.get('low')
    
        sumall[code] = (result['current'] - result['last_close']) * codes.get(code)
        print(result, str(round((result['current'] - result['last_close'])/result['last_close']*100, 2))+'%', str(round(sumall[code], 2)))
    
    # print('Today： ', str(round(sum(sumall.values())-210-781.2, 2)))
    today = round(sum(sumall.values()) + daydelta, 2)
    print(datetimeformat, '  Today: ', str(today), '  Month: ', str(round(today + daystart, 2)), '  Year: ', str(round(sum(monthall), 2)))
    
    time.sleep(2)
    for i in range(0, 55, 2):
        sys.stdout.write(str(i+1)+' ')
        time.sleep(2)
        sys.stdout.flush()
    
    print()
else:
    # pass
    print(datetimeformat, '  duchang bu kai men!')

