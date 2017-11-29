#!/bin/bash -x

url="https://discordapp.com/api/download/canary?platform=linux&format=tar.gz"
discord_dir="DiscordCanary"
rel=27

# get the latest tgz
url2=$(curl -s "$url" | grep "a href=" | cut -d= -f2 | cut -d'"' -f2)
file=${url2##*/}
[ -s "$file" ] || curl -s -O "$url2"

# add the spec and desktop files
git pull
tar xf "$file"
cp ./*.spec ./*.desktop "$discord_dir"

# re-tar and cleanup
tar czf "$file" "$discord_dir"
rm -rf "$discord_dir"

# build srpm
fedpkg --release f$rel --module-name discord-canary mockbuild

# push to copr
ver="${file##*-}"
ver="${ver%.tar.gz}"
#copr-cli build discord-canary ./results*/"$ver"/1.fc$rel/*.src.rpm
rm ./*.tar.gz
