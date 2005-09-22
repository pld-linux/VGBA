#
Summary:	GameBoy emulator
Summary(pl):	Emulator GameBoya
Name:		VGBA
Version:	3.0
Release:	1
License:	Copyright (distributable)
Group:		Applications
Source0:	http://fms.komkon.org/%{name}/%{name}30-Linux-80x86-bin.tar.Z
# Source0-md5:	9e335c3ae6770b1cbfee8fd354321736
URL:		http://fms.komkon.org/VGBA
ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual GameBoy (VGB) is an emulator of the GameBoy videogame handheld produced by Nintendo. It runs GameBoy, Super GameBoy, and GameBoy Color games on PCs, Macs, PocketPCs, or just about any other sufficiently fast computer in existence. It can also help to debug GameBoy software without using a costly development system.

%prep
%setup -q -c 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vgba $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc VGBA.html
%attr(755,root,root) %{_bindir}/vgba
