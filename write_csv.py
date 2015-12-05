#coding:utf-8
import csv
csvfile = file('csv_test.csv','web')
writer = csv.writer(csvfile)
writer.writerow(['姓名','年龄','电话'])

data = [('小红','22','13813009876'),
		('小明','19','13813009866')
		]
writer.writerow(data)
csvfile.close()