# NER_tagger

Polyglot based Named entty extraction for text highlighting. 
Two methods publically available:
* lang_detect - given a text returns language code using polyglot's Detector
* find_entites - given a text runs lang_detect and, in case if the detected language is available, performs named entities extraction. If language is available returns a dictionary with keys: 'lang' for lang code and 'ner_result' for resulting text which is list of lists of tuples. Tuples contain words from the text while lists group text by sentenses.

For sample text:
The Detroit Pistons didn’t get to see much of them together on the court, part of the reason their playoff hopes are just about finished. So they’re trying to take the positives from a strong finish in a season where so much else went wrong. Andre Drummond narrowly missed a second straight 20-20 game with 22 points and 17 rebounds, and the Pistons beat the New York Knicks 115-109 on Saturday for their fourth straight victory.

find_entities would output the following:

{'lang': 'en', 'ner_result': [[('The', None), ('Detroit Pistons', 'I-ORG'), ('Detroit Pistons didn’t', 'I-PER'), ('get', None), ('to', None), ('see', None), ('much', None), ('of', None), ('them', None), ('together', None), ('on', None), ('the', None), ('court', None), (',', None), ('part', None), ('reason', None), ('their', None), ('playoff', None), ('hopes', None), ('are', None), ('just', None), ('about', None), ('finished', None), ('.', None)], [('So', None), ('they’re', None), ('trying', None), ('to', None), ('take', None), ('the', None), ('positives', None), ('from', None), ('a', None), ('strong', None), ('finish', None), ('in', None), ('season', None), ('where', None), ('so', None), ('much', None), ('else', None), ('went', None), ('wrong', None), ('.', None)], [('Andre Drummond', 'I-PER'), ('narrowly', None), ('missed', None), ('a', None), ('second', None), ('straight', None), ('20', None), ('-', None), ('game', None), ('with', None), ('22', None), ('points', None), ('and', None), ('17', None), ('rebounds', None), (',', None), ('the', None), ('Detroit Pistons', 'I-ORG'), ('beat', None), ('New York Knicks', 'I-ORG'), ('115', None), ('109', None), ('on', None), ('Saturday', None), ('for', None), ('their', None), ('fourth', None), ('victory', None), ('.', None)]]}
