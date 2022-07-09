from Veiculo import Veiculo

class Carro(Veiculo):
  def __init__(self, marca, modelo, portas):
    self.marca = marca
    self.modelo = modelo
    self.__portas = portas

  @property
  def marcaVeiculo(self):
     return self.marca

  @marcaVeiculo.setter
  def marcaVeiculo(self, valor):
     self.marca = valor

  @property
  def modeloVeiculo(self):
     return self.modelo

  @modeloVeiculo.setter
  def modeloVeiculo(self, valor):
     self.modelo = valor

  @property
  def portasVeiculo(self):
     return self.__portas

  @portasVeiculo.setter
  def portasVeiculo(self, valor):
     self.__portas = valor


  def getInformacoes(self):
      super().getInformacoes()
      print(f"""
  Portas: {self.__portas} 
  """)

