# Program to measure the similarity between two sentences using jaccard similarity.
from nltk.corpus import stopwords     # nltk-natural language toolkit
from nltk.tokenize import word_tokenize

# X = input("Enter first string: ").lower()
# Y = input("Enter second string: ").lower()
X ="Define Newton 3rd Law"
Y ="Explain Newton 3rd Law of motion"
# X = 'numpy is used for working with arrays'
# Y = 'pandas is used for working with data'

# tokenization  - seperating sentence into words
X_list = word_tokenize(X)
Y_list = word_tokenize(Y)
# print(X_list)
# print(Y_list)


# sw contains the list of stopwords
sw = stopwords.words('english')
l1 =[]
l2 =[]

# remove stop words from the string
X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}
# print(X_set)
# print(Y_set)

#UNION
# form a set containing keywords of both strings
rvector = X_set.union(Y_set)
# print(rvector)
dnom = len(rvector)
# print(dnom)

#INTERSECTION
intersection = X_set.intersection(Y_set)
print(intersection)
numerator = len(intersection)
# print(numerator)

jaccard = numerator/dnom
print("jaccard : ",jaccard)

if jaccard>=0.5:
	print("SIMILLAR")
else:
	print('DISSIMILAR')


# for w in rvector:
# 	if w in X_set:
# 		l1.append(1) # create a vector
# 	else:
# 		l1.append(0)
# 	if w in Y_set:
# 		l2.append(1)
# 	else:
# 		l2.append(0)
# c = 0
# print(l1)
# print(l2)

# def jaccard_similarity(x,y):
#   """ returns the jaccard similarity between two lists """
#   intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
#   union_cardinality = len(set.union(*[set(x), set(y)]))
#   res = intersection_cardinality/float(union_cardinality)
#   if res>=0.5:
# 	  print("similar")
#   else:
# 	  print("Dissimilar")
#   return res


# print('jaccard: %.3f' %jaccard_similarity(X_set,Y_set))

# cosine formula
# for i in range(len(rvector)):
# 		c+= l1[i]*l2[i]
# cosine = c / float((sum(l1)*sum(l2))**0.5)
# if cosine >= 0.5:
# 	print("simillar")
# print("cosine similarity: ", cosine)


# sentences = ["define newton 3rd law",
# "explain 3rd law of motion"]
# sentences = [sent.lower().split(" ") for sent in sentences]
# jaccard_similarity(sentences[0], sentences[1])
# # print('Jaccard:',)