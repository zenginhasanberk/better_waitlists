import requests
import notifypy
import pandas as pd
import smtplib
from pywhatkit import send_mail
from bs4 import BeautifulSoup


def main():
    courseUrl = input(
        "Please input course URL (just copy and paste from the URL bar above)\n"
    )

    try:
        r = requests.get(
            "https://lsa.umich.edu/cg/cg_detail.aspx?content=2410EECS280001&termArray=f_22_2410"
        )
    except:
        print("Incorrect URL!")
        return
    else:
        print("")

    soup = BeautifulSoup(r.text, "html.parser")

    results1 = soup.find_all(
        "div",
        attrs={
            "class": "row clsschedulerow toppadding_main bottompadding_main",
            "style": "margin-left:0px; margin-right:0px; background-color: #eff0f1;",
        },
    )
    results2 = soup.find_all(
        "div",
        attrs={
            "class": "row clsschedulerow toppadding_main bottompadding_main",
            "style": "margin-left:0px; margin-right:0px; background-color: #ffffff;",
        },
    )

    list = []

    for result in results1:
        dict = {}
        for tag in result.find_all("div", class_="hidden-md hidden-lg xs_label"):
            if tag.next_sibling.strip() != "":
                dict[tag.text] = tag.next_sibling.strip()
            else:
                if tag.text == "Section:":
                    dict[tag.text] = result.find("span").text
                elif tag.text == "Instruction Mode:":
                    if result.find_all("i", class_="fa fa-user"):
                        dict[tag.text] = result.find_all("i", class_="fa fa-user")[
                            0
                        ].next_sibling.strip()
                    else:
                        dict[tag.text] = result.find_all("i", class_="fa fa-desktop")[
                            0
                        ].next_sibling.strip()
                elif tag.text == "Enroll Stat:":
                    dict[tag.text] = result.find_all("span")[1].text
                elif tag.text == "Meeting Day/Time/Location:":
                    dict[tag.text] = (
                        result.find_all("td", attrs={"class": "MPCol_Day"})[0].text,
                        result.find_all("td", attrs={"class": "MPCol_Time"})[
                            0
                        ].text.strip(),
                    )

        list.append(dict)

    for result in results2:
        dict = {}
        for tag in result.find_all("div", class_="hidden-md hidden-lg xs_label"):
            if tag.next_sibling.strip() != "":
                dict[tag.text] = tag.next_sibling.strip()
            else:
                if tag.text == "Section:":
                    dict[tag.text] = result.find("span").text
                elif tag.text == "Instruction Mode:":
                    if result.find_all("i", class_="fa fa-user"):
                        dict[tag.text] = result.find_all("i", class_="fa fa-user")[
                            0
                        ].next_sibling.strip()
                    else:
                        dict[tag.text] = result.find_all("i", class_="fa fa-desktop")[
                            0
                        ].next_sibling.strip()
                elif tag.text == "Enroll Stat:":
                    dict[tag.text] = result.find_all("span")[1].text
                elif tag.text == "Meeting Day/Time/Location:":
                    dict[tag.text] = (
                        result.find_all("td", attrs={"class": "MPCol_Day"})[0].text,
                        result.find_all("td", attrs={"class": "MPCol_Time"})[
                            0
                        ].text.strip(),
                    )

        list.append(dict)

    sorted = sorted(list, key=lambda elem: elem["Section:"])
    print(sorted)

    # for element in state:
    # print(element.text)
    # print(state)

    # print(result.find_all('span'))
