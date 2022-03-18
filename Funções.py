import time
from time import sleep
#_______________________________________________________________________
#função de boas-vindas

def boasVindas():
    print("Oie, como vai? Meu nome é Amie e eu estou super feliz de te ter por aqui!!")
    nome = input("Como é seu nome, lindeza? ")
    print(f'Uau, {nome}, que nome lindo! Prazer em te conhecer!')

#função para cadastro
def cadastro():
    nomeCompleto = input("Por favor, insira seu nome completo: ").lower()

    nomeDeUsuario = input("Como você quer ser chamado(a)? ").lower()
    caracteresMinimos = 4

    arquivo = open(f"usuarios\{nomeDeUsuario}.txt", 'w')
    arquivo.write(f'{nomeDeUsuario}')
    arquivo.close()

    if len(nomeDeUsuario) <= caracteresMinimos:
        print('''Seu nome de usuário precisa ter mais de quatro letras, meu bem.
        Tente novamente.''')
        nomeDeUsuario = input("Como você quer ser chamado(a)? ").lower()
        arquivo = open(f"usuarios\{nomeDeUsuario}.txt", 'w')
        arquivo.write(f'{nomeDeUsuario}')
        arquivo.close()

    senha = input("Por favor, insira uma senha forte: ").lower()
    confirmaSenha = input("Por favor, confirme sua senha: ").lower()

    while confirmaSenha != senha:
        print("Confirmação falhou, tente novamente.")
        confirmaSenha = input("Por favor, confirme sua senha: ").lower()
        if confirmaSenha == senha:
            break
        arquivo = open(f"usuarios\{senha}.txt", 'r')
        arquivo.write(f'{senha}')
        arquivo.close()

    print(f'''Perfeito, {nomeDeUsuario}.
    Seu cadastro está concluído e a gente já pode se divertir juntos!''')
#--------------------------------------------------------------------------------------
#função para login
def login():
    print("Bem-vindo de volta! Vamos fazer seu login.")
    nomeDeUsuario = input("Insira o seu nome de usuário: ").lower()
    senha = input("Insira sua senha: ").lower()

    arquivo = open(f"usuarios\{nomeDeUsuario}.txt", 'r')
    for lista in arquivo:
        global valores
        valores = lista.split()
    if valores[0] == nomeDeUsuario:
        print(f'Rroi, {nomeDeUsuario}, né? Log-in efetuado com sucesso.')
#--------------------------------------------------------------------------------------
#função para filmes de terror e suspense
def filmesTerror():
    print(''' AH! Como você tem coragem de assistir a essas coisas?!
            Bom, de certa forma, escolhi três filmes INCRÍVEIS
            só para você!
            ''')
    sleep(4)
    print(''' 3° CORRA!
        O filme conta a história de um fotógrafo chamado Chris, que
        viaja para conhecer os pais da namorada dele.
        Até aí tudo bem, só que o pessoal era esquisito PRA CARAMBA e o
        tempo todo ele meio que temia ser recepcionado com preconceito, uma 
        vez que era negro. Quando a noite chega, as coisas ficam mais sérias
        e o clima muda completamente. Ele logo se vê sem saída e percebe
        que há algo de muito errado com aquela família.''')
    sleep(2)
    print("Um baita filmaço, vale muito a pena.")
    print(''' 2° JOGOS MORTAIS
        O filme conta uma história sinistra de dois homens que são
        sequestrados por um serial killer chamado "Jigsaw". Eles logo
        descobrem que fazem parte de um jogo macabro onde para sobreviver,
        precisam se sacrificar um pouco - no caso dos homens, um precisa
        matar o outro pela segurança de sua mulher e filha.
        O filme é dahora, mas não recomendo se tiver estômago fraco.
        ''')
    sleep(4)
    print(''' 1° ILHA DO MEDO
         O filme conta a história de Teddy Daniels, um detetive veterano de guerra investigando
         o desaparecimento de uma assassina em um presídio psiquiátrico. Ao chegar lá, algo
         MUITO louco começa a acontecer na cabeça dele, de modo que o homem
         não consegue mais distinguir o que é real e o que não é. 
         ''')
    sleep(2)
    print("Esse é um dos meus favoritos! Uma obra prima super bem dirigida e cheia de reviravoltas.")
