
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale ,exhale")

class fish(Animal):

        def breathe(self):
            super().breathe()
            print("Doing this underwater")
        def num_eye(self):
            print(f"The number of eyes {self.num_eyes}")
            print("That sees through the darkness of water")

        def swim(self):
            print("Moving in water")



nemo = fish()
nemo.swim()
nemo.num_eye()
nemo.breathe()