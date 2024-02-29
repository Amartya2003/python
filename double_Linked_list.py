class Node:
	def __init__(self, dataPrevious=None, data=None, dataNext=None):
		self.prev = dataPrevious
		self.data = data
		self.next = dataNext
		
class DoubleLinkedList:
	def __init__(self):
		self.head = None
			
	def print_forward(self, node):
		print(node.next)
		
	def print_backward(self, node):
		print(node.prev)
		
	def insert_at_beginning(self, data):
		node = Node(None, data, self.head)
		self.head = node
		
	def print_list(self):
		if self.head == None:
			print("List is empty")
			return
		
		itr = self.head
		llstr = ""
		
		while itr:
			llstr += str(itr.data) + "<-->"
			itr = itr.next
			
		print(llstr)
		
	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None, None)
			
		itr = self.head
		while itr.next:
			itr = itr.next
			
		itr.next = Node(itr.prev, data, None)
			
	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)
			
		

if __name__ == '__main__':
	dll = DoubleLinkedList()
	dll.insert_values([1,2,3,4,5,6,7])
	dll.print_list()
	
