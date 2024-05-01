class car:
    def __init__(self,windows,tyre,engine):
        self.windows=windows
        self.tyre=tyre
        self.engine=engine


    def self_driving(self):
        print("this is self driving {} car".format(self.engine))

car1=car(4,4,"petrol")

car1.self_driving()