from selenium import webdriver
import time
import datetime as dt
import csv
import os
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup


URL_text = 'https://twitter.com/'+input("Enter the Twitter username: ").replace(' ','').replace('@','')
browz = webdriver.Chrome('C:/chromedriver.exe')
browz.get(URL_text)
input("\nPLEASE DO NOT FORGET TO LOG IN. ")
input("\nCONFIRM THAT YOU ARE ON THE CORRECT PAGE AND HAVE LOGGED IN.\n")

page = soup(browz.page_source,'lxml')
AllHomeItems = []

try:
    NameBanner = page.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wbh5a2"})
    username = NameBanner.find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
    AllHomeItems.append(username)
except:
    AllHomeItems.append("")
    
try:
    NameBanner = page.find("div",{"class":"css-1dbjc4n r-15d164r r-1g94qm0"})
    fullname = NameBanner.find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
    AllHomeItems.append(fullname)
except:
    AllHomeItems.append("")
    
try:
    Badges = NameBanner.find("span",{"class":"css-901oao css-16my406 r-18u37iz r-1q142lx r-1qd0xha r-1b6yd1w r-ad9z0x r-bcqeeo r-qvutc0"})
    badge = Badges.svg['aria-label']
    AllHomeItems.append(badge)
except:
    AllHomeItems.append("")
    
try:
    HomeHeader = page.find("div",{"class":"css-1dbjc4n r-ku1wi2 r-1j3t67a r-m611by"})
    IconPic = HomeHeader.find("img",{"class":"css-9pa8cd"})
    icon = IconPic['src']
    AllHomeItems.append(icon)
except:
    AllHomeItems.append("")

try:
    TopBanner = page.find("a",{"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-o7ynqc r-6416eg"})
    banner = TopBanner.find("img",{"class":"css-9pa8cd"})['src']
    AllHomeItems.append(banner)
except:
    AllHomeItems.append("")
    
try:
    bio = HomeHeader.find("div",{"data-testid":"UserDescription"}).text
    AllHomeItems.append(bio)
except:
    AllHomeItems.append("")
    
try:
    HeaderItems = HomeHeader.find("div",{"data-testid":"UserProfileHeader_Items"})
    Items = HeaderItems.findAll("span",{"class":"css-901oao css-16my406 r-1re7ezh r-4qtqp9 r-1qd0xha r-ad9z0x r-zso239 r-bcqeeo r-qvutc0"})
    headitem1 = Items[0].text
    AllHomeItems.append(headitem1)
except:
    AllHomeItems.append("")

try:
    HeaderItems = HomeHeader.find("div",{"data-testid":"UserProfileHeader_Items"})
    Items = HeaderItems.findAll("span",{"class":"css-901oao css-16my406 r-1re7ezh r-4qtqp9 r-1qd0xha r-ad9z0x r-zso239 r-bcqeeo r-qvutc0"})
    headitem2 = Items[1].text
    AllHomeItems.append(headitem2)
except:
    AllHomeItems.append("")
    
try:
    website = HeaderItems.find("a",{"role":"link"}).text
    AllHomeItems.append(website)
except:
    AllHomeItems.append("")
    
try:
    TippyTop = page.find("div",{"class":"css-1dbjc4n r-aqfbo4 r-14lw9ot r-my5ep6 r-rull8r r-qklmqi r-gtdqiz r-ipm5af r-1g40b8q"})
    num_tweets = TippyTop.find("div",{"class":"css-901oao css-bfa6kz r-1re7ezh r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-qvutc0"}).text
    AllHomeItems.append(num_tweets)
except:
    try:
        TippyTop = page.find("div",{"class":"css-1dbjc4n r-1awozwy r-18u37iz r-1h3ijdo r-1777fci r-1jgb5lz r-1ye8kvj r-1j3t67a r-13qz1uu"})
        num_tweets = TippyTop.find("div",{"class":"css-901oao css-bfa6kz r-1re7ezh r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-qvutc0"}).text 
        AllHomeItems.append(num_tweets)
    except:
        AllHomeItems.append("")
        
