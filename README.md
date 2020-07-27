## Microsoft-Teams-Auto-Joiner (Work In Progress)

# This is a modified version of an existing repo.
# Original Repo by [Tobias Panker](https://GitHub.com/TobiasPankner) : [link](https://GitHub.com/TobiasPankner/Teams-Auto-Joiner)

# What's New In This Repo?
- 


- [Prerequisites](#prerequisites)
- [Configuration options](#configuration-options)
- [Run the script](#run-the-script)  

Python script to automatically join Microsoft Teams meetings.  
Automatically turns off your microphone and camera before joining.
Specify your team name and time. That's it!


## Prerequisites  
  
 - Python3 ([Download](https://www.python.org/downloads/))  
   
## Configuration options  
  
- **email/password:**  
The email/password of your Microsoft account (can be left empty if you don't want to automatically login)

- **auto_leave_after_min:**  
If set to a value greater than zero, the bot leaves every meeting after the specified time (in minutes). Useful if you know the length of your meeting, if this is left a the default the bot will stay in the meeting until a new one is available.

- To be completed ...


## Run the script  
  
 2. Edit the "config.json" file specify your configurations
 3. Install dependencies:   ```pip install -r requirements.txt``` 
 4. Run [auto_joiner.py](auto_joiner.py): `python auto_joiner.py`  
 5. After starting, teams might be in Grid view, if this is the case change the view to list    
<img src="https://i.imgur.com/GODoJYf.png?2" width="300" height="245" />
