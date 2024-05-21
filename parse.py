from bs4 import BeautifulSoup
import re
from datetime import datetime
# Reading the data inside the xml
# file to a variable under the name 
# data
with open('en.sahih.xml', 'r') as f:
    data = f.read()
 
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object 
Bs_data = BeautifulSoup(data, "xml")
 
# Finding all instances of tag 
# `unique`
surah = Bs_data.find_all('sura')
z = 0

text = """
<rss version="2.0">
    <channel>
    <title>Quran</title>
    <description>Entirety of the Holy quran</description>
    <link>http://coderz75.github.io</link>
    <language>en-us</language>
    <category domain="coderz75.github.io">Ayat</category>
    <copyright>Copyright 2024 Coderz75</copyright>
"""
a = 1

for i in surah:
    b = 1
    for x in i:
        l= re.search('(?<=text=")(.*)(?=")',str(x))
        if l:
            l = l.span()
            l= str(x)[l[0]:l[1]]
            date = datetime.now()
            ffff = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            ff = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
            text += f"""
<item>
        <title>Al-Quran-{a}:{b}</title>
        <description>{l}</description>
        <guid>https://coderz75.github.io</guid>
        <link>https://coderz75.github.io</link>
        <pubDate>{ffff[date.weekday()]}, {date.day} {ff[date.month]} {date.year}</pubDate>
</item>
"""
            b+=1
    a+=1
            
text += """
    </channel>
</rss>
"""

with open("quran_rss.xml", "w") as f:
    f.write(text)