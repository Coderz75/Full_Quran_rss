from bs4 import BeautifulSoup
import re
 
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
            text += f"""
<item>
        <title>Al-Quran-{a}:{b}</title>
        <description>{l}</description>
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