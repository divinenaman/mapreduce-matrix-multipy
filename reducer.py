#!/usr/bin/env python
import re
import sys

def input_handler(file):
    rows = []
    cols = []
    
    row_regex = re.compile(r'^\d+R$')
    col_regex = re.compile(r'^\d+C$')

    for line in file:
        try:
                   
            _type,data = line.rstrip().split('\t',1)

            if row_regex.match(_type)!=None:
                index = int(_type[0:-1])
                rows.insert(index,data)

            elif col_regex.match(_type)!=None:
                index = int(_type[0:-1])
                cols.insert(index,data)
        except:
            pass

    return rows,cols

def mul(row,col):
    result = [row[i]*col[i] for i in range(len(row))]
    return sum(result)

def main(separator='\t'):
    
    rows,cols = input_handler(sys.stdin)

    for i,row in enumerate(rows):
        for j,col in enumerate(cols):

            row_ele = list(map(int,row.split(' ')))
            col_ele = list(map(int,col.split(' ')))

            if len(col_ele) == len(row_ele):
                result = mul(row_ele,col_ele)
                print(f'{i}{j}{separator}{result}')
    
if __name__ == "__main__":
    main()