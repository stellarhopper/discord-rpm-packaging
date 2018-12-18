#!/bin/bash -x

url="https://discordapp.com/api/download/canary?platform=linux&format=tar.gz"
discord_dir="DiscordCanary"
rel=28

install()
{
	local oldver="$(rpm -q discord-canary)"

	# if discord wasn't locally installed already, skip
	[ -z "$oldver" ] && return

	sudo dnf install -y ./results_discord-canary/$ver/1.fc$rel/*.x86_64.rpm

	# The binary seems to have lost its executable attribute
	sudo chmod +x /opt/DiscordCanary/DiscordCanary
}

# get the latest tgz
url2=$(curl -s "$url" | grep "a href=" | cut -d= -f2 | cut -d'"' -f2)
file=${url2##*/}
[ -s "$file" ] || curl -s -O "$url2"
ver="${file##*-}"
ver="${ver%.tar.gz}"

inst_ver="$(rpm -qv discord-canary | cut -d'-' -f3)"
if [ -n "$inst_ver" ]; then
	if [[ "$ver" == "$inst_ver" ]]; then
		if [[ "$1" == "force" ]]; then
			: force build
		else
			echo "$ver already installed"
			exit 0
		fi
	fi
fi

# prepare spec, push
git reset --hard HEAD
git pull -q

# If spec already has the currently downloaded veresion, then it may be a rebuild
if ! grep -q $ver discord-canary.spec; then
	sed -i "s/$(grep "Version:" discord-canary.spec | cut -d' ' -f9-)/$ver/" discord-canary.spec
	git commit -am "Update to $ver (Automated)"
	git push
fi

# add the spec and desktop files
tar xf "$file"
cp ./*.spec ./*.desktop "$discord_dir"

# re-tar and cleanup
tar czf "$file" "$discord_dir"
rm -rf "$discord_dir"

# build srpm
fedpkg --release f$rel --module-name discord-canary mockbuild

# push to copr
# copr-cli build discord-canary ./results*/"$ver"/1.fc$rel/*.src.rpm
rm ./*.tar.gz

install
