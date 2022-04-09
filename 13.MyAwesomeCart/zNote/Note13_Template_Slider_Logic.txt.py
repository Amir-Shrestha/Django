Totalpost=16
TotalSlideWith4Posts=int(Totalpost/4)

print('Total Slides Slider :')
print('    First(1) Active Slide :') #first post with index 0 is taken by this !
for i in range(1,TotalSlideWith4Posts):
    print('   ',i+1," Slide")

Slide=1
print(Slide, ' Slide :')
for i in range(1,Totalpost+1):
    print('........', i , " Post")
    # if i%4 == 0:
    #     print(i)
    #     Slide+=1
    #     print(Slide,' Slide :')
    if i%4 == 0 and i!=Totalpost: #also check last iteration
        Slide+=1
        print(Slide,' Slide :')

