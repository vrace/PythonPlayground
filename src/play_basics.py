#!/usr/bin/env python3
import re
import sys
import os
import glob
from datetime import date, datetime, timedelta


def play_replace():
    message = "the quick brown fox jumps over the lazy dog"

    s = message.replace(' ', '-')
    print(message)
    print(s)

    ss = message.split()
    for word in ss:
        print(word)

    dirty = "%@# Hola! Amigo! #@$"
    clean = dirty.strip("@#$% ")
    print(dirty)
    print(clean)


def play_regular_expression():
    original = "The quick brown fox jumps over the lazy dog"
    str_list = original.split()
    pattern = re.compile("(?P<match_word>The)", re.I)
    count = 0
    for word in str_list:
        match = pattern.search(word)
        if match:
            print(match.group("match_word"))
            count += 1
    print(f"Found {count} matches")
    print(pattern.sub("a", original).capitalize())


def play_date_time():
    today = date.today()
    print(today)
    print(today.year)
    print(today.month)
    print(today.day)
    print(f"Today's datetime: {datetime.today()}")
    one_day = timedelta(days=1)
    yesterday = today - one_day
    print(f"Yesterday is {yesterday}")
    print(f"Tomorrow is {today + one_day}")
    eight_hours = timedelta(hours=8)
    print(f"Eight hours, days = {eight_hours.days}, seconds = {eight_hours.seconds}")
    date_diff = today - yesterday
    print(date_diff)
    print(f"format today: {today.strftime('%m/%d/%Y')}")
    print(f"format today: {today.strftime('%b %d, %Y')}")
    print(f"format today: {today.strftime('%Y-%m-%d')}")
    print(f"format today: {today.strftime('%B %d, %Y')}")
    date_created = datetime.strptime("2012-12-21", "%Y-%m-%d")
    print(date_created.strftime("%b %d, %Y"))


def play_list():
    data_list = [3, 7, 2, 1]
    print(f"The list is {data_list}, and it has {len(data_list)} elements.")
    print(f"The max value in the list is {max(data_list)}, and the min value is {min(data_list)}.")
    print(f"The last value in the list is {data_list[-1]}.")
    digit_list = list(str(0x3f3f3f3f))
    print(f"Another list is {digit_list}, and it has {len(digit_list)} elements.")
    print(f"'6' appears {digit_list.count('6')} times in the list.")
    print(f"First 3 elements in the list is {digit_list[:3]}.")
    print(f"And the 3 elements after the first 3 elements is {digit_list[3:6]}.")
    print(f"And the last 3 elements in the list is {digit_list[-3:]}")
    data_list.append(4)
    print(f"After appending an element in the list...{data_list}")
    data_list.append(data_list[-1])
    print(f"After repeating the last element...{data_list}")
    data_list.append(data_list[-1] * data_list[-2])
    print(f"After appending an element that is multiply last two elements...{data_list}")
    data_list.remove(4)
    print(f"After removing 4...{data_list}...okay we still have a 4. It just removes the first match.")
    data_list.pop()
    print(f"Pop something...{data_list}.")
    data_list.reverse()
    print(f"Let's reverse it...{data_list}")
    data_list.sort()
    print(f"And then sort it...{data_list}")
    sorted_list = sorted(digit_list)
    print(f"The sorted list...{sorted_list}")


def play_tuple():
    tuple_data = (3, 7, 21)
    print(f"The tuple is {tuple_data}, and it has {len(tuple_data)} elements.")
    print(f"First element: {tuple_data[0]}, Second: {tuple_data[1]}, and Last one: {tuple_data[2]}.")
    print(f"A longer tuple: {tuple_data + tuple_data}")
    a, b, ab = tuple_data
    print(f"{a} * {b} = {ab}")
    a, b = b, a
    print(f"{a} * {b} = {ab}")


def play_dictionary():
    dict_data = {"one": 1, "two": 2, "three": 3}
    print(f"The dictionary is {dict_data}, and it has {len(dict_data)} elements.")
    print(f"Two is {dict_data['two']}.")
    dup = dict_data.copy()
    dup["four"] = 4
    print(f"Original dict: {dict_data}.")
    print(f"And the copy after some changes: {dup}.")
    print(f"The copy has keys: {dup.keys()}.")
    print(f"And values: {dup.values()}.")
    print(f"And items: {dup.items()}.")
    sorted_dict = sorted(dup)
    print(f"Whaaat we can sort a dict?!...{sorted_dict}")


def play_for_loop():
    data = [1, 2, 3, 4, 5]
    print(f"The original data is {data}")
    doubled_data = [it * 2 for it in data]
    print(f"Doubled data is {doubled_data}")
    selected_data = [it for it in data if it % 2 == 0]
    print(f"Even elements in the list {selected_data}")


def play_exception():
    try:
        print("I'm trying to divide by zero!")
        print(f"The output is {10/0}")
    except ZeroDivisionError as e:
        print(f"As I expected we got some exception - {e}")
    else:
        print("-- should not go here --")
    finally:
        print("Finally...")


def play_sys():
    print(f"The script name is {sys.argv[0]}")


def read_file_contents(file_name):
    try:
        with open(file_name, "r") as file_reader:
            return [row.strip() for row in file_reader]
    except Exception as e:
        print(f"Error reading file, error: {e}")
        return []


def read_file_to_one_liner(file_name):
    return ' '.join(read_file_contents(file_name))


def play_file():
    contents = read_file_contents("../res/sample.txt")
    print(f"The rows...{contents}")
    print(f"Joined row...{' '.join(contents)}")
    content_lines = [read_file_to_one_liner(file_name) for file_name in glob.glob(os.path.join("../res", "*.txt"))]
    print(f"Here's the collected content lines...{content_lines}")


if __name__ == "__main__":
    play_replace()
    play_regular_expression()
    play_date_time()
    play_list()
    play_tuple()
    play_dictionary()
    play_for_loop()
    play_exception()
    play_sys()
    play_file()
