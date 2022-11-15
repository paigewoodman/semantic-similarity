
import spacy
nlp = spacy.load('en_core_web_md')

#Running code 1 from task PDF
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"words : {word1}, {word2} | similarity: {word1.similarity(word2)}")
print(f"words : {word3}, {word2} | similarity: {word3.similarity(word2)}")
print(f"words : {word3}, {word1} | similarity: {word3.similarity(word1)}")

"""Output:
words : cat, monkey | similarity: 0.5929930274321619
words : banana, monkey | similarity: 0.40415016164997786
words : banana, cat | similarity: 0.22358825939615987
"""

#Write a note about what you found interesting about the similarities 
# between cat, monkey and banana
    # I think it is interesting that spacy is able to establish a 40.04...% 
    # similarity between monkey and banana whilst still having a very
    # low similarity between cat and banana of 22.35...%

#My own example of above code:
word1 = nlp("dark")
word2 = nlp("outside")
word3 = nlp("night")
print(f"words : {word1}, {word2} | similarity: {word1.similarity(word2)}")
print(f"words : {word3}, {word2} | similarity: {word3.similarity(word2)}")
print(f"words : {word3}, {word1} | similarity: {word3.similarity(word1)}")

"""Output:
words : dark, outside | similarity: 0.2843720348437748
words : night, outside | similarity: 0.40937484205688945
words : night, dark | similarity: 0.34953138563225805
"""
    #I was surprised that the similarity between night and dark
    # was so low, I thought that it would be higher as it is typically
    #dark at night


#Run the example file with the simpler language model ‘en_core_web_sm’
#and write a note on what you notice is different from the model
#'en_core_web_md'.

    #Using the simpler model of spacy, gave a lower similarity on the 
    #complaints, where as the more advance model, en_core_web_md was able
    #to establish a high similarity when comparing complaints with complaints,
    #and recipes with recipes.
    #For example: the advance model, gave a 83.5..% similarity on the first 2
    #complaints that were compared, where as the simple model gave them a 
    #similarity of 50.9..% which is considerably lower.

    #The simple model also gave a message when comparing:

"""c:\Users\paige\Dropbox\PW22090003643\Software Engineer Bootcamp\T38\example.py:38:
 UserWarning: [W007] The model you're using has no word vectors loaded, so the result 
 of the Doc.similarity method will be based on the tagger, parser and NER, which may not
give useful similarity judgements. This may happen if you're using one of the small models,
e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors.
You can always add your own word vectors, or use one of the larger models instead if available."""

    #This shows that the simple model is not ideal when comparing large pieces of text.

