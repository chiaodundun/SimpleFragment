#! /usr/bin/python3

'''
Expected behaviour:
    import mesApi
    try:
        mesApi.SendMessage("Your message ( DEFAULT: bhai result agya hai) ",[number ( in int form, and with list) ])
    except Exception as e:
        print(e)


'''

from isconnected import check_connection
import json
import os
import requests



class SendMessage:
    '''
    Sends the message to a phone
    '''
    def __init__(self,message='Bhai result agya hai' ,numbers=None ):
        '''
        
        :param message  The messge to be sent
        :param numbers  List of numbers the message to be sent
        '''
        self.message = message
        self.numbers = []
        if numbers is None:
            raise ValueError("No number given")
        self.numbers = ','.join(map(str,numbers))
        self.send_message()


    def send_message(self):
        url = 'https://www.fast2sms.com/dev/bulk'
        auth_key = os.environ.get('Fast2SmsAuthKey',0)
        if auth_key==0:
            raise RuntimeError("Authorization key invalid")
        queryString = {
                    'authorization':auth_key,
                    'sender_id': "FSTSMS",
                    'message':self.message,
                    'language':'english',
                    'route':'p',
                    'numbers':self.numbers
                    }
        headers = {
                    'cache-control':'no-cache'
                   }

        check_connection()  #will throw an error if problem with net connectivity
        response = requests.get(url,params=queryString,headers=headers)
        res = json.loads(response.text)
        if res['return']=='false':   # message not sent successfully
             raise Exception("{}".format(res['message']))



if __name__=='__main__':
    SendMessage(numbers=[9459372335])

