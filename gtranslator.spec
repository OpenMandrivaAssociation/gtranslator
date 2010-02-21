%define version 1.9.9

Summary:	Translation (.po) file editor with many features
Name:		gtranslator
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2+
Group:		Editors
URL:		http://sourceforge.net/projects/gtranslator/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/%{name}-%{version}.tar.bz2
BuildRequires:  imagemagick
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	libgnomeui2-devel
BuildRequires:	scrollkeeper
BuildRequires:	gtkspell-devel
BuildRequires:	unique-devel
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	libgdl-devel >= 2.27.2-2mdv
BuildRequires:	subversion-devel
BuildRequires:	libsoup-2.4-devel
BuildRequires:	libgdict1.0-devel
BuildRequires:	gucharmap-devel
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
	--disable-scrollkeeper --disable-schemas-install \
	--enable-compile-warnings=maximum \
	--enable-debug=no --disable-static

%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std UPDATE_DESKTOP=true


rm -f %buildroot%_libdir/gtranslator/*.la

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

%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog DEPENDS NEWS README THANKS TODO
%{_sysconfdir}/gconf/schemas/gtranslator.schemas
%{_bindir}/gtranslator
%{_datadir}/gtranslator
%{_libdir}/gtranslator
%{_datadir}/omf/%name
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/*/apps/gtranslator.*
%{_datadir}/pixmaps/*
%{_datadir}/gtk-doc/html/gtranslator

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gtranslator-2.0
