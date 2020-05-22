# TITLE: Game Paper, Scissors, Rock
----

## 1.0 ABOUT

| ![_HUMAN_](./static/image/human.png) | _VS._ | ![**BOT**](./static/image/bot.png) |
|:-------:|:-:|:-----:|
|**Human**|   |**Bot**|

* Version: 2.0
* Author: Joshua Harvey
* Contact: harvey.gamedev@gmail.com

----

## 2.0 INTRO

* You may look through the code if you like, however it's not perfect or coded very well!
But trust me, it's written 100% better than version 1.0 and 1.1 which I won't release
since they're slow, really only nothing but text.
* But if you find that it helps you in some way or another, please use whatever code you
need from it. All I ask is that you don't completely copy the game 100%, word for word,
or something like that.
* If you have any suggestions, find a bug, just have an opinion or just help me become
a better programmer, please send an e-mail to the address given above. Even if you have
good sources that you can recommend or game ideas.

----

## 3.0 HOW TO RUN / PLAY

> ![_실행화면_](https://goo.gl/R2fXFj)

* **Requirements:**
	- a **Python 3.x** interpeter and the **pygame** module
* **How to run:**
	- Run the app.py script in the Python 3.x interpeter
* **How to play:**
	- It's basically click and point (exciting, I know. Next GoTY)
	- **[F1]** ...... Resets the game
	- **[ESC]** ..... Quits the game
	- Pick either **paper**, **scissors** or **rock** and the bot will pick one.
	- You'll know if you won or lost.

----

## 4.0 KNOWN BUGS

- Sometimes the title will move straight to the controls menu
	(Raising the SCRIPT_DELAY variable helps a bit (Default = 40))

- "Paper, Scissors and Rock" doesn't disappear straight away after picking one on the results screen
	(I don't plan to fix this because it doesn't affect anything but I know why it happens.)

----

## 5.0 SOME EXPLAINATIONS

> Not compiled into an .exe or other extension
I did this mainly so the code is open to anyone that wants to read it. It might help some-one or
even myself.

> Getting the login name in game_settings.py
I feel has if some-one might think it's weird or malicious to get the user's name using the
os module's getlogin() function so I thought I might explain it. I just wanted it like that so the
game isn't using the generic 'player' or something for the name. I thought it might be a nice touch
to use the name of the person who might be playing the game. If you don't know what the os.getlogin
function does, it gets the username of the person playing the game.

> On Windows it works (at least on mine), Mac, I don't know but linux, I've only tried it on Raspbian
and it doesn't. For this, if it can't get the name of the person, it'll just use 'Player' instead.
I'm guessing it's just a permission thing.

> Why the directories for the static if there's not that many of them?
I'm very organised and I like my things sorted. When I started programming last year, my first game
(Not this one) was a pygame one. Basically the app.py file was lost in a sea of images and stuff.

> Version 2?
Yes. Most games I make are for fun and just to mess around with, nothing serious or worth putting
online. This project isn't a serious one but I feel like it's good enough to put online. It's not
the greatest game ever made but it'll probably keep children busy, you got no-one to actually play
paper, scissors, rock with or a good time waster if you're bored.

> As I mentioned above, version 1.0 and 1.1 are ones I felt like they were the base sorta game.
They are flawed, they're really just a text game, performance is bad and the design is horrible
Version 2.0 has a little more visual appeal, coded a bit better, faster and some nice little touches
to it but not anything too fancy. I tend to discard projects because of the reason that they're not
interesting at all, they have no appeal to them, they're coded extremely bad or I'm not happy with them.

----

* Project site : [https://www.pygame.org/project/3634/5724](https://www.pygame.org/project/3634/5724)

| <img src="https://goo.gl/xW851H" alt="pygame_logo" width="350"> |
|:----:|
| **PyGame LOGO**|
