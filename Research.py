from Relevance import Relevance

states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
          'RJ', 'RN', 'RS', 'RO',
          'RR', 'SC', 'SP', 'SE', 'TO']
subjects = ["Desemprego e desigualdade",
            "Questões éticas e morais",
            "Segurança cibernética e privacidade",
            "Controle e regulamentação",
            "Potencial desenvolvimento de IA superinteligente"
            ]
research = {}
listRelevance = {}
percentRelevance = {}


def initResearch():
    for state in states:
        research[state] = []


def menu():
    initResearch()
    while True:
        choice = str(input("""
Menu
0- Finalizar o Programa
1- Realizar avaliação
2- Relatório
Escolha: """))
        if choice == "0":
            break
        elif choice == "1":
            state = str(input("Qual a sigla do seu estado? ")).upper()
            if state in states:
                doQuestions(state)
            else:
                print("Digite um estado válido!")
        elif choice == "2":
            researchedState = str(input("Qual seu estado? ")).upper()
            if researchedState in states:
                calculateRelevances(research[researchedState])
                showRelevance(researchedState)
            else:
                print("Digite um estado válido!")


def doQuestions(state):
    relevance = Relevance()
    for index, attribute in enumerate(relevance.__dict__.items()):
        subject = subjects[index]
        rate = getRate(subject)
        relevance.__setattr__(attribute[0], rate)
    research[state].append(relevance)


def calculateRelevances(relevanceListByState):
    initListRelevance()
    for relevance in relevanceListByState:
        for index, attribute in enumerate(relevance.__dict__.items()):
            listRelevance[attribute[0]].append(attribute[1])
    for key, values in listRelevance.items():
        percentRelevance[key] = sum(values) / len(values)


def showRelevance(state):
    for subject, percentItem in zip(subjects, percentRelevance.items()):
        percent = str(percentItem[1])
        print(
            "Em relação à inteligência a artificial, os entrevistados do estado {}, tem {}% de preocupação com {}".format(
                state, percent, subject
            ))


def initListRelevance():
    listRelevance.clear()
    relevance = Relevance()
    for attr, _ in relevance.__dict__.items():
        listRelevance[attr] = []


def getRate(subject):
    rate = 20
    info = int(input("Em relação à inteligência artificial, qual seu nível de preocupação com {}? ".format(subject)))
    if 1 <= info <= 5:
        rate = info * 20
    return rate


menu()
