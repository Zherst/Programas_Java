class pessoa:
    def __init__(self,name,idade,p,h):
        self.nome = name
        self.idade = idade
        self.peso   = p
        self.altura = h
    def calcIMC(self):
        return round(self.peso/self.altura**2)
    
class medicamento:
    def __init__(self,**d):
        self.nome        = d['n'] 
        self.finalidade  = d['f']
        self.preco       = d['p']

class paciente(pessoa):
    def __init__(self,n,i,p,h,**D):
        pessoa.__init__(self,n,i,p,h)
        self.comorbidade = D['doenca']
    def envelhecer(self,anos):
        self.idade += anos
    def engordar(self,kgs):
        self.peso += kgs
    def crescer(self,medida):
        self.altura += medida

class medico(pessoa):
    def __init__(self,n,i,p,h, **Di):
        pessoa.__init__(self,n,i,p,h)
        self.CRM = Di.pop('crm','--')
        self.especialidade = Di.pop('esp', '--')
        self.paciente = []
        if 'listaP' in Di:
            for x in Di['listaP']:
                self.paciente.append(x)
        self.medicamento = []
        if 'listaM' in Di:
            for x in Di['listaM']:
                self.medicamento.append(x)
    def addPaciente(self,novoP):
        if novoP not in self.paciente:
            self.paciente.append(novoP)
    def addMedicamento(self,novoM):
        if novoM not in self.medicamento:
            self.medicamento.append(novoM)

#====================================================================

medic1 = medicamento(n="neosaldina DIP", f ='enxaqueca', p= 18.50)
medic2 = medicamento(n='Dipirona', f ='febre', p=15.42)
medic3 = medicamento(n='Omeoprazol', f ='dor de estômago', p=12.00)
medic4 = medicamento(n='Rinitil', f ='rinite', p=32.50)

pac1 = paciente('Maria', 18, 32.8, 1.60, doenca='febre' )
pac2 = paciente('Daniel', 45, 82, 1.92, doenca='dor de estômago')
pac3 = paciente('Joaquina', 22, 65, 1.85, doenca='rinite')
pac4 = paciente('kevin', 12, 32, 1.68, doenca='rinite')

medico1 = medico('Afonso Botelho', 58, 68, 1.72, listaP=[pac1,pac2,pac3], listaM=[medic1,medic2,medic3,medic4])

for x in medico1.paciente:
    print(x.nome)

#média dos preços indicados pelo médico

m = 0
cont = 1
for x in medico1.medicamento:
    m += x.preco
    cont += 1
print(f'preço médio dos medicamentos vale R$ {round(m/cont, 2)}')