try:
    FollowLine = HomeHeader.findAll("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-hkyrab r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"})
    followers = FollowLine[1].text
    AllHomeItems.append(followers)
except:
    AllHomeItems.append("")
try:
    FollowLine = HomeHeader.findAll("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-hkyrab r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"})
    following = FollowLine[0].text
    AllHomeItems.append(following)
except:
    AllHomeItems.append("")

AllHomeItems.append("~ARCHIVE STARTED %s"%dt.datetime.now().strftime("%Y/%m/%d @%H:%M:%S"))



if not os.path.exists('TwitterArchives'):
    os.mkdir('TwitterArchives')
    os.chdir('TwitterArchives')
else:
    os.chdir('TwitterArchives')
    
fol_name = '%s-%s'%(AllHomeItems[0].replace('@','').replace(' ',''),dt.datetime.now().strftime("%Y-%m-%d_%H%M"))
if not os.path.exists(fol_name):
    os.mkdir(fol_name)
    os.chdir(fol_name)
else:
    os.chdir(fol_name)
    
    
    
twitter_filename = 'Twitter_%s-%s.txt'%(AllHomeItems[0].replace('@','').replace(' ',''),dt.datetime.now().strftime("%Y-%m-%d_%H%M"))
f = open(twitter_filename,'w')
f.writelines(AllHomeItems[-1])
f.writelines('\n\n')
for h in AllHomeItems[:-1]:
    f.writelines(h)
    f.writelines('\n')
f.close()


RealTweetColl = []
StatusIDs = []
n=0
old_num = -1
new_num = 0
tmax= int(float(input("HOW MANY TWEETS WOULD YOU LIKE TO ARCHIVE? \n(for CNN's volume of content, for example, 300 = ~1 week, 800 = ~1 month)\n")))
nmax=round(tmax/7)

while len(RealTweetColl)<=tmax:
    n += 1
    old_num = len(RealTweetColl)
    TweetElements = browz.find_elements_by_xpath("//article[@role='article']")
    TweetCollection = []
    
    try:
        for t in TweetElements:
            TweetCollection.append(soup(t.get_attribute('innerHTML')))
    except:
        try:
            TweetCollection = []
            time.sleep(1)
            TweetElements = browz.find_elements_by_xpath("//article[@role='article']")
            time.sleep(1)
            for t in TweetElements:
                TweetCollection.append(soup(t.get_attribute('innerHTML')))
        except:
            TweetCollection = []
            TweetElements = []
            browz.execute_script("window.scrollBy(0,-980)")

    for t in TweetCollection:
        HeaderThenStatus = []
        try:
            PostHeader = t.find("div",{"class":"css-1dbjc4n r-m611by"})
            PostInfo = '(%s) '%PostHeader.find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"})['href'].replace('/','') + PostHeader.find("div",{"class":"css-1dbjc4n r-d0pm55"}).find("span",{"class":"css-901oao css-16my406 css-cens5h r-1re7ezh r-1qd0xha r-n6v787 r-1sf4r6n r-bcqeeo r-qvutc0"}).text
            HeaderThenStatus.append(PostInfo)
        except:
            try:
                PostHeader = t.find("div",{"class":"css-1dbjc4n r-m611by"})
                PostInfo = '(%s) '%PostHeader.find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"})['href'].replace('/','') + PostHeader.find("div",{"class":"css-1dbjc4n r-d0pm55"}).find("span",{"class":"css-901oao css-16my406 css-cens5h r-1re7ezh r-1qd0xha r-n6v787 r-1sf4r6n r-bcqeeo r-qvutc0"}).text
                HeaderThenStatus.append(PostInfo)
            except:
                try:
                    PostHeader = t.find("div",{"class":"css-1dbjc4n r-m611by"})
                    PostInfo = PostHeader.find("div",{"class":"css-1dbjc4n r-d0pm55"}).find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
                    HeaderThenStatus.append(PostInfo)
                except:
                    try:
                        PostAdFooter = t.find("div",{"class":"css-1dbjc4n r-1awozwy r-18u37iz r-156q2ks"}).find("div",{"class":"css-901oao r-1re7ezh r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-qvutc0"})
                        Promotion = PostAdFooter.find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
                        HeaderThenStatus.append(Promotion)
                    except:
                        HeaderThenStatus.append("~HEADER NA!")
        try:
            status = t.find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"})['href']
            HeaderThenStatus.append(status)
        except:
            HeaderThenStatus.append("~STATUS NA!")

        if HeaderThenStatus not in StatusIDs:
            StatusIDs.append(HeaderThenStatus)
            RealTweetColl.append(t)
            
    new_num = len(RealTweetColl)

    try:
        browz.execute_script("return arguments[0].scrollIntoView();",TweetElements[-1])
        time.sleep(2)
    except StaleElementReferenceException as Exception:
        browz.execute_script("window.scrollBy(0,980)")
        n=-1
        time.sleep(2)
    except:
        browz.execute_script("window.scrollBy(0,980)")
        time.sleep(2)
    if n>=nmax and old_num==new_num:
        browz.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        break