#--------------------------------------------------------------------------------------
#função para filme de comédia
def filmesComedia():
    print('''Nada como um filme de comédia para tirar um pouco o estresse, não é?
    Pois bem, eu separei uns super legais para você!''')
    sleep(4)
    print('''

    1°) FAMÍLIA DO BAGULHO
    O filme conta a história de um pequeno negociador de drogas, que 
    encurralado depois de perder seu estoque, precisa se resolver com seu fornecedor.
    Acontece que ele tem que buscar um pacote de drogas no México, e para passar
    na fronteira tranquilamente, ele monta uma família falsa com uma stripper, uma mendiga
    e um garoto perdido.
    O filme é um absurdo de tão engraçado. Eu recomendo 100%!!
    ''')
    sleep(5)
    print('''
    1°) MENINAS MALVADAS
    Clássico, né? O filme conta a história de Cady, uma garota criada a vida inteira
    na África e educada em casa, e sua aventura no tenebroso ensino médio. Ao chegar na escola,
    ela se depara com um grupo de garotas populares: a abelha rainha, chamada Regina George,
    e suas melhores amigas, as "poderosas". Tendo um plano arquitetado para destruir elas,
    Cady se envolve entre as garotas. Só que quanto mais ela adentra no mundo delas, mais difícil
    fica de voltar atrás.
    ''')
    sleep(3)
    print("E então? Anda usando rosa todas as quartas?")
#--------------------------------------------------------------------------------------
#função para filme de fantasia e ficção
def filmesFantasia():
    print('''Entrar em um mundo novo é fantástico, não é?
    Separei uns filmes MARAVILHOSOS de fantasia e ficção só para você!
    ''')
    sleep(4)
    print('''
    3°) O LABIRINTO DO FAUNO
    Ofélia perdeu o pai na guerra. Sua mãe se casou novamente com Vidal,
    um dos vilões mais detestáveis dos contos de fada, um capitão do exército
    franquista que é absolutamente medonho e vil. Ele ordena que sua esposa pegue
    a estrada para encontrá-lo no interior. Em uma parada na estrada, Ofélia en-
    contra um olho de pedra e na margem da via, encontra uma estrela de onde o olho caiu.
    É então que sua jornada mítica pelas florestras ancestrais começa.
    ''')
    sleep(8)
    print('''
    2°) NOIVA CADÁVER
    As famílias de Victor e Victoria estão arranjando seu casamento. Nervoso com a
    cerimônia, Victor vai sozinho à floresta para ensaiar seus votos, mas o que ele 
    pensava ser um tronco velho de árvore é na verdade o braço esquelético de Emily,
    uma noiva assassinada depois de fugir com seu amor. Convencida de que Victor 
    confessou seu amor, ela o leva para o mundo dos mortos.
    ''')
    sleep(8)
    print('''
    1°) INTERESTELAR
    As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas
    recebe a missão de verificar possíveis planetas para receberem a população 
    mundial, possibilitanto a continuação da espécie. Cooper é chamado para liderar o grupo
    e aceita a missão mesmo sabendo que pode nunca mais ver os filhos.
    ''')
#--------------------------------------------------------------------------------------
#função para serie de drama
def seriesDrama():
    print('''Séries dramáticas são perfeitas para um dia chuvoso e um cobertozinho com chocolate.
    Separei umas séries maravilhosas dignas de maratona só para você!''')
    sleep(4)
    print('''
    3°) O GÂMBITO DA RAINHA
    Beth Harmon é colocada em um orfanato depois de sofrer um acidente de 
    carro com sua mãe. Lá, ela descobre seu talento impressionante para o 
    xadrez e a dependência pelos ansiolíticos dado às crianças.
    ''')
    sleep(6)
    print('''
    2°) BLACK MIRROR
    Cada episódio da série conta uma história diferente envolvendo tecnologias
    em níveis avançados, refletindo seu lado negro e mostrando que nem toda novidade
    traz só benefícios.
    ''')
    sleep(5)
    print('''
    1°) GAME OF THRONES 
    Situada nos continentes fictícios de Westeros e Essos, a série
    centra-se no Trono de Ferro dos Setes Reinos e segue um enredo de alianças
    e conflitos entre as famílias nobres dinásticas, seja competindo para
    reinvidicar o trono ou lutando por sua independência.
    ''')
