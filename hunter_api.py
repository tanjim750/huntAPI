#usr/bin/bash
clear
bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning


echo
echo
echo
echo $cy"       ░  █   █"$cy" █   █"$cy" █▀▄   █"$cy" ▀▀█▀▀"$i"   ▄▀▀▀▄  █▀▀▀▄ ▀▀█▀▀  ░"
echo $cy"       ░  █▀▀▀█"$cy" █   █"$cy" █  ▀▄ █"$cy"   █  "$i"   █▄▄▄█  █▄▄▄▀   █    ░"
echo $cy"       ░  █   █"$cy" █▄▄▄█"$cy" █    ▀█"$cy"   █  "$i"   █   █  █     ▄▄█▄▄  ░"
echo







echo
echo
echo
      echo $cy"   |"$me"1"$cy"|"$pur"  Use automatic"$i" Crawler"
      echo $cy"   |"$me"2"$cy"|"$pur"  Use Wordlist"$i" Hunting"
      echo $cy"   |"$me"0"$cy"|"$me"  EXIT"
echo
    


echo $me"╔═══"$bi"["$i"Tanjim"$bi"]"$me"══════"$bi"["$i""HuntApi""$bi"]"
echo $me"║"
read -p"╚═══➣➣ " pil

if [ $pil = 1 ]
then
echo $i
python main.py
fi

if [ $pil = 0 ]
then
echo
echo
echo
echo $me"    ______   _  __    ____   ______
   / ____/  | |/ /   /  _/  /_  __/
  / __/     |   /    / /     / /
 / /___    /   |   _/ /     / /
/_____/   /_/|_|  /___/    /_/"
echo
sleep 2
echo $cy" Thanks for support us "
sleep 2
exit
fi