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

# sw contains the list of stopwords
sw = stopwords.words('english')
l1 =[]
l2 =[]

# remove stop words from the string
X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

#UNION
# form a set containing keywords of both strings
rvector = X_set.union(Y_set)
dnom = len(rvector)

#INTERSECTION
intersection = X_set.intersection(Y_set)
print(intersection)
numerator = len(intersection)

jaccard = numerator/dnom
print("jaccard : ",jaccard)

if jaccard>=0.5:
	print("SIMILLAR")
else:
	print('DISSIMILAR')