#--------------------------------------------------------------------------------------
#função para série de terror
def serieTerror():
    print('''
    Séries de terror são ótimas para aumentar a adrenalina e nos poupar de
    algumas noites de sono, não é verdade?!''')
    sleep(4)
    print(''''
    2°) AMERICAN HORROR STORY
    Com temas psicodélicos, cada temporada é uma história diferente explorando
    o sobrenatural e as raízes do medo humano. Com assombrações, bruxas e palhaços
    assassinos, a série é perfeita para quem gosta de levar uns bons sustos.
    ''')
    sleep(3)
    print('''
    1° A MALDIÇÃO DA MANSÃO BLY
    Baseada no livro "A Volta do Parafuso", a série conta a história de uma jovem
    indo trabalhar no interior para cuidar de duas crianças órfãs, Miles e Dora.
    Embora a casa pareça comum de primeira vista, logo ela descobre os segredos
    horripilantes que rondam a mansão e as crianças.
    ''')
#--------------------------------------------------------------------------------------
#função para série de comédia 
def seriesComedia():
    print('''Seja um besteirol ou um conjunto de críticas à sociedade,
    séries de comédia sempre dão um jeitinho de ganhar nosso coração
    e as nossas risadas!''')
    sleep(3)
    print('''
    3°) THE BIG BANG THEORY
    A série acompanha a vida de quatro físicos nerds em sua vida rotineira acerca
    de estudos, quadrinhos, filmes e séries de ficção científica e experimentos
    físicos, e a interação deles com sua vizinha absolutamente normal.
    ''')
    sleep(5)
    print('''
    2°) THE OFFICE
    A série é focada em colegas de trabalho, em um escritório numa fábrica de papéis.
    Além de bastante cômica e com personagens fora do padrão, a série é responsável
    por fazer diversas críticas sociais e até hoje é ACLAMADÍSSIMA pela crítica, você
    vai amar.
    ''')
    sleep(8)
    print('''
    1°) BROOKLYN 99
    Parecidinha com The Office, Brooklyn Nine-Nine se passa em uma delegacia,
    com o foco no detetive Jake Peralta. Com um tom leve e absurdamente brincalhão e
    com personagens bem caricatos, a série tira risadas de você a cada instante,
    mas também é responsável por enaltecer pontos importantes a serem discutidos,
    como a representatividade LGBT e críticas ao racismo e machismo.
    ''')
#--------------------------------------------------------------------------------------
#função para músicas de rock
def musicasRock():
    print('''WOW, então temos um(a) rockeiro(a) entre nós?
    Chega mais! Ozzy Osbourne tá' te mandando um beijo!''')
    sleep(2)
    print('''
    DRAIN YOU -- NIRVANA
    "Uma garota olha para a outra e diz: tenho sorte de ter você
    Não me importo com o que pensa, a menos que seja sobre mim
    É agora meu dever te drenar completamente
    Viajo em um tubo que termina na sua infecção"
    ''')
    sleep(5)
    print('''
    DARK NECESSITIES -- RED HOT CHILLI PEPPERS
    "Você não entende a minha mente
    Você não conhece meu tipo
    Necessidades obscuras são partes do meu ser
    Diga ao mundo que eu estou
    Caindo do céu
    Necessidades obscuras são parte do meu ser"
    ''')
    sleep(5)
    print('''
    AINDA É CEDO -- LEGIÃO URBANA
    "Mas egoísta que eu sou, esqueci de ajudar
     A ela como ela me ajudou, e não quis me separar
     Ela também estava perdida, e por isso, se agarrava a mim também
     E eu me agarrava a ela, eu não tinha mais ninguém
     E eu dizia 'ainda é cedo'"
    ''')
    sleep(5)
    print('''
    FLORES -- TITÃS
    "Chorei até ficar cansado
    De ver os meus olhos no espelho
    Chorei por ter despedaçado
    As flores que estão no canteiro

    Os punhos e os pulsos cortados
    E o resto do meu corpo inteiro
    Há flores cobrindo o telhado e embaixo do meu travesseiro
    Há flores em todos os lados
    Há flores em tudo que eu vejo"
    ''')