print('Tweets:',len(RealTweetColl),' Loops:',n,'\n')



PostingHeader = []
FileIndex  =  []
TweeterNickname = []
TweeterUsername = []
TweeterBadge  =  []
TweetDate  =  []
TweetTime  =  []
TweeterIcon  =  []
TweetStatus  =  []
TweetReplyingTo = []
TweetLanguage = []
TweetText  =  []
TweetInTextLinks = []
TweetHashtags = []
TweetMentions = []
TweetPhotos = []
TweetVideo = []
TweetVideoViews = []
TweetVideoDuration = []
ArticlePicture = []
ArticleTitle  =  []
ArticleSummary = []
ArticleSource = []
ArticleLink  =  []
QuoteExist = []
QuotedNickname = []
QuotedUsername = []
QuotedBadge  =  []
QuotedIcon  =  []
QuoteDate  =  []
QuoteTime  =  []
QuoteLanguage = []
QuoteText  =  []
QuotePhotos = []
QuoteVideo  =  []
QuoteThread = []
FooterComments = []
FooterRetweets = []
FooterLikes  =  []
FooterThread  =  []


for t in RealTweetColl:
    try:
        PostHeader = t.find("div",{"class":"css-1dbjc4n r-m611by"})
        PostInfo = '(%s) '%PostHeader.find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"})['href'].replace('/','') + PostHeader.find("div",{"class":"css-1dbjc4n r-d0pm55"}).find("span",{"class":"css-901oao css-16my406 css-cens5h r-1re7ezh r-1qd0xha r-n6v787 r-1sf4r6n r-bcqeeo r-qvutc0"}).text
        PostingHeader.append(PostInfo)
    except:
        try:
            PostHeader = t.find("div",{"class":"css-1dbjc4n r-m611by"})
            PostInfo = '(%s) '%PostHeader.find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"})['href'].replace('/','') + PostHeader.find("div",{"class":"css-1dbjc4n r-d0pm55"}).find("span",{"class":"css-901oao css-16my406 css-cens5h r-1re7ezh r-1qd0xha r-n6v787 r-1sf4r6n r-bcqeeo r-qvutc0"}).text
            PostingHeader.append(PostInfo)
        except:
            try:
                PostHeader = t.find("div",{"class":"css-1dbjc4n r-m611by"})
                PostInfo = PostHeader.find("div",{"class":"css-1dbjc4n r-d0pm55"}).find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
                PostingHeader.append(PostInfo)
            except:
                try:
                    PostAdFooter = t.find("div",{"class":"css-1dbjc4n r-1awozwy r-18u37iz r-156q2ks"}).find("div",{"class":"css-901oao r-1re7ezh r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-qvutc0"})
                    Promotion = PostAdFooter.find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
                    PostingHeader.append(Promotion)
                except:
                    PostingHeader.append('')


