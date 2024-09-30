from web_pages_cs import web_page_cs110, web_page_ed_stem
from bs4 import BeautifulSoup
from date_conversion import convert_date
from assignment_tracker import Driver
import requests

XPATHS_ED_STEM = {"i_username": '//*[@id="x1"]', "i_username": '//*[@id="x2"]'}


months = {"Sept": "Sep", "Aug": "Aug"}
ED_STEM_LINK = "https://edstem.org/us/dashboard"
CSCI_PAGE_LINK = "https://csci110.page/"

# page_source_csci =

cs110_soup = BeautifulSoup(web_page_cs110, "html.parser")

week1 = cs110_soup.find_all("dl")


def get_all_assignments_cs110(page_source):
    all_assignments = {}
    time_string = "11:59pm"
    year = 2024
    cs110_soup = BeautifulSoup(page_source, "html.parser")
    dl_elements = cs110_soup.find_all("dl")
    for dl_element in dl_elements:
        if dl_element.parent.name == "dd":
            dt_texts = dl_element.find("dt").text
            if "Due" in dt_texts:
                dt_lists = dt_texts.split("Due: ")
                assignment_name = dt_lists[0]
                assignment_due_date = (
                    f'{months[dt_lists[1].split(" ")[0]]} {dt_lists[1].split(" ")[1]}'
                )
                converted_assignment_due_date = convert_date(
                    year, f"{assignment_due_date}  {time_string}"
                )
                all_assignments[converted_assignment_due_date] = assignment_name
    return all_assignments


ed_stem_driver = Driver(ED_STEM_LINK, XPATHS_ED_STEM)


# print(get_all_assignments_cs110(web_page_cs110))

# records = week1.find_all("dd")
# # print(records)
# for i in records:
#     j = i.find_all("dt")
#     for k in j:
#         if k:
#             print(k.text)
# if j:
#     try:
#         if "Due:" in i.find("dd").text:
#             print(i.find("dd").find("dd").text, "  if")
#         print(i.find("dd").text, "else")
#     except AttributeError as e:
#         pass
# print(i.find("dd"))
# print(cs110_soup.find("dd").find("dd").find_next("dd").find_next("dd").text)


# print(cs110_soup.find("dd").find("dd").find_next("dd").parent.find("dt").text)

# with open("test.txt", "w") as f:
#     for i in cs110_soup:
#         if i.parent.name == "dt" and i.parent.name.find_all("a"):
#             f.write(i.text)
#             f.write("\n")
# for j in i.find_all("dd"):
#     # f.write(str(j.text))
#     # f.write("\n")
#     for k in j.find_all("dd"):
#         if "Due" in k.text:
#             f.write(str(k.text))
#             f.write("\n")
# for j in i.find_all("dt"):
#     f.write(j.text)
#     f.write("\n")
# f.write()
