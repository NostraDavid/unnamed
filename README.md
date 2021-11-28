# the unnamed project (TUP, for short)

This is not a game. This is not a game engine. This is just some code to solve a problem that I have with Minecraft and Minecraft-like games.

## The problem

Minecraft, with Optifine, can have a VERY large draw distance of 64. Note that this does NOT mean `64x64=4096` chunks total, oh no no. This means `1+(64*4)+((64^2)*4) = 16,641` chunks. With `16*16*256 = 65536` blocks *per chunk*, this means a total of `1,090,584,576` blocks that need to be handled.

| setting | # of chunks | # of blocks   |
| ------- | ----------- | ------------- |
| 2       | 25          | 1,638,400     |
| 4       | 81          | 5,308,416     |
| 8       | 289         | 18,939,904    |
| 16      | 1,089       | 71,368,704    |
| 24      | 2,401       | 157,351,936   |
| 32      | 4,225       | 276,889,600   |
| 48      | 9,409       | 616,628,224   |
| 64      | 16,641      | 1,090,584,576 |

## The solution
