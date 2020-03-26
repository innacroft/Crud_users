
def returnfn(number):
    for i in range(1,number+1):

        cuadrado=i**2
        cubo= i**3
        print('el cuadrado de {} es {}, el cubo de {} es {}'.format(i,cuadrado,i,cubo) )


   
    
    

if __name__ == "__main__":
    
    number= input('Ingrese el valor del numero')
    returnfn(int(number))
