import unittest
from assignment_tracker import (
    get_index_next_assignment,
    get_index_immediate_assignment,
    get_index_immediate_two_assignments,
    add_duplicates,
)
import datetime


class ParsingAssignments(unittest.TestCase):

    def test_get_index_immediate_assignment(self):
        grades = [
            "10",
            "30",
            "50",
            "28",
            "93.1",
            "50 (A)",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "84%",
        ]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            datetime.datetime(2024, 8, 9, 9, 55),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        assert get_index_immediate_assignment(grades, submitted_dates) == 6

        grades = []
        submitted_dates = []
        assert get_index_immediate_assignment(grades, submitted_dates) == None

        grades = ["10", "30", "50", "28", "93.1", "50 (A)"]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
        ]

        assert get_index_immediate_assignment(grades, submitted_dates) == None

        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            datetime.datetime(2024, 8, 9, 9, 55),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        grades = ["10", "30", "50", "28", "93.1", "-", "50 (A)"]
        assert get_index_immediate_assignment(grades, submitted_dates) == 5

        grades = ["10", "-"]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
        ]
        assert get_index_immediate_assignment(grades, submitted_dates) == None

        grades = ["10", "30", "-"]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 19, 2),
            "",
        ]
        assert get_index_immediate_assignment(grades, submitted_dates) == 2

    def test_add_duplicates(self):
        due_dates = [
            datetime.datetime(2024, 8, 19, 23, 59),
            datetime.datetime(2024, 8, 19, 23, 59),
            datetime.datetime(2024, 8, 20, 23, 59),
            datetime.datetime(2024, 8, 20, 23, 59),
            datetime.datetime(2024, 9, 9, 11, 15),
            datetime.datetime(2024, 9, 18, 23, 59),
            datetime.datetime(2024, 9, 20, 11, 0),
            datetime.datetime(2024, 9, 20, 23, 59),
            datetime.datetime(2024, 9, 20, 23, 59),
            datetime.datetime(2024, 10, 6, 23, 59),
            datetime.datetime(2024, 10, 19, 23, 59),
            datetime.datetime(2024, 10, 27, 23, 59),
            datetime.datetime(2024, 11, 10, 23, 59),
            datetime.datetime(2024, 11, 24, 23, 59),
            datetime.datetime(2024, 11, 24, 23, 59),
            datetime.datetime(2024, 12, 4, 23, 59),
            datetime.datetime(2024, 12, 4, 23, 59),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        indices = []
        index = 0
        add_duplicates(index, due_dates, indices)
        assert indices == [0, 1]

        index = 2
        indices = []
        add_duplicates(index, due_dates, indices)
        assert indices == [2, 3]

        index = 3
        indices = []
        add_duplicates(index, due_dates, indices)
        assert indices == [3]

        index = 6
        indices = []
        add_duplicates(index, due_dates, indices)
        assert indices == [6, 7, 8]

        index = 15
        indices = []
        add_duplicates(index, due_dates, indices)
        assert indices == [15, 16]

        index = 16
        indices = []
        add_duplicates(index, due_dates, indices)
        assert indices == [16]

        indices = []
        index = 17
        add_duplicates(index, due_dates, indices)
        assert indices == [17]

        indices = []
        index = 19
        add_duplicates(index, due_dates, indices)
        assert indices == [19]

    def test_get_index_next_assignment(self):
        grades = [
            "10",
            "30",
            "50",
            "28",
            "93.1",
            "50 (A)",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "84%",
        ]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            datetime.datetime(2024, 8, 9, 9, 55),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        due_dates = [
            datetime.datetime(2024, 8, 19, 23, 59),
            datetime.datetime(2024, 8, 19, 23, 59),
            datetime.datetime(2024, 8, 20, 23, 59),
            datetime.datetime(2024, 8, 20, 23, 59),
            datetime.datetime(2024, 9, 9, 11, 15),
            datetime.datetime(2024, 9, 18, 23, 59),
            datetime.datetime(2024, 9, 20, 11, 0),
            datetime.datetime(2024, 9, 20, 23, 59),
            datetime.datetime(2024, 9, 20, 23, 59),
            datetime.datetime(2024, 10, 6, 23, 59),
            datetime.datetime(2024, 10, 19, 23, 59),
            datetime.datetime(2024, 10, 27, 23, 59),
            datetime.datetime(2024, 11, 10, 23, 59),
            datetime.datetime(2024, 11, 24, 23, 59),
            datetime.datetime(2024, 11, 24, 23, 59),
            datetime.datetime(2024, 12, 4, 23, 59),
            datetime.datetime(2024, 12, 4, 23, 59),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        assert get_index_next_assignment(0, due_dates, submitted_dates, grades) == 2
        assert get_index_next_assignment(2, due_dates, submitted_dates, grades) == 4
        assert get_index_next_assignment(4, due_dates, submitted_dates, grades) == 5
        assert get_index_next_assignment(16, due_dates, submitted_dates, grades) == 17
        assert get_index_next_assignment(17, due_dates, submitted_dates, grades) == 18

    def test_get_index_immediate_two_assignments(self):
        due_dates = [
            datetime.datetime(2024, 8, 19, 23, 59),
            datetime.datetime(2024, 8, 19, 23, 59),
            datetime.datetime(2024, 8, 20, 23, 59),
            datetime.datetime(2024, 8, 20, 23, 59),
            datetime.datetime(2024, 9, 9, 11, 15),
            datetime.datetime(2024, 9, 18, 23, 59),
            datetime.datetime(2024, 9, 20, 11, 0),
            datetime.datetime(2024, 9, 20, 23, 59),
            datetime.datetime(2024, 9, 20, 23, 59),
            datetime.datetime(2024, 10, 6, 23, 59),
            datetime.datetime(2024, 10, 19, 23, 59),
            datetime.datetime(2024, 10, 27, 23, 59),
            datetime.datetime(2024, 11, 10, 23, 59),
            datetime.datetime(2024, 11, 24, 23, 59),
            datetime.datetime(2024, 11, 24, 23, 59),
            datetime.datetime(2024, 12, 4, 23, 59),
            datetime.datetime(2024, 12, 4, 23, 59),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        grades = [
            "10",
            "30",
            "50",
            "28",
            "93.1",
            "50 (A)",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "84%",
        ]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            datetime.datetime(2024, 8, 9, 9, 55),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        assert get_index_immediate_two_assignments(
            grades, submitted_dates, due_dates
        ) == [
            6,
            7,
            8,
            9,
        ]
        grades = ["10", "30", "50", "28", "93.1", "50 (A)"]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
            "",
        ]
        assert (
            get_index_immediate_two_assignments(grades, submitted_dates, due_dates)
            == []
        )

        grades = ["10", "30", "50", "28", "93.1", "50 (A)", "-", "-"]
        submitted_dates = [
            datetime.datetime(2024, 8, 19, 19, 2),
            datetime.datetime(2024, 8, 19, 21, 50),
            datetime.datetime(2024, 8, 20, 13, 2),
            datetime.datetime(2024, 8, 28, 12, 30),
            datetime.datetime(2024, 9, 9, 10, 29),
            "",
            "",
            "",
        ]
        due_dates = []
        assert get_index_immediate_two_assignments(
            grades, submitted_dates, due_dates
        ) == [6]


# a = []
# b = []

# # a = ['10', '30', '50', '28', '93.1', '50 (A)', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '84%']
# a = ["10", "30", "50", "28", "93.1", "50 (A)", "-", "-"]
# b = [
#     datetime.datetime(2024, 8, 19, 19, 2),
#     datetime.datetime(2024, 8, 19, 21, 50),
#     datetime.datetime(2024, 8, 20, 13, 2),
#     datetime.datetime(2024, 8, 28, 12, 30),
#     datetime.datetime(2024, 9, 9, 10, 29),
#     "",
#     "",
# ]
# # c = []
# c = [
#     datetime.datetime(2024, 8, 19, 23, 59),
#     datetime.datetime(2024, 8, 19, 23, 59),
#     datetime.datetime(2024, 8, 20, 23, 59),
#     datetime.datetime(2024, 8, 26, 23, 59),
#     datetime.datetime(2024, 9, 9, 11, 15),
#     datetime.datetime(2024, 9, 18, 23, 59),
#     datetime.datetime(2024, 9, 22, 23, 59),
#     "",
#     "",
# ]
# # b = [datetime.datetime(2024, 8, 19, 19, 2), datetime.datetime(2024, 8, 19, 21, 50), datetime.datetime(2024, 8, 20, 13, 2), datetime.datetime(2024, 8, 28, 12, 30), datetime.datetime(2024, 9, 9, 10, 29), '', '', '', '', '', '', '', '', '', '', '', '', datetime.datetime(2024, 8, 9, 9, 55), '', '', '', '', '', '', '']
# c = [
#     datetime.datetime(2024, 8, 19, 23, 59),
#     datetime.datetime(2024, 8, 19, 23, 59),
#     datetime.datetime(2024, 8, 20, 23, 59),
#     datetime.datetime(2024, 8, 26, 23, 59),
#     datetime.datetime(2024, 9, 9, 11, 15),
#     datetime.datetime(2024, 9, 18, 23, 59),
#     datetime.datetime(2024, 9, 20, 11, 0),
#     datetime.datetime(2024, 9, 23, 23, 59),
#     datetime.datetime(2024, 9, 30, 23, 59),
#     datetime.datetime(2024, 10, 6, 23, 59),
#     datetime.datetime(2024, 10, 19, 23, 59),
#     datetime.datetime(2024, 10, 27, 23, 59),
#     datetime.datetime(2024, 11, 10, 23, 59),
#     datetime.datetime(2024, 11, 24, 23, 59),
#     datetime.datetime(2024, 11, 24, 23, 59),
#     datetime.datetime(2024, 12, 4, 23, 59),
#     datetime.datetime(2024, 12, 4, 23, 59),
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
# ]
# d = [
#     "Syllabus Agreement Form",
#     "Play Bill",
#     "Getting to Know You",
#     "Vocabulary Game",
#     "Vocabulary - Test I",
#     "Stagecrafters Auditions",
#     "Monologues",
#     "AS YOU LIKE IT,  by William Shakespeare",
#     "Scene Shop, Costume / Prop Morgue Organization",
#     "Dance",
#     "Aaron Douglas",
#     "Visual Arts Unit",
#     "Music Reflection",
#     "HOME, by Samm Art Williams",
#     "Stagecrafters Production Technical Work",
#     "Creative Project - Final Examination",
#     "Extra Credit Option",
#     "Roll Call Attendance",
# ]
# e = [
#     "https://fisk.instructure.com//courses/14858/assignments/103769",
#     "https://fisk.instructure.com//courses/14858/assignments/103764",
#     "https://fisk.instructure.com//courses/14858/assignments/105265/submissions/46665",
#     "https://fisk.instructure.com//courses/14858/assignments/103772",
#     "https://fisk.instructure.com//courses/14858/assignments/103754/submissions/46665",
#     "https://fisk.instructure.com//courses/14858/assignments/103767",
#     "https://fisk.instructure.com//courses/14858/assignments/103762",
#     "https://fisk.instructure.com//courses/14858/assignments/104910",
#     "https://fisk.instructure.com//courses/14858/assignments/103758",
#     "https://fisk.instructure.com//courses/14858/assignments/103760",
#     "https://fisk.instructure.com//courses/14858/assignments/103756",
#     "https://fisk.instructure.com//courses/14858/assignments/103771",
#     "https://fisk.instructure.com//courses/14858/assignments/103763",
#     "https://fisk.instructure.com//courses/14858/assignments/104909",
#     "https://fisk.instructure.com//courses/14858/assignments/103768",
#     "https://fisk.instructure.com//courses/14858/assignments/103759",
#     "https://fisk.instructure.com//courses/14858/assignments/103761",
#     "https://fisk.instructure.com//courses/14858/assignments/103765/submissions/46665",
# ]
# print(scores)

# date_format = '%Y-%m-%d %H:%M:%S'


# date_stra = '2023-03-15 14:30:00'
# date_strb = '2023-03-16 14:30:00'
# date_strc = '2023-03-17 14:30:01'
# date_strd = '2023-03-17 14:30:02'
# date_str = '2023-03-17 14:30:03'
# date_str1 = '2023-03-28 14:30:00'
# date_str2 = '2023-03-28 14:30:00'
# date_str3 = '2023-03-29 14:30:00'
# date_str4 = '2023-03-30 14:30:00'
# date_str5 = '2023-03-31 14:30:00'


# date_obja = datetime.strptime(date_stra, date_format)
# date_objb = datetime.strptime(date_strb, date_format)
# date_objc = datetime.strptime(date_strc, date_format)
# date_objd = datetime.strptime(date_strd, date_format)
# date_obj1 = datetime.strptime(date_str, date_format)
# date_obj2 = datetime.strptime(date_str1, date_format)
# date_obj3 = datetime.strptime(date_str2, date_format)
# date_obj4 = datetime.strptime(date_str3, date_format)
# date_obj5 = datetime.strptime(date_str4, date_format)
# date_obj6 = datetime.strptime(date_str5, date_format)

# due_dates = [date_obja,date_objb,date_objc,date_objd,date_obj1, date_obj2, date_obj3, date_obj4, date_obj5, date_obj6]

# print(due_dates)

# # index = get_index_immediate_assignment()
# indices = get_immediate_two_assignments(3, due_dates)
# # print(indices)
# for i in indices:
#     print(due_dates[i])

if __name__ == "__main__":
    unittest.main()
