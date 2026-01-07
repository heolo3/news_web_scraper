import requests
import bs4
import lxml

input_num = 0

print("(1) CNN \n(2) NYT  \n(3) WSJ  \n(4) BBC")
while True:
    user_input = input("Which news outlets headlines would you like to see today? (Please input the assigned number) ")
    if user_input.isdigit():
        input_num = int(user_input)
        break
    else:
        print("Invalid input! Please enter a valid integer for the desired outlet's news.")

if(input_num == 1):
    cnn_res = requests.get("https://www.cnn.com/")
    cnn_soup = bs4.BeautifulSoup(cnn_res.text, "lxml")

    for item in cnn_soup.select(".container__headline-text"):
        print(item.text)
elif(input_num == 2):
    nyt_res = requests.get("https://www.nytimes.com/")
    nyt_soup = bs4.BeautifulSoup(nyt_res.text, "lxml")

    for item in nyt_soup.select(".indicate-hover"):
        print(item.text)
elif(input_num == 3):
    wsj_res = requests.get("https://www.wsj.com/")
    wsj_soup = bs4.BeautifulSoup(wsj_res.text, "lxml")

    for item in wsj_soup.select("div > h3"):
        print(item.text)
elif(input_num == 4):
    bbc_res = requests.get("https://www.bbc.com/")
    bbc_soup = bs4.BeautifulSoup(bbc_res.text, "lxml")

    for item in bbc_soup.select("h2"):
        print(item.text)
else:
    print("Invalid input! Please select one of the four news outlets above.")