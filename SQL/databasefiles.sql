# data file

data files contains the actual data.

datafiles also contains indexes , snapshots , data dictionary of data before the modification
A database can have one or more data files
a database should have atleast one data file
One datafile is dedicated to only on database
size of the datafile can be extended automatically when the volume of the data increases
======================================================================

control file

control file is a binary file that contain the information abotut the database which is required to maintain the integrity of
  the database and is used to start and operate the database.
control file is able to modify by the oracle server only
-represents the current state of the database
-contains the start time of the database
-control file is associated with only one database

contains name and ID of hte database
Name and location of the redo log files and datafiles
redo log archive file information
redo log history 
backup information 
tablespace information
checkpoint information
