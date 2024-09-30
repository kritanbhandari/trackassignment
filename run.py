from assignment_tracker import (
    Driver,
    get_index_immediate_two_assignments,
    get_username_password,
    sign_in,
    click_prompts,
    get_lists,
    get_grade_page_source,
    get_table_assignment_names,
)

# from async_func import sign_in, click_prompts, get_grade_page_source
from xpaths import XPATHS
from database import TableDatabase
import sqlite3
from database import TableDatabase
import threading
import concurrent.futures

# import datetime

# Drivers for each page
LINK_CANVAS = "https://fisk.instructure.com/"
driver1 = Driver(LINK_CANVAS, XPATHS)
driver2 = Driver(LINK_CANVAS, XPATHS)
driver3 = Driver(LINK_CANVAS, XPATHS)
driver4 = Driver(LINK_CANVAS, XPATHS)

# # Database connections and cursors
connection = sqlite3.connect("table_data.db")
cursor = connection.cursor()
table_assignments = TableDatabase(connection, "Assignments", cursor)
table_assignments.create_table()


# # year = 2024
def create_run_threads_get_page_source(targets, quantity, args):
    result_list = []
    r = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(0, quantity):
            a, b = args[i]
            c = targets[i]
            r.append(executor.submit(c, a, b))
    for f in concurrent.futures.as_completed(r):
        result_list.append(f.result())
    return result_list


def create_run_threads(targets, quantity, args):
    threads_list = []
    for i in range(0, quantity):
        if args:
            t = threading.Thread(target=targets[i], args=args[i])
        else:
            t = threading.Thread(target=targets[i])
        t.start()
        threads_list.append(t)
    for i in threads_list:
        i.join()


quantity = 4
username, password = get_username_password()


start_targets = [driver1.start, driver2.start, driver3.start, driver4.start]
start_args = []

sign_in_targets = [sign_in for _ in range(0, quantity)]
sign_in_args = [
    (driver1, username, password),
    (driver2, username, password),
    (driver3, username, password),
    (driver4, username, password),
]

click_prompts_targets = [click_prompts for _ in range(0, quantity)]
click_prompts_args = [(driver1,), (driver2,), (driver3,), (driver4,)]

get_grade_page_source_targets = [get_grade_page_source for _ in range(0, quantity)]
get_grade_page_source_args = [
    (driver1, "composition"),
    (driver2, "creative_arts"),
    (driver3, "elementary_french"),
    (driver4, "NSO"),
]

create_run_threads(start_targets, quantity, start_args)
create_run_threads(sign_in_targets, quantity, sign_in_args)
create_run_threads(click_prompts_targets, quantity, click_prompts_args)


page_sources = create_run_threads_get_page_source(
    get_grade_page_source_targets, quantity, get_grade_page_source_args
)
current_assignments_names = get_table_assignment_names(table_assignments)


def insert_assignment_into_tables(
    table_assignments,
    indices,
    current_assignments_names,
    assignment_subject_name,
    assignment_names,
    assignment_due_dates,
    assignment_submitted_dates,
    assignment_scores,
    assignment_links,
):
    for i in indices:
        if not assignment_names[i] in current_assignments_names:
            table_assignments.insert_assignment(
                assignment_subject_name,
                assignment_names[i],
                assignment_due_dates[i],
                assignment_submitted_dates[i],
                assignment_scores[i],
                assignment_links[i],
            )
            current_assignments_names.append(assignment_names[i])


for page_source in page_sources:
    (
        assignment_subject_name,
        assignment_names,
        assignment_links,
        assignment_due_dates,
        assignment_submitted_dates,
        assignment_scores,
    ) = get_lists(page_source)
    indices = get_index_immediate_two_assignments(
        assignment_scores, assignment_submitted_dates, assignment_due_dates
    )
    insert_assignment_into_tables(
        table_assignments,
        indices,
        current_assignments_names,
        assignment_subject_name,
        assignment_names,
        assignment_due_dates,
        assignment_submitted_dates,
        assignment_scores,
        assignment_links,
    )
for i in table_assignments.query_rows():
    print(i)


start_targets = [driver1.end, driver2.end, driver3.end, driver4.end]
start_args = []
create_run_threads(start_targets, quantity, start_args)

# (
#     composition_assignment_names,
#     composition_assignment_links,
#     composition_assignment_due_dates,
#     composition_assignment_submitted_dates,
#     composition_assignment_scores,
# ) = get_lists(composition_page_source)

# (
#     creative_arts_assignment_names,
#     creative_arts_assignment_links,
#     creative_arts_assignment_due_dates,
#     creative_arts_assignment_submitted_dates,
#     creative_arts_assignment_scores,
# ) = get_lists(creative_arts_page_source)

# (
#     elementary_french_assignment_names,
#     elementary_french_assignment_links,
#     elementary_french_assignment_due_dates,
#     elementary_french_assignment_submitted_dates,
#     elementary_french_assignment_scores,
# ) = get_lists(elementary_french_page_source)

# (
#     NSO_assignment_names,
#     NSO_assignment_links,
#     NSO_assignment_due_dates,
#     NSO_assignment_submitted_dates,
#     NSO_assignment_scores,
# ) = get_lists(NSO_page_source)

# print(
#     composition_assignment_names,
#     composition_assignment_links,
#     composition_assignment_due_dates,
#     composition_assignment_submitted_dates,
#     composition_assignment_scores,
# )
# print("\n")
# print(
#     creative_arts_assignment_names,
#     creative_arts_assignment_links,
#     creative_arts_assignment_due_dates,
#     creative_arts_assignment_submitted_dates,
#     creative_arts_assignment_scores,
# )
# print("\n")

# print(
#     elementary_french_assignment_names,
#     elementary_french_assignment_links,
#     elementary_french_assignment_due_dates,
#     elementary_french_assignment_submitted_dates,
#     elementary_french_assignment_scores,
# )
# print("\n")

# print(
#     NSO_assignment_names,
#     NSO_assignment_links,
#     NSO_assignment_due_dates,
#     NSO_assignment_submitted_dates,
#     NSO_assignment_scores,
# )

# indices = get_index_immediate_two_assignments(scores, submitted_dates, due_dates)

# table_assignments = TableDatabase(connection, "Assignments", cursor=cursor)
# table_assignments.create_table()


# for i in indices:
#     if not assignment_names[i] in current_assignments_names:
#         table_assignments.insert_assignment(
#             "Creative Arts",
#             assignment_names[i],
#             due_dates[i],
#             submitted_dates[i],
#             scores[i],
#             links[i],
#         )
#         current_assignments_names.append(assignment_names[i])
# print(table_assignments.query_rows())


# for i in table_assignments.query_rows():
#     print(i)


# print("\n")
# if index:
#     print(index)
#     print(due_dates[index])
#     print(assignment_names[index])

# for due_date, assignment_name, submitted_date, link, score in zip(due_dates, assignment_names, submitted_dates, links, scores):
#         due_date = convert_date(year, due_date)
#         submitted_date = convert_date(year, submitted_date)
#         try:
#             table_assignments.insert_assignment("Creative Arts", assignment_name, due_date, submitted_date, score, link)
#         except IntegrityError:


# with open("index.html", 'w') as file:
#     for due_date, assignment_name, submitted_date, link, score in zip(due_dates, assignment_names, submitted_dates, links, scores):
#         file.write(f"{str(assignment_name)}\t{str(link)}\t{str(due_date)}\t{str(submitted_date)}\t{str(score)}\t")
#         file.write('\n')
# driver.end()
# new_table.insert_assignment("Composition", "Ethos", date, date, "10", "https://youtube.com" )
