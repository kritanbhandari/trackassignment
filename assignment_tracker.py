from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from encryption_decryption import decrypter
from operator import itemgetter
import csv
from reading_grades import ParseTableDataCanvas
from sqlite3 import IntegrityError
from datetime import datetime
from page import web_page


class Driver:
    def __init__(self, link, xpaths):
        self.link = link
        self.driver = webdriver.Firefox()
        self.xpath = xpaths

    def start(self):
        self.driver.get(self.link)
        self.driver.maximize_window()

    def check_element_exists(self, xpath):
        while True:
            try:
                if self.driver.find_element(By.XPATH, xpath):
                    # print(xpath)
                    break
            except NoSuchElementException:
                time.sleep(1)
        time.sleep(
            2
        )  # Some elements might not appear on the screen (for instance pop-up) even if they exist
        return True

    def find_element(self, xpath):
        if self.check_element_exists(xpath):
            return self.driver.find_element(By.XPATH, xpath)

    def end(self):
        self.driver.close()


def get_index_immediate_assignment(grades, submitted_dates):
    """Returns the index of the assignment that has the earliest due date.
    Returns None if all assignments have been submitted and/or graded or there are no assignments.
    """
    index_immediate_assignment = 0
    while index_immediate_assignment < len(grades) and index_immediate_assignment < len(
        submitted_dates
    ):
        if (
            grades[index_immediate_assignment] == "-"
            and not submitted_dates[index_immediate_assignment]
        ):
            return index_immediate_assignment
        index_immediate_assignment += 1


def add_duplicates(index, due_dates, index_list):
    """Adds index of the same due dates to the list passed, so that the duplicates dates are also included"""
    index_list.append(index)
    if due_dates[index + 1]:
        if due_dates[index].strftime("%d %b") != due_dates[index + 1].strftime("%d %b"):
            return index_list
        add_duplicates(index + 1, due_dates, index_list)


def get_index_next_assignment(
    index_immediate_assignment, due_dates, submitted_dates, grades
):
    """Returns the index of the next assignment that is due after the earliest due date"""
    if due_dates[index_immediate_assignment + 1]:
        while index_immediate_assignment < len(due_dates) and due_dates[
            index_immediate_assignment
        ].strftime("%d %b") == due_dates[index_immediate_assignment + 1].strftime(
            "%d %b"
        ):
            index_immediate_assignment += 1
    if (
        not submitted_dates[index_immediate_assignment + 1]
        and grades[index_immediate_assignment + 1] == "-"
    ):
        return index_immediate_assignment + 1


def get_index_immediate_two_assignments(scores, submitted_dates, due_dates):
    """Returns a list with the indices of the earliest two assignments that are due.
    Also Includes duplicate due dates. Only returns one index when due dates aren't available
    """
    indices = []
    try:
        index1 = get_index_immediate_assignment(scores, submitted_dates)
        if index1:
            add_duplicates(index1, due_dates, indices)
            index2 = get_index_next_assignment(
                index1, due_dates, submitted_dates, scores
            )
            print(submitted_dates[index1 + 2])
            if index2:
                # print(index2)
                add_duplicates(index2, due_dates, indices)
    except IndexError:
        pass
    return indices


