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

###### Indexes

Indexes will have a B-Tree or B+Tree structure depending on the engine.

If an index is not present within the collection the query will have to visit each document to perfomr the query.

The index must take into account multikey values.

Multikey and DotNotation


