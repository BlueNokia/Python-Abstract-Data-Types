
class stack:
	def __init__(self):
		self.list = []
		
	def isEmpty (self):
		return self.list == []
		
	def push ( self, num):
		 self.list.append(num)
		 
	def pop ( self):
		return self.list.pop()
		
	def peek ( self):
		return self.list[len(self.list) - 1]
		
	def print_currentStack( self):
		print "The current stack is:"
		for i in range(len(self.list)):
			print self.list[len(self.list) - i - 1]
		print "End of Stack"
		
	def size( self):
		return len(self.list)
		
if __name__ == '__main__':
	S = stack()
	print S.isEmpty()
	S.push(4)
	S.push(9)
	S.push(0)
	S.push(-2)
	S.print_currentStack()
	print S.pop()
	print S.pop()
	S.print_currentStack()
	print S.size()
	print S.peek()
	
