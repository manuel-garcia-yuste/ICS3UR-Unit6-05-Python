#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program takes your mark and calculates the average

import random


def average(marks):
    # This calculates average of the marks with a passed list

    total = 0
    items = 0

    # process
    for number in marks:
        total = total + number
        items = items + 1

    # Calculates average
    average = total / items

    # output
    return round(average)


def main():
    # This is a list to hold the 20 numbers
    marks = []
    final_average = 0
    mark = 0

    # This welcomes user
    print("It calculates the average of your marks")
    print("Write -1 when you finish")

    # process
    while mark != -1:
        # input
        mark = int(input("Mark: "))
        marks.append(mark)

    marks.pop()

    final_average = average(marks)
    print("The average is " + str(final_average))


if __name__ == "__main__":
    main()
