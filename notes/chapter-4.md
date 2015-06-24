#### Chapter 4

Pluggable Storage Engines

- Mongo now allows pluggable engines
- Is the interface between the persistent storage and the DB itself
- The storage engine is the one that directly sets the format of indexes and the data file format

###### Engines

- MMAP
- WiredTiger

###### MMAPv1

- Uses MMAP system call to allocate files and mem.
- Mongo needs a place to allocate docs
- Collection Level Locking
- Try to update in place within pagination limits if not possible we have to allocate into new location

[__100 GB VM__]

[__100 GB __] 


