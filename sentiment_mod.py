import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.tokenize import word_tokenize
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers=classifiers
    def classify(self,features):
        votes=[]
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence (self, features):
        votes=[]
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()
all_words=[]
documents =[]

allowed_word_types = ["J"]

for r in short_pos.split('\n'):
    documents.append((r,"pos"))
    words = word_tokenize(r)
    pos=nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
for r in short_neg.split('\n'):
    documents.append((r,"neg"))
    words = word_tokenize(r)
    pos=nltk.pos_tag(words)
    for w in pos:
       if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

save_documents=open("pickled/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()


short_pos_words=word_tokenize(short_pos)
short_neg_words=word_tokenize(short_neg)



all_words=nltk.FreqDist(all_words)

word_features=list(all_words.keys())[:5000]

save_documents=open("pickled/word_features1k.pickle","wb")
pickle.dump(word_features, save_documents)
save_documents.close()

def find_features(document):
    words=set(document)
    features = {}
    for w in word_features:
        features[w]=(w in words)
    return features
featuresets = [(find_features(rev),category) for (rev,category) in documents]
random.shuffle(featuresets)
#positive
training_set = featuresets[:10000]
testing_set = featuresets[10000:]



BN_classifier = SklearnClassifier(BernoulliNB())
BN_classifier.train(training_set)


save_documents=open("pickled/BN_classifier1k.pickle","wb")
pickle.dump(BN_classifier, save_documents)
save_documents.close()

LR_classifier = SklearnClassifier(LogisticRegression())
LR_classifier.train(training_set)


save_documents=open("pickled/LR_classifier1k.pickle","wb")
pickle.dump(LR_classifier, save_documents)
save_documents.close()


SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)


save_documents=open("pickled/SVC_classifier1k.pickle","wb")
pickle.dump(SVC_classifier, save_documents)
save_documents.close()

LSVC_classifier = SklearnClassifier(LinearSVC())
LSVC_classifier.train(training_set)


save_documents=open("pickled/LSVC_classifier1k.pickle","wb")
pickle.dump(LSVC_classifier, save_documents)
save_documents.close()

NSVC_classifier = SklearnClassifier(NuSVC())
NSVC_classifier.train(training_set)

save_documents=open("pickled/NSVC_classifier1k.pickle","wb")
pickle.dump(NSVC_classifier, save_documents)
save_documents.close()

voted_classifier = VoteClassifier(BN_classifier,
                                  LR_classifier,
                                  SVC_classifier,
                                  LSVC_classifier,
                                  NSVC_classifier)
def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

