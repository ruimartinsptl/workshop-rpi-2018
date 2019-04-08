    Rui Martins, rui@martins.pt [Setembro de 2018]

# Configurar Raspberry PI com WiFi, sem usar monitor e teclado (headless setup).

## <a name="indice"></a>Índice
* [Introdução](#introducao)
* [Pré-Requisitos](#prerequisitos)
* [Descarregar a imagem do sistema operativo](#download_image)
* [Copiar a imagem para o cartão](#clone_image_to_card)
	* [Windows, Linux ou Mac](#clone_image_to_card-windows-linux-mac)
	* [Windows](#clone_image_to_card-windows)
	* [Linux](#clone_image_to_card-linux)
	* [MacOS X](#clone_image_to_card-mac)
* [Preparar raspberry para ser acedido e configurado por outro computador](#prepare_remote)
	* [SSH](#ssh)
	* [Configurar WiFi](#ligar-wifi)
	* [VNC](#vnc)

[Voltar ao Índice](#indice) | [Passo seguinte - Introdução](#introducao)

## <a name="introducao"></a>Introdução

![Raspberry PI 3 B+](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/RPi3-B-Plus-intro.jpg)
https://www.waveshare.com/img/devkit/RPi3-B-Plus/RPi3-B-Plus-intro.jpg

Um raspberry pi é um computador, na sua board tem um processor, RAM, interfaces USB, interface HDMI, (...) mas que usa um cartão de memória (ou PEN USB) como memória secundária, em vez dos discos rigidos que normalmente são usados nos computadores tradicionais.

Tal como os computadores tradicionais tem que ser configurados com sistema operativo para funcionar, o mesmo se passa com os raspberry pi.

A diferença é que nos computadores tradicionais, usas um DVD ou uma PEN para instalar o sistema operativo no disco rigido do computador (sem remover o disco do computador), mas no raspberry, o sistema operativo é gravado num computador directamente no cartão de memória, e quando se coloca o cartão no raspberry, este está pronto a arrancar o sistema operativo.

O sistema operativo que vamos usar no raspberry pi é o Raspbian.

No entanto, por questões de segurança, por omissão, quando um raspberry arranca o Raspbian, este não permite ligações SSH nem VNC externas, ou seja, não consegues usar ou configurar o raspberry sem lhe ligar um monitor e um teclado.

A solução para este problema está descrita nos proximos passos.

[Voltar ao Índice](#indice) | [Passo seguinte - Pré-Requisitos](#prerequisitos)

## <a name="prerequisitos"></a>Pré-Requisitos
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

[Voltar ao Índice](#indice)

[Voltar ao Índice](#indice) | [Passo anterior - Introdução](#introducao) | [Passo seguinte - Pré-Requisitos](#prerequisitos)

## <a name="download_image"></a> Descarregar a imagem do sistema operativo.

Existem vários sistemas operativos já pré configurados para serem executados no raspberry, na página oficial podemos encontrar várias alternativas:

![Raspberry PI Operative Systems](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/OS-RPi.png)

No entanto o Raspbian é dos mais utilizados e documentados, com suporte oficial. É um sistema operativo baseado em [Debian](https://www.debian.org/ "Visit Debian website") (Muito semelhante a [Ubuntu](https://www.ubuntu.com/ "Visit Ubuntu website"), [Kali linux](https://www.kali.org/ "Visit Kali linux website"), ...)

Para descarregar a imagem do Raspbian vai à seguinte ligação: [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/ "Download Raspbian") , e descarrega a versão com linha de comandos e ambiente gráfico, ou a versão minimalista, só com linha de comandos e sem abiente gráfico.

![Download Raspbian](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/download-raspbian.png)

No nosso caso, vamos optar pela versão com ambiente gráfico, pois iremos utilizar mais à frente.

[Voltar ao Índice](#indice)

## <a name="clone_image_to_card"></a>Copiar a imagem para o cartão
Após se ter feito download da imagem do sistema operativo, este tem que ser escrito num cartão de memóra.

Vou aqui apresentar várias alternativas para resolver este passo, algumas delas obrigam a primeiro descomprimir o ficheiro com a imagem (ex: `2018-06-27-raspbian-stretch.zip`), outras obrigam a que o cartão de memória seja desmontado do sistema operativo, antes de ser escrito.

### <a name="clone_image_to_card-windows-linux-mac"></a>Windows, linux, ou mac

#### Etcher [solução muito fácil]
A forma mais facil de se clonar a imagem para um cartão de memória é atravez do [Etcher](https://etcher.io/ "Visit Etcher website").

![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/Etcher.png)

Após a imagem ter sido copiada para o cartão, o cartão é desmontado automáticamente, deverás remover o cartão e voltar a colocar, para que seja montada a partição de `/boot` e poderes assim continuar as configurações de SSH, etc...

[Voltar ao Índice](#indice)


### <a name="clone_image_to_card-windows"></a>Windows

Recomendo a utilização do [Etcher](https://etcher.io/ "Visit Etcher website"), no entanto, também é muito utilizado o [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/), que é semelhante ao [Etcher](https://etcher.io/ "Visit Etcher website")

[Voltar ao Índice](#indice)

### <a name="clone_image_to_card-linux"></a>Linux

#### Linha de comandos
* Descomprime o ficheiro `2018-06-27-raspbian-stretch.img` dentro do `2018-06-27-raspbian-stretch.zip`.
* Abre a linha de comandos, executa `lsblk`, verifica que discos `/dev/sdX` existem, insere o cartão de memória e volta a executar `lsblk`, agora vê qual é o novo disco que aparece na lista dos `/dev/sdX`.
* Desmonta todas as partições desse disco.
* `sudo dd bs=4M if=~/Downloads/2018-06-27-raspbian-stretch.img of=/dev/sdX conv=fsync`
	* `~/Downloads/2018-06-27-raspbian-stretch.img` é o caminho completo da imagem que descomprimiste, o `if` significa `input file`;
	* `/dev/sdX` é o caminho para o cartão de memória, deves substituir o `X` pelo numero correspondente. `of` significa `output file`;
	* **NOTA:** Certifica-te que não estás a escrever para uma unidade USB errada! Se não tens muita prática, remove do PC todos os discos externos, e PENs que não estejas a usar :)
	* Se o `Block Size` estiver a dar erro, tenta `1M` em vez de `4M`. No caso do MacOS X, o `M` pode ter que ser em MAIUSCULA ou minuscula, em função de softwares que possas ter instalado no PC
	* Se quiseres ser mais nerd, e ver o progresso, podes executar o seguinte comando: `(pv -n ~/Downloads/2018-06-27-raspbian-stretch.img | dd of=/dev/sdX bs=4M) 2>&1 | dialog --gauge "A clonar imagem para o cartão, Aguarde pf..." 10 70 0`

[Voltar ao Índice](#indice)

### <a name="clone_image_to_card-mac"></a>MacOS X

#### Linha de comandos

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

[Voltar ao Índice](#indice)

## <a name="prepare_remote"></a>Preparar raspberry para ser acedido e configurado por outro computador
Neste momento o cartão de memória estaria pronto para ir para o raspberry, caso tivesses monitor e teclado.
Como não é o caso, vamos agora preparar o sistema operativo para que permita ligações externas e para que se ligue ao WiFi

### Preparar raspberry para servir SSH

Para acederes por SSH ao raspberry, basta que no cartão, dentro da partição chamada `boot`, cries um ficheiro chamado `ssh`, este ficheiro pode estar vazio. O Raspbian ao arrancar, irá detectar a presença desse ficheiro como sendo um pedido para ligar o protocolo de SSH.

![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/slash_boot.png)

Caso prefiras criar o ficheiro pela linha de comandos em linux ou mac, podes usar o comando `touch ssh`.

![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/touch_ssh.png)

A partir deste momento, já podes aceder ao teu raspberry a partir de outro computador na mesma rede, mas ainda estás limitado, só funcionará se tiveres o raspberry ligado por cabo de rede.

Caso pretendas aceder ao raspberry a partir da rede wifi, tens que configurar o passo [**Ligar WiFi** ](#ligar-wifi)

Nota: Se pretenderes executar aplicações com ambiente gráfico por SSH, deves executar o comando `ssh` com o parametro `-X`. Iremos demonstrar mais à frente.

[Voltar ao Índice](#indice)

### <a name="ligar-wifi"></a>Ligar WiFi

Para que o teu raspberry se ligue automáticamente à rede wifi, é preciso também configurar na partição `/boot` do cartão um ficheiro com o nome `wpa_supplicant.conf`

(Se preferires criar o ficheiro pela linha de comandos do linux ou mac, podes usar o seguinte comando: `nano wpa_supplicant.conf`)

Dentro do ficheiro, deves colocar o seguinte conteúdo:

```
country=PT
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="workshop8"
    psk="password"
    key_mgmt=WPA-PSK
}
```

Agora sim, se ejectares o cartão e o colocares no raspberry, este irá ligar-se automáticamente à rede WiFi.

[Voltar ao Índice](#indice)

### Descobrir IP do raspberry
Se o raspberry não estiver configurado com IP estático, mas sim com DHCP, e não soubermos qual é o IP que lhe vai ser atribuído quando se ligar à rede, podemos usar ferramentas de pesquisa de IPs, como o [AngryIP Scanner](https://angryip.org/download), LanScan Pro, etc...

![Angry-IP-Scanner](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/Angry-IP-Scanner.png)

![LanScan Pro](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/LanScanPro.png)

[Voltar ao Índice](#indice)

### Ligar por SSH

#### Windows
No windows podes usar o [Putty](https://www.putty.org/)
**TODO: Colocar imagem**

**Nota:** Podemos redireccionar as janelas do ambiente gráfico para o nosso computador, no entanto precisamos de instalar um XServer, e activar a opção de `X11 forewarding` no putty:

https://sourceforge.net/projects/xming/

Exemplo de uma aplicação que está instalada no raspberry, mas a janela está a ser mostrada no windows:

![Chromium a correr no Raspberry](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/chromium-ssh-windows.png)


#### Linux e Mac OS
Por linha de comandos executa o seguinte comando:
`ssh <nome de utilizador>@<ip dp raspberry>`

Ex: `ssh pi@10.79.72.107`


**Nota:** Podemos redireccionar as janelas do ambiente gráfico para o nosso computador, adicionar `-X` ao comando ssh

[Voltar ao Índice](#indice)

### Transferir ficheiros por SCP
`scp <user>@<ip>:<path> <path>`

`scp <path> <user>@<ip>:<path>`

### Transferir ficheiros por SFTP
Instalar o [Filezilla](https://filezilla-project.org), e criar uma nova ligação SFTP.

![](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/Filezilla-1.png)

![](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/Filezilla-2.png)

### Ligar VNC
Se te for mais conveniente, podes utilizar o protocolo VNC para interagir com o raspberry, para isso, tens que primeiro activar o protocolo de VNC.

Para activar o protocolo de VNC, vais executar o comando `sudo raspi-config` escolher a opção `5 Interfacing Options` e depois `enable` em `P3 VNC`.

No teu computador deves instalar o UltraVNC Client a partir deste link: [https://www.realvnc.com/en/connect/download/viewer](https://www.realvnc.com/en/connect/download/viewer)

![Chromium a correr no Raspberry](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/UltraVNC-1.png)

![Chromium a correr no Raspberry](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/UltraVNC-2.png)

No MacOS não precisas de instalar o UltraVNC, podes usar directamente a ferramenta de partilhad e ecrã que acompanha o sistema operativo. (TODO: Completar)

[Voltar ao Índice](#indice)

# Algumas configurações iniciais
`sudo rpi-update # Updating firmware [Opcional]`

`sudo reboot # (Se tiver sido executado o rpi-update)`

```
# ldconfig is a program that is used to maintain the shared library cache.
# This cache is typically stored in the file /etc/ld.so.cache and is used by
# the system to map a shared library name to the location of the corresponding
sudo ldconfig
```

`sudo raspi-config`

![raspi-config](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/raspi-config.png)

* Expand File Sistem
* Update
* Locale
* Boot Options -> DESKTOP
* Video Memory
* Output Audio
* ...

**NOTA:**
O raspi-config pode ser configurado apenas por linha de comandos, sem precisar de interação humana. Seguem aqui alguns exemplos de como o fazer:

`sudo raspi-config nonint do_wifi_country PT`
`sudo raspi-config nonint do_hostname rpi-demo`

Mais informações: [https://github.com/RPi-Distro/raspi-config/blob/master/raspi-config](https://github.com/RPi-Distro/raspi-config/blob/master/raspi-config)


# Outros:

`sudo apt-get install -y vim` # Editor

`sudo apt-get install -y eog` # Visualizar imagens

`sudo apt-get install screen` # Deixar aplicações em execução quando se fecha a ligação SSH

`sudo apt-get install htop` #

# Remover programas que não fazem falta:
`sudo apt-get purge wolfram-engine`

`sudo apt-get purge libreoffice* `

`sudo apt-get clean`

`sudo apt-get autoremove`



# Instalar OpenCV

## OpenCV 2.x
`sudo apt-get install -y libopencv-dev python-dev python-opencv python-numpy`

## OpenCV 3.x
`TODO: Documentr aqui`

# Processar imagens
## O que é uma imagem
![raspi-config](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/MatBasicImageForComputer.jpg)

![raspi-config](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/RGB-matrix.png)




# Não esquecer de adicionar ao guião:

SSH com Chave Publica || ssh-copy-id pi@123.213.123.123

SSH Greating



PIL

OpenCV

PWM



