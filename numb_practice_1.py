#!/usr/bin/env python3

#Let's assume you are planning to use your Python skills to build a social networking service.
#You decide to host your application on servers running in the cloud. You pick a hosting provider
#that charges $0.51 per hour. You will launch your service using one server and want to know
#how much it will cost to operate per day and per month.

#Write a Python program that displays the answers to the following questions:

#How much does it cost to operate one server per day?
#How much does it cost to operate one server per month?


#hosting provider charges per hour
cost_per_hour = 0.51

#cost to operate one server per day
cost_per_day = 24 * cost_per_hour
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))

#cost to operate one server per month
cost_per_month = 30 * cost_per_day
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))