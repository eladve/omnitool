# omnitool
a tool that automatically takes screenshots in the background, OCRs them, and stores them. It then allows to search inside those screenshots.

See here for vision and ideas for future development: https://twitter.com/verbine/status/1256598690770411521

the file omnitool_capture.py is the file that should run in the background, captures the data and builds the database
the file omnitool_search.py is the file that searches the database

Remarks for each file can be found inside the file. Some ideas for improvements can be found in the "Issues".

NOTES:
- This is a very rough prototype. It's badly-written and not productized. But it does show how to build a tool like this.
- Hard-drive usage: the tool accumulates data at around 1K per second, so around 1.5GB per month.
- The spirit and insight of this tool is that since we as users interact with the screen, then the screen should have all information that we need, if we just process it well enough. So API integrations and such are a fools' errand, and if you jt have strong enough visual processing and NLP, you can create an omnitool that does not need to explicitly integrate with any other tool. It's a bit inspired by Robotic Process Automation (e.g. UIPath) and by Memex (https://getmemex.com/)  
- Privacy: the tool takes a screenshot each 10 seconds, and those screenshots are stored on the hardrive and never deleted. So this is obviously a significant privacy risk. If someone has access to your computer, they can see everything you've done and everything that was displayed on your screen since you started running this program. (That data stays on your computer and doesn't go anywhere -- the program does not communicate with the internet.) Use at your own risk.
- If you work on improving this tool, it's important to remember that the inverted index can always be re-built from the main database. So the only changes that would break the database's backwards compatibility are changes to the database collection (which are going to be rare). So feel free to go wild with changing the invertex index -- it can always be rebuilt.


THIS TOOL IS A PROTOTYPE AND NOT READY FOR PROPER USE. IT IS PROVIDED WITH NO GUARANTEE AND NO RESPONSIBILITY. 
