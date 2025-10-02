class CoffeMaker:
    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        print("PIP PIP")
        print("O café esta pronto")

    def __boil_water(self):
        print("Fervendo água...")

    def __mix(self):
        print("Juntando café e água...")


coffe_maker = CoffeMaker()
coffe_maker.make_coffe
