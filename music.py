#Music Player

import vlc

list = ["yt5s.io-Plants vs Zombies Music - Daytime in Front Yard (Horde)-(480p).mp4",
        "yt5s.io-Plants vs Zombies Music - Night Time in Front Yard (Horde)-(480p).mp4",
        "yt5s.io-Plants vs Zombies Soundtrack. [Day Stage].mp4",
        "yt5s.io-Plants vs Zombies Soundtrack. [Main Menu].mp4",
        "yt5s.io-Plants vs Zombies Soundtrack. [Night Stage] (1).mp4"]

song1 = vlc.MediaPlayer("yt5s.io-Plants vs Zombies Music - Daytime in Front Yard (Horde)-(480p).mp4")
song2 = vlc.MediaPlayer("yt5s.io-Plants vs Zombies Music - Night Time in Front Yard (Horde)-(480p).mp4")
song3 = vlc.MediaPlayer("yt5s.io-Plants vs Zombies Soundtrack. [Day Stage].mp4")
song4 = vlc.MediaPlayer("yt5s.io-Plants vs Zombies Soundtrack. [Main Menu].mp4")
song5 = vlc.MediaPlayer("yt5s.io-Plants vs Zombies Soundtrack. [Night Stage] (1).mp4")

print("1 Daytime in Front Yard")
print("2 Night Time in Front Yard")
print("3 Day Stage")
print("4 Main Menu")
print("5 Night Stage")

while True:
    try:
        song = int(input("Chose a Number "))
        break
    except:
        print("That is not an option, try again")

if song == 1:
    song1.play()
elif song == 2:
    song2.play()
elif song == 3:
    song3.play()
elif song == 4:
    song4.play()
elif song == 5:
    song5.play()

input()
