Summary:	GameBoy Advance emulator
Summary(pl):	Emulator GameBoya Advance
Name:		VGBA
Version:	3.0
Release:	1
License:	Copyright (distributable)
Group:		Applications
Source0:	http://fms.komkon.org/VGBA/%{name}30-Linux-80x86-bin.tar.Z
# Source0-md5:	9e335c3ae6770b1cbfee8fd354321736
URL:		http://fms.komkon.org/VGBA/
ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual GameBoy Advance (VGBA) is an emulator of the GameBoy Advance
videogame handheld produced by Nintendo. It runs GameBoy Advance games
on PCs or PocketPCs. It can also help to debug GameBoy Advance
software without using a costly development system.

%description -l pl
Virtual GameBoy Advance (VGBA) to emulator kieszonkowej gry
telewizyjnej GameBoy Advance produkowanej przez Nintendo. Uruchamia
gry z GameBoya Advance na komputerach PC i PocketPC. Mo¿e tak¿e pomóc
przy poprawianiu oprogramowania dla GameBoya Advance bez kosztownego
systemu programistycznego.

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
