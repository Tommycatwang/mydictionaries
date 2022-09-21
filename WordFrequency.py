readbook=open('sometext.txt','r')
list_words={}
for wordon in readbook:
    wordon =wordon.lower()
    wordread = wordon.split(" ")
    for wordreadd in wordread:
        if wordreadd in list_words:
            list_words[wordreadd]= list_words[wordreadd] +1

        else:
            list_words[wordreadd] = 1

for read in list_words.keys():
    print(read + ',' + str(list_words[read]))

readbook.close()