#--------------------------------------------------------------------------------------
#função para musica pop
def musicasPop():
    print("Ah, música popular é tão boa! Você também tem vontade de dar uma dançadinha?")
    sleep(2)
    print('''
    GINGA -- IZA
    "Sagacidade para viver
    Lutar, cair, crescer
    Sem arriar ou se render
    Tem que defender
    Observar e absorver
    Com fé no amor, no bem
    Se liga no meu proceder
    Sigo em frente e vou além"
    ''')
    sleep(4)
    print('''
    TALK TOO MUCH -- COIN 
    "Cafeína, conversa fiada
    Espere pelo clima artificial
    Discutindo eventos atuais
    Eu não vou ter pressa
    
    Não sou o pensador adiantado
    Você leu minha mente
    É melhor deixar sem dizer
    Por que não posso deixar sem dizer?"
    ''')
    sleep(4)
    print('''
    SUNFLOWER -- REX ORANGE COUNTY
    "Tentando manter minha mente firme
    Girassóis ainda crescem a noite
    Esperando por um minuto até o Sol ser visto
    através dos meus olhos"
    ''')
    sleep(4)
    print('''
    BONSAI -- SUPERCOMBO
    "Eu prefiro a minha cama
    Botar o meu pijama
    Sintonizar a mente
    Morar em Bangladesh
    Trocar ideia com os peixe
    Romance em filme de horror"
    ''')
#--------------------------------------------------------------------------------------
#função para música retro
def musicaRetro():
    print("Então você é daqueles que ama o passado?! As músicas antigas são puro ouro!")
    sleep(2)
    print('''
    FOR NO ONE -- THE BEATLES
    "E nos olhos dela você não vê nada
    Nenhum sinal de amor por trás das lágrimas
    Choradas por ninguém
    Um amor que devia ter durado anos"
    ''')
    sleep(4)
    print('''
    STUCK ON YOU - ELVIS PRESLEY
    "Você pode sacudir uma macieira até uma maçã cair
    Sacudir sacudir, docinho
    Mas você nunca vai me abalar
    Vou agarrar-me como cola
    Agarrar porque estou
    Colado em você"
    ''')
    sleep(4)
    print('''
    HAVE YOU HEARD? -- THE DUPREES
    "Você ouviu dizer?
    Do dia que eles vão se casar
    Boatos vêm e vão
    Mesmo assim gostaria de saber
    Se é verdade, você não vai me dizer?
    Você ouviu dizer?"
    ''')
    sleep(4)
    print('''
    BEAT IT - MICHAEL JACKSON
    "Eles me disseram "nunca mais volte aqui!
    Não quero ver sua cara, é melhor você desaparecer!"
    O fogo nos olhos deles, e suas palavras foram bem claras
    Então cai fora, apenas caia fora!"
    ''')
#--------------------------------------------------------------------------------------
#função para livros
def livros():
    print(''' Ah, uma alma literária! Seja um amante por leitura ou
    alguém que está começando sua jornada pelos livros agora, tenho
    ótimas opções para te recomendar!''')
    sleep(4)
    print('''
    Admirável Mundo Novo -- Aldous Huxley
    A terra agora se divide em dez grandes regiões administrativas.
    A população de dois bilhões de seres humanos é formada por castas com
    traços distintos manipulados pela engenharia genética: nos laboratórios
    são definidos os pouco dotados, destinados aos rigores do trabalho braçal,
    e também os que crescem para comandar. Não há espaço para a surpresa, para
    o imprevisto. O slogan "comunidade, identidade, estabilidade" sustenta
    a trama do tecido social. Estamos no ano 632 depois de Ford - aquele da linha
    de automóveis - quando o amor é proibido e o sexo, estimulado. 
    ''')
    sleep(12)
    print('''
    A Vida Por Um Fio -- Álvaro Cardoso Gomes
    Aos dezenove anos, Dênis está internado num hospital para recuperação
    de dependentes químicos. Entre alucinações e insônia, repensa sua vida,
    recordando o que aconteceu até chegar ali.
    ''')
    sleep(10)
    print('''
    Laranja Mecânica -- Antony Burguess
    Pelas ruas de um metrópole decadente , Alex, o jovem líder de uma gangue
    de adolescentes, tem por diversão cometer perversidades e atos de violência.
    Depois de ir longe demais, é preso pelo governo e submetido a um método
    experimental de recondicionamento de mentes criminosas.
    ''')
