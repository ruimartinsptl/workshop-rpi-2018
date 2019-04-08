    Rui Martins, rui@martins.pt [Setembro de 2018]

# Workshop - Raspberry Pi: Introdução, Visão por Computador e GPIOs

## <a name="indice"></a>Indice
* [Introdução](#introducao)
* [Pré-Requisitos para o workshop](#prerequisitos)
* [1ª parte: Configurar Raspberry PI com WiFi, sem usar monitor e teclado (headless setup)](#parte1)
* [2ª parte: Visão por computador num Raspberry PI com Python e OpenCV](#parte2)
* [3ª parte: Configuração de GPIOs](#parte3)
* [Mini-Projecto](#projecto)

[Voltar ao indice](#indice) | [Passo seguinte - Introdução](#introducao)

## <a name="introducao"></a>Introdução

![Raspberry PI 3 B+](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/RPi3-B-Plus-intro.jpg)
https://www.waveshare.com/img/devkit/RPi3-B-Plus/RPi3-B-Plus-intro.jpg

Um raspberry pi é um computador, na sua board tem um processor, RAM, interfaces USB, interface HDMI, (...) mas que usa um cartão de memória (ou PEN USB) como memória secundária, em vez dos discos rigidos que normalmente são usados nos computadores tradicionais.

Tal como os computadores tradicionais tem que ser configurados com sistema operativo para funcionar, o mesmo se passa com os raspberry pi.

A diferença é que nos computadores tradicionais, usas um DVD ou uma PEN para instalar o sistema operativo no disco rigido do computador (sem remover o disco do computador), mas no raspberry, o sistema operativo é gravado num computador directamente no cartão de memória, e quando se coloca o cartão no raspberry, este está pronto a arrancar o sistema operativo.

O sistema operativo que vamos usar no raspberry pi é o Raspbian.

No entanto, por questões de segurança, por omissão, quando um raspberry arranca o Raspbian, este não permite ligações SSH nem VNC externas, ou seja, não consegues usar ou configurar o raspberry sem lhe ligar um monitor e um teclado.

A solução para este problema está descrita nos proximos passos.

[Voltar ao indice](#indice) | [Passo seguinte - Pré-Requisitos](#prerequisitos)

## <a name="prerequisitos"></a>Pré-Requisitos para o workshop
Hardware:

* Raspberry Pi (1, 2, ou 3)
* PSU (Alimentador electrico de preferencia com 2A, podem usar a do telemovel)
* Cartão de memória SD ou micro SD (com 8Gb ou mais)
* Pen Wifi (caso o Raspberry Pi não tenha wifi integrado)

Software:

* Windows:
	* Etcher ou Win32DiskImager
	* Putty
	* xming
	* FileZilla
	* Ultra VNC
* Linux:
	* Etcher (Opcional)
	* FileZilla
	* Ultra VNC
* MacOS X:
	* Etcher (Opcional)
	* Lan Scan ou software semelhante (Opcional)
	* FileZilla
	* Ultra VNC

Outros:

* Bash (Não obrigatório)
* Python 3 (Não obrigatório)

[Voltar ao indice](#indice)


## <a name="parte1"></a>1ª parte: Configurar Raspberry PI com WiFi, sem usar monitor e teclado (headless setup).

[Voltar ao indice](#indice)


## <a name="parte2"></a>2ª parte: Visão por computador num Raspberry PI com Python e OpenCV

[Voltar ao indice](#indice)

## <a name="parte3"></a>3ª parte: Configuração de GPIOs

[Voltar ao indice](#indice)


## <a name="projecto"></a>Mini-projecto

[Voltar ao indice](#indice)

# Não esquecer de adicionar ao guião:

SSH com Chave Publica || ssh-copy-id pi@123.213.123.123

SSH Greating



PIL

OpenCV

PWM



