# import streamlit as st

# import numpy as np
# import bs4 as bs
# import urllib.request
# import re
# import argparse
# import nltk
# import logging
# import heapq



import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
from model import model_0, model_1, model_2

def main():
    # pre download the bert model
    text_0 = '''Pelosi and Treasury Secretary Steven Mnuchin each raised the prospect of resuming negotiations on a stimulus package earlier Thursday, without giving any indication that they’d moved closer to a compromise.
Mnuchin said during a Senate Banking Committee hearing on Thursday that a targeted pandemic relief package was “still needed.”
“If the Democrats are willing to sit down, I’m willing to sit down anytime for bipartisan legislation. Let’s pass something quickly,” Mnuchin said.
The House speaker told reporters Wednesday she wasn’t sure when she and Mnuchin would next talk.
“We are ready for a negotiation,” she said. “I am talking with my caucus and my leadership and we will see what we are going to do,” Pelosi said.
The prospect of talks helped push stocks higher briefly. But that optimism was tempered by reports showing a resurgence in coronavirus cases in Europe, and investors pulled stocks back off session highs.
Lawmakers on both sides remained skeptical a deal could be had before the Nov. 3 election.
'''
    from summarizer import Summarizer
    model = Summarizer()
    sum_text = model(text_0, ratio = 0.1)
    # UI with Streamlit
    # Sidebar
    st.sidebar.title("About Me")
    st.sidebar.write("")
    st.sidebar.info("This is a demo application of Newsly, which offers you summarized news article wtih machine learning and deep learning techniques.")

    # Add a selectbox to the sidebar:
    algo_picked = st.sidebar.selectbox(
    'Which algorithm would you like to pick',
    ('TF-IDF-based', 'TextRank', 'BERT Embedding')
    )

    # call the models to be preloaded, especially bert model takes long to download
    model_00 = model_0
    model_11 = model_1
    model_22 = model_2

    model_selected = model_00
    if algo_picked == 'TextRank':
        model_selected = model_11
    elif algo_picked == 'BERT Embedding':
        model_selected = model_22

    turn_on_org = False
    org_onOff = st.sidebar.selectbox(
    'Show the orignal text',
    ('No', 'Yes')
    )
    if org_onOff == 'Yes':
        turn_on_org = True


    # # Add a slider to the sidebar:
    # add_slider = st.sidebar.slider(
    # 'Select a range of values',
    # 0.0, 100.0, (25.0, 75.0)
    # )

    # Main space
    st.title('Newsly, we help you read faster!')
    st.write("You can copy and paste the full paragraph in the box below for summarization!")


    # Taking in url

    # select which model

    # run specific model
    sum_text = model_selected(test_text)
    # output result
    user_input = st.text_input("", 'Paste your article/URL here.')
    st.write("Note: paste URL directly might cause error on some websites, such as CNN")

    num_org = len(test_text.split(' '))
    num_sum = len(sum_text.split(' '))

    st.header('Summarized Article:')
    st.subheader(f'Number of Words: {num_sum}')
    st.write(sum_text)
    if turn_on_org:
        st.header('Original Article:')
        st.subheader(f'Number of Words: {num_org}')
        st.write(test_text)




    return 42



