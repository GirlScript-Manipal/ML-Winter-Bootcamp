l1= [() , (1,4,3) , (),("p" , "s" , "v") , (),("valentines"), () , ("",""),() , (143)]
def fu(var):
    if var!=0:
        return var
print("The list:")
print(l1)
l2= list(filter(fu,l1))
print("modified list" )
l2.reverse()
print(l2)
