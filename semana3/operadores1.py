x = 1
y = 2
z = 3

resp_a = x >= y
print('Letra a: ', resp_a)

resp_b = x <= y and y < z
print('Letra b: ', resp_b)

resp_c = not(x >= y)
print('Letra c: ', resp_c)

resp_d = x >= (z - 2)
print('Letra d: ', resp_d)

resp_e = (x > z) and (x < y)
print('Letra e: ', resp_e)

resp_f = (y > x) and (z > y) and (z > x)
print('Letra f: ', resp_f)

resp_g = (x < 0) or (y > x)
print('Letra g: ', resp_g)

resp_h = (x < 0) or (y > x) and (y < z) 
print('Letra h: ', resp_h)

resp_i = 2 + x < y * 4 and x - 3 > 6 + y / 2
print('Letra i: ', resp_i)

resp_j = ((2 + x) < (y * 4)) and ((x - 3) > (6 + y / 2))
print('Letra j: ', resp_j)