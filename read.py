data = []
count = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		count = count +1
		data.append(line)
		if count % 1000 == 0 :
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

total_len = 0
for d in data :
	total_len += len(d)
print('留言平均長度為: ',total_len/ len(data))
