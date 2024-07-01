#!/usr/bin/env python
# coding: utf-8

# In[1]:


logo='''██╗    ██╗███████╗██████╗     ███████╗ ██████╗██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     
██║ █╗ ██║█████╗  ██████╔╝    ███████╗██║     ██████╔╝███████║██████╔╝██║██╔██╗ ██║██║  ███╗    
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██║██║╚██╗██║██║   ██║    
╚███╔███╔╝███████╗██████╔╝    ███████║╚██████╗██║  ██║██║  ██║██║     ██║██║ ╚████║╚██████╔╝    
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝  '''

print(logo)
logo1='''  _______        _       _   _                   
 |__   __|      | |     | \ | |                  
    | | ___  ___| |__   |  \| | _____      _____ 
    | |/ _ \/ __| '_ \  | . ` |/ _ \ \ /\ / / __|
    | |  __/ (__| | | | | |\  |  __/\ V  V /\__ \
    |_|\___|\___|_| |_| |_| \_|\___| \_/\_/ |___/'''
logo2='''   _       _       _   _                   
      | |     | |     | \ | |                  
      | | ___ | |__   |  \| | _____      _____ 
  _   | |/ _ \| '_ \  | . ` |/ _ \ \ /\ / / __|
 | |__| | (_) | |_) | | |\  |  __/\ V  V /\__ \
  \____/ \___/|_.__/  |_| \_|\___| \_/\_/ |___/'''

def hackernews():
        import requests
        from bs4 import BeautifulSoup
        import pprint
        res = requests.get('https://news.ycombinator.com/news')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        subtext = soup.select('.subtext')

        def sort_stories_by_votes(hnlist):
            return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

        def create_custom_hn(links, subtext):
            hn = []
            for idx, item in enumerate(links):
                title = item.getText()
                href = item.get('href', None)
                vote = subtext[idx].select('.score')
                if len(vote):
                    points = int(vote[0].getText().replace(' points', ''))
                    if points > 99:
                        hn.append({'title': title, 'link': href, 'votes': points})
            return sort_stories_by_votes(hn)
        pprint.pprint(create_custom_hn(links, subtext))


def jobscrape():
        import requests
        from bs4 import BeautifulSoup as soup
        import pprint
        page = requests.get("https://chennai.craigslist.org/search/jjj?query=software+engineer")
        bsobj = soup(page.content, 'lxml')
        links = []
        for link in bsobj.findAll('li', {'class': 'result-row'}):
            links.append(link.a['href'])
        pprint.pprint(links)
        title = []
        for link in links:
            page = requests.get(link)
            bsobj = soup(page.content, 'lxml')
            # print(bsobj)
            print(bsobj.findAll('h1')[0].text.strip())
            title.append(bsobj.findAll('h1')[0].text.strip())
            for i in bsobj.findAll('section', {'id': 'postingbody'}):
                print(i.text.strip())

print("*********choice menu**********")
print("Enter 1 for getting technology related updates")
print("Enter 2 for getting job related updates")
pref='y'
while(pref=='y'):
    choice = int(input("Enter your choice:"))
    if choice==1:
         print(logo1)
         hackernews()
    elif choice==2:
        print(logo2)
        jobscrape()
    else:
        print("Invalid Choice")
    print("Do you want to continue?type y for yes and n for no")
    pref=input()
print("******Hope you got the required information.Thank you for using this web scraper.*******")


# In[ ]:




