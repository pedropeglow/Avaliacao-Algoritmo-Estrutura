class Veiculo():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  @property
  def marcaVeiculo(self):
    pass

  @marcaVeiculo.setter
  def marcaVeiculo(self, valor):
    pass

  @property
  def modeloVeiculo(self):
    pass

  @modeloVeiculo.setter
  def modeloVeiculo(self, valor):
    pass

  def getInformacoes(self):
    print("-"*28)
    print(f"""
  Marca: {self.marca} 
  Modelo: {self.modelo}
  """)