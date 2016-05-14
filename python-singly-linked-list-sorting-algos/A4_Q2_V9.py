class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

   ##Testing out github

   ##hello

<<<<<<< HEAD:A4_Q2_V9.py
   ##omg I can't

=======
>>>>>>> 7c0bb1dd4c5e84a964b6550307b7cf3fc0fe5baa:python-singly-linked-list-sorting-algos/A4_Q2_V9.py
'''A4_Q2_V9 testing all of the sorting methods'''

class Person:
	def __init__(self, name, personality):
		self.name = name
		self.personality = personality
	def getPersonality(self):
		return self.personality
	def __str__(self):
		return "Name - " + self.name + "||Personality - " + str(self.personality)

class Chair:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
	def set_data(self, data):
		self.data = data
	def get_data(self):
		return self.data
	def set_next(self, next):
		self.next = next
	def get_next(self):
		return self.next
	def __str__(self):
		return "chair: " + self.data.name + " || " + str(self.data.personality)


class Classroom:
	def __init__(self):
		self.head = None
		self.last = None
		self.length = 0

	def insert(self, person):
		'''inserts a person to the head of the classroom'''
		temp = Chair(person)
		if person == None:
			'''case 1: no person is added'''
			print("There is no person to insert!")
		if self.head == None:
			'''case 2: classroom is empty'''
			self.head = temp
			self.last = temp
			self.length = 1
		else:
			temp.set_next(self.head)
			self.head = temp
			self.length += 1

	def add(self, person):
		'''Adds the person to the correct position in the list'''
		temp = Chair(person)
		if self.head == None:
			'''case 1: empty list'''
			self.head = temp
			self.last = temp
		elif temp.get_data().personality < self.head.get_data().personality:
			temp.set_next(self.head)
			self.head = temp
		elif temp.get_data().personality > self.last.get_data().personality:
				self.last.set_next(temp)
				self.last = temp
		else:
			current = self.head
			next = self.head.get_next()
			while next != None:
				if temp.get_data().personality < next.get_data().personality:
					temp.set_next(next)
					current.set_next(temp)
					break
				current = next
				next = current.get_next()

	def contains(self, personality):
		'''checks if personality is contained the list/classroom and returns a 
		boolean value'''
		f = False
		current = self.head
		while current != None:
			if current.get_data().personality == personality:
				f = True
				break
			current = current.get_next()
		return f

	def remove(self, personality):
		'''finds the person based on his/her personality rating and removes the 
		person from the list'''
		if self.head == None:
			'''case 1: empty classroom'''
			print("There are no chairs in this classroom! Cannot remove anything")
		if self.contains(personality) == False:
			'''case 2: personality is not in the classroom'''
			print(str(personality) + " is not in the list!")
		if self.head.get_data().personality == personality:
			self.head = self.head.get_next()
			self.length -= 1
		else:
			prev = self.head
			current = self.head.get_next()
			while current != None:
				if current.get_data().personality == personality:
					prev.set_next(current.get_next())
					current.set_next(None)
					self.length -= 1
					break
				prev = current
				current = prev.get_next()

	def bubble_sort(self):
		'''bubble sort the classroom'''
		if self.head == None:
			'''case 1: empty classroom'''
			print("There's nothing to sort!")
		if self.head == self.last:
			'''case 2: only one chair in the classroom'''
			print("There's only one element in the list!")
		else:
			sorted = False
			count = 0
			while not sorted:
				sorted = True
				prev = self.head
				current = self.head.get_next()
				while current != None:
					if prev.get_data().personality > current.get_data().personality:
						sorted = False
						temp = prev.get_data()
						prev.set_data(current.get_data())
						current.set_data(temp)
						count += 1
						print("swap " + str(count) + ": " + self.return_list())
						print(" ")
					prev = current
					current = current.get_next()

	def insertion_sort(self):
		'''insertion sort the classroom'''
		if self.head == None:
			'''case 1: empty classroom'''
			print("There's nothing to sort!")
		if self.head == self.last:
			'''case 2: one chair in classroom'''
			print("There's on one element in the list!")
		else:
			prev = self.head
			current = self.head.get_next()
			while current != None:
				if prev.get_data().personality > current.get_data().personality:
					print("head: " + str(self.head.get_data().personality))
					print("prev: " + str(prev.get_data().personality))
					print("current: " + str(current.get_data().personality))
					self.print_list()
					print("  ")
					prev.set_next(current.get_next())
					current_1 = self.head
					next = self.head.get_next()
					while current_1 != prev.get_next():
						if current.get_data().personality < self.head.get_data().personality:
							current.set_next(self.head)
							self.head = current
							break
						elif current.get_data().personality < next.get_data().personality:
							current.set_next(next)
							current_1.set_next(current)
							break
						current_1 = next
						next = current_1.get_next()
				prev = current
				current = current.get_next()

	def find_chair(self, person):
		'''finds the chair containing the person in the classroom -> returns the chair
		   used as a helper function to other sorting methods'''
		found = False
		current = self.head
		while current != None:
			if current.get_data() == person:
				found = True
				return current
				break
			current = current.get_next()

	def print_list(self):
		'''prints the list'''
		a = []
		current = self.head
		while current != None:
			a.append(current.get_data().name + " : " + str(current.get_data().personality))
			current = current.get_next()
		print(bcolors.OKGREEN + str(a) + bcolors.ENDC)

	def return_list(self):
		'''returns the list'''
		a = []
		current = self.head
		while current != None:
			a.append(current.get_data().name + " : " + str(current.get_data().personality))
			current = current.get_next()
		return(str(bcolors.OKGREEN + str(a) + bcolors.ENDC))

	def swap(self, A, B):
		'''swaps the data in two chairs'''
		temp = A.get_data()
		A.set_data(B.get_data())
		B.set_data(temp)

	def partition_chair(self, lo_person_chair, hi_person_chair):
		'''partitions the list using the last person in the classroom as the pivot'''
		pivot = hi_person_chair
		print(bcolors.WARNING + "pivot: " + str(pivot.get_data()) + bcolors.ENDC)
		hi_chair = hi_person_chair
		print(bcolors.WARNING + "hi_chair: " + str(hi_chair.get_data()) + bcolors.ENDC)
		current = lo_person_chair
		print(bcolors.WARNING + "current: " + str(current.get_data()) + bcolors.ENDC)
		switcher = current
		while current != hi_chair:
			if current.get_data().personality < pivot.get_data().personality:
				print("current: " + str(current.get_data().personality))
				print("pivot: " + str(pivot.get_data().personality))
				self.print_list()
				self.swap(switcher, current)
				switcher = switcher.get_next()
			print("current: " + str(current.get_data().personality))
			print("pivot: " + str(pivot.get_data().personality))
			self.print_list()
			current = current.get_next()
		self.swap(pivot, switcher)
		print("final partition: " + self.return_list())
		return switcher

	def quick_sort(self, lo_person_chair, hi_person_chair):
		print("quick sort was called!")
		self.print_list()
		if self.is_after_chair(lo_person_chair, hi_person_chair) == True:
			m = self.partition_chair(lo_person_chair, hi_person_chair)
			self.quick_sort(m.get_next(), self.last)
			lower = self.find_before(self.head, self.last, m)
			self.quick_sort(lo_person_chair, lower)

	def find_before(self, first_chair, last_chair, person_chair):
		'''find the chair before the person_chair'''
		print("find_before was called")
		current = first_chair
		last = last_chair
		personn = person_chair
		print("current: " + current.get_data().name)
		print("last: " + last.get_data().name)
		#print(last.get_next().get_data().name)
		while current != last.get_next():
			if current.get_next() == personn:
				print("before person was found: " + current.get_data().name)
				return current
				break
			current = current.get_next()
		return None

	def is_after_chair(self, first_chair, last_chair):
		'''boolean: returns True if the last_chair is after first_chair'''
		print("is_after_chair was called")
		if first_chair == last_chair:
			found = False
		elif first_chair == None or last_chair == None:
			found = False
		else:
			current = first_chair
			print(current.get_data().name)
			lastt = last_chair
			found = False
			while current != None:
				if lastt == current:
					found = True
					return True
					break
				current = current.get_next()
		return found	
	
	def get_length(self):
		return self.length

	def radix_sort(self):
		'''radix sort the classroom'''
		if self.head == None:
			print("The Classroom is empty!")
		elif self.head == self.last:
			print("There is only one person in the classroom")
		else:
			len_list = self.get_length()
			modulus = 10
			div = 1
			while True:
				new_list = [[],[],[],[],[],[],[],[],[],[]]
				current = self.head
				while current != None:
					current_value = current.get_data().personality
					least_digit = current_value % modulus
					least_digit /= div
					least_digit = int(least_digit)
					new_list[least_digit].append(current)
					current = current.get_next()
					#self.print_list()
				modulus = modulus * 10
				div = div * 10

				if len(new_list[0]) == len_list:
					print("done")
					break
				self.head = None
				self.last = None #clears the classroom
				A = [str(a) for i in new_list for a in i]
				print(A)
				print(" ")
				for x in reversed(new_list):
					for y in reversed(x):
						self.insert(y.get_data())
	def clear(self):
		self.head = None
		self.last = None

