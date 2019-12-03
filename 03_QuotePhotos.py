# THIS IS FOR IN-QUOTE PHOTOS!!! 

old_tab = browz.window_handles[0]
browz.switch_to.window(old_tab)
browz.execute_script("newtab = window.open();")
new_tab = browz.window_handles[1]
browz.switch_to.window(old_tab)
small_alphabet = ['A','B','C','D']
q_redu = []
q_redui = []

if not os.path.exists('Photos'):
    os.mkdir('Photos')
    os.chdir('Photos')
else:
    os.chdir('Photos')
    
if not os.path.exists('QuotePhotos'):
    os.mkdir('QuotePhotos')
    os.chdir('QuotePhotos')
else:
    os.chdir('QuotePhotos')

for i,P in enumerate(QuotePhotos):
    if len(P)>0:
        for n,L in enumerate(P):
            browz.switch_to.window(new_tab)
            if L not in q_redu:
                q_redu.append(L)
                q_redui.append([i,n])
                browz.get(L)
                QP_name = 'Quote_%i_Photo_%s.png'%(i+1,small_alphabet[n])
                try:
                    WebDriverWait(browz,5).until(EC.presence_of_element_located((By.TAG_NAME,'img')))
                    QP_elem = browz.find_element_by_tag_name('img')
                    QP_elem.screenshot(QP_name)
                except:
                    f = open(QP_name+'.ERROR','w')
                    f.close()
            else:
                q_redu.append('')
                q_redui.append([i,n])
                QP_name = 'Quote_%i_Photo_%s.png'%(i+1,small_alphabet[n])
                f = open(QP_name+'.SAMEAS%i%s.ERROR'%(q_redu.index(L),small_alphabet[q_redui[q_redu.index(L)][1]]),'w')
                f.close()
    else:
        q_redui.append([i,0])
        q_redu.append('')
    
browz.close()
browz.switch_to.window(old_tab)
os.chdir('..')
os.chdir('..')