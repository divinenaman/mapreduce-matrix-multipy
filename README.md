## MapReduce and Hadoop streaming API
- Matrix Multilication program on the hadoop architecture using Python

## Input format
- semi-colon(;) separated rows
- space(' ') separated columns
- next-line (\n) end of martix
- example : ```	1 2 3;5 6 7 \n
		2 3 3;0 9 0;4 5 6
	     ```

## Output format
- key: row number,column number
- value: value of element at key
	
## Run (hadoop-3.2.2)

``` 
	$ bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-file /path/to/mapper.py    -mapper /path/to/func/mapper.py \
	-file /path/to/reducer.py   -reducer /path/to/func/reducer.py \
	-input /path/to/input/* 	-output /path/to/output
````
