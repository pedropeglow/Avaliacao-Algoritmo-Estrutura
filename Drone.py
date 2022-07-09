from Veiculo import Veiculo

class Drone(Veiculo):
  def __init__(self, marca, modelo, qtdeHelices):
    self.marca = marca
    self.modelo = modelo
    self._qtdeHelices = qtdeHelices

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
     return self._qtdeHelices

  @portasVeiculo.setter
  def portasVeiculo(self, valor):
     self._qtdeHelices = valor


  def getInformacoes(self):
      super().getInformacoes()
      print(f"""
  Quantidade de Hélices: {self._qtdeHelices} 
  """)

