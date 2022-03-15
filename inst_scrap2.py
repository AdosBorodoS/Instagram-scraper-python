import requests
import undetected_chromedriver as uc
import time as t
import warnings
import os
import shutil
def scrap_intsgram(sliptime=3,                                 
                                way_to_chrom='C:\Program Files\Google\Chrome\Application\chrome.exe',
                                Accaunt_link='https://www.instagram.com/borodidanil/', 
                                Folder_forscraping_results_name="Folder_", 
                                DIR_save="E:/texttttt/",                   
                                public_count_posts=-1,                      
                                like_file=True,
                                like_text=True,
                                closing_chrom_window=False,
                                getting_text_under_post=True,
                                getting_pic_post=True):
 

    warnings.filterwarnings('ignore')

    Instagram1=uc.Chrome(way_to_chrom)
    Instagram1.get(Accaunt_link)
    Instagram1.maximize_window()
    
    
    """
    technical functions for debugging
    """
    def gettingpage_logs(post_page_1):
        with open('page_sours.txt','w',encoding='UTF-8') as fail:
            fail.write(post_page_1)
    def get_ing_fromurl(link):
        r=requests.get(link)

        with open("instagram.jpg",'wb') as f: 
            f.write(r.content)
    """
    technical functions for debugging
    """
    
    def download_pic():
        try_index=0 
        found=False       
        while try_index<5:
            try:
                t.sleep(sliptime)
                but_dow=Instagram1.find_element_by_class_name('buttonForPost')
                t.sleep(sliptime)
                but_dow.click()
                found=True
                break
            except Exception as err:
                print(err)
                try_index+=1
        return found
    def get_pic_post():
        ind=0
        found_button=True
        while ind!=10:
            try:
                if found_button==True:
                    t.sleep(sliptime)
                    result=download_pic()
                    ind+=1
                    Next_pic=Instagram1.find_element_by_class_name('coreSpriteRightChevron')
                    Next_pic.click()
                else:
                    break    
            except Exception as err:
                found_button=False
                print('button not found')
        return ind 
    def get_post_count(numb=-1):
        t.sleep(3)
        main_page=Instagram1.page_source
        post_conter=main_page.find('<span class="g47SY ">')
        post_conter=main_page[post_conter+21:post_conter+100]
        post_conter=post_conter.split('<')
        post_conter=int(post_conter[0])
        if numb<=-1:
            result_count_post=post_conter    
        elif post_conter>numb:
            result_count_post=numb
        else:
            print("There ar't so much post, I choos all posts")
            result_count_post=numb
            
        return result_count_post  
    def getting_likes(like_text_format=True):
        post_page=Instagram1.page_source
        liks_start=post_page.find('<button class="sqdOP yWX7d     _8A5w5    " type="button">')

        if liks_start>=0:
            try:
                liks=post_page[liks_start+57:liks_start+67]
                liks=liks.split('<')
                if int(liks[0][0]) in (1,2,3,4,5,6,7,8,9,0):
                    liks=liks[0].split(' ')
                    liks=int(liks[0])
                else:
                    liks=''

            except Exception:
                liks=''
            
            
            
            try:
                if liks=='':
                    liks_start=post_page.find('<div class="_7UhW9   xLCgt        qyrsm KV-D4              fDxYl    T0kll "><span>')
                    liks=post_page[liks_start+82:liks_start+87]
                    liks=liks.split('<')
                    liks=int(liks[0])
            except Exception:
                liks=''
            
            
            
            try:
                if liks=='':
                    liks_start=post_page.find('ещё <span>')
                    liks=post_page[liks_start+10:liks_start+20]
                    liks=liks.split('<')
                    liks=int(liks[0])+1
            except Exception:
                pass
                

                if type(liks)==type([0,1]):
                    if like_text_format==True:
                        liks='0 like, like not found'
                    else:
                        liks=0
        return liks




    t.sleep(sliptime)
    # getting number post
    public_count=get_post_count(public_count_posts)



    # open first post
    item=Instagram1.find_element_by_class_name('_9AhH0')
    item.click()
    if like_file==True:
        with open(DIR_save+'likes_log.txt','w') as file:
            file.write('Likes log structure made as Folder of post name --> number likes \n\n\n')


    # main cycle
    for i in range(public_count):
        # get number likes
        t.sleep(sliptime+1)
        posts_like=getting_likes(like_text)


        result=1
        if getting_pic_post==True:
            try_index=0        
            while try_index<5:
                try:    
                    result=get_pic_post()
                    break
                except Exception as err:
                    print(err)
                    try_index+=1



        # Getting text under post
        t.sleep(sliptime)
        page=Instagram1.page_source
        start_text=page.find('<span class="_7UhW9   xLCgt      MMzan   KV-D4           se6yk       T0kll ">')
        end_text=page[start_text+77:]
        end_text=end_text[:1500]
        end_text=end_text.split('<')
        end_text=end_text[0]
        




        
        # sotr post staf
        index_of_folder=str(i)
        if getting_text_under_post==False and getting_pic_post==False:
            pass
        elif getting_text_under_post==True or getting_pic_post==True:
            folder_name=Folder_forscraping_results_name+str(i)
            os.mkdir(DIR_save+folder_name)
            if getting_pic_post==True:
                for pic_muve_index in range(result):
                    dir_list=os.listdir(DIR_save)
                    dir_list.sort
                    shutil.move(DIR_save+dir_list[0],DIR_save+folder_name)
        



        #wrting text post to txt in sort folder
        if getting_text_under_post==True:
            with open(DIR_save+folder_name+'/post_text.txt','w',encoding="UTF-8")as file:
                file.write(end_text)
        



        # getting likes log file
        if like_file==True:
            if like_text==True and (getting_text_under_post==True or getting_pic_post==True):
                with open(DIR_save+'likes_log.txt','a') as file:
                    file.write(folder_name+' --> '+str(posts_like)+'\n')
            else:
                with open(DIR_save+'likes_log.txt','a') as file:
                    file.write(index_of_folder+' ; '+str(posts_like)+'\n')
        
        
        
        
        #Getting "Next post" button 
        try_index=0
        found=False
        
        while try_index<5:
            try:
                t.sleep(sliptime)
                but=Instagram1.find_element_by_class_name('l8mY4')
                but.click()
                found=True
                break
            except Exception as err:
                print(err)
                try_index+=1



        if found==False:
            print('"Next post" button not found')
            print('scraping was successful')

    # Closing chrom window
    if closing_chrom_window==True:
        Instagram1.close()




####################################################################################################################################################################
#  function call example
scrap_intsgram(sliptime=2,
                closing_chrom_window=True,
                public_count_posts=100,
                getting_pic_post=False)

####################################################################################################################################################################