import sys

class NoSolutionError(Exception):
    def __str__(self):
        return 'there is no solution but god'



class QuadEquation:
    def __init__(self, a, b, c):
        if not isinstance(a,(float,int)):
            raise TypeError('a must be numeric')
        if not isinstance(b,(float,int)):
            raise TypeError('b must be numeric')
        if not isinstance(c,(float,int)):
            raise TypeError('c must be numeric')
        
        self._a=a
        self._b=b
        self._c=c

    def getSolutions(self):
        try:
            self.hasSolutions()
            
        except NoSolutionError():
            pass
        return ((-self._b+(self._b**2-4*self._a*self._c)**(1/2))/(2*self._a),((-self._b-(self._b**2-4*self._a*self._c)**(1/2))/(2*self._a)))

    def hasSolutions(self):
        if self._b**2-4*self._a*self._c <=0:
            raise NoSolutionError()
        else:
            return True

    def __str__(self):
        return f'dis equation sure has {self._a!s} and {self._b!s}... but dont forget {self._c}! '

if __name__ == '__main__':
    l = []
    print("insert values for coeffs: [ctrl-c to solve]")
    while True:
        try:
            coeff = float(input())
            l.append(coeff)
        except KeyboardInterrupt:
            break
        except ValueError:
            print('Valori non numerici detected')
            sys.exit()
    
    print('calculating...')
    if len(l) == 3:
        try:
            eq = QuadEquation(l[0], l[1], l[2])
            print(eq.hasSolutions())
            print(eq.getSolutions())
        
        except NoSolutionError as e:
            print(e)
    else:
        raise ValueError('hai sgravato col numero di coefficienti')
    


