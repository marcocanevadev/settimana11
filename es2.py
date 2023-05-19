class Television:

    maxChannel = 999;
    maxVolume = 100;
    def __init__(self,brand,model):
        if not isinstance(brand, str):
            raise TypeError('brand must be string')
        if not isinstance(model, str):
            raise TypeError('model must be string')
        
        self._brand = brand
        self._model = model
        self._powerOn = False
        self._volume = 50
        self._muted = False
        self._channel = 1
        self._prevChan = 1

    def getPower(self):
        return self._powerOn
    def getChannel(self):
        return self._channel

    def togglePower(self):
        if self.getPower() == True:
            self._powerOn = False
        else:
            self._powerOn = True

    def volumeUp(self):             
        if self.getPower == True:
            if self._volume < self.maxVolume:
                self._volume += 1

    def volumeDown(self):           
        if self.getPower()== True:
            if self._volume > 0:
                self._volume -= 1

    def toggleMute(self):
        if self.getPower() == True:
            if self._muted == False:
                self._muted = True
            else:
                self._muted = False
   
    def channelUp(self):            
        if self.getPower() == True:
            self._prevChan = self._channel
            self._channel = (self._channel+1)%self.maxChannel
            
    def channelDown(self):
        if self.getPower() == True:
            self._prevChan = self._channel
            self._channel = ((self._channel-2)%(self.maxChannel))+1

    def setChannel(self, number):
        if self.getPower() == True:
            self._prevChan = self._channel
            if number < 1:
                self._channel = 1
            elif number > self.maxChannel:
                self._channel = self.maxChannel
            else:
                self._channel = number 

    def jumpPrevChan(self):
        if self.getPower() == True:
            self._prevChan, self._channel = self._channel, self._prevChan
    def __str__(self):
        return f' {type(self).__name__!s}:\nBrand:\t\t{self._brand!s}\nModel:\t\t{self._model!s}\nPower:\t\t{self._powerOn!s}\nVolume:\t\t{self._volume!s}\nMuted:\t\t{self._muted!s}\nChannel:\t{self._channel!s}\nPrevChannel:\t{self._prevChan!s}\n'
    

class DeluxeTv(Television):
    def __init__(self,name,brand):
        super().__init__(name,brand)
        self._favorites = []

    def addToFavorites(self):
        if self.getPower()==True:
            self._favorites.append(self.getChannel())

    def JumpToFavorites(self):
        if self.getPower() == True:
            self.setChannel([x for x in self._favorites if x > self.getChannel()][0])

    def __str__(self):
        return super().__str__()+f'Favorites:\t{self._favorites!s}\n'    


if __name__ == '__main__':
    n = Television('a','a1')
    d = DeluxeTv('b','b1')
    print('\t---init---')
    print(n)
    print(d)
    d.togglePower()
    d.setChannel(7)
    d.addToFavorites()
    d.setChannel(11)
    d.addToFavorites()
    print('\t---togglePower, add to favs: [7, 11]---')
    print(d)
    d.setChannel(8)
    d.JumpToFavorites()
    print('\t---setChann: 8, jumpToFav---')
    print(d)