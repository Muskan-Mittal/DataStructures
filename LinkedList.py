class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.next_node = None


class Linked_List(object):
	def __init__(self):
		self.head = Node()
		self.size = 0

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


if __name__ == '__main__':
	my_list = Linked_List()

	my_list.append(1)
	my_list.append(2)
	my_list.append(3)

	my_list.display()
