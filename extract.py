# importing the libraries
from bs4 import BeautifulSoup
import requests
import csv
import os
import configparser


def title_extractor(url,sep,key,filepath,tag,fields):
    '''

    :param url:url of the link
    :type url: str
    :param sep: seperator used to split the sentence
    :type sep: str
    :param key: keyword to find the line to be extracted
    :type key: str
    :param filepath: output path
    :type filepath: str
    :param tag: html tag to be used for extracting the text
    :type tag: str
    :param fields: group of header used in csv file
    :type fields: str
    :return: file with the extracted text
    :rtype: csv
    '''

    # Make a GET request to fetch the raw HTML content
    try:
        html_content = requests.get(url).text
    except Exception as e:
        print(f"Error in the url link: {e}")
        exit()


    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")

    #extract tag from the html
    title = soup.find_all(tag)

    #header of csv file
    fields =fields.split(",")
    rows =[]

    #check whether file is already present then delete it
    if os.path.isfile(filepath):
        try:
            os.remove(filepath)
        except Exception as e :
            print(f"please close the file or enter new filepath: {e}")
            exit()

    #looping over the extracted text
    for i,j in enumerate(title):
        row=[]
        if sep == "None":
            title_list = j.text.split()
            sep=" "
        else:
            title_list = j.text.split(sep)
        temp1 = list(map(lambda x: x.lower(), title_list))
        temp2 = list(map(lambda x: x.strip(), temp1))
        #checking for the keyword in the extracted text
        if key in list(map(lambda x: x.lower(),temp2)):
            row.append(str(i + 1))
            row.append(sep.join(title_list[1:]))
        else:
            continue

        #list the tag with keywords
        rows.append(row)

    try:
        with open(filepath, 'w',newline="") as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)
    except Exception as e:
        print(f"Enter proper filepath : {e}")
        exit()

    result = f"File saved in {filepath}"

    print(result)





if __name__ == '__main__':
    config_parser = configparser.ConfigParser()
    config_parser.read("config.ini")
    URL = config_parser.get('DETAILS', 'URL')
    SEP = config_parser.get('DETAILS', 'SEP')
    KEY = config_parser.get('DETAILS', 'KEY')
    TAG = config_parser.get('DETAILS', 'TAG')
    FILEPATH = config_parser.get('DETAILS', 'FILEPATH')
    FIELD = config_parser.get('DETAILS', 'FIELD')
    title_extractor(URL,SEP,KEY,FILEPATH,TAG, FIELD)




