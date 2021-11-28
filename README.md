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

I've played [Lugaru](https://store.steampowered.com/app/25010/Lugaru_HD/) and one interesting technique that David Rosen used was that to reduce the drawing distance of the game, instead of using a standard fog effect, like so many games do, it fades the floor into a background.

My idea is to apply this onto a Minecraft-like engine. 'Engine' not meaning a *game* engine here. This is going to be created to *specifically* show off this solution.

This means I'll have to re-create a Minecraft-like world and then apply this idea to it.

## Hypothetical Q&A

Q: Why not do it as a Minecraft Mod?  
A: Because I don't like Java.

Q: OK, but why not do it as a Minecraft Mod?  
A: Because I'm also curious to how a Minecraft world is to be built (somewhat performantly)

Q: Why Python?  
A: Because I use it daily for work, which means familiarity for me, and I don't care about performance for this one project. This isn't meant to be a performant videogame, but as a proof of concept (POC).

Q: Wait, you just said you wanted to make it "somewhat performantly", but also "I don't care about performance"  
A: Ye. If the performance drops below 30 FPS on 2160p I'll have a quick look on if I can improve a *little bit*, but I don't want to spend literal days to improve performance. It should be faster than a slideshow, but I'm not aiming for bajillion FPS. This ain't Quake.

Q: Why 2160p, specifically?  
A: That's just my native resolution. I don't plan to add any options. I just want it to run, and have it run faster than PowerPoint. Those are my only real requirements.
