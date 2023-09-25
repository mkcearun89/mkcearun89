redo log files are storing the changes happened in the database and the log files are useful when there is a
failure happening in DB.

redo log files are combined in groups. LGWR writes the redo log files and writes the redo log groups in a cyclic fashion.

when the last group of redo log group filled completely LGWR writes from the begining of redo log group 1.

DB configuration happened in two modes 
1. Archive mode 
2. Non Archive mode

non archive mode:
Once the last group redo log write happens the checkpoint event occurs and the LGWR writes the first log in group.

Archive mode.
Once the last redo log group fills the archiving will happen and the LGWR will start writing from the begining.
Archiving can be done automaticall or manually


