# Focus on yourSELF
Writeup author: **taodragon_**

Point count: 429pts

Provided files:
- `docker-compose.yml`

Description:
>Have you focused on yourself recently? Author: NoobHackers

# Solution

The `/view?image=` endpoint has a path traversal vulnerability that allows us to read any file. The contents of the file are in the base64 data of the image, which can be viewed by inspect element.
According to the provided `docker-compose.yml`, the flag is stored in the `FLAG` environment variable.
To view environment variables, we can read `/proc/self/environ`. Visiting `/view?image=../../proc/self/environ` and extracting the base64 data gives us the flag.

Flag: `n00bz{Th3_3nv1r0nm3nt_det3rmine5_4h3_S3lF_9fa0b845205e}`
