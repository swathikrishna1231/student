def notify(sender,message):
    return sender.send(message)
class Emailsender:
    def send(self,message):
        return f"{message}Emailsender:send via through EMAIL"
class SMSsender:
    def send(self,message): 
        return f"{message}SMSsender:send via through SMS SENDER"
email=Emailsender()
sms=SMSsender()
notify(email,"hai swathi")

    
    