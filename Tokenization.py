# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:37:13 2020

@author: raoha
"""

#Tokenization of paragraphs/sentences
import nltk
nltk.download()

paragraph = """In the eighties, children always used to ask me questions such as “When can I sing the Song of India?” Today, the youth are asking me, “What I can give to India?” This shows that the nation is on a positive growth trajectory.

The change in pattern of the questions is indicative of the transformation which has taken place over the years. Also, I receive many e-mails and letters asking me “what I can give to India, my country?”

When I study the letters, messages and mails that I have received and also the personal interactions with the people, I can clearly see abundant opportunities in which every citizen can contribute. I thought of sharing this with you: My topic of this address will be — “What can I give to my nation?"

In Indian history, our nation has come across a situation, all at a time, an ascending economic trajectory, continuously rising foreign exchange reserves, increasing domestic investment with investors’ confidence rising steadily, global successes of Indian managerial and entrepreneurial talents, global recognition of technological competence, energy of 540 million youth, umbilical connectivities of more than 25 million people of Indian origin in various parts of the planet and the interest shown by many developed countries to invest in our engineers and scientists through setting up of new Research and Development Centres in India.

The distinction between the public and the private sectors and the illusory primacy of one over the other is vanishing. Also, there is a trend that many young people are opting for creating new enterprises instead of being mere employees.

Providing leadership for the one billion people with multi-cultural, multi-language and multi-religious backgrounds is indeed the core competence of our nation. Our technological competence and value systems with civilisational heritage are highly respected by the world community. Also, Foreign Institutional Investors find investing in India attractive as the returns are high and assured. Indian industrialists are also investing abroad and opening new business ventures.

Our Gross Domestic Product which stands at US $729 billion is poised to grow at 10% annually which along with various other concurrent actions, will enhance the welfare of farmers, workers, professionals and unleash creativity of entrepreneurs, business persons, scientists, engineers and all other constituents  of society.

Today due to the open sky policy and competitiveness air travel has become affordable for the growing middle class. The Railways have introduced many improvements and people can book tickets through the Internet. The revolution in travel has not only connected people but also boosted tourism and the economy. Tele-density in the country has gone up to 18%."""
               
# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenizing words
words = nltk.word_tokenize(paragraph)