'''bibliotecas!!'''
#------------------------------------------------
from random import choice
import time
from time import sleep
import string
import datetime
from datetime import date
import Funções
from Funções import boasVindas
from Funções import cadastro
from Funções import login
from Funções import filmesTerror
from Funções import filmesComedia
from Funções import filmesFantasia
from Funções import seriesComedia
from Funções import seriesDrama
from Funções import serieTerror
from Funções import musicaRetro
from Funções import musicasPop
from Funções import musicasRock
from Funções import livros
from Funções import dicasCovid
from Funções import dicasSaude
#-----------------------------------------------------------------------------------------------------
boasVindas()
sleep(3)
print(''' Acontece que eu sou BEM esquecida das coisas, e não consigo lembrar
se a gente já se conhece ou não...''')

cadastroOuLogin = input('''A gente já se conhece, ou é a sua primeira vez por aqui??
1 - Nos conhecemos;
2 - Nunca nem vi.
''')

if cadastroOuLogin == '1':
    login()
if cadastroOuLogin == '2':
    cadastro()

#método para atrasar um pouco o código
segundos = 4
print('''Então, já se decidiu como a gente vai se divertir?
Não?? :o 
Não acredito!
Bom, eu tenho diversas funcionalidades que permitem que a gente se divirta pra caramba. ''')

