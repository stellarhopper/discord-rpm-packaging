Name:           discord-canary
Version:        0.0.18
Release:        1%{?dist}
Summary:        Experimental canary build for Discord

License:        proprietary
URL:            https://discordapp.com/
Source0:        https://discordapp.com/api/download/canary?platform=linux&format=tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  libXScrnSaver libcxx
Requires:       libXScrnSaver libcxx
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
install -m 755 Discord.desktop %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
/opt/DiscordCanary/
%{_bindir}/DiscordCanary
/usr/share/applications/Discord.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Sun Jun  9 2017 Vishal Verma <vishal@stellar.sh>
- Update to discord-canary-0.0.18

* Wed May 31 2017 Xavier Stouder <xavier@stouder.io>
- Update to discord-canary-0.0.17

* Sat May  6 2017 Jan Varga <jano4varga@gmail.com>
- Update to discord-canary-0.0.16

* Tue Jan 31 2017 Vishal Verma <vishal@stellar.sh>
- Add a dependency for libcxx and bump the release to '2'

* Thu Jan 26 2017 Joel Vasallo <joelvasallo@gmail.com>
- Update to discord-canary-0.0.15

* Thu Jan  5 2017 Sean Callaway <seancallaway@fedoraproject.org>
- Update to discord-canary-0.0.13

* Sat Nov 12 2016 Vishal Verma <vishal@stellar.sh>
- Update to discord-canary-0.0.11

* Sun Nov  6 2016 Vishal Verma <vishal@stellar.sh>
- Update to discord-canary-0.0.10

* Fri Oct 21 2016 Vishal Verma <vishal@stellar.sh>
- Update to discord-canary-0.0.9
- Use desktop-file-install to install the desktop file

* Fri Jul  8 2016 Vishal Verma <vishal@stellar.sh>
- Initial build (using discord-canary-0.0.8), adding .desktop file
- 
