# import pandas as pd
import os
import time
# from datetime import datetime

path = 'data/intraQuarter'


def Key_Stats(gather='Total Debt/Equity (mrq)'):
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    # print(stock_list)
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        print(each_dir)
        # ticker = each_dir.split('/')[1]
        ticker = os.path.basename(os.path.normpath(each_dir))
        if len(each_file) > 0:
            for fn in each_file:
                # date_stamp = datetime.strptime(fn, '%Y%m%d%H%M%S.html')
                # unix_time = time.mktime(date_stamp.timetuple())
                # print(date_stamp, unix_time)
                full_file_path = each_dir + '/' + fn
                # print(full_file_path)
                source = open(full_file_path, 'r').read()
                # print(source)
                value = source.\
                    split(gather + ':</td><td class="yfnc_tabledata1">')[1].\
                    split('</td>')[0]
                print(ticker + ':', value)

                time.sleep(3)

Key_Stats()
