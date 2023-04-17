#!/usr/bin/env python3

#Let's assume you are planning to use your Python skills to build a social networking service.
#You decide to host your application on servers running in the cloud. You pick a hosting provider
#that charges $0.51 per hour. You will launch your service using one server and want to know
#how much it will cost to operate per day and per month.

#Write a Python program that displays the answers to the following questions:

#How much does it cost to operate one server per day?
#How much does it cost to operate one server per month?
#How much does it cost to operate twenty servers per day?
#How much does it cost to operate twenty servers per month?
#How many days can I operate one server with $918?


#hosting provider charges per hour
cost_per_hour = 0.51

#cost to operate one server per day
cost_per_day = 24 * cost_per_hour
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))

#cost to operate one server per month
cost_per_month = 30 * cost_per_day
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))

#cost to operate 20 servers per day
cost_twenty_servers_per_day = 20 * cost_per_day
print('cost to operate twenty servers per day is ${:.2f}.'.format(cost_twenty_servers_per_day))

#cost to operate 20 servers per month
cost_twenty_servers_per_month = 30 * cost_twenty_servers_per_day
print('cost to operate twenty servers per month is ${:.2f}.'.format(cost_twenty_servers_per_month))

#budgeting
budget = 918
operational_days = budget / cost_per_day
print('a server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))