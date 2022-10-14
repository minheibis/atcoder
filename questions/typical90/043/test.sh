#!/bin/bash
for test_file in `find test_[0-9][0-9].txt`
do
    echo $test_file
    ANS_FILE=`echo $test_file | sed -e 's/.txt/_ans.txt/g'`
    python myans_09.py < $test_file > $ANS_FILE
done