Rui Martins
rui@martins.pt

# Configurar Raspberry PI com WiFi, sem usar monitor e teclado.

## Introdução

Um raspberry pi é um computador, na sua board tem um processor, RAM, interfaces USB, interface HDMI, (...) mas que usa um cartão de memória (ou PEN USB) como memória secundária, em vez dos discos rigidos que normalmente são usados nos computadores tradicionais.
Tal como os computadores tradicionais tem que ser configurados com sistema operativo para funcionar, o mesmo se passa com os raspberry pi.

A diferença é que nos computadores tradicionais, usas um DVD ou uma PEN para instalar o sistema operativo no disco rigido do computador (sem remover o disco do computador), mas no raspberry, o sistema operativo é gravado num computador directamente no cartão de memória, e quando se coloca o cartão no raspberry, este está pronto a arrancar o sistema operativo.

O sistema operativo que vamos usar no raspberry pi é o Raspbian.

No entanto, por questões de segurança, por omissão, quando um raspberry arranca o Raspbian, não permite ligações externas, ou seja, não consegues usar ou configurar o raspberry sem lhe ligar um monitor e um teclado.

A solução para este problema está descrita nos proximos passos.

## Descarregar a imagem do sistema operativo.

Existem vários sistemas operativos já pré configurados para serem executados no raspberry, na página oficial podemos encontrar várias alternativas:

![Raspberry PI Operative Systems](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/OS-RPi.png)

No entanto o Raspbian é dos mais utilizados e documentados, com suporte oficial. É um sistema operativo baseado em [Debian](https://www.debian.org/ "Visit Debian website") (Muito semelhante a [Ubuntu](https://www.ubuntu.com/ "Visit Ubuntu website"), [Kali linux](https://www.kali.org/ "Visit Kali linux website"), ...)

Para descarregar a imagem do Raspbian vai à seguinte ligação: [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/ "Download Raspbian") , e descarrega a versão com linha de comandos e ambiente gráfico, ou a versão minimalista, só com linha de comandos e sem abiente gráfico.

No nosso caso, vamos optar pela versão com ambiente gráfico, pois iremos utilizar mais à frente.


![Download Raspbian](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/download-raspbian.png)


## Copiar a imagem para o cartão

## Preparar raspberry para ser acedido e configurado por outro computador

### Ligar SSH

### Ligar VNC

### Ligar WiFi


Não esquecer:
SSH -X
PIL
OpenCV
PWM



