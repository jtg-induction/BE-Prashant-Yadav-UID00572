from django.conf import settings
from django.db import connection
from django.test import TestCase

from todos import utils as todos_utils

class TestSetupMixin(object):

    def setUp(self):
        settings.DEBUG = True  # For using connection.queries.


class ORMUtilTest(TestSetupMixin, TestCase):
    fixtures = ['fixtures/01_data_dump.json', ]

    def test_fetch_all_users(self):
        expected_data = [
            {
                "id": 1,
                "first_name": "Amal",
                "last_name": "Raj",
                "email": "amal.raj@joshtechnologygroup.com"
            }, {
                "id": 2,
                "first_name": "Gurpreet",
                "last_name": "Singh",
                "email": "gurpreet.singh@joshtechnologygroup.com"
            }, {
                "id": 3,
                "first_name": "Naveen",
                "last_name": "Kumar",
                "email": "naveenk@joshtechnologygroup.com"
            }, {
                "id": 4,
                "first_name": "Nikhil",
                "last_name": "Khurana",
                "email": "nikhil.khurana@joshtechnologygroup.com"
            }, {
                "id": 6,
                "first_name": "Sunny",
                "last_name": "Singhal",
                "email": "sunny.singhal@joshtechnologygroup.com"
            }, {
                "id": 7,
                "first_name": "Chirag",
                "last_name": "Gupta",
                "email": "chirag.gupta@joshtechnologygroup.com"
            }
        ]
        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_all_users()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            list1=data or [],
            list2=expected_data,
        )

    def test_fetch_all_todo_list_with_user_details(self):
        expected_data = [
            {
                "id": 2,
                "name": "TODO - 2",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 3,
                "name": "TODO - 3",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 4,
                "name": "TODO - 4",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 5,
                "name": "TODO - 5",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 6,
                "name": "TODO - 6",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 7,
                "name": "TODO - 7",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 8,
                "name": "TODO - 8",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 9,
                "name": "TODO - 9",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 10,
                "name": "TODO - 10",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 11,
                "name": "TODO - 11",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 12,
                "name": "TODO - 12",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 13,
                "name": "TODO - 13",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 14,
                "name": "TODO - 14",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 15,
                "name": "TODO - 15",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 16,
                "name": "TODO - 16",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 17,
                "name": "TODO - 17",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 18,
                "name": "TODO - 18",
                "status": "Done",
                "created_at": "05:30 AM, 26 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 19,
                "name": "TODO - 19",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }, {
                "id": 20,
                "name": "TODO - 20",
                "status": "To Do",
                "created_at": "05:30 AM, 03 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 21,
                "name": "TODO - 21",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 22,
                "name": "TODO - 22",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 23,
                "name": "TODO - 23",
                "status": "To Do",
                "created_at": "05:30 AM, 03 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 24,
                "name": "TODO - 24",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 25,
                "name": "TODO - 25",
                "status": "Done",
                "created_at": "05:30 AM, 26 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 26,
                "name": "TODO - 26",
                "status": "To Do",
                "created_at": "05:30 AM, 03 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 27,
                "name": "TODO - 27",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 28,
                "name": "TODO - 28",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 29,
                "name": "TODO - 29",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 30,
                "name": "TODO - 30",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 31,
                "name": "TODO - 31",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 32,
                "name": "TODO - 32",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 33,
                "name": "TODO - 33",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 34,
                "name": "TODO - 34",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 35,
                "name": "TODO - 35",
                "status": "Done",
                "created_at": "05:30 AM, 26 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 36,
                "name": "TODO - 36",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 37,
                "name": "TODO - 37",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 38,
                "name": "TODO - 38",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 39,
                "name": "TODO - 39",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 40,
                "name": "TODO - 40",
                "status": "To Do",
                "created_at": "05:30 AM, 03 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 41,
                "name": "TODO - 41",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 42,
                "name": "TODO - 42",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 43,
                "name": "TODO - 43",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Gurpreet",
                    "last_name": "Singh",
                    "email": "gurpreet.singh@joshtechnologygroup.com"
                }
            }, {
                "id": 44,
                "name": "TODO - 44",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 45,
                "name": "TODO - 45",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 46,
                "name": "TODO - 46",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 47,
                "name": "TODO - 47",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 48,
                "name": "TODO - 48",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 49,
                "name": "TODO - 49",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 50,
                "name": "TODO - 50",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 51,
                "name": "TODO - 51",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 52,
                "name": "TODO - 52",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 53,
                "name": "TODO - 53",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 54,
                "name": "TODO - 54",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 55,
                "name": "TODO - 55",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 56,
                "name": "TODO - 56",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 57,
                "name": "TODO - 57",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 58,
                "name": "TODO - 58",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 59,
                "name": "TODO - 59",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 60,
                "name": "TODO - 60",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 61,
                "name": "TODO - 61",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Naveen",
                    "last_name": "Kumar",
                    "email": "naveenk@joshtechnologygroup.com"
                }
            }, {
                "id": 62,
                "name": "TODO - 62",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 63,
                "name": "TODO - 63",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 64,
                "name": "TODO - 64",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 65,
                "name": "TODO - 65",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 66,
                "name": "TODO - 66",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 67,
                "name": "TODO - 67",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 68,
                "name": "TODO - 68",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 69,
                "name": "TODO - 69",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 70,
                "name": "TODO - 70",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 71,
                "name": "TODO - 71",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Nikhil",
                    "last_name": "Khurana",
                    "email": "nikhil.khurana@joshtechnologygroup.com"
                }
            }, {
                "id": 72,
                "name": "TODO - 72",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 73,
                "name": "TODO - 73",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 74,
                "name": "TODO - 74",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 75,
                "name": "TODO - 75",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 76,
                "name": "TODO - 76",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 77,
                "name": "TODO - 77",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 78,
                "name": "TODO - 78",
                "status": "Done",
                "created_at": "05:30 AM, 26 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 79,
                "name": "TODO - 79",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 80,
                "name": "TODO - 80",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 81,
                "name": "TODO - 81",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 82,
                "name": "TODO - 82",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 83,
                "name": "TODO - 83",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 84,
                "name": "TODO - 84",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 85,
                "name": "TODO - 85",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 86,
                "name": "TODO - 86",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 87,
                "name": "TODO - 87",
                "status": "Done",
                "created_at": "05:30 AM, 26 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 88,
                "name": "TODO - 88",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 89,
                "name": "TODO - 89",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 90,
                "name": "TODO - 90",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 91,
                "name": "TODO - 91",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 92,
                "name": "TODO - 92",
                "status": "Done",
                "created_at": "05:30 AM, 26 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 93,
                "name": "TODO - 93",
                "status": "To Do",
                "created_at": "05:30 AM, 03 Jan, 2022",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 94,
                "name": "TODO - 94",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 95,
                "name": "TODO - 95",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 96,
                "name": "TODO - 96",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 97,
                "name": "TODO - 97",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 98,
                "name": "TODO - 98",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 99,
                "name": "TODO - 99",
                "status": "To Do",
                "created_at": "05:30 AM, 28 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 100,
                "name": "TODO - 100",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 101,
                "name": "TODO - 101",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Sunny",
                    "last_name": "Singhal",
                    "email": "sunny.singhal@joshtechnologygroup.com"
                }
            }, {
                "id": 102,
                "name": "TODO - 102",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 103,
                "name": "TODO - 103",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 104,
                "name": "TODO - 104",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 105,
                "name": "TODO - 105",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 106,
                "name": "TODO - 106",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 107,
                "name": "TODO - 107",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 108,
                "name": "TODO - 108",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 109,
                "name": "TODO - 109",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 110,
                "name": "TODO - 110",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 111,
                "name": "TODO - 111",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 112,
                "name": "TODO - 112",
                "status": "To Do",
                "created_at": "05:30 AM, 30 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 113,
                "name": "TODO - 113",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 114,
                "name": "TODO - 114",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 115,
                "name": "TODO - 115",
                "status": "To Do",
                "created_at": "05:30 AM, 27 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 116,
                "name": "TODO - 116",
                "status": "Done",
                "created_at": "05:30 AM, 29 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 117,
                "name": "TODO - 117",
                "status": "To Do",
                "created_at": "05:30 AM, 31 Dec, 2021",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 118,
                "name": "TODO - 118",
                "status": "Done",
                "created_at": "05:30 AM, 01 Jan, 2022",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 119,
                "name": "TODO - 119",
                "status": "To Do",
                "created_at": "05:30 AM, 02 Jan, 2022",
                "creator": {
                    "first_name": "Chirag",
                    "last_name": "Gupta",
                    "email": "chirag.gupta@joshtechnologygroup.com"
                }
            }, {
                "id": 1,
                "name": "TODO - 1",
                "status": "To Do",
                "created_at": "05:30 AM, 25 Dec, 2021",
                "creator": {
                    "first_name": "Amal",
                    "last_name": "Raj",
                    "email": "amal.raj@joshtechnologygroup.com"
                }
            }
        ]
        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_all_todo_list_with_user_details()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertCountEqual(
            data,
            expected_data
        )

    def test_fetch_projects_details(self):
        expected_data = [
            {'id': 5, 'name': 'Project E', 'status': 'In progress', 'existing_member_count': 1, 'max_members': 1},
            {'id': 4, 'name': 'Project D', 'status': 'In progress', 'existing_member_count': 1, 'max_members': 4},
            {'id': 10, 'name': 'Project J', 'status': 'Completed', 'existing_member_count': 3, 'max_members': 3},
            {'id': 6, 'name': 'Project F', 'status': 'To be started', 'existing_member_count': 4, 'max_members': 5},
            {'id': 2, 'name': 'Project B', 'status': 'Completed', 'existing_member_count': 2, 'max_members': 2},
            {'id': 7, 'name': 'Project G', 'status': 'In progress', 'existing_member_count': 2, 'max_members': 2},
            {'id': 1, 'name': 'Project A', 'status': 'To be started', 'existing_member_count': 2, 'max_members': 3},
            {'id': 8, 'name': 'Project H', 'status': 'To be started', 'existing_member_count': 1, 'max_members': 1},
            {'id': 11, 'name': 'Project K', 'status': 'To be started', 'existing_member_count': 4, 'max_members': 4},
            {'id': 9, 'name': 'Project I', 'status': 'Completed', 'existing_member_count': 2, 'max_members': 2},
            {'id': 3, 'name': 'Project C', 'status': 'In progress', 'existing_member_count': 3, 'max_members': 3}
        ]
        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_projects_details()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertCountEqual(
            data,
            expected_data
        )

    def test_fetch_users_todo_stats(self):
        expected_data = [
            {'id': 4, 'first_name': 'Nikhil', 'last_name': 'Khurana', 'email': 'nikhil.khurana@joshtechnologygroup.com',
             'completed_count': 3, 'pending_count': 7},
            {'id': 6, 'first_name': 'Sunny', 'last_name': 'Singhal', 'email': 'sunny.singhal@joshtechnologygroup.com',
             'completed_count': 8, 'pending_count': 22},
            {'id': 2, 'first_name': 'Gurpreet', 'last_name': 'Singh', 'email': 'gurpreet.singh@joshtechnologygroup.com',
             'completed_count': 9, 'pending_count': 15},
            {'id': 7, 'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
             'completed_count': 8, 'pending_count': 10},
            {'id': 3, 'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
             'completed_count': 5, 'pending_count': 13},
            {'id': 1, 'first_name': 'Amal', 'last_name': 'Raj', 'email': 'amal.raj@joshtechnologygroup.com',
             'completed_count': 3, 'pending_count': 16}
        ]

        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_users_todo_stats()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertCountEqual(
            data,
            expected_data
        )

    def test_fetch_five_users_with_max_pending_todos(self):
        expected_data = [
            {'id': 6, 'first_name': 'Sunny', 'last_name': 'Singhal', 'email': 'sunny.singhal@joshtechnologygroup.com',
             'pending_count': 22},
            {'id': 1, 'first_name': 'Amal', 'last_name': 'Raj', 'email': 'amal.raj@joshtechnologygroup.com',
             'pending_count': 16},
            {'id': 2, 'first_name': 'Gurpreet', 'last_name': 'Singh', 'email': 'gurpreet.singh@joshtechnologygroup.com',
             'pending_count': 15},
            {'id': 3, 'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
             'pending_count': 13},
            {'id': 7, 'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
             'pending_count': 10}
        ]

        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_five_users_with_max_pending_todos()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            data,
            expected_data
        )

    def test_fetch_users_with_n_pending_todos(self):
        expected_data = [
            {'id': 7, 'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
             'pending_count': 10}
        ]

        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_users_with_n_pending_todos(n=10)
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            data,
            expected_data
        )

    def test_fetch_completed_todos_with_in_date_range(self):
        expected_data = [
            {
                'id': 18, 'name': 'TODO - 18', 'creator': 'Amal Raj', 'email': 'amal.raj@joshtechnologygroup.com',
                'created_at': '05:30 AM, 26 Dec, 2021', 'status': 'Done'
            },
            {
                'id': 25, 'name': 'TODO - 25', 'creator': 'Gurpreet Singh',
                'email': 'gurpreet.singh@joshtechnologygroup.com', 'created_at': '05:30 AM, 26 Dec, 2021',
                'status': 'Done'
            },
            {
                'id': 35, 'name': 'TODO - 35', 'creator': 'Gurpreet Singh',
                'email': 'gurpreet.singh@joshtechnologygroup.com',
                'created_at': '05:30 AM, 26 Dec, 2021', 'status': 'Done'
            },
            {
                'id': 78, 'name': 'TODO - 78', 'creator': 'Sunny Singhal',
                'email': 'sunny.singhal@joshtechnologygroup.com', 'created_at': '05:30 AM, 26 Dec, 2021',
                'status': 'Done'
            },
            {
                'id': 87, 'name': 'TODO - 87', 'creator': 'Sunny Singhal',
                'email': 'sunny.singhal@joshtechnologygroup.com',
                'created_at': '05:30 AM, 26 Dec, 2021', 'status': 'Done'
            },
            {
                'id': 92, 'name': 'TODO - 92', 'creator': 'Sunny Singhal',
                'email': 'sunny.singhal@joshtechnologygroup.com', 'created_at': '05:30 AM, 26 Dec, 2021',
                'status': 'Done'
            }
        ]
        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_completed_todos_with_in_date_range('21-12-2021', '29-12-2021')
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            data,
            expected_data
        )

    def test_fetch_project_with_member_name_start_or_end_with_a(self):
        expected_data = [
            {'project_name': 'Project G', 'done': False, 'max_members': 2},
            {'project_name': 'Project J', 'done': True, 'max_members': 3},
            {'project_name': 'Project K', 'done': False, 'max_members': 4},
            {'project_name': 'Project B', 'done': True, 'max_members': 2},
            {'project_name': 'Project I', 'done': True, 'max_members': 2},
            {'project_name': 'Project E', 'done': False, 'max_members': 1},
            {'project_name': 'Project C', 'done': False, 'max_members': 3},
            {'project_name': 'Project F', 'done': False, 'max_members': 5}
        ]

        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_project_with_member_name_start_or_end_with_a()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            data,
            expected_data
        )

    def test_fetch_project_wise_report(self):
        expected_data = [
            {'project_title': 'Project A', 'report': [
                {'first_name': 'Gurpreet', 'last_name': 'Singh', 'email': 'gurpreet.singh@joshtechnologygroup.com',
                 'pending_count': 15, 'completed_count': 9},
                {'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
                 'pending_count': 13, 'completed_count': 5}]}, {'project_title': 'Project B', 'report': [
                {'first_name': 'Amal', 'last_name': 'Raj', 'email': 'amal.raj@joshtechnologygroup.com',
                 'pending_count': 16, 'completed_count': 3},
                {'first_name': 'Nikhil', 'last_name': 'Khurana', 'email': 'nikhil.khurana@joshtechnologygroup.com',
                 'pending_count': 7, 'completed_count': 3}]}, {'project_title': 'Project C', 'report': [
                {'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
                 'pending_count': 10, 'completed_count': 8},
                {'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
                 'pending_count': 13, 'completed_count': 5},
                {'first_name': 'Sunny', 'last_name': 'Singhal', 'email': 'sunny.singhal@joshtechnologygroup.com',
                 'pending_count': 22, 'completed_count': 8}]}, {'project_title': 'Project D', 'report': [
                {'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
                 'pending_count': 13, 'completed_count': 5}]}, {'project_title': 'Project E', 'report': [
                {'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
                 'pending_count': 10, 'completed_count': 8}]}, {'project_title': 'Project F', 'report': [
                {'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
                 'pending_count': 10, 'completed_count': 8},
                {'first_name': 'Gurpreet', 'last_name': 'Singh', 'email': 'gurpreet.singh@joshtechnologygroup.com',
                 'pending_count': 15, 'completed_count': 9},
                {'first_name': 'Nikhil', 'last_name': 'Khurana', 'email': 'nikhil.khurana@joshtechnologygroup.com',
                 'pending_count': 7, 'completed_count': 3},
                {'first_name': 'Sunny', 'last_name': 'Singhal', 'email': 'sunny.singhal@joshtechnologygroup.com',
                 'pending_count': 22, 'completed_count': 8}]}, {'project_title': 'Project G', 'report': [
                {'first_name': 'Amal', 'last_name': 'Raj', 'email': 'amal.raj@joshtechnologygroup.com',
                 'pending_count': 16, 'completed_count': 3},
                {'first_name': 'Nikhil', 'last_name': 'Khurana', 'email': 'nikhil.khurana@joshtechnologygroup.com',
                 'pending_count': 7, 'completed_count': 3}]}, {'project_title': 'Project H', 'report': [
                {'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
                 'pending_count': 13, 'completed_count': 5}]}, {'project_title': 'Project I', 'report': [
                {'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
                 'pending_count': 10, 'completed_count': 8},
                {'first_name': 'Sunny', 'last_name': 'Singhal', 'email': 'sunny.singhal@joshtechnologygroup.com',
                 'pending_count': 22, 'completed_count': 8}]}, {'project_title': 'Project J', 'report': [
                {'first_name': 'Gurpreet', 'last_name': 'Singh', 'email': 'gurpreet.singh@joshtechnologygroup.com',
                 'pending_count': 15, 'completed_count': 9},
                {'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
                 'pending_count': 13, 'completed_count': 5},
                {'first_name': 'Nikhil', 'last_name': 'Khurana', 'email': 'nikhil.khurana@joshtechnologygroup.com',
                 'pending_count': 7, 'completed_count': 3}]}, {'project_title': 'Project K', 'report': [
                {'first_name': 'Amal', 'last_name': 'Raj', 'email': 'amal.raj@joshtechnologygroup.com',
                 'pending_count': 16, 'completed_count': 3},
                {'first_name': 'Chirag', 'last_name': 'Gupta', 'email': 'chirag.gupta@joshtechnologygroup.com',
                 'pending_count': 10, 'completed_count': 8},
                {'first_name': 'Naveen', 'last_name': 'Kumar', 'email': 'naveenk@joshtechnologygroup.com',
                 'pending_count': 13, 'completed_count': 5},
                {'first_name': 'Nikhil', 'last_name': 'Khurana', 'email': 'nikhil.khurana@joshtechnologygroup.com',
                 'pending_count': 7, 'completed_count': 3}]}
        ]

        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_project_wise_report()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            2,
            msg='Expected only 2 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            data,
            expected_data
        )

    def test_fetch_user_wise_project_status(self):
        expected_data = [
            {
                'first_name': 'Nikhil',
                'last_name': 'Khurana',
                'email': 'nikhil.khurana@joshtechnologygroup.com',
                'to_do_projects': ['Project F', 'Project K'],
                'in_progress_projects': ['Project G'],
                'completed_projects': ['Project B', 'Project J']
            }, {
                'first_name': 'Sunny',
                'last_name': 'Singhal',
                'email': 'sunny.singhal@joshtechnologygroup.com',
                'to_do_projects': ['Project F'],
                'in_progress_projects': ['Project C'],
                'completed_projects': ['Project I']
            }, {
                'first_name': 'Gurpreet',
                'last_name': 'Singh',
                'email': 'gurpreet.singh@joshtechnologygroup.com',
                'to_do_projects': ['Project A', 'Project F'],
                'in_progress_projects': [],
                'completed_projects': ['Project J']
            }, {
                'first_name': 'Chirag',
                'last_name': 'Gupta',
                'email': 'chirag.gupta@joshtechnologygroup.com',
                'to_do_projects': ['Project F', 'Project K'],
                'in_progress_projects': ['Project C', 'Project E'],
                'completed_projects': ['Project I']
            }, {
                'first_name': 'Naveen',
                'last_name': 'Kumar',
                'email': 'naveenk@joshtechnologygroup.com',
                'to_do_projects': ['Project A', 'Project H', 'Project K'],
                'in_progress_projects': ['Project C', 'Project D'],
                'completed_projects': ['Project J']
            }, {
                'first_name': 'Amal',
                'last_name': 'Raj',
                'email': 'amal.raj@joshtechnologygroup.com',
                'to_do_projects': ['Project K'],
                'in_progress_projects': ['Project G'],
                'completed_projects': ['Project B']
            }
        ]

        db_hit_count = len(connection.queries)
        data = todos_utils.fetch_user_wise_project_status()
        new_db_hit_count = len(connection.queries)
        actual_hit_count = new_db_hit_count - db_hit_count
        self.assertEqual(
            actual_hit_count,
            1,
            msg='Expected only 1 db hit got {}'.format(new_db_hit_count - db_hit_count)
        )
        self.assertListEqual(
            data,
            expected_data
        )



