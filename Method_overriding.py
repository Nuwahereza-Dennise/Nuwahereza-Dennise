class Mother:
    def move(self):
        print("A mother moves by walking")

class Baby(Mother):
    def move(self):
        print("A baby moves by crawling")
baby1 = Baby()
baby1.move()