import sys
sys.setrecursionlimit(10**5)

class JavaClass:

	def __init__(self, name):
		self.__name = name
		self.__parent = None
		self.__children = list()
	
	def set_parent(self, parent):
		self.__parent = parent

	def add_child(self, child):
		self.__children.append(child)

	def is_child_of(self, java_class):
		if not self.__parent:
			return False
		elif self.__parent == java_class:
			return True
		else:
			return self.__parent.is_child_of(java_class)

	def is_parent_of(self, java_class):
		if not self.__children:
			return False
		elif java_class in self.__children:
			return True
		else:
			result = False
			for child in self.__children:
				result |= child.is_parent_of(java_class)
				if result: break
			return result

	def is_family(self, java_class):
		return int(self.is_child_of(java_class) or self.is_parent_of(java_class))

def input():
	return sys.stdin.readline()

def generate_class(child, parent):
	if parent not in classes:
		classes[parent] = JavaClass(parent)
	if child not in classes:
		classes[child] = JavaClass(child)
	classes[child].set_parent(classes[parent])
	classes[parent].add_child(classes[child])

N = int(input())
classes = dict()
for _ in range(N-1):
	A, B = input().split()
	generate_class(A, B)

A, B = input().split()
print(classes[A].is_family(classes[B]))