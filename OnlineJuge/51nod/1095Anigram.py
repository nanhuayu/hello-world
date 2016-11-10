# -*- coding: utf-8 -*-
#2016/10/28

def get_hash(w):
    word_hash = 0
    for i in w:
        word_hash += ord(i)**4
    return word_hash

word_list = []
for _ in range(int(raw_input())):
    word_list.append(raw_input())   
#word_list = [raw_input() for for i in range(int(raw_input()))]
#print word_list

word_dict = dict()
for word in word_list:
    word_hash = get_hash(word)
    if word_hash in word_dict:
        #word_dict[word_hash].append(word)
        word_dict[word_hash].add(word)
    else:word_dict[word_hash] = set([word])

#print word_hash
#print word_dict

for _ in range(int(raw_input())):
    word_s = raw_input()
    word_h = get_hash(word_s)
    if word_h in word_dict:
        print len(word_dict[word_h])-1 if word_s in word_dict[word_h] else len(word_dict[word_h])
    else:print 0