for t in RealTweetColl:
    try:
        NameSection = t.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wtj0ep r-zl2h9q"}).find("div",{"class":"css-1dbjc4n r-18u37iz r-1wbh5a2 r-dnmrzs r-1ny4l3l"})
        tweet_fullname = NameSection.find("div",{"class":"css-1dbjc4n r-18u37iz r-dnmrzs"}).text
        try:
            emojis_present = NameSection.findAll("div",{"class":"css-1dbjc4n r-xoduu5 r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-h9hxbl r-417010"})
            if len(emojis_present)>0:
                emojis = ''
                for emo in emojis_present:
                    emojis = emojis + emo['aria-label']
                tweet_fullname = tweet_fullname + ' [[Emojis:' + emojis + ']]'
        except:
            emojis_present = []
        TweeterNickname.append(tweet_fullname)
    except:
        TweeterNickname.append('')
    try:
        NameSection = t.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wtj0ep r-zl2h9q"}).find("div",{"class":"css-1dbjc4n r-18u37iz r-1wbh5a2 r-dnmrzs r-1ny4l3l"})
        tweet_username = NameSection.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wbh5a2 r-1f6r7vd"}).text
        TweeterUsername.append(tweet_username)
    except:
        TweeterUsername.append('')
    try:
        NameSection = t.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wtj0ep r-zl2h9q"}).find("div",{"class":"css-1dbjc4n r-18u37iz r-1wbh5a2 r-dnmrzs r-1ny4l3l"})
        badge = NameSection.find("div",{"class":"css-901oao r-hkyrab r-18u37iz r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}).find("svg")['aria-label']
        TweeterBadge.append(badge)
    except:
        TweeterBadge.append('')
    try:
        tweet_time = t.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wtj0ep r-zl2h9q"}).find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"})['title']
        tweet_date = tweet_time.split(' � ')[1]
        tweet_clock = tweet_time.split(' � ')[0]
        TweetDate.append(tweet_date)
        TweetTime.append(tweet_clock)
    except:
        TweetTime.append('')
        TweetDate.append('')

for t in RealTweetColl:
    try:
        IconPart = t.find("div",{"class":"css-1dbjc4n r-18kxxzh r-1wbh5a2 r-13qz1uu"})
        original_icon = IconPart.find("img",{"class":"css-9pa8cd"})['src']
        TweeterIcon.append(original_icon)
    except: 
        TweeterIcon.append('')

for t in RealTweetColl:
    try:
        status = t.find("a",{"class":"css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"})['href']
        TweetStatus.append('https://twitter.com'+status)
    except:
        TweetStatus.append('')

for t in RealTweetColl:
    try:
        ReplyingTo = t.find("div",{"class":"css-1dbjc4n r-4qtqp9 r-18u37iz r-1wtj0ep r-zl2h9q"}).text 
        TweetReplyingTo.append(ReplyingTo)
    except:
        TweetReplyingTo.append('')
        
langcodes = {'ar':'arabic','en':'english','es':'spanish','fr':'french','af':'afrikaans', \
                'sq':'albanian','am':'amharic','hy':'armenian','bn':'bengali','cs':'czech', \
                'zh':'chinese','cn':'chinese','zh-cn':'chinese','de':'german','nl':'dutch', \
                'el':'greek','eo':'esperanto','et':'estonian','fa':'persian','ka':'georgian', \
                'ga':'irish','ht':'Haitian Creole','he':'hebrew','ha':'hausa','hi':'hindi','rm':'romansh', \
                'is':'icelandic','id':'indonesian','it':'italian','ja':'japanese','ki':'gikuyu', \
                'rw':'Kinya Rwandan','kg':'congolese','la':'latin','ms':'malay','mg':'malagasy', \
                'mn':'mongolian','my':'burmese','ne':'nepali','no':'norwegian','pt':'portuguese', \
                'pl':'polish','qu':'quechua','ro':'romanian','ru':'russian','sa':'sanskrit', \
                'sk':'slovak','sl':'slovenian','so':'somali','sr':'serbian','sw':'swahili','da':'danish', \
                'sv':'swedish','tl':'Filipino Tagalog','th':'thai','bo':'tibetan','tr':'turkish', \
                'ug':'uyghur','uk':'ukrainian','ur':'urdu','uz':'uzbek','vi':'vietnamese', \
                'yi':'yiddish','yo':'yoruba','zu':'zulu','fi':'finnish','ko':'korean','km':'khmer'}
        
