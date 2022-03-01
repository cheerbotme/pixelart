# pixelart

Basic pixelart functionality for a Raspberry Pi Zero W with a [Pimoroni unicorn hd HAT](https://shop.pimoroni.com/products/unicorn-hat-hd).

<p align="left">

   <img src="https://user-images.githubusercontent.com/3211305/156248954-0797aaf1-b347-4686-9215-875d67e3c85a.gif" width="25%">
   
</p>

<p align="left">

   <img src="https://user-images.githubusercontent.com/3211305/153781064-9af06cec-1ed1-4ec5-ac61-96858b8ebcd2.gif" width="25%">

</p>

<!-- 

## BuffiGWEI challenge! 

Can you make a better 16x16 BuffiGWEI sprite than this 16x16 pixelart?

Do it before https://schellingpoint.gitcoin.co at ETHDenver and you might get your pixel displayed at Schelling Point!

<p align="left">

   <img src="https://user-images.githubusercontent.com/3211305/153782055-150bc5df-1699-46f5-8e73-412339c39575.png" width="25%">

</p>

For context, this is the BuffiGWEI cartoon:

<p align="left">

   <img src="https://user-images.githubusercontent.com/3211305/153782026-4ae4137a-1459-4db6-97ab-e7d018a0701f.jpeg" width="25%">

</p>

If so, share it on this repo with a pull request or tag @bestape in a tweet with your submission.

-->

## how to make a sprite with SVG

Use the `greenpill.svg` as a template and output the PNG as a `16x512` pixel file.

To follow the `cheerbot/sprite.svg` convention, save the PNG in the `cheerbot/sprite` folder.

Name the PNG the number you want to show it in the sequence followed by `sprite.png`.

For instance, `06sprite.ong` for the 7th sprite (assume the count starts at 00).

If you want a sprite with more than 32 frames, add a dash to the PNG with the sequence in the sprite.

For insance, `08-2sprite.png` for the 2nd part of the 9th sprite.

Inkscape is a free SVG editing tool.

In Ubuntu, you can install Inkscape in Terminal (open Terminal with the `ctrl+alt+t` command):

* `sudo add-apt-repository ppa:inkscape.dev/stable`

* `sudo apt update`

* `sudo apt install inkscape`

## how to make a sprite with MP4

You can also convert a 1:1 video into a sprite.

Install ffmpeg and ImageMagick:

* `sudo apt update`

* `sudo apt install ffmpeg`

* `sudo apt install imagemagick`

Then convert the video into JPG:

* `ffmpeg -i *.mp4 -filter:v fps=20 "%02d.jpg"`

Experiment with `fps=` to find a multiple of 32.

Then make a sprite with:

* `convert *.jpg +append NAME.png`

Use Inkscape to resize the sprite to 16x512.

## how to install cheerbot on Raspberry Pi

Modify this repo's `wpa_supplicant.conf` with your wifi's information. 

Follow the instructions here to flash a Raspberry Pi OS on a SD card:

* `https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager`

When done, select the SD card's `boot` partition: 

* drag/drop this repo's `ssh` into the `boot` partition

* drag/drop the `wpa_supplicant.conf` you modified into the `boot` partition.

Select the SD card's `rootfs` partition and navigate to the `home/pi` folder:

* drag/drop this repo's `cheerbot` folder into the `home/pi` folder

Eject the SD, put it into the Raspberry Pi, plug the power USB into the Raspberry Pi and wait for the Raspberry Pi to boot up. 

When booted, open Terminal in your computer `ctrl+alt+t` and SSH into the Raspberry Pi with `ssh pi@raspberrypi`.

When you have entered the Raspberry Pi with SSH: 

* change the password with `passwd`

* turn on cheerbot at startup with: 

  * `sudo crontab -e` 

  * add `@reboot python3 /home/pi/cheerbot/sprite.py` to the end of the file

  * save and exit the file

* install the unicorn hd HAT dependencies with `curl https://get.pimoroni.com/unicornhathd | bash`

## join the Discord and help buidl cheerbot

https://discord.gg/KXzXR7DVqb
