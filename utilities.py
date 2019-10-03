import string

# define basic stopwords list
stopwords = [
    'if','and','the','as','like','to',
    'you','i','we','me','that','this',
    'is','for','of','my','has','a',
    'an','at','out','on','or','your',
    'our','do','not','yes','no','these',
    'those','dont',
    # including "advanced" stopwords
    'have','just','any','who','what',
    'where','why','how','with','from'
]


def fetchilarity_score(path1,path2,mode='script'):    
    if mode=='script':
        # get the files
        with open(path1,'r') as file:
            text1 = file.read().replace('\n', '')

        with open(path2,'r') as file:
            text2 = file.read().replace('\n', '')
    else: 
        # the paths are actual text
        text1=path1
        text2=path2

    # remove punctuation
    text1,text2 = (
        [
            ''.join(['' if letter in string.punctuation else letter for letter in text]).lower().split(' ')
            for text in [text1,text2]
        ]
    )

    
    # get similarity score of raw text words    
    fetchilarity_raw = len(set(text1).intersection(set(text2))) / len(set(text1+text2))
    

    # get similarity score with all stopwords removed
    # check to make sure we're not removing all words
    temp1,temp2 = (
        [word for word in text if not word in stopwords]
        for text in [text1,text2]
    )
    if len(temp1)<2 or len(temp2)<2:
        pass
    else:
        text1,text2 = (
            [word for word in text if not word in stopwords]
            for text in [text1,text2]
        )


    
    # without stopwords
    fetchilarity_stopwords_removed = len(set(text1).intersection(set(text2))) / len(set(text1+text2))
    
    
    # overall score
    fetchilarity = (fetchilarity_raw + fetchilarity_stopwords_removed)/2
    

    ####
    return fetchilarity