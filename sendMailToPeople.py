from __future__ import print_function
from twilio.rest import TwilioRestClient
import smtplib
import sched, time
import random
import datetime

def send_email(username):
    carriers = ["@mms.att.net", "@myboostmobile.com", "@messaging.sprintpcs.com", "@tmomail.net", "@mms.uscc.net", "@vtext.com", "@vmobl.com"]
    with open('addresses.txt') as f:
        plain = f.readlines()
    nums = []
    for p in plain:
        nums.append(p.rstrip('\n'))

    for num in nums:
        print("Sent a text to %s at %s" % (num, datetime.datetime.now()))
        for carrier in carriers:
            server.sendmail(username, num + carrier, msg)


if __name__ == '__main__':
    with open('credentials.txt') as f:
        content = f.readlines()

    username = content[0].rstrip('\n')
    password = content[1].rstrip('\n')

    times = 0

    while 1:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)

        msg = "You need to send a pic of your fall 2016 gpa to Cole Stanley. He explained how to in his Slack announcement two weeks ago."

        send_email(username)

        minute_delay = .5

        times += 1
        print("Number of texts sent: %s\n" % times)

        server.quit()
        time.sleep(60 * minute_delay)
