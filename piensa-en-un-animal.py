def ask(q) :
    ans = raw_input(q)
    return (ans=="si")

class Knowledge :
    pass

class Question (Knowledge) :

    def __init__(self,qtext,ifyes,ifno) :
        self.qtext = qtext
        self.ifyes = ifyes
        self.ifno = ifno

    def play(self) :
        if ask(self.qtext) :
            self.ifyes = self.ifyes.play()
        else :
            self.ifno = self.ifno.play()
        return self

class Answer (Knowledge) :

    def __init__(self,atext) :
        self.atext = atext

    def play(self) :
        if ask("Es un {}".format(self.atext)) :
            print "Lo sabia!"
        else :
            animal=raw_input("En que animal estas pensando? ")
            question=raw_input("Que pregunta hubiera diferenciado "
                               "entre {} y {}".format(self.atext,animal))
            if ask("La respuesta para {} hubiera sido".format(animal)) :
                return Question(question,Answer(animal),self)
            else :
                return Question(question,self,Answer(animal))       

kb = Question("Tiene cuatro patas?",
              Question("Es peludo?",
                       Answer("perro"),
                       Answer("cerdo")),
              Answer("mono"))
while(True) :
    print "Piensa en un animal"
    kb = kb.play()
    if not ask("Nuevo juego?"):
        break
    
