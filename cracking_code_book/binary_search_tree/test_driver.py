import bst
import iterative_bst
import threadedtree
import random
import time

trials = range(1000)
upper_bound = 1000
samples = 800
test_suite = random.sample(range(upper_bound), samples)

print "------------",len(trials),"TRIALS ------------"

start_standard_bst = time.time()
for trial in trials:
	standard_bst = bst.Binary_Search_Tree()
	for test_val in test_suite:
		standard_bst.insert(test_val)
end_standard_bst = time.time()
print "Insert of ",samples,"records into standard BST:", end_standard_bst - start_standard_bst

start_iter_bst = time.time()
for trial in trials:
	iter_bst = iterative_bst.Binary_Search_Tree_Iterative()
	for test_val in test_suite:
		iter_bst.insert(test_val)
end_iter_bst = time.time()
print "Insert of ",samples,"records into iterative BST:", end_iter_bst - start_iter_bst

start_threaded_bst = time.time()
for trial in trials:
	threaded_bst = threadedtree.ThreadedTree()
	for test_val in test_suite:
		threaded_bst.insert(test_val)
end_threaded_bst = time.time()
print "Insert of ",samples,"records into threaded BST:", end_threaded_bst - start_threaded_bst

print

start_standard_bst_traverse = time.time()
for trial in trials:
	standard_bst.print_tree()
end_standard_bst_traverse = time.time()
print "Traversal of",samples,"records in standard BST:", end_standard_bst_traverse - start_standard_bst_traverse

start_iter_bst_traverse = time.time()
for trial in trials:
	iter_bst.print_tree()
end_iter_bst_traverse = time.time()
print "Traversal of",samples,"records in iterative BST:", end_iter_bst_traverse - start_iter_bst_traverse

start_threaded_bst_traverse = time.time()
for trial in trials:
	threaded_bst.in_order()
end_threaded_bst_traverse = time.time()
print "Traversal of",samples,"records in threaded BST:", end_threaded_bst_traverse - start_threaded_bst_traverse