def abusive_tweets(sentence, slurs):
    """
    checks if the sentence has any of the slur words defined in the set, and returns a tuple
    of (sentence, is_abusive). is_abusive is a boolean flag

    sentence - each line of the file is passed as a list. I'm assuming that each line
    is already filtered for non empty strings and lines with only special characters. 
    Only lowercase characters are passed i.e lower() is used while passing the sentence.

    slurs - words which denote abuse/ racist remarks are passed as a set
    """
    is_abusive = 'false'
    if any(slur in sentence for slur in slurs):
        is_abusive = 'true'
    
    return (sentence, is_abusive)



def degree_of_profanity(abusive_tweet, slur):
    """
    A single tweet along with the racist word is passed into the function. Profanity degree is
    calculated as the number of racist words in the sentence over the number of words

    abusive_tweet - a single tweet which is already marked offensive/abusive

    slur - a list of swear words which is present in the tweet

    """
    words = abusive_tweet.split()

    profanity_degree = sum(1 for word in words if word in slur)/len(words)

    return (abusive_tweet, profanity_degree)


if 'name' == '__main__':

    #words which are marked as racist words are defined as a set here
    slur_words = {}
    
    tweets = []

    profanity_degree_of_each_tweet = []
    #input_file.txt is a place holder. Enter the file here as which contains a list of tweets
    #I'm assuming the file is already filtered for non empty lines and lines with only whitespace
    #characters using a suitable regex method
    with open('input_file.txt') as input_file:

        #each line in the input file is stripped and passed to the function defined above. A tuple
        #tweets along with the boolean value is got as a result
        
        for line in input_file:
            if not line.strip():
                continue
            else:
               tweets.append(abusive_tweets(line,slur_words))

        # for each of teh positive tweet, the degree of profanity of the tweet is calculated
        for tweet in tweets:
            if tweet[1]:
                profanity_degree_of_each_tweet.append(degree_of_profanity(tweet,slur_words))

