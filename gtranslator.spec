Summary:	Translation (.po) file editor with many features
Name:		gtranslator
Version:	46.0
Release:	1
License:	GPLv2+
Group:		Editors
URL:		https://projects.gnome.org/gtranslator
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gtranslator/45/gtranslator-%{version}.tar.xz

BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gtksourceview-5)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libgda-6.0)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	itstool
BuildRequires:	yelp-tools
#BuildRequires:	gtk-doc
BuildRequires:	gnome-common
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	gettext-devel
Requires:	gettext
Requires:	iso-codes
Requires:	python3dist(pygobject)
Requires:	python-gobject3

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
%autosetup -p1

%build
%meson 	\
	-Dgtk_doc=false
%meson_build

%install
%meson_install

rm -f %buildroot%_libdir/gtranslator/*.la

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/gtranslator
%{_datadir}/gtksourceview-5/language-specs/gtranslator.lang
%{_datadir}/gtranslator/
%{_datadir}/applications/*.desktop
%{_metainfodir}/org.gnome.Gtranslator.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gtranslator*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.gtranslator*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Gtranslator.gschema.xml
%{_mandir}/man?/*

%files devel
%{_includedir}/gtr-marshal.h
