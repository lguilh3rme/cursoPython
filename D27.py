#encoding: utf-8
nm = str(raw_input('Nome completo: ')).strip()#strip tira os espaços
n = nm.split() #.split() fatia
print('Seu primeiro nome é {}. O ultimo é {}'.format(n[0],n[-1]))