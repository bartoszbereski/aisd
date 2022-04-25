class Hanoi:
	def __init__(self):
		self.count = 1
	def hanoi(self,n, sour, dest, buff):
		if n==1 :
			print(f'Move disk from {sour} source to {dest} dest, moves: {self.count}')
			return
		self.hanoi(n-1, sour, buff, dest)
		self.count += 1
		print(f'Move disk from {sour} source to {dest} dest , moves: {self.count}')
		self.count += 1
		self.hanoi(n-1, buff, dest, sour)

if __name__ == '__main__':
	n = 4
	k = Hanoi()
	Hanoi.hanoi(k,n,'A','B','C')