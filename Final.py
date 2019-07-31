from urllib import request
import nltk
from nltk import word_tokenize

#nltk.download('punkt')
urlDBL = "http://www.gutenberg.org/files/2814/old/dblnr11.txt"
url2ULY = "http://www.gutenberg.org/files/4300/4300-0.txt"
url3POA = "http://www.gutenberg.org/files/4217/4217-0.txt"

url4BPP = "http://www.gutenberg.org/cache/epub/2346/pg2346.txt"
url5HOB = "http://www.gutenberg.org/cache/epub/3070/pg3070.txt"
url6SIS = "http://www.gutenberg.org/files/244/244-0.txt"

url7JSR = "http://www.gutenberg.org/cache/epub/5670/pg5670.txt"
url8NAD = "http://www.gutenberg.org/files/1245/1245-0.txt"
url9TVO = "http://www.gutenberg.org/files/144/144-0.txt"

responseDBL = request.urlopen(urlDBL)
responseULY = request.urlopen(url2ULY)
responsePOA = request.urlopen(url3POA)

responseBPP = request.urlopen(url4BPP)
responseHOB = request.urlopen(url5HOB)
responseSIS = request.urlopen(url6SIS)

responseJSR = request.urlopen(url7JSR)
responseNAD = request.urlopen(url8NAD)
responseTVO = request.urlopen(url9TVO)

rawDBL = responseDBL.read().decode('utf8')
rawULY = responseULY.read().decode('utf8')
rawPOA = responsePOA.read().decode('utf8')

rawBPP = responseBPP.read().decode('utf8')
rawHOB = responseHOB.read().decode('utf8')
rawSIS = responseSIS.read().decode('utf8')

rawJSR = responseJSR.read().decode('utf8')
rawNAD = responseNAD.read().decode('utf8')
rawTVO = responseTVO.read().decode('utf8')

tokensDBL = word_tokenize(rawDBL)
tokensULY = word_tokenize(rawULY)
tokensPOA = word_tokenize(rawPOA)

tokensBPP = word_tokenize(rawBPP)
tokensHOB = word_tokenize(rawHOB)
tokensSIS = word_tokenize(rawSIS)

tokensJSR = word_tokenize(rawJSR)
tokensNAD = word_tokenize(rawNAD)
tokensTVO = word_tokenize(rawTVO)

print(len(tokensJSR))
print(tokensNAD[23])
