#Driver code for bard mail 


import Bard_mail

result=Bard_mail.mail_check()

if result%2==0:
    Bard_mail.auto_read()
    Bard_mail.draft_maker()
    print('Successfull mail')
    
elif result%2!=0:
	print('Mail box is empty')
else:
	pass
