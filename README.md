## __Motivation__

My niece asked me to create a way to send a lot of messages in WhatsApp to her friend in her birthday. So I made this script using _Python 3_ and _Selenium_ to automate this process and send more messages possible would be a manual way.

## __Requirements__
* Python3
* Pip3
* Selenium
* Firefox
* Firefox Webdriver for Selenium

### __Download and instalation__
#### Selenium

```{bash}
pip3 install Selenium
```

#### Firefox
```{bash}
sudo apt-get install firefox
```

#### Firefox webdriver

* __Step 1__: Go to the [Geckodriver releases page](https://github.com/mozilla/geckodriver/releases). Find the latest version of the driver for your platform and download it. The version used was __v.0.26.0__:

```{bash}
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
```

* __Step 2__: Extract the file with:
```{bash}
tar -xvzf geckodriver*
```

* __Step 3__: Make it executable:
```{bash}
chmod +x geckodriver
```

* __Step 4__: Move the executable file for __usr/local/bin__:
```{bash}
sudo mv geckodriver /usr/local/bin/
```

## __Variables__

* enter_name_element: The element in HTML area where enter the contact or group name to select
* send_message_element: The element in HTML area where the Bot will typed the messages and send

Both can change over time, so if you accuse NoSuchElementException, go to Web Developer and find the class related to these variables.

* delay: The time between sending two messages

Take care with the time, if you set a small one, WhatsApp can block your account.

## __Messages__

There is a archive named _messages.py_, put all the messages you want to send in the list named _msgList_.

The bot will send messages at random.

## __Running__

* __Step 1__: Run _main.py_:

```{bash}
python3 main.py
```

* __Step 2__: Print in console, how many messages do you want to send  and the name of the contact or the group

* __Step 3__: Log in in Web WhatsApp with the QR Code. Everytime you run, you have to log in again.

* __Step 4__: Press Enter in terminal.