seventh=None
import time
import selenium
import sys
import html2text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
counter=0
howlong = 0
try:
    while counter<=howlong:
        try:
            browser.quit()       
        except:
            pass
        counter+=1
        f=open('usernamepass.txt','r') 
        p=f.readlines()
        try:
            usp = p[counter].split(' ')
        except:
            sys.exit()
        howlong = len(p)-1


        start_time = time.time()
        print("Welcome to the Unweighted GPA Calculator by Suhas Hariharan, Work in Progress. Currently not working if you have Attendanc Free as a period.")

        userz=usp[0]
        passz=usp[1]
        behind = len(passz) - 1
        if passz[behind] == "\n":
            passz = passz[0:behind]
        WINDOW_SIZE = "1920,1080"
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get("https://powerschool.sas.edu.sg/public/")
        try:
            username = browser.find_element_by_id("fieldAccount")
            password = browser.find_element_by_id("fieldPassword")
            username.send_keys(userz)
            password.send_keys(passz+"\n")
        except:
            print('error attempting to continue')
        browser.get('https://powerschool.sas.edu.sg/guardian/homeHS.html')
        listofcodesnotparsed=browser.find_elements_by_xpath('//a[contains(@href, "scores.html")]')
        listofcodesparsed=[]

        for i in listofcodesnotparsed:
            listofcodesparsed.append(i.get_attribute('outerHTML'))
        listofcodesparsed.pop(0)
        string = ''.join(listofcodesparsed)
        alllinks=[]
        index=0
        for i in string:
                index+=1
                if i == "f":
                       

                        if string[index]=="r":
                                



                                valuez=[string[index+3],string[index+4],string[index+5],string[index+6],string[index+7],string[index+8],string[index+9],string[index+10],string[index+11]]
                                alllinks.append(valuez)
                                
        baseurl='https://powerschool.sas.edu.sg/guardian/scores.html?frn='
        print(len(alllinks))
        if len(alllinks) == 6:
            url1=baseurl+"".join(alllinks[0])
            url2=baseurl+"".join(alllinks[1])
            url3=baseurl+"".join(alllinks[2])
            url4=baseurl+"".join(alllinks[3])
            url5=baseurl+"".join(alllinks[4])
            url6=baseurl+"".join(alllinks[5])

            #eventually figure out which is double block and weight accordingly
        elif len(alllinks)==7:
            url1=baseurl+"".join(alllinks[0])
            url2=baseurl+"".join(alllinks[1])
            url3=baseurl+"".join(alllinks[2])
            url4=baseurl+"".join(alllinks[3])
            url5=baseurl+"".join(alllinks[4])
            url6=baseurl+"".join(alllinks[5])
            url7=baseurl+"".join(alllinks[6])
            extralink=url7
            
            try:
                extralink=baseurl+"".join(alllinks[7])
            except:
                pass
            
        elif len(alllinks)==8:
            url1=baseurl+"".join(alllinks[0])
            url2=baseurl+"".join(alllinks[1])
            url3=baseurl+"".join(alllinks[2])
            url4=baseurl+"".join(alllinks[3])
            url5=baseurl+"".join(alllinks[4])
            url6=baseurl+"".join(alllinks[5])
            url7=baseurl+"".join(alllinks[6])
            extralink=baseurl+"".join(alllinks[7])

            
        def getgrades(linktopage):
                WINDOW_SIZE = "1920,1080"

                chrome_options = Options()  
                chrome_options.add_argument("--headless")  
                chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

                browser = webdriver.Chrome(chrome_options=chrome_options)
                
                browser.get("https://powerschool.sas.edu.sg/public/")

                username = browser.find_element_by_id("fieldAccount")
                password = browser.find_element_by_id("fieldPassword")
                username.send_keys(userz)
                password.send_keys(passz+"\n")

                browser.get(linktopage)
                random_grades = browser.find_element_by_tag_name('tbody')
                random_grades = random_grades.get_attribute('innerHTML')

                with open('grades.html', 'w') as f:
                    f.write("")
                    f.close()
                with open('grades.html', 'a') as f:
                    f.write(random_grades)
                    f.write('<td />')
                    f.close()
                with open('grades.html', 'r') as f:
                    f= (f.readlines())
                h = html2text.HTML2Text()
                h.ignore_links = True
                final = h.handle(str(f))
                doubleblock=browser.find_element_by_class_name('box-round').text
                ndoubleblock=doubleblock.split(' ')
                global seventh
                
           
                for i in final:
                        if i in ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']:
                                if i == "F":
                                        shouldnot=final.find(i) + 1
                                        if final[shouldnot] == "i":
                                                continue


                                
                                else:
                                        shouldnot= final.find(i)+1
                                        if final[shouldnot] in ["+","-"]:
                                                finalgrade=[i,final[shouldnot]]
                                                
                                                finallettergrade = ''.join(finalgrade)
                                                if ndoubleblock[0] == "English" and ndoubleblock[1] == "9/World":
                                                    seventh=finallettergrade
                                                    
                                                    return(finallettergrade,seventh)
                                                else:
                                                    pass
                                                    
                
                                                return(finallettergrade)
                                        else:
                                            finallettergrade = (i)
                                            if ndoubleblock[0] == "English" and ndoubleblock[1] == "9/World":
                                                    seventh=finallettergrade
                                                    print('dubletruble')
                                                    return(finallettergrade,seventh)
                                                    
                                            else:
                                                
                                                print('noduble')
                                            return(finallettergrade)
                


                
                


        first=getgrades(url1)
        if type(first)==list or type(first)==tuple:
            seventh=first[1]
            first=first[0]

        second=getgrades(url2)
        if type(second)==list or type(second)==tuple:
            seventh=second[1]
            second=second[0]
        third=getgrades(url3)
        if type(third)==list or type(third)==tuple:
            seventh=third[1]
            third=third[0]

        fourth=getgrades(url4)
        if type(fourth)==list or type(fourth)==tuple:
            seventh=fourth[1]
            fourth=fourth[0]

        fifth=getgrades(url5)
        if type(fifth)==list or type(fifth)==tuple:
            seventh=fifth[1]
            fifth=fifth[0]

        sixth = getgrades(url6)
        if type(sixth)==list or type(sixth)==tuple:
            seventh=sixth[1]
            sixth=sixth[0]




        allgrades=[first,second,third,fourth,fifth,sixth,seventh]


                #seventh=input("The program has detected that you are taking 6 subjects instead of 7, please enter the grade of the subject you are doing a double block in(eg. World Studies): ")
        try:
            print("dont skip this")
            allgrades=[first,second,third,fourth,fifth,sixth,seventh]
        except:
            pass


        else:
                try:
                    seventh=getgrades(url7)
                    print('not in double block, proceeding')
                except:
                    pass

        for i in allgrades:
            if i is None:
                allgrades.pop(allgrades.index(i))
                if len(allgrades) > 5:
                    finalgradeifnot = getgrades(extralink)
                    allgrades.append(finalgradeifnot)
        total = 0
        for element in allgrades:
                if element == "A+":
                    total = total + 4.5
                elif element == "A":
                    total = total + 4.0
                elif element == "A-":
                    total = total + 3.7
                elif element == "B+":
                    total = total + 3.3
                elif element == "B":
                    total = total + 3.0
                elif element == "B-":
                    total = total + 2.7
                elif element == "C+":
                    total = total + 2.3
                elif element == "C":
                    total = total + 2.0
                elif element == "C-":
                    total = total + 1.7
                elif element == "D+":
                    total = total + 1.3
                elif element == "D":
                        total=total+1.0
                elif element == "F":
                        total=total+0
            
        gpa = total /7
        try:
            print("tryblockgottentoo")
            with open ('gpas.txt','r') as file:
                zcounter=counter-1
                z=file.read()
                g=z.split('\n')
                oldgpa = g[zcounter]
        except:
            oldgpa=0
            
        
    
        
        if str(gpa) != oldgpa:
            
            print('GPA has changed!')
            p=open('gpas.txt','r+')
            z=p.read()
            g=z.split('\n')
            zcounter = counter - 1
            z=z.replace(oldgpa,str(gpa))
            p.close()
            with open('gpas.txt', 'w') as file:
                file.write(z)
                file.close()
        else:
            print('nothing happens')
            
            
        print("--- %s seconds ---" % (time.time() - start_time))
        print(gpa)
        browser.quit()       

        try:
            browser.quit()       
        except:
            pass
    
    

            
            
            
            
except Exception as e:
    print(e)
    browser.quit()
    sys.exit()
    
