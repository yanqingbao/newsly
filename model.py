# define which model to use

# 1. TF-IDF

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter

extra_words = list(STOP_WORDS) + list(punctuation) + ['\n']
nlp = spacy.load("en_core_web_md")

def model_0(text, limit = 4):
    keyword = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    doc = nlp(text.lower())
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)

    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for w in freq_word:
        freq_word[w] = (freq_word[w]/max_freq)

    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]

    summary = []
    sorted_x = sorted(sent_strength.items(), key=lambda kv: kv[1], reverse=True)

    counter = 0
    for i in range(len(sorted_x)):
        summary.append(str(sorted_x[i][0]).capitalize())

        counter += 1
        if(counter >= limit):
            break

    sum_text =  ' '.join(summary)
    sum_text = sum_text.replace('\n', ' ')
    return " ".join(sum_text.split())


# text_short = top_sentence(text_3, num_sentences)

# 2. TextRank
def model_1(text):
    from gensim.summarization.summarizer import summarize
    sum_text = summarize(text, ratio = 0.1)
    sum_text = sum_text.replace('\n', ' ')
    return " ".join(sum_text.split())
# 3. Bert Embedding
def model_2(text):
    from summarizer import Summarizer
    model = Summarizer()
    sum_text = model(text, ratio = 0.1)
    # return model.run_embeddings(text)
    sum_text = sum_text.replace('\n', ' ')
    return " ".join(sum_text.split())




# # Function to convert number into string
# # Switcher is dictionary data type here
# def numbers_to_strings(argument):
#     switcher = {
#         0: model_0()
#         1: model_1()
#         2: model_2()
#     }
#
#     # get() method of dictionary data type returns
#     # value of passed argument if it is present
#     # in dictionary otherwise second argument will
#     # be assigned as default value of passed argument
#     return switcher.get(argument, "nothing")

text_test = """ Democrats Crafting New $2.4 Trillion Stimulus Bill to Spur Talks

House Democrats have started drafting a stimulus proposal of roughly $2.4 trillion that they can take into possible negotiations with the White House and Senate Republicans, according to House Democratic officials.
The Democrat-only plan also would address demands from swing-state lawmakers in the party for passage of a virus-relief plan before they adjourn for the stretch run of their reelection campaigns -- even if it doesn’t result in a deal that gets signed into law.
The bill could get passed by the House next week. While smaller than the $3.4 trillion package the House passed in May, it remains much larger than what Senate Republicans have said they could accept. President Donald Trump has indicated he’d be willing to go as high as $1.5 trillion.

“When you are talking about $2.2 trillion and $1.5 trillion you are in deal-making territory” Democratic Representative Dan Kildee said. House Speaker Nancy Pelosi and Senate Democratic leader Chuck Schumer had earlier pressed the White House for a $2.2 trillion package.
As the top-line figure remains well above what the Trump administration has favored, the new House bill may do little on its own to resolve the impasse in talks that’s persisted since August. Senate Republicans proved unable to coalesce around an earlier $1 trillion proposal, and instead backed a $650 billion plan that ended up getting blocked by Democrats as insufficient.
The bill adds to the previous $2.2 trillion Pelosi-Schumer plan with help for the U.S. airline industry to avert massive job losses, which could start Oct. 1 when restrictions expire from a prior round of federal assistance. Also included is small-business aid and a bailout for restaurants.


Pelosi and Treasury Secretary Steven Mnuchin each raised the prospect of resuming negotiations on a stimulus package earlier Thursday, without giving any indication that they’d moved closer to a compromise.
Mnuchin said during a Senate Banking Committee hearing on Thursday that a targeted pandemic relief package was “still needed.”
“If the Democrats are willing to sit down, I’m willing to sit down anytime for bipartisan legislation. Let’s pass something quickly,” Mnuchin said.
The House speaker told reporters Wednesday she wasn’t sure when she and Mnuchin would next talk.
“We are ready for a negotiation,” she said. “I am talking with my caucus and my leadership and we will see what we are going to do,” Pelosi said.
The prospect of talks helped push stocks higher briefly. But that optimism was tempered by reports showing a resurgence in coronavirus cases in Europe, and investors pulled stocks back off session highs.
Lawmakers on both sides remained skeptical a deal could be had before the Nov. 3 election.

Texas Representative Kevin Brady, the top Republican on the tax writing committee, said the effort to draft a Democratic-only bill wasn’t a good sign.
“It’s a waste of time,” he said. “She could draft ten more partisan bills -- it doesn’t get us an inch closer,” he said, referring to Pelosi.
Senate Appropriations Chairman Richard Shelby, an Alabama Republican, said, “There’s always a chance around here, as you know, but it is slim.”

“I don’t think we are going to get it done before whatever break we have before the elections,” Democratic Senator Ben Cardin of Maryland said. The Republicans are “underestimating” the danger to the economy and are unlikely to accept a significant stimulus, he added.
The risk of a slowdown in the recovery is rising with the lack of movement on fiscal stimulus. Initial claims for unemployment insurance remained at a level above the peak during the Great Recession of 2007-09, the latest weekly data showed on Thursday.
Fed Chair Jerome Powell reiterated his conclusion that “it’s likely that additional fiscal support will be needed,” speaking at the same Senate panel where Mnuchin was testifying.
The recovery has been faster than anticipated so far, Powell said, thanks to income support to those affected by the pandemic.
“The risk is that they’ll go through that money, ultimately, and have to cut back on spending and maybe lose their home,” the Fed chief said. “That’s the downside risk of no further action.”

The plan for a fresh House vote on stimulus follows weeks of resistance from Pelosi to suggestions from moderate members for a vote on a new Democratic package. About a dozen moderate members this week began threatening to mutiny and back a Republican procedural move to force a House floor vote on small-business relief. Some of those members on Thursday began circulating a letter opposing the GOP move, as Pelosi proceeded toward a House compromise vote.
— With assistance by Craig Torres, Catarina Saraiva, Laura Litvan, and Saleha Mohsin
"""
# # # Driver program
# if __name__ == "__main__":
#     # print(f'Original Text: \n')
#     # print(text_test)
#     print(f'Model_0:\n')
#     print(model_0(text_test))
#     print(f'model_1:\n')
#     print(model_1(text_test))
#     print(f'Model_2:\n')
#     print(model_2(text_test))
