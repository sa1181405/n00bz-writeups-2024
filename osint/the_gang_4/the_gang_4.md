
# Osint/The Gang 4
**Writeup Author:** wjat
**Original Solver:** wjat
**Point Value:** 492

**Provided Files:**
  - N/A

**Description:**
Can you find more information about his flight? Time to close John Doe's case one and for all! Author: NoobMaster Note: Flag format: n00bz{DateOfFlight(DD/MM/YYYY)_FlightNumber_IATAairportCodeOfDeparture_IATAairportCodeofArrival_ACTUALtimeOfDeparture_ACTUALtimeOfArrival_GateofDeparture_AirplaneModel} Example: n00bz{26/06/2024_AA1337_DFW_SFO_13:37_15:51_32A_AirbusA319-400} Please use the above format to format your flag.


# Solution

A lot of information can be gathered from The Hangout Discord server (see gang 3 writeup). Searching on flightstats.com using the date (3 Aug), time (~1 pm arrival), arrival airport (Bengaluru, BLR), airline (Air India) and knowing the other airport is in Delhi, we find [this flight](https://www.flightstats.com/v2/flight-tracker/AI/506?year=2024&month=8&date=3&flightId=1266296156%20?!).

Discord messages with info:
```
NoobHacker
 — 
03/07/2024 06:10
Hey @John Doe , How's the weather in Delhi? I heard it's super hot
Censored1375
 — 
03/07/2024 06:11
It's always raining in Bengaluru LOL
John Doe
 — 
03/07/2024 06:11
At least it does rain lol, Delhi is soo hoot dude. Just started raining recently so hopefully gets better
NoobHacker
 — 
03/07/2024 06:13
Bro Bengaluru is a literal paradise compared to Delhi
Censored1375
 — 
03/07/2024 06:13
😆
John Doe
 — 
03/07/2024 06:13
Can't wait to get there bro...
NoobHacker
 — 
03/07/2024 06:14
At least you get to sleep before your flight. Mine was at 4 am in the morning 💀
Censored1375
 — 
03/07/2024 06:14
Unlucky 😂 What time is yours @John Doe ? 
John Doe
 — 
03/07/2024 06:14
9:40 am in the morning is the scheduled time, but nowadays flights are always getting delayed
```
```
NoobHacker
 — 
02/08/2024 12:47
What time should I pick you up?
John Doe
 — 
02/08/2024 12:47
lands around 1, so probably 1:30ish
NoobHacker
 — 
02/08/2024 12:48
k
John Doe
 — 
02/08/2024 12:48
cya 👀
Censored1375
 — 
Yesterday at 09:34
how was your flight?
John Doe
 — 
Yesterday at 09:34
it was good
Air India food is so 🔥
```


Final flag:
`n00bz{03/08/2024_AI506_DEL_BLR_10:03_12:44_30_AirbusA350-900}`
