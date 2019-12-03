# THIS IS FOR DIRECTLY POSTED PHOTOS!!! 

old_tab = browz.window_handles[0]
browz.switch_to.window(old_tab)
browz.execute_script("newtab = window.open();")
new_tab = browz.window_handles[1]
browz.switch_to.window(old_tab)
small_alphabet = ['A','B','C','D']
redu = []
redui = []

os.chdir('TwitterArchives')
os.chdir(fol_name)

if not os.path.exists('Photos'):
    os.mkdir('Photos')
    os.chdir('Photos')
else:
    os.chdir('Photos')

for i,P in enumerate(TweetPhotos):
    if len(P)>0:
        for n,L in enumerate(P):
            browz.switch_to.window(new_tab)
            if L not in redu:
                redu.append(L)
                redui.append([i,n])
                browz.get(L)
                photo_name = 'Tweet_%i_Photo_%s.png'%(i+1,small_alphabet[n])
                try:
                    WebDriverWait(browz,5).until(EC.presence_of_element_located((By.TAG_NAME,'img')))
                    pic_elem = browz.find_element_by_tag_name('img')
                    pic_elem.screenshot(photo_name)
                except:
                    f = open(photo_name+'.ERROR','w')
                    f.close()
            else:
                redu.append('')
                redui.append([i,n])
                photo_name = 'Tweet_%i_Photo_%s.png'%(i+1,small_alphabet[n])
                f = open(photo_name+'.SAMEAS%i%s.ERROR'%(redu.index(L),small_alphabet[redui[redu.index(L)][1]]),'w')
                f.close()
    else:
        redui.append([i,0])
        redu.append('')
    
browz.close()
browz.switch_to.window(old_tab)
os.chdir('..')