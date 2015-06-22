#!/bin/bash
mongoimport --host 127.0.0.1:29017 -d school -c students < students.json
