# Microsoft-Teams-Auto-Joiner

### This is a modified version of an existing repo.
### Original Repo by [Tobias Pankner](https://GitHub.com/TobiasPankner) : [Link](https://GitHub.com/TobiasPankner/Teams-Auto-Joiner)

### What's New In This Repo?
- In this version, you can schedule which meeting to join, when to join and when to exit.


### Documentation
- [Prerequisites](#prerequisites)
- [Configuration options](#configuration-options)
- [Run the script](#run-the-script)  


Python script to automatically join Microsoft Teams meetings.  

Automatically turns off your microphone and camera before joining.

Specify your team name and time. That's it!


## Prerequisites  
  
 - Python3 ([Download](https://www.python.org/downloads/))  
   
## Configuration options  
  
Open the config.json file and add your configurations.

- **email/password:**  
The email/password of your Microsoft account (can be left empty if you don't want to automatically login)

- **auto_leave_after_min:**  
If set to a value greater than zero, the bot leaves the meeting after the specified time (in minutes).

- **teamname:**<br/>
Set the team name of the meeting you want to join here. Case Sensitive Alert!

- **meetingtime:**<br/>
Set the time at which you want to join the meeting. 24 hours clock. Example: "17:30".


## Run the script  
 1. Before starting, teams might be in Grid view, if this is the case change the view to list. 
 2. Edit the "config.json" file to specify your configurations.
 3. Install dependencies:   ```pip install -r requirements.txt``` 
 4. Run [auto_joiner.py](auto_joiner.py): `python auto_joiner.py`
 <img src="https://i.imgur.com/GODoJYf.png?2" width="300" height="245" />
 
 ## Additional Note
 The script will not join a meeting with no participants. So make sure to have some of your friends in the meeting while testing it out.