sleep(segundos)
data = date.today()
dataDoDia = '{}/{}/{}'.format(data.day,data.month,data.year)
historico = []
historicoTotal = (f"{dataDoDia} -", historico)
contador = 0
while contador != '6':
    oQueFazer = input('''
    O que você quer fazer agora?

    1 - Quero que me recomende algo;
    2 - Quero dicas de saúde;
    3 - Quero conselhos amorosos;
    4 - Quero ver minha lista de melhores amigos;
    5 - Quero jogar forca!;
    6 - Quero sair!!
    ''')

    sleep(segundos)
    if oQueFazer == '1':
        print(" ----- RECOMENDAÇÕES ----- ")
        escolha1 = 'Você quer que eu te recomende algo.'
        historico.append(escolha1)
        print("Eu sou muito boa recomendando coisas, modesta parte.")
        oQueRecomendar = input('''
        O que quer que eu te recomende?
        01 - Filmes;
        02 - Seriados;
        03 - Músicas;
        05 - Livros;
        ''').lower()
        if (oQueRecomendar == '1') or (oQueRecomendar == 'Filmes') or (oQueRecomendar == 'filmes'):
            escolha2 = 'Você pediu que eu te recomendasse filmes.'
            historico.append(escolha2)
            print("Irra! Eu AMO filmes!")
            generos = ['Suspense', 'suspense', 'comedia', 'comédia', 'fantasia', 'fantasia']
            generoDeFilme = input('''Bom, pra eu te recomendar um filme bonzaço,
            me diz qual é o seu gênero favorito!
            - Suspense e terror;
            - Comédia;
            - Fantasia
            ''').lower()
            if (generoDeFilme == 'suspense e terror') or (generoDeFilme == 'Suspense e Terror'):
                escolha3 = '-Pediu que eu te recomendasse filmes de terror e suspense'
                historico.append(escolha3)
                filmesTerror()
            if (generoDeFilme == 'comédia') or (generoDeFilme == 'comedia'):
                escolha3 = '-Pediu que eu te recomendasse filmes de comédia'
                historico.append(escolha3)
                filmesComedia()
            if (generoDeFilme == 'fantasia') or (generoDeFilme == 'Fantasia'):
                escolha3 = '-Pediu que eu te recomendasse filmes de fantasia'
                historico.append(escolha3)
                filmesFantasia()
        if (oQueRecomendar == '2') or (oQueRecomendar == 'seriados') or (oQueRecomendar == 'Seriados'):
            escolha2 = '-Você pediu que eu te recomendasse séries'
            historico.append(escolha2)
            print("Maratonar é maravilhoso, não é? Está procurando algo para maratonar?")
            generoSerie = ['1', '2', '3']
            generoDeSerie = input('''Qual seu gênero favorito de séries?
            - 1: Comédia;
            - 2: Terror;
            - 3: Drama.
            ''')
            if (generoDeSerie =='1') or (generoDeSerie == 'comedia') or (generoDeSerie == 'Comédia'):
                escolha3 = '-Pediu que eu te recomendasse séries de comédia'
                historico.append(escolha3)
                seriesComedia()
            if (generoDeSerie == '2') or (generoDeSerie == 'terror') or (generoDeSerie == 'Terror'):
                escolha3 = '-Pediu que eu te recomendasse séries de terror'
                historico.append(escolha3)
                serieTerror()
            if (generoDeSerie == '3') or (generoDeSerie == 'drama') or (generoDeSerie == 'Drama'):
                escolha3 = '-Pediu que eu te recomendasse séries de drama'
                historico.append(escolha3)
                seriesDrama()
        if (oQueRecomendar == '3') or (oQueRecomendar == 'musicas') or (oQueRecomendar == 'Músicas'):
            escolha2 = '-Pediu que eu te recomendasse músicas'
            historico.append(escolha2)
            print("Ah, que legal! Está procurando algo novo para ouvir?")
            estilos = ['1', '2', '3']
            estiloMusical = input(''' Só para eu saber, qual tipo de música quer que eu te recomende?
            1 - Retrô;
            2 - Pop;
            3 - Rock
            ''').lower()
            if (estiloMusical == '1') or (estiloMusical == 'Retrô') or (estiloMusical == 'retro') or (estiloMusical == 'retrô'):
                escolha3 = "-Pediu que eu te recomendasse um retrozão top!"
                historico.append(escolha3)
                musicaRetro()
            if (estiloMusical == '2') or (estiloMusical == 'pop') or (estiloMusical == 'Pop'):
                escolha3 = "-Pediu que eu te recomendasse música pop"
                historico.append(escolha3)
                musicasPop()
            if (estiloMusical == '3') or (estiloMusical == 'rock') or (estiloMusical == 'Rock'):
                escolha3 = '-Pediu que eu recomendasse um rock bacana'
                historico.append(escolha3)
                musicasRock()
        if (oQueRecomendar == 'livros') or (oQueRecomendar == 'Livros') or (oQueRecomendar == '5'):
            escolha2 = '-Pediu que te recomendasse livros'
            historico.append(escolha2)
            livros()
    if oQueFazer == '2':
        print(" ----- DICAS DE SAÚDE ----- ")
        escolha1 = '-Você pediu que eu te desse dicas de saúde'
        print('''Que ótimo que quer dicas de sáude.
        É sempre importante manter-se bem e em forma para garantir uma melhor qualidade de vida''')
        sobreSaude = input(''' Dentro do nosso setor fictício de saúde, você pode fazer
        algumas coisinhas. Por onde quer começar?
        
        1 -- Quero calcular meu índice de massa corpórea;
        2 -- Quero saber como me proteger do coronavirus!;
        3 -- Quero saber dicas de saúde no geral
        R:
        ''')
        if sobreSaude == '1':
            escolha2 = '-Pediu que eu calculasse seu IMC'
            historico.append(escolha2)
            print(''' Você sabe o que o IMC (índice de massa corpórea) quer dizer?
            O IMC é um parâmetro para sabermos se o peso está de acordo com a altura,
            o que pode interferir diretamenre na saúde e qualidade de vida do indivíduo.
            A partir do resultado do IMC é possível saber se a pessoa está dentro
            do peso ideal.''')
            idade = input("Vamos começar? Qual sua idade? R: ")
            altura = float(input("Qual sua altura? R: "))
            peso = float(input("Qual seu peso? R: "))

            imc = peso/(altura * altura)
            if imc < 18.5:
                print (f'''Ops! Você está magrinho demais! Seu IMC é de {imc:.2f}.
                Trate de comer mais feijão e banana!''')
            if (imc >= 18.5) and (imc < 25):
                print(f''' Meus parabéns, você está em um nível considerado saudável!
                Mantenha-se assim e não terá problemas. Seu IMC é de {imc:.2f}''')
            if (imc >= 25) and (imc < 30):
                print(f'''Hmm, você está em sobrepeso. Seria legal começar uma dieta,
                quem sabe praticar alguns exercícios! Seu IMC é de {imc:.2f}''')
            if (imc >= 30) and (imc < 35):
                print(f''' Puxa, parece que você tem um grau leve de obesidade.
                Por mais que um corpo cheinho não afete na sua beleza e autoestima, chega uma
                hora que ele afeta sua saúde como um todo. Por isso, considere uma dieta e exercícios.
                Seu IMC é de {imc:.2f}''')
            if (imc >= 35) and (imc < 40):
                print(f''' Puxa, parece que você tem um grau grave de obesidade.
                Por mais que um corpo cheinho não afete na sua beleza e autoestima, chega uma
                hora que ele afeta sua saúde como um todo. Por isso, faça uma dieta e exercícios.
                Seu IMC é de {imc:.2f}''')
            if imc > 40:
                print(f''' Por favor, cuide da sua saúde. Você tem obesidade mórbida, e por mais
                que sua beleza e autoestima não sejam afetados, sua saúde corre perigo.
                Procure um nutricionista, faça exercícios e se cuide!
                Seu IMC é de {imc:.2f}''')
        if sobreSaude == '2':
            escolha2 = '-Pediu que eu desse dicas de combate ao Coronavirus'
            historico.append(escolha2)
            dicasCovid()
        if sobreSaude == '3':
            escolha2 = '-Pediu que eu desse dicas de saúde no geral'
            historico.append(escolha2)
            dicasSaude()
    if oQueFazer == '3':
        print(" ----- CONSELHOS AMOROSOS ----- ")
        escolha1 = '-Pediu que eu te desse conselhos amorosos'
        historico.append(escolha1)
        print(''' Está precisando saber como tratar seu crush? Não se preocupe, eu vou te ajudar!
        1 - Elogie sua beleza
        Elogios à aparência não é tudo, mas ajuda a melhorar a autoestima de quem você gosta!
        Além disso, beleza não é só exterior; sempre elogie suas ações, mudanças, inteligência e etc.
        ''')
        sleep(4)
        print('''
        2 - Demonstre carinho
        Cada um tem um jeitinho próprio de demonstrar carinho, mesmo bruto ou duvidoso em certos
        casos. De toda forma, procure sempre deixar bem claro o seu afeto por tal pessoa. Que tal
        perguntar se chegou em casa bem? Ou dar "bom dia" todos os dias, e perguntar como foi o dia?
        ''')
        sleep(4)
        print('''
        3 - Faça com que se sinta importante
        Sempre é bom fazer com que tal pessoa sinta que tem um espaço de importância na sua vida.
        Assim, os laços de confiança aumentam e a aproximação ocorre naturalmente.
        ''')
        sleep(4)
        print('''
        4 - Diga o que sente
        Não precisa ser verbalmente, algumas pessoas são tímidas ou sente medo que a relação
        mude depois da declaração. Bem, isso é normal. Nesse caso, diga que você gosta de tal pessoa
        com ações, como por exemplo, comprar algum doce ou bombom que ela irá gostar.
        Fazer surpresinhas é uma boa também.
        ''')
    if oQueFazer == '4':
        print(" ----- LISTA DE MELHORES AMIGOS ----- ")
        escolha1 = '-Pediu para modificar a lista de melhores amigos'
        print(''' A ideia é que eu sirva para ser sua melhor amiga, mas 
        compreendo que seu coração é grande demais e cabem outras pessoas.
        Por sorte, eu sei de bastante gente que você pode conhecer, assim, quem sabe
        não viramos um grupo de amigos?!''' )
        listaDeAmigos = {}
        amigo = 0
        while amigo != '6':
            oQueFazerAmigos = input('''
            O que deseja fazer?
            1 - Adicionar um novo amigo na listenha;
            2 - Ver a minha lista;
            3 - Ver se alguém está na lista;
            4 - Tirar alguém da lista :(
            5 - Pesquisar o contato pela descrição;
            6 - Parar;
            R:
            ''')
            if oQueFazerAmigos == '1':
                escolha2 = '-Pediu para adicionar algum amigo na lista de amigos'
                historico.append(escolha2)
                amigoParaAdicionar = input("Qual o nome do bebê que você quer//////////////////// adicionar? R: ")
                listaDeAmigos[f"{amigoParaAdicionar}"] = input("Descreva-o com uma palavra, hihi. R: ")
                print("Ótimo, amigo adicionado com sucesso!!")
                print(listaDeAmigos)
            if oQueFazerAmigos == '2':
                escolha2 = '-Pediu que mostrasse a lista de melhores amigos'
                historico.append(escolha2)
                print(f'Essa é a sua listinha! {listaDeAmigos}')
            if oQueFazerAmigos == '3':
                escolha2 = '-Pediu que verificasse alguém na lista de melhores amigos'
                historico.append(escolha2)
                print("Ah, quer ver se alguém está na lista? Ok, vamos lá.")
                amigoParaVerificar = input("Qual amigo deseja verificar? R: ")
                print(listaDeAmigos.get(f'{amigoParaVerificar}', 'Opss! Essa pessoa não está na lista!'))
            if oQueFazerAmigos == '4':
                escolha2 = '-Pediu que tirasse alguém da lista de melhores amigos'
                historico.append(escolha2)
                amigoParaApagar = input("Caramba, desfez a amizade? Que triste. Quem quer tirar da lista? R: ")
                print(listaDeAmigos.pop(f'{amigoParaApagar}', 'Opss! Essa pessoa não está na lista, você não pode excluí-la!!'))
                print(listaDeAmigos)
            if oQueFazerAmigos == '5':
                escolha2 = '-Pediu para verificar um amigo na lista de amigos pela descrição atribuída'
                historico.append(escolha2)
                amigoPelaDescricao = input("Qual a descrição do amigo que quer achar? R: ")
                print(amigoPelaDescricao in listaDeAmigos.values())
            if oQueFazerAmigos == '6':
                break
    if oQueFazer == '5':
        escolha1 = 'Pediu para jogar forca'
        historico.append(escolha1)
        vocabulario = ["harrypotter", "senhordosaneis", "gameofthrones", "ascronicasdenarnia"]
        palavra = choice(vocabulario)

        print("--------- Jogo da Forca -------- ")
        print("Vamos jogar?!")

        chances = 6
        alfabeto = list("abcdefghijklmnopqrstuvwxyz")
        tentativas = []

        dicas = print("DICAS: Grande obra de fantasia, que contém bruxos, magia e criaturas extraordinárias!")

        while True:
            print(tentativas)
            print(f'Você tem {chances} chances.')

            for letra in palavra:
                if letra in tentativas:
                    print(letra,end= ' ')
                else:
                    print(' _ ', end=' ')
    
            palpite = input("Digite seu palpite ou digite 0 para sair: ")

            if palpite == '0':
                break
            elif palpite not in alfabeto or palpite == '':
                print("Opss, isso não é uma letra, bebê.")
                continue
            elif palpite in tentativas:
                print("Não entendi, amor...")
            tentativas.append(palpite)
            if palpite in palavra:
                print("Irra, acertou!!")
            else:
                print("Você errou!")
                chances -= 1
        if chances == 0:
            print("Que pena, parece que você perdeu!")
            break
        elif set(palavra).issubset(set(tentativas)):
            print("Parabéns, você acertou!! Você ganhou!")
            break
    if oQueFazer == '6':
        escolha1 = '-Pediu para sair'
        historico.append(escolha1)
        print(''' Já está indo? Ah, que pena! :(
            Espero que tenha gostado de mim. A gente se vê na próxima!
            ''')
        print(historicoTotal)
        quit()
            