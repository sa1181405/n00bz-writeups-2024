It was 9:13 PM. We had just solved `WaaS` and `The Gang 4`. Only `Shop` was left. The race was on for the last spot in the top 3. {lufimio} cooked up a script, but only had 1 hour of screen time left. 30 minutes went by and {lufimio} was still making local fixes. {lolmenow} and {Tao} were trying to figure out how to interact with smart contracts. At 9:46, {lolmenow} appeared to get a hit using code from ChatGPT...
```
Attack executed!
Flag bought!
```
...we rushed to get new creds...
```
! lolmenow
 — 
Yesterday at 21:46
damn
wait
i gotta get new creds
wjat
 — 
Yesterday at 21:46
bruh
quick
quick
Tao
 — 
Yesterday at 21:46
gogogo
! lolmenow
 — 
Yesterday at 21:46
OKAY
AHHHJ
```
...but it was a dud.
```
! lolmenow
 — 
Yesterday at 21:49
gpt added debugging
oh wait
i just read over the script
it will always print flag bought
💀
wjat
 — 
Yesterday at 21:50
💀😭
```
And at 10:06 PM, {lufimio}'s screen time ran out. We were so cooked. We spent the next hour trying figure out how to implement the Reentrancy attack properly and how to deploy it remotely... without {lufimio}. There was some... interesting conversation.
```
Tao
 — 
Yesterday at 22:37
also wait i just realized this is just capitalism
! lolmenow
 — 
Yesterday at 22:37
🤣
Tao
 — 
Yesterday at 22:38
this is just software infused with capitalism
just like open source software is communism
well kind of
this is more extreme
! lolmenow
 — 
Yesterday at 22:38
?!
COMMUNIIIIIIIIIIIIIIIIIIIIIIISM
Tao
 — 
Yesterday at 22:39
which makes most cryptocurrencies a weird culturally left economically right thing
```
We saw some hope - ties were broken by first bloods?! If confirmed, this would be huge. We were leading on first bloods and there were none left to take. Unfortunately... we were trolled again. At least by a human this time. {lolmenow} and {Tao} continued locking in while {wjat} got absolutely carried and left to do homework....
```
! lolmenow
 — 
Yesterday at 23:09
ok
wait
i just found a writeup
https://toh.necst.it/xmasctf2021/ethereum/XMAS-CTF/
X-MAS CTF - 残響
CTFs write-ups by the PoliMi Security Team.
wjat
 — 
Yesterday at 23:10
NO WAY?!
! lolmenow
 — 
Yesterday at 23:10
literally the same attack
wjat
 — 
Yesterday at 23:10
!!!!!!!!!!!
! lolmenow
 — 
Yesterday at 23:10
founda nother one
https://medium.com/@secureblockchain/blockchain-exploitation-labs-reentrancy-my-notes-2a7ffd9cfe8a
```
{lolmenow} found some past writeups on the same vulnerability! But... then we ran into errors connecting to the blockchain.
```
! lolmenow
 — 
Yesterday at 23:39
wait @Tao
To connect to the blockchain provided we can use a web-based IDE, Remix, that provides the possibility to connect to an external blockchain.
Tao
 — 
Yesterday at 23:40
yes but it wont connect for some reason
! lolmenow
 — 
Yesterday at 23:40
!?
With Remix IDE all we have to do is: open the File Explorer tab and upload the three contracts, then go to the Solidity Compiler tab and compile the three contracts by selecting the correct version of solidity (in this case 0.6.0) and finally deploy the contracts by going to the Deploy and Run Transactions tab. 
! lolmenow
 — 
Yesterday at 23:40
ss pls 
Tao
 — 
Yesterday at 23:41
Image
! lolmenow
 — 
Yesterday at 23:41
that means the instance timed out
it terminates every 10 minutes
you need to create a new one
Tao
 — 
Yesterday at 23:41
i got this instance just now
like at 11:40
```
It turns out, the author of the challenge had to enable HTTP requests from remix for us to be able to solve the chall without using web3.
```
Tao
 — 
Today at 00:06
im opening a ticket because i cant connect
! lolmenow
 — 
Today at 00:06
i already did
the author has to enable http requests from remix

[some messages skipped]

! lolmenow
 — 
Today at 00:07
our 3rd place relies on noobmaster WAKING UP
AND ENABLING HTTP REQUESTS
like why sleep

[some messages skipped]

! lolmenow
 — 
Today at 00:11
our only option is web3
or wait 8 hours for noobmaster to wake up

```
At this point, {wjat} decided to throw the problem at ChatGPT and blindly follow the instructions to hopefully cook up something {lolmenow} and {Tao} missed. This resulted in 12 files, 0 learning, and 2 hours of sleep deprivation. During this time, {lolmenow} failed to beg staff and suffered at the delight of {Censored} [an admin]. Nothing much happened until 7:45 AM the next day. This was the situtation:
```
lufimio
 — 
Today at 07:45
im awake
has it been solved
and yes my internet got blocked
! lolmenow
 — 
Today at 07:45
no 😔
lufimio
 — 
Today at 07:47
at least they havent solved it
did you get a new attacking script from chat gpt
! lolmenow
 — 
Today at 07:49
yes but it ain’t working. we can solve it if the developers enable http requests from remix
lufimio
 — 
Today at 07:49
does it work locally
! lolmenow
 — 
Today at 07:49
Tao says it does
```
It was starting to look up. Even better, after an hour, {lufimio} managed to cook something up.
```
lufimio
 — 
Today at 08:50
nvm i got it to work locally on mine
i also have a yt vid on someone doing a similar thing using web3 python
we might win

[some messages skipped]

! lolmenow
 — 
Today at 09:00
👀👀👀👀
If we had remix we didn’t need to code in web3
lufimio
 — 
Today at 09:00
i have a resource
it should be fine
youll need to run it tho
my internet is blocking nc
! lolmenow
 — 
Today at 09:01
Okay ping me
lufimio
 — 
Today at 09:01
ill ping everyone when i got a script
! lolmenow
 — 
Today at 09:01
Alr
lufimio
 — 
Today at 09:48
[Pinging the team]
i might have done it

[some messages skipped]

! lolmenow
 — 
Today at 09:48
Oh my God
lufimio
 — 
Today at 09:48
testquick
! lolmenow
 — 
Today at 09:49
I’m getting on my pc ASAP
lufimio
 — 
Today at 09:49
i have unti 10:15 
! lolmenow
 — 
Today at 09:49
Crap
Okay
lufimio
 — 
Today at 09:49
and then i might be able to get my phone
and help
! lolmenow
 — 
Today at 09:49
Okay my pc is booting
lufimio
 — 
Today at 09:50
send all of the output
! lolmenow
 — 
Today at 09:50
Okay okay
lufimio
 — 
Today at 09:50
i have a lot of debugging
also i forgot to change the port
! lolmenow
 — 
Today at 09:52
I am typing the url for the CTF website as we speak
lufimio
 — 
Today at 09:53
blockchain.n00bzUnit3d.xyz
nc blockchain.n00bzUnit3d.xyz 39999
! lolmenow
 — 
Today at 09:54
do i need the Shop.sol in the same dir
lufimio
 — 
Today at 09:54
yh
```
{lufimio} had cooked up the script, but their internet was blocked. {lolmenow} had to run it on their computer, with {lufimio} standing by to recieve error messages and bug-fix. It was intense! After a while of this...
```
! lolmenow
 — 
Today at 10:26

└─$ python3 solve.py
[x] Opening connection to blockchain.n00bzUnit3d.xyz on port 39999
[x] Opening connection to blockchain.n00bzUnit3d.xyz on port 39999: Trying 64.23.154.146
[+] Opening connection to blockchain.n00bzUnit3d.xyz on port 39999: Done
[*] Closed connection to blockchain.n00bzUnit3d.xyz port 39999
contract_address='0xdb73e8439f697cEb90b497a17290AE26De27fd6d'

Expand
message.txt5 KB
you got more ether
YOU GOT MORE ETHER
Account Balance: 173.998443048 ether
```
{lolmenow} got more ether through the exploit, on the actual blockchain for the challenge!! And we solved it!!!
```
! lolmenow
 — 
Today at 10:40
its looping lufimio
ITS LOOPING
WE HAVE 600 ETHR
WE HAVE 1088
WE HAVE 1389
WE HAVE 2003
lufimio
 — 
Today at 10:40
IT WORKED ‼️ ‼️ ‼️ ‼️ ‼️ ‼️ ‼️ ‼️
‼️
! lolmenow
 — 
Today at 10:40
WE HAVE 2613
lufimio
 — 
Today at 10:40
‼️
‼️
‼️
! lolmenow
 — 
Today at 10:40
WE HAVE 3003
lufimio
 — 
Today at 10:40
WE WIN ‼️ ‼️ ‼️ ‼️
! lolmenow
 — 
Today at 10:40
ITS STILL GOING
lufimio
 — 
Today at 10:40
‼️
‼️
‼️
what iteration
! lolmenow
 — 
Today at 10:41
its done
im netcatting
to input secret
WE.
GOT
THE
F*CKING FLAG
lufimio
 — 
Today at 10:41
you enter
! lolmenow
 — 
Today at 10:41

└─$ nc blockchain.n00bzUnit3d.xyz 39999
[1] Get an instance
[2] Get the flag
Choice: 2
Please enter the hash provided during deployment: 0dc5358c1fe0606e02095431e657c746956ff12458be7622206f085ed43bfd79
Flag: n00bz{5h0uld_h4v3_sub7r4ct3d_f1r5t}

enter
lufimio
 — 
Today at 10:41
my thing is broken
! lolmenow
 — 
Today at 10:41
ok
submitted
lufimio
 — 
Today at 10:42
NUMBER 1 LETS GO ‼️ ‼️ ‼️ ‼️ ‼️
```
But of course, it wasn't meant to be.
```
! lolmenow
 — 
Today at 10:42
hang on wait let me check scoreboard
NOOOOOOOOOOOOOOOOOOOOO people solved it overnight
```
![pbchocolate in 4th](https://i.ibb.co/K2KyYjt/4image.webp)
Another 4th place. 😔 Another bare miss of the podium... 😔 like CatTheQuest, but with no top 50 or top 5 prize. 😔 It was over.
