#encoding:utf-8
import numpy as np
import pandas as pd
import time

def formatTime(x):
    date = str(x['Date'])
    recevied_date = str(x['Date_received'])
    coupon = str(x['Coupon_id'])
    if(date == 'nan' or recevied_date == 'nan' or coupon == 'nan'):
        return 0
    beginTime = time.mktime(time.strptime(recevied_date, '%Y%m%d'))
    endTime = time.mktime(time.strptime(date, '%Y%m%d'))
    if((endTime - beginTime) / (24 * 60 * 60) < 15):
        return 1
    else:
        return 0

def formatDiscount(x):
    rate = str(x['Discount_rate'])
    if(rate == 'nan'):
        return 0
    else:
        a = rate.split(':')
        if(len(a) < 2):
            return 0
        else:
            return float(a[0]) / float(a[1])

df = pd.read_csv(open('/Users/ouakira/Downloads/ccf_offline_stage1_train.csv'), dtype=np.str, delimiter=",")

# clean = df.dropna()
# clean['time'] = clean.apply(formatTime, axis=1)
# clean = clean.drop('Date_received', axis = 1)
# clean = clean.drop('Date', axis = 1)
# clean['distance'] = clean.apply(formatDistance, axis=1)
# clean = clean.drop('Distance', axis = 1)
# clean = clean.drop('Discount_rate', axis = 1)

target = df.apply(formatTime, axis=1)
df = df.drop('Date_received', axis = 1)
df['distance'] = df.apply(formatDiscount, axis=1)
df = df.drop('Discount_rate', axis = 1)
df = df.fillna(0)
print(df)
from sklearn import svm
clf = svm.SVC(C=10000.0, kernel='rbf')
clf = clf.fit(df, target)
tdf = pd.read_csv(open('/Users/ouakira/Downloads/ccf_offline_stage1_test_revised.csv'), dtype=np.str, delimiter=",")
tdf['distance'] = tdf.apply(formatDiscount, axis=1)
tdf = tdf.drop('Discount_rate', axis = 1)
tdf = tdf.fillna(0)
pred = clf.predict(tdf)
print(pred)
print(np.sum(pred == 1))



