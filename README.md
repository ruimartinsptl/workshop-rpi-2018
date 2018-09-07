    Rui Martins, rui@martins.pt [Setembro de 2018]

# Configurar Raspberry PI com WiFi, sem usar monitor e teclado.

## <a name="indice"></a>Indice
* [Introdução](#introducao)
* [Pré-Requisitos](#prerequisitos)
* [Descarregar a imagem do sistema operativo](#download_image)
* [Copiar a imagem para o cartão](#clone_image_to_card)
	* [Windows](#clone_image_to_card-windows)
	* [Linux](#clone_image_to_card-linux)
	* [MacOS X](#clone_image_to_card-mac)
* [Preparar raspberry para ser acedido e configurado por outro computador](#prepare_remote)
	* [SSH](#ssh)
	* [Configurar WiFi](#ligar-wifi)
	* [VNC](#vnc)

[Voltar ao indice](#indice)

## <a name="introducao"></a>Introdução

![Raspberry PI 3 B+](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/RPi3-B-Plus-intro.jpg)
https://www.waveshare.com/img/devkit/RPi3-B-Plus/RPi3-B-Plus-intro.jpg

Um raspberry pi é um computador, na sua board tem um processor, RAM, interfaces USB, interface HDMI, (...) mas que usa um cartão de memória (ou PEN USB) como memória secundária, em vez dos discos rigidos que normalmente são usados nos computadores tradicionais.

Tal como os computadores tradicionais tem que ser configurados com sistema operativo para funcionar, o mesmo se passa com os raspberry pi.

A diferença é que nos computadores tradicionais, usas um DVD ou uma PEN para instalar o sistema operativo no disco rigido do computador (sem remover o disco do computador), mas no raspberry, o sistema operativo é gravado num computador directamente no cartão de memória, e quando se coloca o cartão no raspberry, este está pronto a arrancar o sistema operativo.

O sistema operativo que vamos usar no raspberry pi é o Raspbian.

No entanto, por questões de segurança, por omissão, quando um raspberry arranca o Raspbian, este não permite ligações SSH nem VNC externas, ou seja, não consegues usar ou configurar o raspberry sem lhe ligar um monitor e um teclado.

A solução para este problema está descrita nos proximos passos.

[Voltar ao indice](#indice)

## <a name="prerequisitos"></a>Pré-Requisitos
Hardware:

* Raspberry Pi (1, 2, ou 3)
* PSU (Alimentador electrico de preferencia com 2A, podem usar a do telemovel)
* Cartão de memória SD ou micro SD (com 8Gb ou mais)
* Pen Wifi (caso o Raspberry Pi não tenha wifi integrado)

Software:

* Windows:
	* Putty ou software semelhante
* Linux:
	* 
* MacOS X:
	* Etcher (Opcional)
	* Lan Scan ou software semelhante (Opcional)

Outros:

* Bash (Não obrigatório)
* Python 3 (Não obrigatório)

[Voltar ao indice](#indice)

## <a name="download_image"></a> Descarregar a imagem do sistema operativo.

Existem vários sistemas operativos já pré configurados para serem executados no raspberry, na página oficial podemos encontrar várias alternativas:

![Raspberry PI Operative Systems](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/OS-RPi.png)

No entanto o Raspbian é dos mais utilizados e documentados, com suporte oficial. É um sistema operativo baseado em [Debian](https://www.debian.org/ "Visit Debian website") (Muito semelhante a [Ubuntu](https://www.ubuntu.com/ "Visit Ubuntu website"), [Kali linux](https://www.kali.org/ "Visit Kali linux website"), ...)

Para descarregar a imagem do Raspbian vai à seguinte ligação: [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/ "Download Raspbian") , e descarrega a versão com linha de comandos e ambiente gráfico, ou a versão minimalista, só com linha de comandos e sem abiente gráfico.

![Download Raspbian](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/download-raspbian.png)

No nosso caso, vamos optar pela versão com ambiente gráfico, pois iremos utilizar mais à frente.

[Voltar ao indice](#indice)

## <a name="clone_image_to_card"></a>Copiar a imagem para o cartão
Após se ter feito download da imagem do sistema operativo, este tem que ser escrito num cartão de memóra.

Vou aqui apresentar várias alternativas para resolver este passo, algumas delas obrigam a primeiro descomprimir o ficheiro com a imagem (ex: `2018-06-27-raspbian-stretch.zip`), outras obrigam a que o cartão de memória seja desmontado do sistema operativo, antes de ser escrito.

### <a name="clone_image_to_card-windows"></a>Windows

[Voltar ao indice](#indice)

### <a name="clone_image_to_card-linux"></a>Linux


#### Opção 1 - Linha de comandos
* Descomprime o ficheiro `2018-06-27-raspbian-stretch.img` dentro do `2018-06-27-raspbian-stretch.zip`.
* Abre a linha de comandos, executa `lsblk`, verifica que discos `/dev/sdX` existem, insere o cartão de memória e volta a executar `lsblk`, agora vê qual é o novo disco que aparece na lista dos `/dev/sdX`.
* Desmonta todas as partições desse disco.
* `sudo dd bs=4M if=~/Downloads/2018-06-27-raspbian-stretch.img of=/dev/sdX conv=fsync`
	* `~/Downloads/2018-06-27-raspbian-stretch.img` é o caminho completo da imagem que descomprimiste, o `if` significa `input file`;
	* `/dev/sdX` é o caminho para o cartão de memória, deves substituir o `X` pelo numero correspondente. `of` significa `output file`;
	* **NOTA:** Certifica-te que não estás a escrever para uma unidade USB errada! Se não tens muita prática, remove do PC todos os discos externos, e PENs que não estejas a usar :)
	* Se o `Block Size` estiver a dar erro, tenta `1M` em vez de `4M`. No caso do MacOS X, o `M` pode ter que ser em MAIUSCULA ou minuscula, em função de softwares que possas ter instalado no PC
	* Se quiseres ser mais nerd, e ver o progresso, podes executar o seguinte comando: `(pv -n ~/Downloads/2018-06-27-raspbian-stretch.img | dd of=/dev/sdX bs=4M) 2>&1 | dialog --gauge "A clonar imagem para o cartão, Aguarde pf..." 10 70 0`

[Voltar ao indice](#indice)

### <a name="clone_image_to_card-mac"></a>MacOS X

#### Opção 1 - Linha de comandos [solução avançado]

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

[Voltar ao indice](#indice)

#### Opção 2 - Etcher [solução muito fácil]
A forma mais facil de se clonar a imagem para um cartão de memória num MacBook é atravez do [Etcher](https://etcher.io/ "Visit Etcher website"). Não é preciso descomprimir o `zip`, nem é preciso desmontar o cartão de memória previamente.

![diskutil list](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/Etcher.png)

Após a imagem ter sido copiada para o cartão, o cartão é desmontado automáticamente, deverás remover o cartão e voltar a colocar, para que seja montada a partição de `/boot` e poderes assim continuar as configurações de SSH, etc...

[Voltar ao indice](#indice)

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

[Voltar ao indice](#indice)

### <a name="ligar-wifi"></a>Ligar WiFi

Para que o teu raspberry se ligue automáticamente à rede wifi, é preciso também configurar na partição `/boot` do cartão um ficheiro com o nome `wpa_supplicant.conf`

(Se preferires criar o ficheiro pela linha de comandos do linux ou mac, podes usar o seguinte comando: `nano wpa_supplicant.conf`)

Dentro do ficheiro, deves colocar o seguinte conteúdo:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="workshop8"
    psk="password"
    key_mgmt=WPA-PSK
}
```

Agora sim, se ejectares o cartão e o colocares no raspberry, este irá ligar-se automáticamente à rede WiFi.

[Voltar ao indice](#indice)

### Descobrir IP do raspberry
TODO: Inserir imagens LanScan Pro

[Voltar ao indice](#indice)

### Ligar por SSH

`ssh pi@10.79.72.107`

[Voltar ao indice](#indice)

### Ligar VNC

[Voltar ao indice](#indice)

# O que executar na primeira utilização do raspberry
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

# shared library file


sudo apt-get install -y vim
sudo apt-get install -y eog


# Não esquecer de adicionar ao guião:
SSH -X

PIL

OpenCV

PWM



