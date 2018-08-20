# Quran-rotaba-kivy
simple app for memorizing ayat order in pc and mobile


![demo](demo.png)


## utilities used

Python 2.7 + Kivy 1.9.0 : language and framework used for coding

Piskel 0.14.0 : for drawing icons in pixelart style

Buildozer 0.34 : for apk and ios build, only for linux (tested on Ubuntu 16.10)

## build

### run app

install kivy if not done yet

run :

main.py with python

### mobile packaging

install buildozer if not done yet
this step is only for linux
in the app dir run:

init buildozer

buildozer -v android debug

mv .buildozer/android/platform/build/dists/lina/bin/QuranRotaba-0.1-debug.apk .

## version list

create the app's pillar 	v0.1*

## what next?

put relatives aya informations in head bar

create navigation menu to jump ot a specific hizb

## contributions are welcome

for more informations or any suggestion, contribution and others contact me in faisal.adraji@gmail.com