def get_username_password():
    """Getting the encrypted data from a csvfile and decrypting it with the key"""
    with open("data.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        # To get the first line of data
        key, username, password = itemgetter("key", "username", "password")(
            reader.__next__()
        )
    decrypted_username = decrypter(key, username)
    decrypted_password = decrypter(key, password)
    return decrypted_username, decrypted_password


def sign_in(driver, username, password):
    # Sign-in page
    i_username = driver.find_element(driver.xpath["i_username"])
    i_password = driver.find_element(driver.xpath["i_password"])
    b_submit = driver.find_element(driver.xpath["b_submit"])

    i_username.send_keys(username)
    i_password.send_keys(password)
    b_submit.click()


def click_prompts(driver):
    # Clicking prompts
    b_hello_prompt = driver.find_element(driver.xpath["b_hello_prompt"])
    b_hello_prompt.click()

    b_student_tour = driver.find_element(driver.xpath["b_student_tour"])
    b_student_tour.click()


def get_grade_page_source(driver, course_name):
    b_nav_courses = driver.find_element(driver.xpath["b_nav_courses"])
    b_nav_courses.click()

    l_composition = driver.find_element(driver.xpath[f"l_{course_name}"])
    l_composition.click()

    l_composition_grades = driver.find_element(driver.xpath[f"l_{course_name}_grades"])
    l_composition_grades.click()
    return driver.driver.page_source


def get_lists(page_source):
    table_id = "grades_summary"
    composition_table = ParseTableDataCanvas(page_source, table_id)
    composition_table_tag = composition_table.get_table()

    assignment_due_dates = composition_table.find_assignment_due_date(
        composition_table_tag
    )
    assignment_names = composition_table.find_assignment_names(composition_table_tag)
    assignment_submitted_dates = composition_table.find_assignment_submitted_date(
        composition_table_tag
    )
    assignment_links = composition_table.find_assignment_link(composition_table_tag)
    assignment_scores = composition_table.find_assignment_score(composition_table_tag)

    assignment_subject_name = composition_table.find_assignment_name()

    return (
        assignment_subject_name,
        assignment_names,
        assignment_links,
        assignment_due_dates,
        assignment_submitted_dates,
        assignment_scores,
    )


def get_table_assignment_names(table_assignments):
    current_assignments_names = []
    for i in table_assignments.query_rows():
        current_assignments_names.append(i[2])
    return current_assignments_names


# driver = webdriver.Firefox()
# driver.get("https://fisk.instructure.com/")
# driver.maximize_window()

# action = ActionChains(driver)


# def check_element_exists(xpath):
#     while True:
#         try:
#             if driver.find_element(By.XPATH, xpath):
#                 # print(xpath)
#                 break
#         except NoSuchElementException:
#             time.sleep(1)
#     time.sleep(2) #Some elements might not appear on the screen (for instance pop-up) even if they exist
#     return True

# What if the element never exists?

# def find_element(xpath):
#     if check_element_exists(xpath):
#         return driver.find_element(By.XPATH, xpath)
# if __name__ == '__main__':
#     link = "https://fisk.instructure.com/"
#     driver = Driver(link)
#     driver.start()

#     with open('data.csv', 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         # To get the first line of data
#         key, username, password = itemgetter('key', 'username', 'password')(reader.__next__())
#     decrypted_username = decrypter(key, username)
#     decrypted_password = decrypter(key, username)


# i_username = find_element(XPATHS['i_username'])
# i_password = find_element(XPATHS['i_password'])
# b_submit = find_element(XPATHS['b_submit'])

# with open('data.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     # To get the first line of data
#     key, username, password = itemgetter('key', 'username', 'password')(reader.__next__())

# fernet = Fernet(key.encode())

# # Assuming that the user has to login every time the script is run
# i_username.send_keys(fernet.decrypt(username.encode()).decode())
# i_password.send_keys(fernet.decrypt(password.encode()).decode())
# b_submit.click()
# time.sleep(15)


# b_hello_prompt = find_element(XPATHS['b_hello_prompt'])
# b_hello_prompt.click()

# b_student_tour = find_element(XPATHS['b_student_tour'])
# b_student_tour.click()


# b_nav_courses = find_element(XPATHS['b_nav_courses'])
# b_nav_courses.click()

# l_composition = find_element(XPATHS['l_composition'])
# l_composition.click()

# l_composition_grades = find_element(XPATHS['l_composition_grades'])
# l_composition_grades.click()

# html_composition_grades = driver.page_source

# driver.close()

# if __name__ == '__main__':
#     do something


# # Calculus BS


# l_calculus = find_element(XPATHS['l_calculus'])
# l_calculus.click()


# l_access_pearson = find_element(XPATHS['l_access_pearson'])
# l_access_pearson.click()

# time.sleep(6)
# # b_open_pearson = driver.find_element(By.CLASS_NAME, "gravity-btn-cta opener-cta")
# # b_open_pearson.click()
# b_open_pearson = find_element(XPATHS['b_open_pearson'])
# # action.move_to_element(s_open_pearson)
# # time.sleep(4)
# b_open_pearson.click()

# s_open_pearson2 = find_element(XPATHS['s_open_pearson'])
# time.sleep(4)
# s_open_pearson2.click()

# action.send_keys(Keys.ENTER)
# action.send_keys(Keys.ENTER)
# time.sleep(4)


# if check_element_exists(XPATHS['b_accept_cookies']): b_accept_cookies = driver.find_element(By.XPATH, XPATHS['b_accept_cookies'])
# b_accept_cookies.click()

# if check_element_exists(XPATHS['l_calculus_all_assignments_math']): l_calculus_all_assignments_math = driver.find_element(By.XPATH, XPATHS['l_calculus_all_assignments_math'])
# l_calculus_all_assignments_math.click()