def main():
	##Testing Area##
	Rebecca = Person("Rebecca", 50)
	Samantha = Person("Samantha", 34)
	Andrew = Person("Andrew", 89)
	Charlie = Person("Charlie", 69)
	Martha = Person("Martha", 2)
	Alex = Person("Alex", 65)
	Robert = Person("Robert", 3)
	May = Person("May", 71)

	print("===========TESTING AREA============")

	B = Classroom()
	B.insert(Samantha)
	B.insert(Rebecca)
	B.insert(Andrew)
	B.insert(Martha)
	B.insert(Charlie)
	B.insert(Alex)
	B.insert(Robert)
	B.insert(May)

	print("=========TESTING BUBBLE SORT=========")

	B.print_list()

	print("================START===============")
	B.bubble_sort()

	print("===========FINAL LIST===============")
	B.print_list()
	B.clear()

	###########################################

	print("========TESTING INSERTION SORT========")

	B = Classroom()
	B.insert(Samantha)
	B.insert(Rebecca)
	B.insert(Andrew)
	B.insert(Martha)
	B.insert(Charlie)
	B.insert(Alex)
	B.insert(Robert)
	B.insert(May)

	B.print_list()

	print("================START===============")
	B.insertion_sort()

	print("===========FINAL LIST===============")
	B.print_list()
	B.clear()

	###########################################

	print("========TESTING QUICK SORT========")

	B = Classroom()
	B.insert(Samantha)
	B.insert(Rebecca)
	B.insert(Andrew)
	B.insert(Martha)
	B.insert(Charlie)
	B.insert(Alex)
	B.insert(Robert)
	B.insert(May)


	B.print_list()

	print("================START===============")
	B.quick_sort(B.head, B.last)

	print("===========FINAL LIST===============")
	B.print_list()
	B.clear()

	###########################################

	print("========TESTING RADIX SORT========")

	B = Classroom()
	B.insert(Samantha)
	B.insert(Rebecca)
	B.insert(Andrew)
	B.insert(Martha)
	B.insert(Charlie)
	B.insert(Alex)
	B.insert(Robert)
	B.insert(May)

	B.print_list()

	print("================START===============")
	B.radix_sort()

	print("===========FINAL LIST===============")
	B.print_list()

if __name__ == "__main__":
	main()




	# print("head: " + B.head.get_data().name)
	# print("last: " + B.last.get_data().name)
	# print(B.get_length())
