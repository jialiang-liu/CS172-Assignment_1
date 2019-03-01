#!/usr/bin/env python3

import os
import math
import time

# Preparation for records
ddata = os.path.dirname(__file__) + "/data"
ndoc = len([name for name in os.listdir(ddata) if os.path.isfile(os.path.join(ddata, name))])
nterm = [0 for i in range(ndoc)]

# Stop-words
pstop = os.path.dirname(__file__) + "/stoplist.txt"
stoplist = []
with open(pstop, 'r') as f:
	for line in f:
		stoplist.append(line.strip())

# Using dictionary to store terms
# Using linked list to store the frequency
dterm = {}
class Node(object):
	def __init__(self):
		self.docID = 0
		self.docFreq = 0
		self.next = None
class List(object):
	def __init__(self):
		self.head = None
		self.length = 0
	# Create a node for a document that has this term
	def append(self, Node):
		if not self.head:
			self.head = Node
		else:
			node = self.head
			while node.next:
				node = node.next
			node.next = Node
		self.length += 1
	# Update the frequency of a term for a specific document
	def update(self, ID):
		node = self.head
		while node is not None:
			if node.docID == ID:
				node.docFreq += 1
				break
			else:
				node = node.next
	# A function that can get the frequency for a term in a specific document
	def getFreq(self, ID):
		node = self.head
		while node is not None:
			if node.docID == ID:
				return node.docFreq
			else:
				node = node.next
		return 0
	# Check if a document has a node for a term
	def hasNode(self, ID):
		node = self.head
		if node is None:
			return False
		while node is not None:
			if node.docID == ID:
				return True
			else:
				node = node.next
		return False
	'''
	# Print out document number with term frequency
	# I only used it for debugging
	def printout(self):
		node = self.head
		if node is None:
			print("Term does not exist.")
		else:
			while node is not None:
				print("ID:", node.docID, "Posting:", node.docFreq)
				node = node.next
	'''
# Get the document index for a term
def getDocs(term):
	if dterm.__contains__(term):
		return dterm[term].length
	else:
		return 0
# Get term frequency with term and document number
def getPost(term, ID):
	if dterm.__contains__(term):
		return dterm[term].getFreq(ID)
	else:
		return 0
# Compute the TF-IDF
def TFIDF(term):
	global ndoc, nterm
	tf = []
	for i in range(ndoc):
		tf.append(getPost(term, i + 1) / nterm[i])
	if not getDocs(term) == 0:
		idf = math.log(ndoc / getDocs(term))
	else:
		idf = 0
	tfidf = [a * idf for a in tf]
	result = []
	def addzero(a):
		if len(a) == 1:
			return '0' + a
		return a
	for i in range(ndoc):
		result.append([tfidf[i], addzero(str(i + 1)), tf[i], idf])
	result.sort(reverse = True)
	print("--------------------------------------------------------------------")
	print("The result for term \"", end = '')
	print(term, end = '')
	print("\", in the order of TF-IDF:")
	print("  Doc No.       TF       IDF    TF-IDF")
	count = 0
	for info in result:
		print("Document", info[1], end = '')
		print(":", "{:7.4f}".format(info[2]), end = '')
		print(",", "{:7.4f}".format(info[3]), end = '')
		print(",", "{:7.4f}".format(info[0]))
		if not info[0] == 0:
			count += 1
	return count

# Read a document
# Record terms and the number of terms
def readdoc(dno):
	global nterm
	path = os.path.dirname(__file__) + "/data/file" + dno + ".txt"
	idno = int(dno)
	with open(path, 'r') as f:
		# Read the document
		for line in f:
			line = line.strip()
			words = line.split()
			l = len(words)
		for i in range(l):
			words[i] = words[i].lower()
			# Check for stop-words
			if words[i] in stoplist:
				l -= 1
			else:
				# Check if the term exists
				if not dterm.__contains__(words[i]):
					dterm[words[i]] = List()
				# Check if a node of this term for this document has been created
				if not dterm[words[i]].hasNode(idno):
					node = Node()
					node.docID = idno
					dterm[words[i]].append(node)
				# Frequency += 1
				dterm[words[i]].update(idno)
		# Record for the number of terms in this document
		nterm[idno - 1] = l

def test():
	while 1:
		print("Please input the term you want for query, input \"QUIT\" to exit.")
		query = input("Inputs except for \"QUIT\" are NOT cASe SEnsItIve:\n")
		start_2 = time.time()
		if query == "QUIT":
			break
		else:
			query = query.lower()
			count = TFIDF(query)
			global time_1
			end_2 = time.time()
			print(count, "relevant documents were given in", end_2 - start_2 + time_1, "second(s).")
			print("--------------------------------------------------------------------")

# Go through all documents
start_1 = time.time()
for i in range(ndoc):
	dno = str(i + 1)
	if len(dno) == 1:
		dno = '0' + dno
	readdoc(dno)
end_1 = time.time()
time_1 = end_1 - start_1
test()
