'''
This is a hash table implemented by chains
when there is a collisium, append it in a chain
The class include:
1.hashvalue: static, get hash value
2.insert
3.get
4.remove
'''

class HashTable:
	def __init__(self,cap = 11):
		self.cap = cap
		self.slots = [[] for _ in range(self.cap)]
		self.size = 0

	@staticmethod
	def hashvalue(key):
		key = str(key)
		value = 0
		i = 1
		for cha in key:
			value += ord(cha)*i
			i += 1
		return value

	def index(self,hashvalue):
		return hashvalue % self.cap

	def insert(self,key,value):
		currentindex = self.index(HashTable.hashvalue(key))
		key_exists = False
		currentslot = self.slots[currentindex]
		for i,kv in enumerate(currentslot):
			k,v = kv
			if k == key:
				key_exists = True
				break
		if(key_exists):
			currentslot[i] = [key,value]
		else:
			currentslot.append([key,value])
			self.size += 1
		return True

	def get(self,key):
		currentindex = self.index(HashTable.hashvalue(key))
		currentslot = self.slots[currentindex]
		i = 0
		for i,kv in enumerate(currentslot):
			k,v = kv
			if k == key:
				return v
		return False
	def remove(self,key):
		currentindex = self.index(HashTable.hashvalue(key))
		currentslot = self.slots[currentindex]
		i = 0
		for i,kv in enumerate(currentslot):
			k,v = kv
			if k == key:
				del currentslot[i]
				return True
		return False

	def print(self):
		for i,currentslot in enumerate(self.slots):
			print(i,currentslot)

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,value):
		return self.insert(key,value)
	def __delitem__(self,key):
		return self.remove(key)

#Test class
H=HashTable(5)
H[54]='cat'
H[26]='dog'
H[20]="chicken"
H[31]="chicken2"
#print(H.slots)
print(f"size:{H.size}")
print(H[20])
H.print()
del H[54]
H.print()

