class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.next_node = None


class Linked_List(object):
	def __init__(self):
		self.head = Node()

	def append(self, data):
		new_node = Node(data)
		current_node = self.head
		while current_node.next_node is not None:
			current_node = current_node.next_node
		current_node.next_node = new_node

	def length(self):
		current_node = self.head
		total = 0
		while current_node.next_node is not None:
			total += 1
			current_node = current_node.next_node
		return total

	def display(self):
		elements = []
		current_node = self.head
		while current_node.next_node is not None:
			current_node = current_node.next_node
			elements.append(current_node.data)
		print elements

	def get_data_at_an_index(self, index):
		if index >= self.length():
			print "ERROR: Index out of range."
			return None
		current_index = 0
		current_node = self.head
		while True:
			current_node = current_node.next_node
			if current_index is index:
				return current_node.data
			current_index += 1

	def remove_at_an_index(self, index):
		if index >= self.length():
			print "ERROR: Index out of range."
			return
		current_index = 0
		current_node = self.head
		while True:
			previous_node = current_node
			current_node = current_node.next_node
			if current_index is index:
				previous_node.next_node = current_node.next_node
				return
			current_index += 1

	def insert_at_an_index(self, data, index):
		if index >= self.length():
			print "ERROR: Index out of range."
			return
		new_node = Node(data)
		current_index = 0
		current_node = self.head
		while True:
			current_node = current_node.next_node
			if current_index is index:
				new_node.next_node = current_node.next_node
				current_node.next_node = new_node
				return
			current_index += 1


if __name__ == '__main__':
	my_list = Linked_List()

	my_list.append(1)
	my_list.append(2)
	my_list.append(3)

	my_list.display()

	print "Element at 2nd index: %d" % my_list.get_data_at_an_index(2)

	my_list.remove_at_an_index(2)
	print "Element removed at index 2"
	my_list.display()

	my_list.insert_at_an_index(3, 0)
	print "3 inserted at index 0"
	my_list.display()
