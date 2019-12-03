# THIS IS FOR TEXT TRANSLATIONS!!!

trans_url = "https://translate.google.com/#view=home&op=translate&sl=auto&tl=en"
trans_browz = webdriver.Chrome('C:/chromedriver.exe')

g = open(twitter_filename[:-19]+'TEXT_TRANSLATIONS.txt','w',encoding='UTF-8')

for i,t in enumerate(TweetText):
    if TweetLanguage[i]!='English' and TweetLanguage[i]!='' and TweetLanguage[i].lower()!='und' and TweetLanguage[i]!="~ERROR!":
        trans_browz.get(trans_url)
        text_input = trans_browz.find_element_by_xpath("//*[@class='orig tlid-source-text-input goog-textarea']")
        text_input.click()
        text_input.send_keys(TweetText[i])
        WebDriverWait(trans_browz,5).until(EC.presence_of_element_located((By.CLASS_NAME,'tlid-copy-target')))
        text_output = trans_browz.find_element_by_xpath("//*[@class='result tlid-copy-target']")
        text_trans = soup(text_output.get_attribute('innerHTML'),'lxml').find("span",{"class":"tlid-translation"}).text
        g.writelines('['+str(i+1)+']  '+'GOOGLE TRANSLATE FROM '+TweetLanguage[i].upper()+': \n')
        g.writelines(text_trans)
        g.writelines('\n\n')
    else:
        pass

g.close()


# THIS IS FOR QUOTE TRANSLATIONS!!!

g = open(twitter_filename[:-19]+'QUOTE_TRANSLATIONS.txt','w',encoding='UTF-8')

for i,t in enumerate(QuoteText):
    try:
        if QuoteLanguage[i]!='English' and QuoteLanguage[i]!='' and QuoteLanguage[i].lower()!='und' and QuoteLanguage[i]!="~ERROR!":
            trans_browz.get(trans_url)
            text_input = trans_browz.find_element_by_xpath("//*[@class='orig tlid-source-text-input goog-textarea']")
            text_input.click()
            text_input.send_keys(QuoteText[i])
            WebDriverWait(trans_browz,5).until(EC.presence_of_element_located((By.CLASS_NAME,'tlid-copy-target')))
            text_output = trans_browz.find_element_by_xpath("//*[@class='result tlid-copy-target']")
            quot_trans = soup(text_output.get_attribute('innerHTML'),'lxml').find("span",{"class":"tlid-translation"}).text
            g.writelines('['+str(i+1)+']  '+'GOOGLE TRANSLATE FROM '+QuoteLanguage[i].upper()+': \n')
            g.writelines(quot_trans)
            g.writelines('\n\n')
        else:
            pass
    except:
        g.writelines('['+str(i+1)+']  '+'GOOGLE TRANSLATE FROM '+QuoteLanguage[i].upper()+': \n')
        g.writelines('**~~ TRANSLATION ERROR! ~~**')
        g.writelines('\n\n')

g.close()
trans_browz.close()