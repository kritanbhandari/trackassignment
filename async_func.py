from reading_grades import ParseTableDataCanvas


async def sign_in(driver, username, password):
    # Sign-in page
    i_username = await driver.find_element(driver.xpath["i_username"])
    i_password = driver.find_element(driver.xpath["i_password"])
    b_submit = driver.find_element(driver.xpath["b_submit"])

    i_username.send_keys(username)
    i_password.send_keys(password)
    b_submit.click()


async def click_prompts(driver):
    # Clicking prompts
    b_hello_prompt = await driver.find_element(driver.xpath["b_hello_prompt"])
    b_hello_prompt.click()

    b_student_tour = await driver.find_element(driver.xpath["b_student_tour"])
    b_student_tour.click()


async def get_grade_page_source(driver, course_name):
    b_nav_courses = await driver.find_element(driver.xpath["b_nav_courses"])
    b_nav_courses.click()

    l_composition = await driver.find_element(driver.xpath[f"l_{course_name}"])
    l_composition.click()

    l_composition_grades = await driver.find_element(
        driver.xpath[f"l_{course_name}_grades"]
    )
    l_composition_grades.click()
    return driver.driver.page_source


# async def main():
#     await asyncio.gather(
#         driver1.start(), driver2.start(), driver3.start(), driver4.start()
#     )

#     username, password = get_username_password()
#     await asyncio.gather(
#         sign_in(driver1, username, password),
#         sign_in(driver2, username, password),
#         sign_in(driver3, username, password),
#         sign_in(driver4, username, password),
#     )

#     await asyncio.gather(
#         click_prompts(driver1),
#         click_prompts(driver2),
#         click_prompts(driver3),
#         click_prompts(driver4),
#     )
#     composition_page_source = get_grade_page_source(driver1, "composition")
#     creative_arts_page_source = get_grade_page_source(driver2, "creative_arts")
#     elementary_french_page_source = get_grade_page_source(driver3, "elementary_french")
#     NSO_page_source = get_grade_page_source(driver4, "NSO")

#     (
#         composition_assignment_names,
#         composition_assignment_links,
#         composition_assignment_due_dates,
#         composition_assignment_submitted_dates,
#         composition_assignment_scores,
#     ) = get_lists(composition_page_source)

#     (
#         creative_arts_assignment_names,
#         creative_arts_assignment_links,
#         creative_arts_assignment_due_dates,
#         creative_arts_assignment_submitted_dates,
#         creative_arts_assignment_scores,
#     ) = get_lists(creative_arts_page_source)

#     (
#         elementary_french_assignment_names,
#         elementary_french_assignment_links,
#         elementary_french_assignment_due_dates,
#         elementary_french_assignment_submitted_dates,
#         elementary_french_assignment_scores,
#     ) = get_lists(elementary_french_page_source)

#     (
#         NSO_assignment_names,
#         NSO_assignment_links,
#         NSO_assignment_due_dates,
#         NSO_assignment_submitted_dates,
#         NSO_assignment_scores,
#     ) = get_lists(NSO_page_source)

#     print(
#         composition_assignment_names,
#         composition_assignment_links,
#         composition_assignment_due_dates,
#         composition_assignment_submitted_dates,
#         composition_assignment_scores,
#     )
#     print("\n")
#     print(
#         creative_arts_assignment_names,
#         creative_arts_assignment_links,
#         creative_arts_assignment_due_dates,
#         creative_arts_assignment_submitted_dates,
#         creative_arts_assignment_scores,
#     )
#     print("\n")

#     print(
#         elementary_french_assignment_names,
#         elementary_french_assignment_links,
#         elementary_french_assignment_due_dates,
#         elementary_french_assignment_submitted_dates,
#         elementary_french_assignment_scores,
#     )
#     print("\n")

#     print(
#         NSO_assignment_names,
#         NSO_assignment_links,
#         NSO_assignment_due_dates,
#         NSO_assignment_submitted_dates,
#         NSO_assignment_scores,
#     )

# t1 = threading.Thread(target=driver1.start)
# t2 = threading.Thread(target=driver2.start)
# t3 = threading.Thread(target=driver3.start)
# t4 = threading.Thread(target=driver4.start)

# t1.start()
# t2.start()
# t3.start()
# t4.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()

# s1 = threading.Thread(target=sign_in, args=(driver1, username, password))
# s2 = threading.Thread(target=sign_in, args=(driver2, username, password))
# s3 = threading.Thread(target=sign_in, args=(driver3, username, password))
# s4 = threading.Thread(target=sign_in, args=(driver4, username, password))

# s1.start()
# s2.start()
# s3.start()
# s4.start()

# s1.join()
# s2.join()
# s3.join()
# s4.join()


# c1 = threading.Thread(target=click_prompts, args=(driver1,))
# c2 = threading.Thread(target=click_prompts, args=(driver2,))
# c3 = threading.Thread(target=click_prompts, args=(driver3,))
# c4 = threading.Thread(target=click_prompts, args=(driver4,))

# c1.start()
# c2.start()
# c3.start()
# c4.start()

# c1.join()
# c2.join()
# c3.join()
# c4.join()

# p1 = threading.Thread(target=get_grade_page_source(driver1, "composition"))
# p2 = threading.Thread(target=get_grade_page_source(driver2, "creative_arts"))
# p3 = threading.Thread(target=get_grade_page_source(driver3, "elementary_french"))
# p4 = threading.Thread(target=get_grade_page_source(driver4, "NSO"))

# p1.start()
# p2.start()
# p3.start()
# p4.start()

# p1.join()
# p2.join()
# p3.join()
# p4.join()

# driver4.start()
# driver2.start()
# driver3.start()
# driver4.start()

# username, password = get_username_password()
# sign_in(driver1, username, password)
# sign_in(driver2, username, password)
# sign_in(driver3, username, password)
# sign_in(driver4, username, password)

# click_prompts(driver1)
# click_prompts(driver2)
# click_prompts(driver3)
# click_prompts(driver4)

# composition_page_source = get_grade_page_source(driver1, "composition")
# creative_arts_page_source = get_grade_page_source(driver2, "creative_arts")
# elementary_french_page_source = get_grade_page_source(driver3, "elementary_french")
# NSO_page_source = get_grade_page_source(driver4, "NSO")
