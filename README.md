# Redes Neurais

## Perceptron

## Conceitos

- Perceptron, ou neurônio artificial é o odelo mais básico de um sistema de aprendizagem, neste caso, linear.
- É um modelo matemático que recebe várias entradas, x1, x2, … e produz uma única saída binária.
- O Perceptron calcula uma soma ponderada das entradas, subtrai um limite e passa um dos dois valores possíveis como resultado.
- É limitado.

## Perceptron

      i = [1,-2,3,4,5,-6]
      w = [6,5,4,-3,2,1]
      def somatoria(entradas=[], pesos=[]):
          soma = 0
          if len(entradas)== 0 or len(pesos)==0:
              return 0
          comb = zip(entradas,pesos)
          for item in comb:
              soma += item[0]*item[1]
          return soma


      def ativacao_step_function(n):
          if n>0:
              return 1
          return 0

      # def novo_peso(n):
      #     return n *

      print(ativacao_step_function(somatoria(i,w)))

## Perceptron com Numpy

      import numpy as np

      taxa_acerto = 0.95
      taxa_aprendizagem = 0.01
      valor = 0
      geracao = 1

      entradas = np.array([-1,7,5,-4,6,5,-10])
      pesos = np.array([0.8,0.1,0,0.02,0.6,-0.74,0.32])
      # pesos = np.array([0.786,0.206,0.076])
      print(entradas)
      print(pesos)
      def soma(e,p):
          return np.dot(e,p)

      def step_function(n):
          if n>=1:
              return 1
          return 0


      def ajuste_peso(e, err, peso, taxa_aprendizagem ):
          return peso + (taxa_aprendizagem*e*err)

      def calc_err(pesos):
          return

      while valor < taxa_acerto:
          print(f'Geração: {geracao}')
          s = soma(entradas, pesos)
          sf = step_function(s)
          print(f'Valor da stepfunction {sf}')
          if sf >= 1:
              print(f'Resultado atingido na geração: {geracao}')
              valor = sf
          else:
              for ind, p in enumerate(pesos):
                  pesos[ind] = ajuste_peso(entradas[ind],0.15, p, taxa_aprendizagem)
                  print(f'Geração {geracao} => Novo peso {ind}: {pesos[ind]}')
              geracao+=1
              if geracao == 1000:
                  break

## Percepeton - Weight adjustment(Ajuste de peso)

      import numpy as np

      taxa_acerto = 0.95
      taxa_aprendizagem = 0.01
      valor = 0
      geracao = 1

      entradas = np.array([0,0],[0,1],[1,0],[1,1])
      pesos = np.array([0,0])
      # pesos = np.array([0.786,0.206,0.076])
      print(entradas)
      print(pesos)
      def soma(e,p):
          return np.dot(e,p)

      def step_function(n):
          if n>=1:
              return 1
          return 0


      def ajuste_peso(e, err, peso, taxa_aprendizagem ):
          return peso + (taxa_aprendizagem*e*err)

      def calc_err(pesos):
          return

      while valor < taxa_acerto:
          print(f'Geração: {geracao}')
          s = soma(entradas, pesos)
          sf = step_function(s)
          print(f'Valor da stepfunction {sf}')
          if sf >= 1:
              print(f'Resultado atingido na geração: {geracao}')
              valor = sf
          else:
              for ind, p in enumerate(pesos):
                  pesos[ind] = ajuste_peso(entradas[ind],0.15, p, taxa_aprendizagem)
                  print(f'Geração {geracao} => Novo peso {ind}: {pesos[ind]}')
              geracao+=1
              if geracao == 1000:
                  break
