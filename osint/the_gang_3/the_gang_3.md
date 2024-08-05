# tail
Writeup author: **lolmenow**

Point count: 4__pts

Provided files: tail.jpg

Description:
>Can you find out where the OG meetup point is? The flag is in the format n00bz{lat,long} with upto 3 decimal places, rounded. Continue where you left off... Note: Wikipedia can be wrong sometimes ;) Author: NoobMaster

# 

Reading the tweets from the twitter account we found previous, we see several tweets. Here they are:

```
Wanna join us? I have a challenge for you:

The ciphertext (using AES-GCM) is: 1762841d1888f6b02581990abdf0aaba375c85fd3811a6fb405775fb8d
+ the key is the same as last time and the IV is "Lat,Long" up to 3 decimal places. 
Use the city where we met in 2022. Also, use Cyberchef.

I forgot, you will also need this: d5e749da6b02c75cb4c763939632503a
```

Since when was their crypto in osint?!

Anyways, we open cyberchef and change the AES-decrypt function to AES-GCM.

We input the CT, IV (discussed more below) and the GCM tag.

The GCM tag is the "you will also need this part" string.

We also need a key

# IV
Now, for the IV, it discusses a city and key that was used last time.

This is when I was confused for a while. After more searching, I realized that maybe the "last time" was referring to the 2022 version of n00bzCTF.

Sure enough, going to their writeup repo, we see a [challenge](https://github.com/n00bzUnit3d/n00bzCTF-OfficialWriteups/tree/main/osint/john_doe) called "John doe" with some coordinates. This is the IV!

IV: `46.720,33.154`

# Key:

With the knowledge of finding the IV, I assumed their would be a 2023 challenge that was similar to john doe which had the key.

Going to the 2023 repo, we see a [challenge](https://github.com/n00bzUnit3d/n00bzCTF2023-OfficalWriteups/tree/master/OSINT/John%20Doe%20Strikes%20Again) that references John doe!

And we see the key! Being: `YouCanNeverCatchJohnDoe!`

Inputting this into cyberchef, we decrypt the ciphertext into a discord message!

[Recipe for reference](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'UTF8','string':'YouCanNeverCatchJohnDoe!'%7D,%7B'option':'UTF8','string':'46.720,33.154'%7D,'GCM','Hex','Raw',%7B'option':'Hex','string':'d5e749da6b02c75cb4c763939632503a'%7D,%7B'option':'Hex','string':''%7D)&input=MTc2Mjg0MWQxODg4ZjZiMDI1ODE5OTBhYmRmMGFhYmEzNzVjODVmZDM4MTFhNmZiNDA1Nzc1ZmI4ZA)

# Discord server

Joining the discord server, we see a conversation in the general chat.

Using the discord search feature for "OG" we get messages that relate to the "OG" place:

```
Hey @John Doe , How's the weather in Delhi? I heard it's super hot
Censored1375 — 07/03/2024 6:11 AM
It's always raining in Bengaluru LOL
John Doe — 07/03/2024 6:11 AM
At least it does rain lol, Delhi is soo hoot dude. Just started raining recently so hopefully gets better
NoobHacker — 07/03/2024 6:13 AM
Bro Bengaluru is a literal paradise compared to Delhi
Censored1375 — 07/03/2024 6:13 AM
😆
John Doe — 07/03/2024 6:13 AM
Can't wait to get there bro...
NoobHacker — 07/03/2024 6:14 AM
At least you get to sleep before your flight. Mine was at 4 am in the morning 💀
Censored1375 — 07/03/2024 6:14 AM
Unlucky 😂 What time is yours @John Doe ? 
John Doe — 07/03/2024 6:14 AM
9:40 am in the morning is the scheduled time, but nowadays flights are always getting delayed
NoobHacker — 07/03/2024 6:15 AM
We meeting near the statue right?
```

Googling for Bengaluru popular statues, I see a statue called `Statue of Prosperity`

Inputting this into google maps, we get this [result](https://www.google.com/maps/place/Statue+of+Prosperity/@12.9764599,77.5726701,269m/data=!3m1!1e3!4m6!3m5!1s0x3bae17e48d4c75b7:0xd57e41ff4566db30!8m2!3d12.9764808!4d77.5729571!16s%2Fg%2F11j_02053p?entry=ttu)

There are our coordinates!

Final flag: `n00bz{12.976,77.572}`
