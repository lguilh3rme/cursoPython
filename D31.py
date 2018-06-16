#encoding: utf-8
km = float(input('Quantos Km você deseja percorrer? ')) 
if km <= 200:
    print('Sua passagem vai custar {} reais. '.format(km * 0.5)) 
else: 
    print('Sua passagem vai custar {} reais. '.format(km * 0.45))