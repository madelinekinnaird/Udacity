Requirements

Python 3 - ver 3.6.4
Git 
VirtualBox - virtualiztion product
Vagrant - virtual environment builder


Follow the steps below to access the code of this project:

    1. Make sure python is up to date.
    2. Set up vagrant and virtual box.
    3. Download appropriate Udacity folder.
    4. Clone this repository.
    5. Download this database.
    6. Go to the Udacity folder in your bash interface and inside that cd into the vagrant folder.
    7. Open Git Bash and launch the virtual machine withvagrant up
    8. Once Vagrant installs necessary files use vagrant ssh to continue.
    9. The command line will now start with vagrant. Here cd into the /vagrant folder.
    10. Unpack the database folder contents downloaded above over here. You can also copy the contents of this repository here.
    11. Type psql -d news -f newsdata.sql
    12. Type psql -d news
    13. You must run the commands from the Create views section here to run the python program successfully.
    14. Use command python log_analysis.py to run the python program.

Create Views

Views help you address the third question =, while leaving the original database unchanged.

First code:
CREATE VIEW logstar AS
SELECT count(*) as stat, 
status, cast(time as date) as day
FROM log WHERE status like '%404%'
GROUP BY status, day
ORDER BY stat desc limit 3;

Second Code:

CREATE VIEW totalvisitors AS
SELECT count(*) as visitors,
cast(time as date) as errortime
FROM log
GROUP BY errortime;

Third Code:

CREATE VIEW errorcount AS
SELECT * from logstar join totalvisitors
ON logstar.day = totalvisitors.errortime;
