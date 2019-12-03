# THIS IS FOR MAIN TWEET ICONS!!! 

old_tab = browz.window_handles[0]
browz.switch_to.window(old_tab)
browz.execute_script("newtab = window.open();")
new_tab = browz.window_handles[1]
browz.switch_to.window(old_tab)

i_redu = []
i_redui = []

if not os.path.exists('Photos'):
    os.mkdir('Photos')
    os.chdir('Photos')
else:
    os.chdir('Photos')
    
if not os.path.exists('Icons'):
    os.mkdir('Icons')
    os.chdir('Icons')
else:
    os.chdir('Icons')
    
if not os.path.exists('MainTweeterIcons'):
    os.mkdir('MainTweeterIcons')
    os.chdir('MainTweeterIcons')
else:
    os.chdir('MainTweeterIcons')
    
for i,P in enumerate(TweeterIcon):
    if len(P)>0:
        if P not in i_redu:
            browz.switch_to.window(new_tab)
            i_redu.append(P)
            browz.get(P)
            ico_name = '%s-FirstSeen_%i.png'%(TweeterUsername[i].replace('@',''),i+1)
            try:
                WebDriverWait(browz,5).until(EC.presence_of_element_located((By.TAG_NAME,'img')))
                ico_elem = browz.find_element_by_tag_name('img')
                ico_elem.screenshot(ico_name)
            except:
                f = open(ico_name+'.ERROR','w')
                f.close()
        else:
            i_redu.append('')
            i_redui.append(i)
            ico_name = '%s-Redundant_%i.ERROR'%(TweeterUsername[i].replace('@',''),i+1)
            f = open(ico_name,'w')
            f.close()
            
    else:
        i_redu.append('')
        i_redui.append(i)
        
browz.close()
browz.switch_to.window(old_tab)
os.chdir('..')
os.chdir('..')
os.chdir('..')