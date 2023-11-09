import wx

def calcular_imc(peso, altura):
  return peso / ((altura / 100) ** 2)

def classificar_imc(imc):
  if imc < 18.5:
    return "Abaixo do peso", wx.BLACK
  elif imc < 24.9:
    return "Peso normal", wx.BLACK
  elif imc < 29.9:
    return "Sobrepeso", wx.BLACK
  elif imc < 34.9:
    return "Obesidade grau 1", wx.RED
  elif imc < 39.9:
    return "Obesidade grau 2", wx.RED
  else:
    return "Obesidade grau 3", wx.RED

class MyFrame(wx.Frame):

  def __init__(self, parent):
    super().__init__(parent, title="Calculadora de IMC", style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
    self.SetSize((400, 300))
    self.Centre()

    self.panel = wx.Panel(self)
    self.panel.SetBackgroundColour(wx.WHITE)

    self.nome_label = wx.StaticText(self.panel, label="Nome:")
    self.nome_text = wx.TextCtrl(self.panel)

    self.endereco_label = wx.StaticText(self.panel, label="Endereço:")
    self.endereco_text = wx.TextCtrl(self.panel)

    self.peso_label = wx.StaticText(self.panel, label="Peso (kg):")
    self.peso_text = wx.TextCtrl(self.panel)

    self.altura_label = wx.StaticText(self.panel, label="Altura (cm): (ex: 175)")
    self.altura_text = wx.TextCtrl(self.panel)

    self.calcular_button = wx.Button(self.panel, label="Calcular")
    self.calcular_button.Bind(wx.EVT_BUTTON, self.on_calcular)

    self.reiniciar_button = wx.Button(self.panel, label="Reiniciar")
    self.reiniciar_button.Bind(wx.EVT_BUTTON, self.on_reiniciar)

    self.resultado_label = wx.StaticText(self.panel, label="Seu IMC é:")

    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.sizer.Add(self.nome_label, 0, wx.ALIGN_CENTER)
    self.sizer.Add(self.nome_text, 0, wx.EXPAND)
    self.sizer.Add(self.endereco_label, 0, wx.ALIGN_CENTER)
    self.sizer.Add(self.endereco_text, 0, wx.EXPAND)
    self.sizer.Add(self.peso_label, 0, wx.ALIGN_CENTER)
    self.sizer.Add(self.peso_text, 0, wx.EXPAND)
    self.sizer.Add(self.altura_label, 0, wx.ALIGN_CENTER)
    self.sizer.Add(self.altura_text, 0, wx.EXPAND)
    self.sizer.Add(self.calcular_button, 0, wx.ALIGN_CENTER)
    self.sizer.Add(self.reiniciar_button, 0, wx.ALIGN_CENTER)
    self.sizer.Add(self.resultado_label, 0, wx.ALIGN_CENTER)

    self.panel.SetSizer(self.sizer)

  def on_calcular(self, event):
    peso = float(self.peso_text.GetValue().replace(',', '.'))
    altura = float(self.altura_text.GetValue().replace(',', '.'))
    imc = calcular_imc(peso, altura)
    classificacao, cor = classificar_imc(imc)
    self.resultado_label.SetLabel("Seu IMC é: {:.2f} ({})".format(imc, classificacao))
    self.resultado_label.SetForegroundColour(cor)

  def on_reiniciar(self, event):
    self.nome_text.SetValue("")
    self.endereco_text.SetValue("")
    self.peso_text.SetValue("")
    self.altura_text.SetValue("")
    self.resultado_label.SetLabel("Seu IMC é:")
    self.resultado_label.SetForegroundColour(wx.BLACK)

if __name__ == "__main__":
  app = wx.App()
  frame = MyFrame(None)
  frame.Show()
  app.MainLoop()
