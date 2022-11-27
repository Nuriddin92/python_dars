'''davlatlar=['O`zbekiston','Saudiya Arabistoni','Rossiya','Amerika','Xitoy','Yaponiya',]
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)'''

juft_sonlar=list(range(120,1200,2))
#print(juft_sonlar) 
summa=sum(juft_sonlar)
#print(summa)
katta=max(juft_sonlar)
kichik=min(juft_sonlar)
#print(katta-kichik)
#print(len(juft_sonlar))

#print(juft_sonlar[:20], juft_sonlar[260:280], juft_sonlar[520:])

taomlar=['choy','osh','makaron','mastava','shashlik']
nonushta=taomlar[:]
nonushta.remove('osh')
nonushta.remove('makaron')
nonushta.remove('mastava')
nonushta.remove('shashlik')
nonushta.append('asal')
nonushta.append('pishloq')
#print(nonushta, 'va', taomlar)
nonushta=tuple(nonushta)
nonushta[0]='qaymoq va non'
 