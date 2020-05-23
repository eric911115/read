data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len += len(d)
print('平均長度為', sum_len / len(data))
new =[d for d in data if len(d) < 100]

print('一共有', len(new),'資料小於100')
good =[g for g in data if 'good' in g]

print('共有', len(good), '筆資料提到good')