from pywhatkit import send_mail


# code for desktop notification below
"""
notification = notifypy.Notify()
notification.title = 'Open class slot!'
notification.message = 'There is an open slot for your {} class!'.format('CHANGE HERE')
notification.application_name = 'Class Helper'

notification.send()

"""

# important note use google app passwords

# first working code

"""
    for tag in result.find_all('div', class_='hidden-md hidden-lg xs_label'):
        if (tag.next_sibling.strip() != ''):
            print(tag.text, tag.next_sibling.strip())
        else:
            if (tag.text == 'Section:'):
                print(tag.text, result.find('span').text)
            elif (tag.text == 'Instruction Mode:'):
                print(tag.text, result.find_all('i', class_='fa fa-user')[0].next_sibling.strip())
            elif (tag.text == 'Enroll Stat:'):
                print(tag.text, result.find_all('span')[1].text)
            elif (tag.text == 'Meeting Day/Time/Location:'):
                print(tag.text, result.find_all('td', attrs={'class':'MPCol_Day'})[0].text, result.find_all('td', attrs={'class':'MPCol_Time'})[0].text)
    
    break

"""

# second working code

"""

    for tag in result.find_all('div', class_='hidden-md hidden-lg xs_label'):
        if (tag.next_sibling.strip() != ''):
            print(tag.text, tag.next_sibling.strip())
        else:
            if (tag.text == 'Section:'):
                print(tag.text, result.find('span').text)
            elif (tag.text == 'Instruction Mode:'):
                if result.find_all('i', class_='fa fa-user'):
                    print(tag.text, result.find_all('i', class_='fa fa-user')[0].next_sibling.strip())
                else:
                    print(tag.text, result.find_all('i', class_='fa fa-desktop')[0].next_sibling.strip())        
            elif (tag.text == 'Enroll Stat:'):
                print(tag.text, result.find_all('span')[1].text)
            elif (tag.text == 'Meeting Day/Time/Location:'):
                print(tag.text, result.find_all('td', attrs={'class':'MPCol_Day'})[0].text, result.find_all('td', attrs={'class':'MPCol_Time'})[0].text.strip())
    
    break

"""

"""
for result in results1:
    dict = {}
    for tag in result.find_all('div', class_='hidden-md hidden-lg xs_label'):
        if (tag.next_sibling.strip() != ''):
            dict[tag.text] = tag.next_sibling.strip()
        else:
            if (tag.text == 'Section:'):
                dict[tag.text] = result.find('span').text
            elif (tag.text == 'Instruction Mode:'):
                if result.find_all('i', class_='fa fa-user'):
                    dict[tag.text] = result.find_all('i', class_='fa fa-user')[0].next_sibling.strip()
                else:
                    dict[tag.text] = result.find_all('i', class_='fa fa-desktop')[0].next_sibling.strip()    
            elif (tag.text == 'Enroll Stat:'):
                dict[tag.text] = result.find_all('span')[1].text
            elif (tag.text == 'Meeting Day/Time/Location:'):
                dict[tag.text] = result.find_all('td', attrs={'class':'MPCol_Day'})[0].text, result.find_all('td', attrs={'class':'MPCol_Time'})[0].text.strip()
    
    print(dict)
    break
"""
