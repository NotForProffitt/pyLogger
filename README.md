# pyLogger
keylogger written in Python for CMSC 414.

To Use:

Place the logger.py file anywhere on the target system and execute it. This will create two batch scripts in the same directory as the logger.py program and a VBS script placed in the startup folder. The VBS script automatically executes the two batch scripts every time a user logs into the machine. The logger will store timestamped keystrokes and read the clipboard every second.

openLogger.bat checks the integrity of the script files, creates a log directory and file under its own directory, and starts the keylogger.

server.bat starts an http server for LAN access of the log file. visit http://\<target ip\>:8000 to access the log file remotely.
  
The VBS script exists to stop the two batch scripts from opening command prompts that would betray the existence of the keylogger.
