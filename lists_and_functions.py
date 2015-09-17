#Using lists and functions

def TopOrBottom(width):
# width is total width of returned line
    return '%s%s%s' %('+',('=' * (width-2)),'+')

def Fmt(val1,leftbit,val2,rightbit):
# prints two values padded with spaces
# val1 is thing to print on left, val2 is thing to print on right
# leftbit is width of left portion, rightbit is width of right portion
    part2 = '%.2f' % val2
    return '%s%s%s%s' % ('| ',val1.ljust(leftbit-2,' '),part2.rjust(rightbit-2,' '),' |')


items = [['Item_1', 1.75], ['Item_2', 2.50], ['Item_3', 3.50], ]
print TopOrBottom(40)
total = 0
for cntr in range(0,3):
    print Fmt(items[cntr][0],30,items[cntr][1],10)
    total += items[cntr][1]
print TopOrBottom(40)
print Fmt('Total',30,total,10)
print TopOrBottom(40)
