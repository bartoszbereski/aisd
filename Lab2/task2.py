if __name__ == '__main__':
	f = open('zadanie2.csv', 'r')
	items = []
	for line in f:
		val = line.split(',', 1)[1].replace('\n', '').lower()
		if val != '' and val != 'val':
			items.append({'id': 0, 'val': val})
	for i in range(len(items)):
		items[i]['id'] = i + 1
		items[i]['val'].lower()
		deleted_words = []
		for word in items[i]['val'].split(' '):
			if len(word) > 2:
				if abs(ord(word[0]) - ord(word[1])) == 1 :
					items[i]['val'].replace(word,'')
					deleted_words.append(word)
		print(items[i]['id'], deleted_words)