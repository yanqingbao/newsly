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