    Rui Martins, rui@martins.pt [Setembro de 2018]

# Configurar Raspberry PI com WiFi, sem usar monitor e teclado (headless setup).

## <a name="indice"></a>Índice
* [Introdução](#introducao)
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

![Raspberry PI 3 B+](/img/RPi3-B-Plus-intro.jpg)

_https://www.waveshare.com/img/devkit/RPi3-B-Plus/RPi3-B-Plus-intro.jpg_

Um raspberry pi é um computador, na sua board tem um processor, RAM, interfaces USB, interface HDMI, (...) mas que usa um cartão de memória (ou PEN USB) como memória secundária, em vez dos discos rigidos que normalmente são usados nos computadores tradicionais.

Tal como os computadores tradicionais tem que ser configurados com sistema operativo para funcionar, o mesmo se passa com os raspberry pi.

A diferença é que nos computadores tradicionais, usas um DVD ou uma PEN para instalar o sistema operativo no disco rigido do computador (sem remover o disco do computador), mas no raspberry, o sistema operativo é gravado num computador directamente no cartão de memória, e quando se coloca o cartão no raspberry, este está pronto a arrancar o sistema operativo.

O sistema operativo que vamos usar no raspberry pi é o Raspbian.

No entanto, por questões de segurança, por omissão, quando um raspberry arranca o Raspbian, este não permite ligações SSH nem VNC externas, ou seja, não consegues usar ou configurar o raspberry sem lhe ligar um monitor e um teclado.

A solução para este problema está descrita nos proximos passos.


[Voltar ao Índice](#indice) | [Passo anterior - Introdução](#introducao) | [Passo seguinte - Descarregar imagem](#download_image)

## <a name="download_image"></a> Descarregar a imagem do sistema operativo.

Existem vários sistemas operativos já pré configurados para serem executados no raspberry, na página oficial podemos encontrar várias alternativas:

![Raspberry PI Operative Systems](/img/OS-RPi.png)

No entanto o Raspbian é dos mais utilizados e documentados, com suporte oficial. É um sistema operativo baseado em 
[Debian](https://www.debian.org/ "Visit Debian website") (Muito semelhante a 
[Ubuntu](https://www.ubuntu.com/ "Visit Ubuntu website"), 
[Kali linux](https://www.kali.org/ "Visit Kali linux website"),
[MX Linux](https://mxlinux.org/ "Visit MX Linux website"),
[AV Linux](http://www.bandshed.net/avlinux/),
[KNOPPIX](http://www.knopper.net/knoppix/index-en.html "Visit KNOPPIX website"),
[Pure OS](https://pureos.net/ "Visit Pure OS website"),
 ...)

Para descarregar a imagem do Raspbian vai à seguinte ligação: 
[https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/ "Download Raspbian"),
e descarrega a versão com linha de comandos e ambiente gráfico, ou a versão minimalista só com linha de comandos
e sem ambiente gráfico.

![Download Raspbian](/img/download-raspbian.png)

**No nosso caso, vamos optar pela versão com ambiente gráfico**, pois iremos utilizar mais à frente uma ligação VNC.

[Voltar ao Índice](#indice)

## <a name="clone_image_to_card"></a>Copiar a imagem para o cartão
Após se ter feito download da imagem do sistema operativo, este tem que ser escrito num cartão de memóra.

Vou aqui apresentar várias alternativas para resolver este passo, algumas delas obrigam a primeiro descomprimir o ficheiro com a imagem (ex: `2018-06-27-raspbian-stretch.zip`), outras obrigam a que o cartão de memória seja desmontado do sistema operativo, antes de ser escrito.

### <a name="clone_image_to_card-windows-linux-mac"></a>Windows, linux, e mac

#### Etcher [solução muito fácil]
A forma mais facil de se clonar a imagem para um cartão de memória é atravez do [Etcher](https://etcher.io/ "Visit Etcher website").

![etcher](/img/Etcher.png)

Após a imagem ter sido copiada para o cartão, o cartão é desmontado automáticamente, deverás remover o cartão
e voltar a colocar no computador, para que seja montada a partição de `/boot` e poderes assim continuar as
configurações de SSH, wifi, etc...

[Voltar ao Índice](#indice) | [Passo anterior - Descarregar imagem](#download_image) | [Preparar SSH, wifi, ...](#preparar-raspberry-para-ser-acedido-e-configurado-por-outro-computador)


### <a name="clone_image_to_card-windows"></a>Windows

Recomendo a utilização do [Etcher](https://etcher.io/ "Visit Etcher website"), no entanto, também é muito utilizado o [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/), que é semelhante ao [Etcher](https://etcher.io/ "Visit Etcher website")

[Voltar ao Índice](#indice) | [Passo anterior - Descarregar imagem](#download_image) | [Preparar SSH, wifi, ...](#preparar-raspberry-para-ser-acedido-e-configurado-por-outro-computador)

### <a name="clone_image_to_card-linux"></a>Linux e MacOS X

#### Linha de comandos

* Descomprime o ficheiro `2018-06-27-raspbian-stretch.img` dentro do `2018-06-27-raspbian-stretch.zip`.
* Abre a linha de comandos, executa `lsblk`[linux] ou `diskutil list`[mac], verifica que discos `/dev/sdX`[linux] 
`/dev/diskX` [mac] existem, insere o cartão de memória e volta a executar `lsblk`/`diskutil list`, agora vê
qual é o novo disco que aparece na lista dos `/dev/sdX`/`/dev/diskX`, será onde pretender gravar a imagem.

![diskutil list](/img/mac-diskutil.png)

* Desmonta todas as partições desse disco, exemplo: `sudo umount /dev/disk2s1`, `sudo umount /dev/disk2s2`
* `sudo dd bs=4M if=~/Downloads/2018-06-27-raspbian-stretch.img of=/dev/sdX conv=fsync`
	* `~/Downloads/2018-06-27-raspbian-stretch.img` é o caminho completo da imagem que descomprimiste, o `if` significa `input file`;
	* `/dev/sdX` é o caminho para o cartão de memória, deves substituir o `X` pelo numero correspondente. `of` significa `output file`;
	* **NOTA:** Certifica-te que não estás a escrever para uma unidade USB errada! Se não tens muita prática, remove do PC todos os discos externos, e PENs que não estejas a usar :)
	* Se o `Block Size` estiver a dar erro, tenta `1M` em vez de `4M`. No caso do MacOS X, o `M` pode ter que ser em **MAIUSCULA** ou **minuscula**, em função de softwares que eventualmente tenhas instalado no PC
	* Se quiseres ser mais nerd, e ver o progresso, podes executar o seguinte comando: `sudo sh -c '(pv -n ~/Downloads/RaspberryPI-Images/2018-06-27-raspbian-stretch.img | dd of=/dev/disk2 bs=1m) 2>&1 | dialog --gauge "A clonar imagem para o cartão, Aguarde pf..." 10 70 0'`

![dd](/img/dd-with-dialog.png)

[Voltar ao Índice](#indice) | [Passo anterior - Descarregar imagem](#download_image) | [Preparar SSH, wifi, ...](#preparar-raspberry-para-ser-acedido-e-configurado-por-outro-computador)

## <a name="prepare_remote"></a>Preparar raspberry para ser acedido e configurado por outro computador
Neste momento o cartão de memória estaria pronto para ir para o raspberry, caso tivesses monitor e teclado.
Como não é o caso, vamos agora preparar o sistema operativo para que permita ligações externas e para que se ligue ao WiFi automáticamente.

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

(Testado no raspberry pi 1, 2, 3 e 4)
```
country=PT
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

network={
    ssid="nome_da_rede"
    psk="password_do_wifi"
    key_mgmt=WPA-PSK
}
```

Agora sim, se ejectares o cartão e o colocares no raspberry, este irá ligar-se automáticamente à rede WiFi.

[Voltar ao Índice](#indice)

### Descobrir IP do raspberry
Se o raspberry não estiver configurado com IP estático, mas sim com DHCP, 
e não soubermos qual é o IP que lhe vai ser atribuído quando se ligar à rede, 
podemos usar ferramentas de pesquisa de IPs, como o 
[AngryIP Scanner](https://angryip.org/download), 
[LanScan](https://itunes.apple.com/pt/app/lanscan/id472226235?l=en&mt=12), 
etc...

![Angry-IP-Scanner](/img/Angry-IP-Scanner.png)

![LanScan](/img/LanScanPro.png)

[Voltar ao Índice](#indice)

### Ligar por SSH

**Nota:** Por omissão o nome de utilizador e password do raspbian são `pi` e `raspberry`.

#### Windows
No windows podes usar o [Putty](https://www.putty.org/), faz download aqui: [https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

![putty](https://www.digitalocean.com/docs/images/droplets/putty/connect-config.4975aa1eead2990cb1a558981f5d7bbad22706a010a5651478c3b98a00001f87.png)

**Nota:** Podemos redireccionar as janelas do ambiente gráfico para o nosso computador, no entanto precisamos de instalar um XServer (como o xming), e activar a opção de `X11 forewarding` no putty:

xming: [https://sourceforge.net/projects/xming/](https://sourceforge.net/projects/xming/)

!(X11 forewarding)[https://i.stack.imgur.com/B7r4t.png]

Exemplo de uma aplicação que está instalada no raspberry, mas a janela está a ser mostrada no windows:

![Chromium a correr no Raspberry](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/chromium-ssh-windows.png)


#### Linux e Mac OS
Por linha de comandos executa o seguinte comando:
`ssh <nome de utilizador>@<ip dp raspberry>`

Ex: `ssh pi@10.79.72.107`

**Nota 1:** Para evitar que em cada ligação nos seja pedida a password, podemos fazer 
autenticação com chaves publicas/privadas. Para tal basta executarmos o seguinte comando: 
`ssh-copy-id <nome de utilizador>@<ip dp raspberry>`.

**Nota 2:** Podemos redireccionar as janelas do ambiente gráfico para o nosso computador, adicionar `-X` ao comando ssh. Ex: `ssh -X pi@10.79.72.107` (experimenta depois executa por exemplo `chromium-browser` no terminal para abrires o google chrome no raspberry, mas com interface gráfica no teu computador). No caso dos Mac OS, também precisam de um Xserver, como o [XQuartz](https://www.xquartz.org/)

[Voltar ao Índice](#indice)

### Transferir ficheiros por SCP

#### Windows, Linux e MacOS

É possivel copiar ficheiros entre o nosso computador e o raspberry por SSH

`scp <user>@<ip>:<path> <path>` - Copiar do raspberry para o computador

`scp <path> <user>@<ip>:<path>` - Copiar do computador para o raspberry

`scp <user>@<ip>:<path> <user>@<ip>:<path>` - Copiar de um raspberry para outro raspberry

**Nota:** Podemos copiar pastas adicionando o comando `-r` ao `scp`

### Transferir ficheiros por SFTP

Instalar o [Filezilla](https://filezilla-project.org), e criar uma nova ligação SFTP.

![](/img/Filezilla-1.png)

![](/img/Filezilla-2.png)

### Ligar VNC
Se te for mais conveniente, podes utilizar o protocolo VNC para interagir com o raspberry, para isso, tens que primeiro activar o protocolo de VNC.

Para activar o protocolo de VNC, vais executar o comando `sudo raspi-config` escolher a opção `5 Interfacing Options` e depois `enable` em `P3 VNC`.

No teu computador deves instalar o UltraVNC Client a partir deste link: [https://www.realvnc.com/en/connect/download/viewer](https://www.realvnc.com/en/connect/download/viewer)

![Chromium a correr no Raspberry](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/UltraVNC-1.png)

![Chromium a correr no Raspberry](https://github.com/ruimartinsptl/workshop-rpi-2018/raw/master/img/UltraVNC-2.png)

No MacOS não precisas de instalar o UltraVNC, podes usar directamente a ferramenta de partilha de ecrã que acompanha
o sistema operativo, para tal basta abrires o "Finder" e premir as teclas `⌘+k` de seguida inserir o seguinte endereço: 
vnc://<ip-do-raspberry>

Se não ligares nenhum monitor ao raspberry, e no Ultra VNC vires a mensagem "Cannot currently show the dekstop", deverás definir manualmente uma resolução diferente de "default"

![](/img/change-resolution.png)

[Voltar ao Índice](#indice)

# Algumas configurações iniciais

Para termos o raspberry preparado para o nosso workshop vamos fazer algumas configurações iniciais e instalar algum 
software...
Aqui estão descritos os diferentes passos, mas os mesmos estão no ficheiro `00-prepare-raspberry-first-time.sh`  

`sudo rpi-update` # Updating firmware [Opcional]

`sudo reboot` # (Se tiver sido executado o rpi-update)

```
# Actualização do sistema
sudo apt-get -y update 
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
```

`sudo ldconfig`

ldconfig is a program that is used to maintain the shared library cache.
This cache is typically stored in the file /etc/ld.so.cache and is used by
the system to map a shared library name to the location of the corresponding

`sudo raspi-config`

![raspi-config](/img/raspi-config.png)

* Update
* Expand File Sistem
* Locale
* Boot Options -> DESKTOP
* Video Memory
* Output Audio
* ...

**NOTA:**
Se preferires, o raspi-config pode ser configurado apenas por linha de comandos, sem precisar de interação humana. Seguem aqui alguns exemplos de como o fazer:

`# sudo raspi-config nonint do_expand_rootfs`

`sudo raspi-config nonint do_wifi_country PT`

`sudo raspi-config nonint do_hostname rpi-demo`

`# sudo raspi-config nonint do_boot_behaviour B1 # SET BOOT CLI`

`# sudo raspi-config nonint do_boot_behaviour B3 # SET BOOT GUI`

`sudo raspi-config nonint get_vnc`

`sudo raspi-config nonint do_vnc 0`

`raspi-config nonint get_rgpio`

`sudo raspi-config nonint do_rgpio 0`

`raspi-config nonint get_camera`

`raspi-config nonint do_camera 0`

Mais informações: 
- [https://github.com/RPi-Distro/raspi-config/blob/master/raspi-config](https://github.com/RPi-Distro/raspi-config/blob/master/raspi-config)
- [https://github.com/raspberrypi-ui/rc_gui/blob/master/src/rc_gui.c#L23-L70](https://github.com/raspberrypi-ui/rc_gui/blob/master/src/rc_gui.c#L23-L70)


## Outros:

`sudo apt-get install -y vim` # Editor

`sudo apt-get install -y eog eog-plugins` # Visualizar imagens

`sudo apt-get install -y screen` # Deixar aplicações em execução quando se fecha a ligação SSH

`sudo apt-get install -y htop` # Ver processos em execução, memoria em uso, etc...

`sudo apt-get install -y geany` # Editor de texto / código

## Remover programas que não fazem falta:
`sudo apt-get purge -y wolfram-engine`

`sudo apt-get purge -y libreoffice*`

`sudo apt-get clean -y`

`sudo apt-get autoremove -y`


# ----
## cronjob

Para executares automáticamente scripts em função do tempo, podes utilizar cronjobs,
para tal basta executares `crontab -l` para veres os teus trabalhos agendados, e `crontab -e` para os editares.

Podes ver/editar os cronjobs de outros utilizadores no sistema, execurando `crontab -u username -l` e `crontab -u username -e`.


Os cronjobs que adicionares tem que estar neste formato:
```text
* * * * * command to be executed
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```

**Exemplos:**

`0 2 * * * /bin/sh backup.sh` Executa todos os dias às 02h00.

`0 5,17 * * * /scripts/script.sh` Executa todos os dias às 05h00 e às 17h00

`* * * * *  /scripts/script.sh` Executa todos os minutos

`* * * jan,may,aug *  /script/script.sh` Executa todos os minutos durante Janeiro, Maio e Agosto

Ver mais exemplos aqui: [https://tecadmin.net/crontab-in-linux-with-20-examples-of-cron-schedule/](https://tecadmin.net/crontab-in-linux-with-20-examples-of-cron-schedule/)


## screen

Quando tens uma sessão SSH, ao terminares a ligação, todos os processos que lá foram iniciados são terminados. 
Imagina que queres abrir uma sessão SSH, deixar a executar um script, fechar a sessão, e dali a umas horas voltares à sessão em que o script ainda está a correr. Tens que utilizar o screen.

Iniciar sessão screen (depois de abrires a ligação SSH)
`screen`

Depois de iniciares a sessão, podes ver todos os parametros do screen carregando em `CTL+A` e depois em `?`

Podes fazer _detach_ da sessão, carregando em `CTL+A` e depois em `d`, a sessão ficará na mesma activa.

Para voltares à ultima sessão, podes executar `screen -r`

Caso tenhas várias sessões activas, para as veres podes executar `screen -ls`
```text
$ screen -ls
There is a screen on:
	25144.pts-1.rpi-demo	(09/05/19 00:46:07)	(Detached)
1 Socket in /run/screen/S-pi.
```

Poderás voltar a uma sessão especifica, executando: `screen -r 25144`

**NOTA:** Além do screen, o [tmux](https://github.com/tmux/tmux/wiki) também é muito utilizado.

## eog (via ssh -X)

Para visualizares uma imagem a partir de uma sessão SSH, podes por exemplo utilizar o eog, executando `eog imagem.jog`

# Fim da parte 1

## <a name="parte1"></a>1ª parte: Configurar Raspberry PI com WiFi, sem usar monitor e teclado (headless setup).

[Clica para abrires a parte 1](../10-SetupRaspberry)

[Voltar ao Índice](../#indice)


## <a name="parte2"></a>2ª parte: Visão por computador num Raspberry PI com Python e OpenCV

[Clica para abrires a parte 2](../20-ComputerVision)

[Voltar ao Índice](../#indice)

## <a name="parte3"></a>3ª parte: Configuração de GPIOs

[Clica para abrires a parte 3](../30-GPIOs)

[Voltar ao Índice](../#indice)


## <a name="projecto"></a>Mini-projecto

[Clica para abrires a mini projecto](../40-Project)

[Voltar ao Índice](../#indice)
