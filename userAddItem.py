from __future__ import print_function # Python 2/3 compatibility
import boto3
import time
from boto3.dynamodb.conditions import Attr

while True:
    def sendMessage(username,message,receiver):
        table.put_item(
            Item={
                'User ID': username,
                'Timestamp': str(time.time()),
                'Receiver': receiver,
                'Message': message
            }
        )

    def checkForMessage(username):
        response = table.scan(
            FilterExpression=Attr('Receiver').eq(username)
        )
        for i in response['Items']:
            if str(i['Message']) != '':
                print(i['Message'])

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1',aws_access_key_id='AKIAJHWD7G4YB2S4MHIQ',aws_secret_access_key='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')

    table = dynamodb.Table('Messages')

    startTime = time.time()
    username = input("Username: ")
    choice = input("Type 1 to send a message and 2 to view messages sent to you:    ")

    if choice == '1':
        message = input("Message:   ")
        receiver = input("Receiver: ")
        sendMessage(username, message, receiver)

    if choice == '2':
        checkForMessage(username)