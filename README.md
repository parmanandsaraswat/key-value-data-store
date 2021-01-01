# key-value-data-store
A file-based key-value data store that supports the basic CRUD (create, read, update and delete) operations.

This data store is meant to be used as a local storage for one single process on one laptop. The data store must be exposed as a library to clients that can instantiate a class and work with the data store. The data store will support the following functional requirements.

1. create() : Takes the key input and checks whether the key is present is in file. If the key is present, then the key-value is created and inserted.
2. read() : Takes the key input and checks whether the key is present is in file. If the key is present, then the corresponding value is returned.
3. delete() : Takes the key input and checks whether the key is present is in file. If the key is present, then the key-value is deleted from the file.
4. update() : Takes the key input and checks whether the key is present is in file. If the key is present, then the value is modified and updated accordingly.

# The data store will also support the following non-functional requirements.
1. The size of the file storing data must never exceed 1GB.
2. More than one client process cannot be allowed to use the same file as a data store at any given time.
3. A client process is allowed to access the data store using multiple threads, if it desires to. The data store must therefore be thread-safe.
4. The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store.
# Languages used:
Python
# libraries used:
1. Thread
2. json 
3. sys
4. os
5. time
6. pathlib-Path
