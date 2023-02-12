# -*- coding: utf-8 -*-

import sys

from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import os.path
import threading
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import os
from urlextract import URLExtract
import time
import webbrowser


from ui_main import Ui_MainWindow

SCOPES = ['https://mail.google.com/']
json_file = "client.json"
user_id =  'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

load_cnt = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.show()

        self.load_count()

        self.ui.extraxt_link_btn.clicked.connect(self.gmail_client)
        self.ui.clk_links_btn.clicked.connect(self.link_thred)







    def gmail_client(self):

        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    json_file, SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())



        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)
            # request a list of all the messages
            unread_msgs = service.users().messages().list(userId='me', labelIds=[label_id_one, label_id_two]).execute()

            messages = unread_msgs["messages"]

            print("Total unread messages in inbox: ", str(len(messages)))
            final_list = []

            for mssg in messages:
                temp_dict = {}
                m_id = mssg['id']  # get id of individual message

                message = service.users().messages().get(userId=user_id,
                                                         id=m_id).execute()  # fetch the message using API

               # print(message)

                # msg_str = str(base64.urlsafe_b64decode(message["raw"].encode("ASCII")))
                # print(msg_str)
                payld = message['payload']  # get payload of the message
                headr = payld['headers']  # get header of the payload

                body = payld["body"]

                for three in headr:  # getting the Sender
                    if three['name'] == 'From':
                        msg_from = three['value']
                        temp_dict['Sender'] = msg_from
                    else:
                        pass



                if msg_from == "Volutic <support@cgemail.io>":
                    print(msg_from)
                    w_data = str(m_id) + "|" + str(body["data"]) + "\n"
                    print(w_data)

                    file = open("enc_data.txt", "a+")
                    file.write(w_data)
                    file.close()

                    service.users().messages().modify(userId=user_id, id=m_id,
                                                    body={'removeLabelIds': ['UNREAD']}).execute()

                    service.users().messages().delete(userId=user_id, id=m_id).execute()

            self.decode_data()
            self.split_links()




        except HttpError as error:

            print(f'An error occurred: {error}')


    def decode_data(self):

        with open("enc_data.txt", "r") as op_data:

            for i in op_data:

                #print(i.split("|")[1])

                dec_data = i.split("|")[1]

                clean_one = dec_data.replace("-", "+")  # decoding from Base64 to UTF-8
                clean_one = clean_one.replace("_", "/")  # decoding from Base64 to UTF-8

                clean_two = base64.b64decode(bytes(clean_one, 'UTF-8')).decode()
                indent = clean_two.replace("</p>", " ")
                print(indent)

                file = open("dec_data.txt", "a+")
                file.write(indent)
                file.close()

    def split_links(self):

        with open("dec_data.txt", "r") as op_dec_data:

            text = op_dec_data.read()

            extractor = URLExtract()
            urls = extractor.find_urls(text)
            print(urls)

            for i in urls:

                if i != "https://volutic.com/user/settings.aspx":

                    file = open("link_data.txt", "a+")
                    file.write(i + "\n")
                    file.close()
                    print(i)

    def iterate_links(self):
        global load_cnt

        url = "www.google.com"
        webbrowser.open(url)
        time.sleep(20)

        cnt = 0

        link_list = []

        with open("link_data.txt", "r") as link_data:

            for i in link_data:

                link_list.append(i)



        link_data.close()


        for render_link in range(load_cnt, len(link_list)):

            cnt += 1

            print("run")

            urlr = str(link_list[render_link])
            webbrowser.open(urlr)



            time.sleep(50)

            if cnt == 10:
                cnt = 0
                os.system('taskkill /im brave.exe /f')
                url = "www.google.com"
                webbrowser.open(url)
                time.sleep(20)

            file = open("count_data.txt", "w")
            file.write(str(render_link))
            file.close()







    def load_count(self):

        global load_cnt

        with open("count_data.txt", "r") as cnt:

            for i in cnt:

                load_cnt = int(i)
                print(load_cnt)

    def link_thred(self):

        thred1 = threading.Thread(target=self.iterate_links)
        thred1.start()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())