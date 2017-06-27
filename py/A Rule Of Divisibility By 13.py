"""
https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python
"""
def thirt(n):
    seq = [1,10,9,12,3,4]
    n = list(int(i) for i in reversed(str(n)))
    if len(seq) < len(n):
        compute1 = [i for i in seq[0:len(n)-len(seq)]]
        seq.extend(compute1)
    compute1 = sum(i * j for i,j in zip(n,seq))
    compute1 = list(int(i) for i in reversed(str(compute1)))
    compute2 = sum(i * j for i,j in zip(compute1,seq))
    if compute1 == compute2:
        return compute2
    else:
        compute1 = list(int(i) for i in reversed(str(compute2)))
        return sum(i * j for i,j in zip(compute1,seq)) 
