# To-Do Bot: Chat Bot to manage to-do list on Telegram  

**About:** This project aims to develop a chatbot to easly create to-do list making it easy to remove done tasks;

### Setting up a virtualenv
```
sudo apt-get install python3-pip python3-dev python-virtualenv # for Python 3.n
sudo apt-get install sqlite3
virtualenv ToDoBot -p python3 
source ToDoBot/bin/activate
easy_install -U pip
pip install requests, sqlite3
```

## To run the chatbot:  
Firs you should create a bot on Telegram using "The Father Bot". There you can choose a name and get a key to manage it.
This key must be sabe in a file called "API.py", where you shuold set:
```
API = API_CODE_HERE # Enter your API code
```

Then, running ToDoBot.py, it will load the API code, set the sqlite3 database (called 'todo.sqlite'), if necessary.
```
pyton3 ToDoBot.py
```
Then, with `/start` you can start the chatbot.
To create a todo list, just write and sent a message with the tasks you need;
After inserting an item, the bot will return the complete list;
[CreatingList](images/creating_list.png)

Then, when you have a taks done, you can use `/done` to select which taks should be removed from the list.
[done image](images/done.png)
