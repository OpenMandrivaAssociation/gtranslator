%define version 2.91.4

Summary:	Translation (.po) file editor with many features
Name:		gtranslator
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2+
Group:		Editors
URL:		http://projects.gnome.org/gtranslator
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/2.91/gtranslator-%{version}.tar.xz
BuildRequires:  imagemagick
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	libgnomeui2-devel
BuildRequires:	scrollkeeper
BuildRequires:	gtkspell-devel
BuildRequires:	unique-devel
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	pkgconfig(gdl-1.0)
BuildRequires:	subversion-devel
BuildRequires:	libsoup-devel
BuildRequires:	libgdict1.0-devel
BuildRequires:	gucharmap-devel
BuildRequires:	gda4.0-devel
BuildRequires:	glib2-devel >= 2.26
BuildRequires:	gsettings-desktop-schemas-devel
#gw TODO: is this needed?
Requires:	gsettings-desktop-schemas
Requires:	gettext

Requires(post): desktop-file-utils scrollkeeper
Requires(postun): desktop-file-utils scrollkeeper

%description
gtranslator is a comfortable po file editor with many bells and whistles.
It features many useful function which ease the work of translators of po
files immenantly.

%package	devel
Group:		Development/GNOME and GTK+
Requires:	%name = %version
Summary:	Development files for %name

%description	devel
This package contains development files needed to build %name plugins.

%prep
%setup -q

%build
%configure2_5x \
	--disable-scrollkeeper \
	--enable-compile-warnings=maximum \
	--enable-debug=no --disable-static

%make

%install
%makeinstall_std UPDATE_DESKTOP=true


rm -f %buildroot%_libdir/gtranslator/*.la

%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_bindir}/gtranslator
%{_datadir}/gtranslator
%{_libdir}/gtranslator
%{_datadir}/omf/%name
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/*/apps/gtranslator.*
%{_datadir}/pixmaps/*
%{_datadir}/gtk-doc/html/gtranslator
%_datadir/glib-2.0/schemas/org.gnome.gtranslator*.gschema.xml

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gtranslator-2.0
