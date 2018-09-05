    Rui Martins, rui@martins.pt [Setembro de 2018]

# Configurar Raspberry PI com WiFi, sem usar monitor e teclado.

## Introdução

![Raspberry PI 3 B+](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/RPi3-B-Plus-intro.jpg)
https://www.waveshare.com/img/devkit/RPi3-B-Plus/RPi3-B-Plus-intro.jpg

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

![Download Raspbian](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/download-raspbian.png)

No nosso caso, vamos optar pela versão com ambiente gráfico, pois iremos utilizar mais à frente.

## Copiar a imagem para o cartão
Após se ter feito download da imagem do sistema operativo, este tem que ser escrito num cartão de memóra.

Vou aqui apresentar várias alternativas para resolver este passo, algumas delas obrigam a primeiro descomprimir o ficheiro com a imagem (ex: `2018-06-27-raspbian-stretch.zip`), outras obrigam a que o cartão de memória seja desmontado do sistema operativo, antes de ser escrito.

### Windows


### Linux


#### Opção 1
* Descomprime o ficheiro `2018-06-27-raspbian-stretch.img` dentro do `2018-06-27-raspbian-stretch.zip`.
* Abre a linha de comandos, executa `lsblk`, verifica que discos `/dev/sdX` existem, insere o cartão de memória e volta a executar `lsblk`, agora vê qual é o novo disco que aparece na lista dos `/dev/sdX`.
* `sudo dd bs=4M if=~/Downloads/2018-06-27-raspbian-stretch.img of=/dev/sdX conv=fsync`
	* `~/Downloads/2018-06-27-raspbian-stretch.img` é o caminho completo da imagem que descomprimiste, o `if` significa `input file`;
	* `/dev/sdX` é o caminho para o cartão de memória, deves substituir o `X` pelo numero correspondente. `of` significa `output file`;
	* **NOTA:** Certifica-te que não estás a escrever para uma unidade USB errada! Se não tens muita prática, remove do PC todos os discos externos, e PENs que não estejas a usar :)
	* Se o `Block Size` estiver a dar erro, tenta `1M` em vez de `4M`. No caso do MacOS X, o `M` pode ter que ser em MAIUSCULA ou minuscula, em função de softwares que possas ter instalado no PC
	* Se quiseres ser mais nerd, e ver o progresso, podes executar o seguinte comando: `(pv -n ~/Downloads/2018-06-27-raspbian-stretch.img | dd of=/dev/sdX bs=4M) 2>&1 | dialog --gauge "A clonar imagem para o cartão, Aguarde pf..." 10 70 0`

### MacOS X
#### Opção 1
* Descomprime o ficheiro `2018-06-27-raspbian-stretch.img` dentro do `2018-06-27-raspbian-stretch.zip`.
* Abre a linha de comandos, executa `diskutil list`, verifica que discos `/dev/diskX` existem, insere o cartão de memória e volta a executar `diskutil list`, agora vê qual é o novo disco que aparece na lista dos `/dev/diskX`.
	* ![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/mac-diskutil.png)
* Desmonta todas as partições desse disco, exemplo: `sudo umount /dev/disk2s1`, `sudo umount /dev/disk2s2`
* `sudo dd bs=4M if=~/Downloads/2018-06-27-raspbian-stretch.img of=/dev/sdX conv=fsync`
	* `~/Downloads/2018-06-27-raspbian-stretch.img` é o caminho completo da imagem que descomprimiste, o `if` significa `input file`;
	* `/dev/sdX` é o caminho para o cartão de memória, deves substituir o `X` pelo numero correspondente. `of` significa `output file`;
	* **NOTA:** Certifica-te que não estás a escrever para uma unidade USB errada! Se não tens muita prática, remove do PC todos os discos externos, e PENs que não estejas a usar :)
	* Se o `Block Size` estiver a dar erro, tenta `1M` em vez de `4M`. No caso do MacOS X, o `M` pode ter que ser em MAIUSCULA ou minuscula, em função de softwares que possas ter instalado no PC
	* Se quiseres ser mais nerd, e ver o progresso, podes executar o seguinte comando: `sudo sh -c '(pv -n ~/Downloads/RaspberryPI-Images/2018-06-27-raspbian-stretch.img | dd of=/dev/disk2 bs=1m) 2>&1 | dialog --gauge "A clonar imagem para o cartão, Aguarde pf..." 10 70 0'`

		* ![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/dd-with-dialog.png)

#### Opção 2
![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/Etcher.png)

## Preparar raspberry para ser acedido e configurado por outro computador

### Ligar SSH
Dentro da partição `/boot`, cria um ficheiro chamado `ssh`, este ficheiro pode estar vazio.

### Ligar VNC

### Ligar WiFi


Não esquecer:
SSH -X
PIL
OpenCV
PWM