for t in RealTweetColl:
    try:
        TextArea = t.find("div",{"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
        tweet_text = TextArea.text
        try:
            emojis_present = TextArea.findAll("div",{"class":"css-1dbjc4n r-xoduu5 r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-h9hxbl r-417010"})
            if len(emojis_present)>0:
                emojis = ''
                for emo in emojis_present:
                    emojis = emojis + emo['aria-label']
                tweet_text = tweet_text + ' [[Emojis:' + emojis + ']]'
        except:
            emojis_present = []
        TweetText.append(tweet_text)
    except:
        try:
            TextArea = t.find("div",{"class":"css-901oao r-hkyrab r-1qd0xha r-1b43r93 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
            tweet_text = TextArea.text
            try:
                emojis_present = TextArea.findAll("div",{"class":"css-1dbjc4n r-xoduu5 r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-h9hxbl r-417010"})
                if len(emojis_present)>0:
                    emojis = ''
                    for emo in emojis_present:
                        emojis = emojis + emo['aria-label']
                    tweet_text = tweet_text + ' [[Emojis:' + emojis + ']]'
            except:
                emojis_present = []
            TweetText.append(tweet_text)
        except:
            TweetText.append('')
            
    try:
        language = t.find("div",{"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})['lang']
        TweetLanguage.append(langcodes[language].capitalize())
    except:
        TweetLanguage.append('')
        
    try:
        TextArea = t.find("div",{"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
        posted_links = TextArea.findAll("a",{"class":"css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1n1174f r-1loqt21 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
        urls = []
        for u in posted_links:
            if 'src=hashtag_click' not in u['href'] and 'http' in u['href']:
                urls.append(u['href'])
        TweetInTextLinks.append(urls)
    except:
        try:
            TextArea = t.find("div",{"class":"css-901oao r-hkyrab r-1qd0xha r-1b43r93 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
            posted_links = TextArea.findAll("a",{"class":"css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1n1174f r-1loqt21 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
            urls = []
            for u in posted_links:
                if 'src=hashtag_click' not in u['href'] and 'http' in u['href']:
                    urls.append(u['href'])
            TweetInTextLinks.append(urls)
        except:
            TweetInTextLinks.append('')
        
for t in RealTweetColl:
    try:
        TextSection = t.find("div",{"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
        BlueLinks = TextSection.findAll("span",{"class":"r-18u37iz"})
        hashtags = []
        mentions = []
        for b in BlueLinks:
            if '#' in b.text: 
                hashtags.append(b.text)
            if '@' in b.text:
                mentions.append(b.text)
        TweetHashtags.append(hashtags)
        TweetMentions.append(mentions)
    except:
        TweetHashtags.append('')
        TweetMentions.append('')
        
for i,t in enumerate(RealTweetColl):
    try:
        all_photos = []
        MediaSection = t.find("div",{"class":"css-1dbjc4n r-9x6qib r-t23y2h r-1phboty r-rs99b7 r-1udh08x"})
        images_list = MediaSection.findAll("img")
        for im in images_list:
            all_photos.append(im['src'])
        TweetPhotos.append(all_photos)
    except:
        TweetPhotos.append('')
        
for i,t in enumerate(RealTweetColl):
    FileIndex.append(i+1)
    try:
        MediaSection = t.find("div",{"class":"css-1dbjc4n r-9x6qib r-t23y2h r-1phboty r-rs99b7 r-1udh08x"})
        vid = MediaSection.find("video")['src']
        TweetVideo.append(vid)
    except:
        TweetVideo.append('')
    try:
        MediaSection = t.find("div",{"class":"css-1dbjc4n r-9x6qib r-t23y2h r-1phboty r-rs99b7 r-1udh08x"})
        view_count = MediaSection.find("span",{"data-testid":"viewCount"}).text
        TweetVideoViews.append(view_count)
    except:
        TweetVideoViews.append('')
    try:
        MediaSection = t.find("div",{"class":"css-1dbjc4n r-9x6qib r-t23y2h r-1phboty r-rs99b7 r-1udh08x"})
        how_much_left = MediaSection.find("span",{"data-testid":"duration"}).text
        TweetVideoDuration.append(how_much_left)
    except:
        TweetVideoDuration.append('')
        
for i,t in enumerate(RealTweetColl):
    try:
        HyperlinkSection = t.find("div",{"class":"css-1dbjc4n r-9x6qib r-t23y2h r-1phboty r-rs99b7 r-1udh08x r-o7ynqc r-1j63xyz"})
        ArticlePreview = HyperlinkSection.find("a",{"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-18u37iz r-1wtj0ep"})
        PicturePreview = HyperlinkSection.find("a",{"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1pi2tsx r-1udh08x r-13qz1uu"})
    except:
        try:
            HyperlinkSection = t.find("div",{"class":"css-1dbjc4n r-9x6qib r-t23y2h r-1phboty r-rs99b7 r-18u37iz r-1udh08x r-o7ynqc r-1j63xyz"})
            ArticlePreview = HyperlinkSection.find("a",{"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-18u37iz r-1wtj0ep"})
            PicturePreview = HyperlinkSection.find("a",{"class":"css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1pi2tsx r-1udh08x r-13qz1uu"})
        except:
            ArticlePreview = -1
            PicturePreview = -1
    
    try:
        link_image  =  PicturePreview.find("img")['src']
        ArticlePicture.append(link_image)
    except:
        ArticlePicture.append('')
    try:
        link_title  =  ArticlePreview.find("div",{"class":"css-901oao css-bfa6kz r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}).text
        ArticleTitle.append(link_title)
    except:
        try:
            link_title = ArticlePreview.find("div",{"class":"css-901oao css-cens5h r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}).text
            ArticleTitle.append(link_title)
        except:
            ArticleTitle.append('')
    try:
        link_summary = ArticlePreview.find("div",{"class":"css-901oao css-cens5h r-1re7ezh r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}).text
        ArticleSummary.append(link_summary + " ...")
    except:
        ArticleSummary.append('')
    try:
        link_source =  ArticlePreview.find("div",{"class":"css-901oao css-bfa6kz r-1re7ezh r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}).text
        ArticleSource.append(link_source)
    except:
        ArticleSource.append('')
    try:
        link_actual = ArticlePreview['href']
        ArticleLink.append(link_actual)
    except:
        ArticleLink.append('')
        
for t in RealTweetColl:
    try:
        QuoteInside = t.find("div",{"class":"css-901oao r-4iw3lz r-1xk2f4g r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-109y4c4 r-ad9z0x r-bcqeeo r-1udh08x r-wwvuq4 r-u8s1d r-92ng3h r-qvutc0"}).find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
        QuoteExist.append(QuoteInside)
    except:
        QuoteExist.append('')
        
for t in RealTweetColl:
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteTextArea = BlockQuote.find("div",attrs={"lang":True})
        quote_text = QuoteTextArea.text
        try:
            emojis_present = QuoteTextArea.findAll("div",{"class":"css-1dbjc4n r-xoduu5 r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-h9hxbl r-417010"})
            if len(emojis_present)>0:
                emojis = ''
                for emo in emojis_present:
                    emojis = emojis + emo['aria-label']
                quote_text = quote_text + ' [[Emojis:' + emojis + ']]'
        except:
            emojis_present = []
        QuoteText.append(quote_text)
    except:
        QuoteText.append('')
        
for t in RealTweetColl:
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteTextArea = BlockQuote.find("div",attrs={"lang":True})
        quote_lang = QuoteTextArea['lang']
        QuoteLanguage.append(langcodes[quote_lang].capitalize())
    except:
        QuoteLanguage.append('')
        
for i,t in enumerate(RealTweetColl):
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteNameHead = BlockQuote.find("div",{"class":"css-1dbjc4n r-1awozwy r-6koalj r-18u37iz r-1wbh5a2 r-vlx1xi r-156q2ks"})
    except:
        try:
            quote_error = t.find("div",{"class":"css-1dbjc4n r-1u4rsef r-1tlfku8 r-t23y2h r-1phboty r-rs99b7 r-1j3t67a r-1w50u8q"}).find("span",{"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
            quote_error = quote_error.text
            QuoteExist[i] = quote_error
        except:
            QuoteNameHead = -1
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteNameHead = BlockQuote.find("div",{"class":"css-1dbjc4n r-1awozwy r-6koalj r-18u37iz r-1wbh5a2 r-vlx1xi r-156q2ks"})
        quote_fullname = QuoteNameHead.find("div",{"class":"css-1dbjc4n r-18u37iz r-dnmrzs"}).text
        try:
            emojis_present = QuoteNameHead.findAll("div",{"class":"css-1dbjc4n r-xoduu5 r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-h9hxbl r-417010"})
            if len(emojis_present)>0:
                emojis = ''
                for emo in emojis_present:
                    emojis = emojis + emo['aria-label']
                quote_fullname = quote_fullname + ' [[Emojis:' + emojis + ']]'
        except:
            emojis_present = []
        QuotedNickname.append(quote_fullname)
    except:
        QuotedNickname.append('')
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteNameHead = BlockQuote.find("div",{"class":"css-1dbjc4n r-1awozwy r-6koalj r-18u37iz r-1wbh5a2 r-vlx1xi r-156q2ks"})
        quote_username = QuoteNameHead.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wbh5a2 r-1f6r7vd"}).text
        QuotedUsername.append(quote_username)
    except:
        QuotedUsername.append('')
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteNameHead = BlockQuote.find("div",{"class":"css-1dbjc4n r-1awozwy r-6koalj r-18u37iz r-1wbh5a2 r-vlx1xi r-156q2ks"})
        quote_time  =  QuoteNameHead.find("div",{"class":"css-901oao r-1re7ezh r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-yrgyi6 r-qvutc0"}).find("span",{"class":"css-901oao css-16my406 r-1re7ezh r-1q142lx r-1qd0xha r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"})['title']
        QuoteDate.append(quote_time.split(' � ')[1])
        QuoteTime.append(quote_time.split(' � ')[0])
    except:
        QuoteDate.append('')
        QuoteTime.append('')
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteNameHead = BlockQuote.find("div",{"class":"css-1dbjc4n r-1awozwy r-6koalj r-18u37iz r-1wbh5a2 r-vlx1xi r-156q2ks"})
        quote_verified = QuoteNameHead.find("div",{"class":"css-901oao r-hkyrab r-18u37iz r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0"}).find("svg")['aria-label']
        QuotedBadge.append(quote_verified)
    except:
        QuotedBadge.append('')
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteNameHead = BlockQuote.find("div",{"class":"css-1dbjc4n r-1awozwy r-6koalj r-18u37iz r-1wbh5a2 r-vlx1xi r-156q2ks"})
        quote_icon  =  QuoteNameHead.find("div",{"class":"css-1dbjc4n r-sdzlij r-1q142lx r-z80fyv r-7o8qx1 r-1udh08x r-19wmn03"}).find("img",{"class":"css-9pa8cd"})['src']
        QuotedIcon.append(quote_icon)
    except:
        QuotedIcon.append('')
        
for i,t in enumerate(RealTweetColl):
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteMediaArea = BlockQuote.find("div",{"class":"css-1dbjc4n r-1g94qm0"})
        quote_vid = QuoteMediaArea.find("video")['src']
        QuoteVideo.append(quote_vid)
    except:
        QuoteVideo.append('')
        
    try:
        BlockQuote = t.find("div",{"role":"blockquote"})
        QuoteMediaArea = BlockQuote.find("div",{"class":"css-1dbjc4n r-1g94qm0"})
        quote_pic_elems = QuoteMediaArea.findAll("img")
        quote_pics = []
        for p in quote_pic_elems:
            quote_pics.append(p['src'])
        QuotePhotos.append(quote_pics)
    except:
        QuotePhotos.append('')
        
        
for i,t in enumerate(RealTweetColl):
    try:
        interactions = t.find("div",{"class":"css-1dbjc4n r-18u37iz r-1wtj0ep r-156q2ks r-1mdbhws"})['aria-label'].split(', ')
    except:
        interactions = -1
    try:
        FooterComments.append([x for x in interactions if 'repl' in x][0])
    except:
        FooterComments.append('0 replies')
    try:
        FooterRetweets.append([x for x in interactions if 'Retweet' in x][0])
    except:
        FooterRetweets.append('0 Retweets')
    try:
        FooterLikes.append([x for x in interactions if 'like' in x][0])
    except:
        FooterLikes.append('0 likes')
        
for i,t in enumerate(RealTweetColl):
    try:
        thread_present = t.find("div",{"class":"css-1dbjc4n r-1iusvr4 r-46vdb2 r-5f2r5o r-bcqeeo r-atwnbb"}).text
        if 'this thread' in thread_present:
            FooterThread.append('Part of a Thread')
    except:
        FooterThread.append('')


fullList = [PostingHeader,FileIndex,TweeterNickname,TweeterUsername,TweeterBadge,TweetDate,TweetTime,TweeterIcon,TweetStatus,TweetReplyingTo,
           TweetLanguage,TweetText,TweetInTextLinks,TweetHashtags,TweetMentions,TweetPhotos,TweetVideo,TweetVideoViews,TweetVideoDuration,
           ArticlePicture,ArticleTitle,ArticleSummary,ArticleSource,ArticleLink,QuoteExist,QuotedNickname,QuotedUsername,
           QuotedBadge,QuotedIcon,QuoteDate,QuoteTime,QuoteLanguage,QuoteText,QuotePhotos,QuoteVideo,FooterComments,
           FooterRetweets,FooterLikes,FooterThread]

fullList = [list(x) for x in zip(*fullList)]

for i,row in enumerate(fullList):
    for j,col in enumerate(row):
        if col==[]:
            fullList[i][j] = ''
            
with open('Twitter_%s-%s.csv'%(AllHomeItems[0].replace('@','').replace(' ',''),dt.datetime.now().strftime("%Y-%m-%d_%H%M")),'w',newline='',encoding='UTF-8') as csvfile:
    writer1 = csv.writer(csvfile,delimiter=',')
    writer1.writerow(['POSTING_HEADER','FILE_INDEX','TWEETER_NICKNAME','TWEETER_USERNAME','TWEETER_BADGE','TWEET_DATE',
                     'TWEET_TIME','TWEETER_ICON','STATUS_ID','REPLYING_TO','TWEET_LANGUAGE','TWEET_TEXT',
                     'IN_TEXT_LINKS','HASHTAGS','MENTIONS','TWEET_PHOTOS','TWEET_VIDEO','VIDEO_VIEWS','VIDEO_DURATION',
                     'ARTICLE_PICTURE','ARTICLE_TITLE','ARTICLE_SUMMARY','ARTICLE_SOURCE','ARTICLE_LINK','QUOTATION',
                     'QUOTED_NICKNAME','QUOTED_USERNAME','QUOTED_BADGE','QUOTED_ICON','QUOTE_DATE','QUOTE_TIME',
                     'QUOTE_LANGUAGE','QUOTE_TEXT','QUOTE_PHOTOS','QUOTE_VIDEO','COMMENTS','SHARES','LIKES','THREAD'])
    for t in fullList:
        writer1.writerow(t)

f = open(twitter_filename,'a')
f.writelines('\n\n')
f.writelines('~ARCHIVE FINISHED %s'%dt.datetime.now().strftime("%Y/%m/%d @%H:%M:%S"))
f.close()

os.chdir('..')
os.chdir('..')
