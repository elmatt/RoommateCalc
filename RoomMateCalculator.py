import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'email', 'pw' )

cost1 = float(raw_input("How much did roommate #1 (Justin) pay for (KUB), groceries, et cetera?\n"))
r12 = float(raw_input("Does roommate #1 (Justin) owe any $ to roommate #2 (Matt)? Enter 0 if none\n"))
r13 = float(raw_input( "Does roomate #1 (Justin) owe any $ to roommate #3 (Drew)? Enter 0 if none\n"))

cost2 = float(raw_input("How much did roommate #2 (Matt) pay for (Comcast), groceries, et cetera?\n"))
r21 = float(raw_input("Does roommate #2 (Matt) owe any $ to roommate #1 (Justin)? Enter 0 if none\n"))
r23 = float(raw_input("Does roomate #2 (Matt) owe any $ to roommate #3 (Drew)? Enter 0 if none\n"))

cost3 = float(raw_input("How much did roommate #3 (Drew) pay for (anything else), groceries, et cetera?\n"))
r31 = float(raw_input("Does roommate #3 (Drew) owe any $ to roommate #1 (Justin)? Enter 0 if none\n"))
r32 = float(raw_input("Does roomate #3 (Drew) owe any $ to roommate #2 (Matt)? Enter 0 if none\n"))

print("\n******BREAKDOWN********\n\n")

justins_rent = 333.0 - (2*cost1/3) + (cost2/3) + (cost3/3) + r12 + r13 - r21 -r31
matts_rent = 333 + (cost1/3) - (2*cost2/3) + (cost3/3) - r12 + r21 + r23 - r32
drews_rent = 333 + (cost1/3) + (cost2/3) - (2*cost3/3) -r13 - r23 + r31 + r32

print('Justin pays ${} '.format(justins_rent))
print('Matt pays ${} '.format(matts_rent))
print('Drew pays ${} '.format(drews_rent))

#Verzion = vtext.com -- other carriers such as tmobile are tmomail.net
server.sendmail( 'subj', 'yournumber@vtext.com', 'You pay ${} for rent this month'.format(justins_rent) )
server.sendmail( 'subj', 'yournumber@vtext.net', 'You pay ${} for rent this month'.format(matts_rent) )
server.sendmail( 'subj', 'yournumber@vtext.net', 'You pay ${} for rent this month'.format(drews_rent) )
