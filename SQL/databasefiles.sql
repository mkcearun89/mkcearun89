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
===============================================================================

redo log files
redo log files contains the data of the changes happened in the database which is used to recover the 
database during its failure
  - the redo log files can be organized into groups 
  - the data in the redo log?

redo log history 
backup information 
tablespace information
checkpoint information
=======================================================================================
LGWR backgroud process writes the redo log files group in a cyclic fashion

The LGWR writes the logs into redo log file groups , the first group will be written by the LGWR and move the next and move on
once the last group filled and move to the first.
  

