import requests
from bs4 import BeautifulSoup
from collections import Counter


open_file = open("essay_file.txt", 'r')
open_file1 = open("synonyms.txt", 'w')
clean_list = []


def remove_special_characters(special_word):
    string = list(special_word)
    special_char = "!@#$%^&*()_+|}{\":?><-=[]\;',./"
    for char in special_char:
        if char in word:
            string.remove(char)
    new_word = ''.join(string)
    clean_list.append(new_word)


def web_crawl_word(current_word, repeated_number):
    url = "http://www.thesaurus.com/browse/" + current_word
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    open_file1.write("\n*************************************\n")
    open_file1.write("Synonym(s) for: " + current_word + " (" + str(repeated_number) +")")
    open_file1.write("\n*************************************\n")
    for link in soup.find_all('a', {'class': 'css-1hn7aky e1s2bo4t1'}):
        open_file1.write(link.text + '\n')
    open_file1.write('\n')


essay = open_file.read()
word = essay.split()
words = []
for i in word:
    if len(i) >= 5:
        words.append(i)
for j in range(0, len(words)):
    remove_special_characters(words[j])
counter = Counter(words)
num = input("How many words would you like to replace?")
top_num = counter.most_common(int(num))

for k in range(0, int(num)):
    web_crawl_word(str(top_num[k][0]), top_num[k][1])

