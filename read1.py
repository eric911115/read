data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現的次數為:', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用此查詢功能')

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均長度為', sum_len / len(data))
new =[d for d in data if len(d) < 100]

print('一共有', len(new),'資料小於100')
good =[g for g in data if 'good' in g]
good.append(g)
print('共有', len(good), '筆資料提到good')