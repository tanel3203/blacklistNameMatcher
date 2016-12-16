
import terroristFinder as tf

query = raw_input("Please enter name to search in the terrorist list \n")

blacklist = raw_input("Please enter name of blacklist file in same path (e.g. blacklist.tsv) or absolute location \n")

noisefile = raw_input("Please enter name of noise file in same path (e.g. noisefile.tsv) or absolute location \n")



tf.terroristFinder(query, blacklist, noisefile)