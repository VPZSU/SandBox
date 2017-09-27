nombers = [ 3, 5, 7, 9]
strong = [ 'i', 'can', 'do', 'everything' ]
goal = [ nombers, strong ]
print ( goal )
strong.append( 'i\'m  strong' )
print ( goal )
del nombers [0]
print ( nombers + strong )
i_can = nombers + strong
print ( i_can )
print ( nombers * 3 )
nombers_2 = ( 1, 2 )
print ( nombers_2 )


favorite_dish = {'Sofiya' : 'sushi' ,
                 'Emi' : 'borsch' ,
                 'father' : 'beer' ,
                 'mother' : 'eggs' }
print ( favorite_dish )
print ( favorite_dish [ 'father' ])
del  favorite_dish [ 'mother' ]
print ( favorite_dish )
favorite_dish [ 'father'] = ' fish '
print ( favorite_dish )
