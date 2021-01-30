from pixtendv2l import PiXtendV2L  # wczytanie biblioteki
p = PiXtendV2L()                   # stworzenie instancji obiektu sterującego
p.digital_out0 = p.ON              # zmienienie stanu wyjścia DO0 na wysoki
p.close()                          # zamkniecie połączenia z sterownikiem
del p                              # usuniecie obiektu sterującego 