test_text = '''Jim Dwyer, Pulitzer Prize-Winning Journalist, Dies at 63.
Working for New York Newsday, The Daily News and The Times, he covered the human stories of New York in dramatic prose and crusaded against injustice.

Jim Dwyer, a Pulitzer Prize-winning reporter, columnist and author whose stylish journalism captured the human dramas of New York City for readers of New York Newsday, The Daily News and The New York Times for nearly four decades, died on Thursday in Manhattan. He was 63.

His death, at Memorial Sloan Kettering Cancer Center, was announced by Dean Baquet, the executive editor of The Times, and Clifford Levy, the paper’s metropolitan editor, in an email to the Times staff. The cause was complications of lung cancer.

In prose that might have leapt from best-selling novels, Mr. Dwyer portrayed the last minutes of thousands who perished in the collapse of the World Trade Center’s twin towers on Sept. 11, 2001; detailed the terrors of innocent Black youths pulled over and shot by racial-profiling state troopers on the New Jersey Turnpike; and told of the coronavirus besieging a New York City hospital.

Mr. Dwyer won the 1995 Pulitzer for commentary for columns in New York Newsday, and was part of a New York Newsday team that won the 1992 Pulitzer for spot news reporting for coverage of a subway derailment in Manhattan. Colleagues called him a fast, accurate and prolific writer who crusaded against injustice, worked for six metropolitan dailies and wrote or co-wrote six books.

In a kaleidoscopic career, Mr. Dwyer was drawn to tales of discrimination against racial and ethnic minorities, wrongly convicted prisoners and society’s mistreated outcasts. He wrote about subway straphangers and families struggling to make ends meet.

As a student at Fordham University, he had hoped to become a doctor, until he joined the student newspaper, The Fordham Ram, and one day wrote about a rough-looking man having an epileptic seizure on a Bronx sidewalk. Mr. Dwyer stopped to help.

“People passing by were muttering disapproval, ‘junkie,’ ‘scumbag,’ that sort of thing,” he wrote. “The seizure subsided, and those of us who had stayed with him learned he was a veteran and had been having seizures since coming back from Vietnam. A few minutes later, off he went. But that moment stayed with me.”

A 19-year-old cub reporter, he wrote a lead paragraph that set the tone for a career: “Charlie Martinez, whoever he was, lay on the cold sidewalk in front of Dick Gidron’s used Cadillac place on Fordham Road. He had picked a fine afternoon to go into convulsions: the sky was sharp and cool, a fall day that made even Fordham Road look good.”

Mr. Dwyer was hooked. In a 2020 interview for this obituary, he said: “I intended to be pre-med, but The Fordham Ram got in the way of that. It was a crusading student newspaper. I couldn’t resist it. It was a joy for me to discover how much I loved reporting and writing.”

He was an established columnist, having been one for six years at The Daily News and for nine of his 11 years at New York Newsday when The Times hired him to be a general assignment reporter in May 2001, four months before the terrorist attacks at the World Trade Center in Lower Manhattan.

He soon gravitated to tales of injustice: Anthony Faison and Charles Shepherd, innocent men, released after serving 14 years for murder; the city’s $8.75 million settlement with Abner Louima, four years after a police officer sodomized him with a broomstick in a Brooklyn station house; and freedom for Jose Morales after 13 years in prison for a killing he did not commit.

And the day two hijacked jetliners hit the twin towers of the trade center, Mr. Dwyer caught New York’s mood in the subdued phrases of a veteran columnist: “The city changed yesterday. No one, no matter how far from Lower Manhattan, could step on a New York sidewalk untouched by concussions.”

Later, he wrote about artifacts that figured in the 9/11 attack, including a window washer’s squeegee, which had been used to cut a hole in sheetrock to free six men trapped in an elevator on the 50th floor of the South Tower. They fled down stairways, emerging just as the North Tower fell in the distance.

In 2005, Mr. Dwyer and a Times colleague, Kevin Flynn, published “102 Minutes: The Untold Story of the Fight to Survive Inside the Twin Towers.” The book, based in part on a long investigative report published in The Times in 2002, and on survivors accounts and tapes of police and fire operations, chronicled the final minutes of many among the thousands who died in the collapsing towers.

In their book about the 9/11 attack on the World Trade Center, Mr. Dwyer and Kevin Flynn recounted the final minutes of many among the thousands who died in the collapsing towers.
In their book about the 9/11 attack on the World Trade Center, Mr. Dwyer and Kevin Flynn recounted the final minutes of many among the thousands who died in the collapsing towers.
Since 2007, Mr. Dwyer had written The Times’s “About New York” column, succeeding a distinguished line of writers, including Meyer Berger, David Gonzalez and Dan Barry.

In a 2016 interview with The Columbia Journalism Review, Mr. Dwyer was asked if he had the best job in journalism. “I believe I do,” he said. “A big part of my job is to talk with brilliant scientists, great artists, the amazing people you meet just walking around the streets of New York. What could be more fun than that?”

In his last column for The Times, on May 26, he wrote of the devastation caused by the coronavirus, linking the pandemic to his own family’s history and the catastrophic 1918 flu.

“In times to come,” he wrote, “when we are all gone, people not yet born will walk in the sunshine of their own days because of what women and men did at this hour to feed the sick, to heal and comfort.”

James Dwyer, who always went by Jim, in his byline and otherwise, was born in Manhattan on March 4, 1957, the second of four sons of Irish Roman Catholic immigrants, Philip and Mary (Molloy) Dwyer. His father was a public school custodian, his mother an emergency room nurse at Bellevue Hospital. Jim and his three brothers attended Catholic parochial schools in Manhattan.

Jim graduated from the Msgr. William R. Kelly School in 1971. At the Loyola School, a Jesuit-run college-prep high school on the Upper East Side, he played several sports, joined the drama club, was editor of the school newspaper and graduated in 1975.

At Fordham, he earned a bachelor’s degree in general science in 1979. Gov. Andrew M. Cuomo was a classmate. In 1980, he received a master’s degree from the Columbia University Graduate School of Journalism.

He married Catherine Muir, a professor of computer sciences, in 1981. He is survived by his wife; two daughters, Maura Dwyer and Catherine Elizabeth Dwyer; and his three brothers, Patrick, Phil and John.

Mr. Dwyer was a reporter for The Hudson Dispatch in Union City, N.J., from 1980 to 1982; for The Elizabeth (N.J.) Daily Journal in 1982; and for The Record of Hackensack, N.J., in 1983 and 1984. He then joined New York Newsday, a tabloid spinoff of Newsday on Long Island, as a reporter. He was a columnist there from 1986 to 1995 (the year New York Newsday was closed), at first focusing on subways, then on general topics.

Mr. Dwyer covered the subway system for New York Newsday, and his columns became the basis for a book, “Subway Lives: 24 Hours in the Life of the New York Subways.”
Mr. Dwyer covered the subway system for New York Newsday, and his columns became the basis for a book, “Subway Lives: 24 Hours in the Life of the New York Subways.”
His subway columns were expanded into a book, “Subway Lives: 24 Hours in the Life of the New York Subways” (1991). A review in The Los Angeles Times said: “‘Subway Lives’ may be hard-boiled, but it’s best understood as an epic poem, and Dwyer himself comes across as a faintly Homeric figure, a late 20th century urban bard who finds something heroic in (and under) the mean streets of Gotham.”

As part of the Newsday team that covered the 1993 bombing of the World Trade Center, Mr. Dwyer and three colleagues wrote “Two Seconds Under the World” (1994), a book that detailed the trade center attack and explored the early signs of terrorism by Islamic fundamentalists.

His 1998 articles for The Daily News about racial profiling by state troopers on the New Jersey Turnpike led to the indictment of two officers who had stopped and shot several young Black and Latino college students in a roadside confrontation. The wounded men were hospitalized, but recovered. The troopers pleaded guilty to reduced charges, and the state paid $13 million to settle lawsuits.

With the lawyer Barry Scheck and Peter Neufeld, co-founder of the Innocence Project, Mr. Dwyer wrote “Actual Innocence: Five Days to Execution, and Other Dispatches from the Wrongly Convicted” (2000), the stories of 10 of the men they helped.

Mr. Dwyer also wrote “False Conviction: Innocence, Science and Guilt” (2014), and helped narrate a 2012 documentary, “The Central Park Five,” by Ken Burns, David McMahon and Sarah Burns, about five Black and Latino youths wrongfully convicted and imprisoned for the 1989 rape of a white woman who had been jogging in the park.

Mr. Dwyer covered parts of the “Central Park Five” trial in 1990 for New York Newsday and later voiced regrets that he had not been more forceful about his own reservations about the evidence and the case. He noted that the grass had been wet on the night of the attack, “so a record of the first moments of the assault was written in the damp ground.”

He added: “Crime scene photographs showed the trail where Ms. Meili (the victim) was dragged off the road. It was only about 18 inches wide, less than a newspaper spread open. In that trail, there is neither room for, nor trace of, five people. No matter how hard or long you look.”

Robert D. McFadden is a senior writer on the Obituaries desk and the winner of the 1996 Pulitzer Prize for spot news reporting. He joined The Times in May 1961 and is also the co-author of two books.

Subscribe for $1 a week. One day only.

Thanks for reading The Times.
'''





if __name__ == '__main__':
    main()
