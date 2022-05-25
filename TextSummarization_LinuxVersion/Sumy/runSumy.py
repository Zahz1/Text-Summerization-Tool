from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import nltk
nltk.download('punkt')


from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


PathData = "data.txt"
PathResults = "Results/Sumy.txt"

LANGUAGE = "english"
SENTENCES_COUNT = 10


if __name__ == "__main__":

    #fileIn = open(PathData, "r")
    #parser = fileIn.read().replace("\n", " ")
    #fileIn.close()

    #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    #input from file
    parser = PlaintextParser.from_file(PathData, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    listoutput = summarizer(parser.document, SENTENCES_COUNT)
    print(listoutput[0]) #output highest ranked sentence

    #output to file
    fileOut = open(PathResults, "w")
    fileOut.write(str(listoutput[0]))
    fileOut.close()
