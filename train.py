import time
import six.moves.cPickle

import glove
import data_reader

dataset = data_reader.dataset()
x = [row[0] for row in dataset[1:50]]
y = [row[1] for row in dataset[1:50]]
model, tokeniser, dictionarySize = glove.train(x, y)

jsonModel = model.to_json()
open('model.json', 'w').write(jsonModel)
open('model-dictionary-size.dat', 'w').write(str(dictionarySize))
six.moves.cPickle.dump(tokeniser, open("tokeniser.pkl", "wb"))

model.save_weights('model-' + str(time.time()) + '.h5')

print(glove.query(model, tokeniser, dictionarySize, "It is bad"))
print(glove.query(model, tokeniser, dictionarySize, "It is good"))