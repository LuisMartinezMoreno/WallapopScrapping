# WallapopScrapping
This is a tool that scrapes the wallapop selling portal.
It opens wallapop and looks for your desired products periodically, checks if the price has changed, and notifies you via Telegram.
It is meant to be working on a raspberry Pi.

## How to install the program
To get the program fully working, you have to clone it to your raspberry, install the libraries and configure it as follows

### Libraries
You have to install the following python libraries (pip install nameLibrary)
- telegram_send
- tkinter
- selenium

### Configure telegram
You have to create a Telegram bot, follow this tutorial it takes less than 5 minutes! https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580

## Prepare it to work
Now that you have everything set up, you have to configure it to run automatically and with the products you want

### Crontab
- This is a feature in Raspbian, it is a file where every code you write will be executed following some schedule rules.
Here you can check a really helpful tutorial https://www.codementor.io/@gergelykovcs/how-to-run-and-schedule-python-scripts-on-raspberry-pi-n2clhe3kp

- Here is an example of my crontab file:
0 */8 * * * /usr/bin/python /home/pi/Desktop/WallapopScrapping-1/wallapopScraping.py >> /home/pi/mycronlog.txt 
It runs this project every 8 hours

### Code changes
- The last step is to set the products you want to look for in Wallapop, you have to change the itemsToLookFor.JSON file, edit the JSON taking into account that the distance is in meters.
The JSON files in the results folder, are some examples of what you will get after executing it on your machine.

## Example
Everything is left as it was after the execution, the JSON files can be modified to your preferences and the code is commented for everyone who wants to modify it. :)