#--------------------------------------------------------------------------------------
#função para dicas contra a covid-19
def dicasCovid():
    print(''' A doença do coronavirus é infecciosa causada por um vírus recém-descoberto.
    A maioria das pessoas que adoece em decorrência da Covid-19 apresenta sintomas leves a 
    moderados e se recupera sem tratamento especial.
    
    Entre os sintomas estão:
    - Dores e desconforto;
    - Dor de garganta;
    - Tosse seca;
    - Cansaço;
    - Erupção cutânea;
    - Perda de olfato e paladar;
    - Diarréia
    ''')
    sleep(5)
    print('''
    
    Quando não puder lavar as mãos com água e sabão, use álcool em gel.
    O que não pode é ficar contaminando aonde você passa, né?
    
    Não cumprimente pessoas com apertos de mão ou abraços, e evite aproximação.
    É cada um no seu quadrado, mozão.
    
    Não saia muito de casa, apenas se for necessário. Jogue um joguinho,
    maratone uma série. Finja-se de antissocial!
    
    Lave tudo que vier de fora.

    Quando chegar em casa, tire todas as suas roupas e lave-as imediatamente.''')
    sleep(5)
    print("Tem sido tempos dolorosos, mas se nos unirmos, venceremos!")
#--------------------------------------------------------------------------------------
#função para dicas de saúde
def dicasSaude():
    print('''É realmente muito bom que esta se cuidado bem.
    Eu separei umas dicas de saúde que melhorarão e muito sua qualidade de vida.''')
    sleep(4)
    print(''' 
    1 - Mantenha sua alimentação equilibrada.
    Sabe aquele hamburgão que você come todo fim de semana? É! Aquele do BK mesmo.
    PARE! 
    Por mais que seja bastante gostoso jogar umas porcarias na nossa barriga, é imprescindível que
    haja uma certa organização em relação ao que você põe no seu prato. Considere comer mais
    frutas, verduras e hortaliças, reduzir alimentos processados e reduzir açúcares.
    
    Uma boa alimentação pode te deixar mais leve, disposto e feliz''')
    sleep(10)
    print('''
    2 - Pratique exercícios
    Pelo amor de Deus, saia da frente do computador, televisão e celular e vai dar uma corridinha!
    Mesmo que você fique com preguiça no começo, garanto que é só uma questão de tempo
    até se acostumar. Logo você pereberá que exercícios físicos são essenciais para uma
    qualidade de vida à longo prazo.
    
    Isso significa que dar uma caminhada ou uma corridinha pode reduzir significativamente
    os riscos de você obter alguma doença cardíaca, artrite, obesidade, diabetes e hipertensão.
    
    Já pensou quantos benefícios?! E você ainda pode ficar com um corpinho lindo!''')
    sleep(10)
    print('''
    3 - Durma bem
    O sono, meu bem, não é uma opção. Então se você gosta de fazer cosplay de morcego e 
    possui hábitos noturnos na mesma proporção que os diurnos, pare agora mesmo.
    
    Dormir bem é essencial para que você tenha um bom dia. Você tem mais disposição para tarefas
    físicas, além de que seu cérebro fica ativo e se concentra com maior facilidade.
    Quando o indivíduo não possui suas devidas horas de sono REM, ele fica irritadiço e cansado.
    
    Conte carneirinhos ou coloque um sonzinho de chuva no YouTube, mas o essencial é que durma!''')
    sleep(3)
listadeamigos = {('oi', 'amigo')}
print(type(listadeamigos))
