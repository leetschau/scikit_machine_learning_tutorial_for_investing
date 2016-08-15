import pandas as pd
import os
import time
from datetime import datetime

path = 'data/intraQuarter'


def Key_Stats(gather='Total Debt/Equity (mrq)'):
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns=['Date', 'Unix', 'Ticker', 'DE Ratio'])
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = os.path.basename(os.path.normpath(each_dir))
        if len(each_file) > 0:
            for fn in each_file:
                date_stamp = datetime.strptime(fn, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir + '/' + fn
                source = open(full_file_path, 'r').read()
                try:
                    value = float(
                        source.split(
                            gather +
                            ':</td><td class="yfnc_tabledata1">')[1].
                        split('</td>')[0])
                    df = df.append({'Date': date_stamp,
                                    'Unix': unix_time,
                                    'Ticker': ticker,
                                    'DE Ratio': value},
                                   ignore_index=True)
                except Exception as e:
                    print(e)

    resfile = gather.replace(' ', '').replace(')', '').replace('(', '').\
        replace('/', '') + '.csv'
    print(resfile)
    df.to_csv(resfile)

Key_Stats()
