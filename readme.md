# XML Extractor

## Introduction

A configurable software package which will extract the required text based on the keyword and store it in the csv format.

eg. <br />
input<br />

```
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Top stories - European Parliament</title>
    <link>https://www.europarl.europa.eu/news/en</link>
    <description />
    <language>EN</language>
    <copyright>© European Union, 2021 - EP</copyright>
    <pubDate>Tue, 21 Sep 2021 13:07:46 GMT</pubDate>
    <item>
      <title>Top story - State of the European Union Debate 2021 - Addressing Europeans' concerns</title>
      <link>https://www.europarl.europa.eu/news/en/headlines/priorities/soteu2021</link>
      <description>&lt;img src="https://www.europarl.europa.eu/resources/library/images/20210913PHT12318/20210913PHT12318-ms.jpg" align="left" width="125" hspace="5" vspace="0" /&gt;The most important EU debate of the year, looking at last year’s achievements as well as plans and vision for the future, took place on 15 September.&lt;br /&gt; &lt;br /&gt;Source : &lt;a href="https://www.europarl.europa.eu/privacy-policy/en"&gt;© European Union, 2021 - EP&lt;/a&gt;</description>
      <source url="https://www.europarl.europa.eu/rss/doc/top-stories/en.xml">Top stories - European Parliament</source>
      <category domain="type">Top story</category>
      <pubDate>Mon, 13 Sep 2021 13:03:26 GMT</pubDate>
      <guid isPermaLink="false">TST_TST-2021-09-09-11812_EN</guid>
    </item>
  </channel>
</rss>
```
keyword = "Top stories"<br />

```
title_no,stories
1, European Parliament
```

## Requirements

* Install Anaconda based on the operating system. Follow the below link for installation
  >https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

* Clone the repository or download the whole package of XML extractor

* Choose a suitable IDE like Pycharm or VS code.

* Set up the environment in conda and install the requirement by using the below code
    >pip install -r requirement.txt
  
## Packages used along with inbuilt package in conda

* Beautiful Soup
* requests

## Files in the package

* config.ini      :- Configuration file with all the variables defined in it.
* extract.py      :- Python script file to extract the text.
* requirement.txt :- List of python package to be installed.
* readme.md       :- Package details with steps to run the package. 

##Steps to run the package

1. Please follow all the steps mentioned in the requirement section.
2. Edit the config.ini based on your requirement. Details of each parameter is provided in the file with comments. 
```
[DETAILS]
#url of the link
URL = https://www.europarl.europa.eu/rss/doc/top-stories/en.xml
#the seperator
SEP = -
#html tag from where the text to be extracted
TAG = title
#if the title text has prefix like "top stories - European Parliament"
KEY = top stories
#path of file
FILEPATH = C:\Darshan\XML Extractor\data.csv
#header of csv file
FIELD =title_no,stories
```

3. Run the extract.py file once you have the configured your config file. You can run the file in terminal with below code.
>python extract.py


