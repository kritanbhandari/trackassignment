from bs4 import BeautifulSoup
from page import web_page
import re
from date_conversion import convert_date


class ParseTableDataCanvas:
    def __init__(self, page_source, table_id):
        # self.page_source = page_source
        self.table_id = table_id
        self.due_date_css_class = "due"
        self.submitted_date_css_class = "submitted"
        self.score_class = "assignment_score"
        self.link_prefix = "https://fisk.instructure.com/"
        self.href_match = "assignments"
        self.year = 2024
        self.subject_id = "course_select_menu"
        self.page_parsed = BeautifulSoup(page_source, "html.parser")

    def get_table(self):
        """Takes a table id and returns its tag"""
        table_tag = self.page_parsed.find(id=self.table_id)
        return table_tag

    def find_assignment_names(self, table_tag):
        table_links = table_tag.find_all(href=re.compile(self.href_match))
        return [i.text for i in table_links]

    def find_assignment_link(self, table_tag):
        """Takes a table_tag (of the table) and keyword in the link of the table element and returns a list of the elements that match"""
        table_links = table_tag.find_all(href=re.compile(self.href_match))
        return [self.link_prefix + i["href"] for i in table_links]

    def find_assignment_due_date(self, table_tag):
        """Returns all the due dates of the assignments"""
        table_due_dates = table_tag.find_all("td", self.due_date_css_class)
        list_of_due_dates = []
        for due_date in table_due_dates:
            due_date_stripped = due_date.get_text().strip().replace("by", "")
            if due_date_stripped:
                due_date_stripped = convert_date(self.year, due_date_stripped)
            list_of_due_dates.append(due_date_stripped)
        return list_of_due_dates

    def find_assignment_submitted_date(self, table_tag):
        """Returns all the submitted dates of the assignments"""
        table_due_dates = table_tag.find_all("td", self.submitted_date_css_class)
        list_of_submitted_dates = []
        for due_date in table_due_dates:
            due_date_stripped = due_date.get_text().strip().replace("at", "")
            if due_date_stripped:
                due_date_stripped = convert_date(self.year, due_date_stripped)
            list_of_submitted_dates.append(due_date_stripped)
        return list_of_submitted_dates

    def find_assignment_score(self, table_tag):
        """Returns all the scores of the assignments in a list. Returns '-' for non-graded assignments"""
        scores = table_tag.find_all("td", self.score_class)
        list_of_scores = []
        for score_data in scores:
            score_data_text = score_data.get_text(",", strip=True).split(",")
            if score_data_text[1] != "none":
                list_of_scores.append(score_data_text[2])
        return list_of_scores

    def find_assignment_name(self):
        subject_tag = self.page_parsed.find_all("span", class_="ellipsible")
        return subject_tag[1].text.strip()


if __name__ == "__main__":
    new_page = ParseTableDataCanvas(page_source=web_page, table_id="grades_summary")
    # table_tag = new_page.get_table()
    input_tag = new_page.find_assignment_name()
    print(input_tag)
    # for i in input_tag:
    #     print(i)
    # print(new_page.find_assignment_link(table_tag=table_tag))
    # print(table_tag)
    # print(new_page.find_subject_name())
    # with open('index.html', 'w') as f:
    #     # f.write(str(new_page.find_assignment_score(table_tag=table_tag)))
    #     for i in new_page.find_assignment_due_date(table_tag=table_tag):
    #         f.write(str(i))
    #         f.write("\n")
