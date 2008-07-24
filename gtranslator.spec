%define version 1.1.7

Summary:	Translation (.po) file editor with many features
Name:		gtranslator
Version:	%{version}
Release:	%mkrel 4
License:	GPLv2+
Group:		Editors
URL:		http://sourceforge.net/projects/gtranslator/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/%{name}-%{version}.tar.bz2
Patch0:		gtranslator-1.1.7-scrollkeeper-rarian.patch
BuildRequires:	ImageMagick
BuildRequires:	docbook-utils
BuildRequires:	libgnomeui2-devel
BuildRequires:	scrollkeeper
BuildRequires:	perl-XML-Parser
BuildRequires:	gtkspell-devel
Requires:	gettext

Requires(post): desktop-file-utils scrollkeeper
Requires(postun): desktop-file-utils scrollkeeper

%description
gtranslator is a comfortable po file editor with many bells and whistles.
It features many useful function which ease the work of translators of po
files immenantly.


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--enable-compile-warnings=maximum \
	--enable-debug=no

%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

# icons
mkdir -p $RPM_BUILD_ROOT/%{_miconsdir} \
	 $RPM_BUILD_ROOT/%{_iconsdir}
install -m 0644 -D      data/desktop/gtranslator.png $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
convert -geometry 32x32 data/desktop/gtranslator.png $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
convert -geometry 16x16 data/desktop/gtranslator.png $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png

# menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Translation;Development;GTK;
EOF

### Remove files not bundled
# pozilla is for software maintainers ONLY
rm -f $RPM_BUILD_ROOT%{_bindir}/pozilla.sh
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pozilla*

%find_lang %name --with-gnome

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%update_scrollkeeper
%{update_menus}
%endif

%if %mdkversion < 200900
%postun 
%update_scrollkeeper
%{clean_menus}
%endif

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog DEPENDS NEWS README THANKS TODO
%{_bindir}/gtranslator
%{_datadir}/gtranslator
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/%name-C.omf
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/gtranslator.*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
