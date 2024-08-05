# the_gang_2
Writeup author: **lolmenow**

Point count: 412

Provided files: N/A

Description:
>You may have gotten your first flag, but it's just the beginning! John Doe, as overconfident as he is, has left you with a riddle. Maybe it hides some secrets? Continue where you left off last time. Flag will already by wrapped in n00bz{} Author: NoobMaster
# 

Visiting the member profile from the recent puzzle, we see a blog post titled "Who am I?"

Post:

```
Underneath the surface, secrets lie.
Stories untold, hidden from the eye.
Every question leads to more unknown.
Real mysteries, only few are shown.
Never revealing, always concealed.
A hidden truth, never revealed.
Many have searched, but none have found.
Every clue, like whispers, sound.

In the shadows, I silently stand.
Secrets I keep, like grains of sand.

Just a glimpse, you might get to see.
Only hints, no certainty.
Hidden pathways, a cryptic code.
Navigating through the winding road.

Have you the wit to break this scheme?
Answers lie beyond the dream.
Codes and puzzles, all intertwined.
Knowledge and wisdom, together aligned.
Every detail, a piece to decode.
Remember, persistence will lighten the load.

Do you have what it takes to unveil?
Only the cleverest will prevail.
Enter the realm of the unknown.
```

This is an acrostic puzzle. Reading each starting letter of each line spells out "USERNAME IS JOHN HACKER DOE"

Doing basic simple osint searching, we see that the username is a [twitter](https://twitter.com/johnhackerdoe) account.

Scrolling through the tweets gets you the flag.

Final flag: `n00bz{5t0p_ch4s1ng_m3_4f2d1a7d}`
