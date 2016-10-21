Name:           discord-canary
Version:        0.0.9
Release:        1%{?dist}
Summary:        Experimental canary build for Discord

License:        proprietary
URL:            https://discordapp.com/
Source0:        https://discordapp.com/api/download/canary?platform=linux&format=tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  libXScrnSaver
Requires:       libXScrnSaver
AutoReqProv:    no

%description
Discord Linux - VERY Experimental Canary Release 

%global debug_package %{nil}

%prep
%autosetup -n DiscordCanary

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/opt/DiscordCanary
mkdir -p $RPM_BUILD_ROOT/usr/share/applications

cp -r * $RPM_BUILD_ROOT/opt/DiscordCanary/
ln -sf /opt/DiscordCanary/DiscordCanary $RPM_BUILD_ROOT/%{_bindir}/
desktop-file-validate %{buildroot}/%{_datadir}/applications/Discord.desktop

%files
%defattr(-,root,root)
/opt/DiscordCanary/
%{_bindir}/DiscordCanary
/usr/share/applications/Discord.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jul  8 2016 Vishal Verma <vishal@stellar.sh>
- Initial build (using discord-canary-0.0.8), adding .desktop file
- 
