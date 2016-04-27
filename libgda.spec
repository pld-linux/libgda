#
# Conditional build:
%bcond_without	firebird	# Firebird plugin
%bcond_with	freetds		# FreeTDS plugin
%bcond_without	ldap		# LDAP plugin
%bcond_without	mdb		# MDB plugin
%bcond_with	mdb05		# use mdb < 0.6pre1
%bcond_without	mysql		# MySQL plugin
%bcond_with	oci		# Oracle DB plugin
%bcond_without	odbc		# unixODBC plugin
%bcond_without	pgsql		# PostgreSQL plugin
%bcond_without	sqlite		# SQLite plugin
%bcond_without	sybase		# sybase plugin
%bcond_without	xbase		# xbase plugin

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha ppc
%undefine	with_firebird
%endif
Summary:	GNU Data Access library
Summary(pl.UTF-8):	Biblioteka GNU Data Access
Name:		libgda
Version:	1.2.4
Release:	24
Epoch:		1
License:	LGPL v2+/GPL v2+
Group:		Applications/Databases
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgda/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	512a8ed842ce98eb432e69bd6867f437
Patch0:		%{name}-mdb.patch
Patch1:		%{name}-sqlite.patch
Patch2:		%{name}-configure.patch
Patch3:		%{name}-freetds064.patch
Patch4:		%{name}-xbase.patch
Patch5:		%{name}-mdb2.patch
Patch6:		%{name}-gtk-doc.patch
Patch7:		%{name}-sybase.patch
Patch8:		%{name}-firebird.patch
Patch9:		glib.patch
Patch10:	%{name}-xml.patch
Patch11:	%{name}-format.patch
Patch12:	%{name}-mdb-0.7.patch
Patch13:	x32.patch
URL:		http://www.gnome-db.org/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	flex
%{?with_freetds:BuildRequires:	freetds-devel = 0.64}
%{?with_sybase:BuildRequires:	freetds-devel >= 0.82}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
%if %{with_mdb}
%{?with_mdb05:BuildRequires:	mdbtools-devel < 0.6}
%{!?with_mdb05:BuildRequires:	mdbtools-devel >= 0.6}
%endif
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
%{?with_oci:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	scrollkeeper
%{?with_sqlite:BuildRequires:	sqlite3-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xbase:BuildRequires:	xbase-devel >= 2.0.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project but has been separated from it
to allow non-GNOME applications to be developed based on it.

%description -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych.

libgda była częścią projektu GNOME-DB, ale została wydzielona, aby
pozwolić na używanie przez niegnomowe aplikacje.

%package devel
Summary:	GNU Data Access development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.12.1
Requires:	libxml2-devel >= 1:2.6.26
Requires:	libxslt-devel >= 1.1.17
Obsoletes:	libgda0-devel

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data. This subpackage contains development files.

%description devel -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych. Ten podpakiet zawiera pliki dla
programistów używających libgda.

%package static
Summary:	GNU Data Access static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNU Data Access static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNU Data Access.

%package apidocs
Summary:	libgda API documentation
Summary(pl.UTF-8):	Dokumentacja API libgda
Group:		Documentation
Requires(post,postun):	scrollkeeper
Requires:	gtk-doc-common
Requires:	scrollkeeper
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libgda API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgda.

%package -n gda-db
Summary:	GDA Berkeley DB provider
Summary(pl.UTF-8):	Źródło danych Berkeley DB dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-db
This package contains the GDA Berkeley DB provider.

%description -n gda-db -l pl.UTF-8
Pakiet dostarczający dane z Berkeley DB dla GDA.

%package -n gda-firebird
Summary:	GDA Firebird provider
Summary(pl.UTF-8):	Źródło danych Firebird dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-firebird
This package contains the GDA Firebird provider.

%description -n gda-firebird -l pl.UTF-8
Pakiet dostarczający dane z Firebird dla GDA.

%package -n gda-freetds
Summary:	GDA FreeTDS provider
Summary(pl.UTF-8):	Źródło danych FreeTDS dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-freetds
This package contains the GDA FreeTDS provider.

%description -n gda-freetds -l pl.UTF-8
Pakiet dostarczający dane z FreeTDS dla GDA.

%package -n gda-ldap
Summary:	GDA LDAP provider
Summary(pl.UTF-8):	Źródło danych LDAP dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-ldap
This package contains the GDA LDAP provider.

%description -n gda-ldap -l pl.UTF-8
Pakiet dostarczający dane z LDAP dla GDA

%package -n gda-mdb
Summary:	GDA MDB provider
Summary(pl.UTF-8):	Źródło danych MDB
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_mdb05:Requires:	mdbtools-libs < 0.6}
%{!?with_mdb05:Requires:	mdbtools-libs >= 0.6}

%description -n gda-mdb
This package contains the GDA MDB provider.

%description -n gda-mdb -l pl.UTF-8
Pakiet dostarczający dane z MDB dla GDA.

%package -n gda-mysql
Summary:	GDA MySQL provider
Summary(pl.UTF-8):	Źródło danych MySQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libgda-mysql0

%description -n gda-mysql
This package contains the GDA MySQL provider.

%description -n gda-mysql -l pl.UTF-8
Pakiet dostarczający dane z MySQL dla GDA.

%package -n gda-odbc
Summary:	GDA ODBC provider
Summary(pl.UTF-8):	Źródło danych ODBC dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-odbc
This package contains the GDA ODBC provider.

%description -n gda-odbc -l pl.UTF-8
Pakiet dostarczający dane z ODBC dla GDA.

%package -n gda-oracle
Summary:	GDA Oracle provider
Summary(pl.UTF-8):	Źródło danych Oracle dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gda-oracle
This package contains the GDA Oracle provider.

%description -n gda-oracle -l pl.UTF-8
Pakiet dostarczający dane z bazy Oracle dla GDA.

%package -n gda-postgres
Summary:	GDA PostgreSQL provider
Summary(pl.UTF-8):	Źródło danych PostgreSQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libgda-postgres0

%description -n gda-postgres
This package contains the GDA PostgreSQL provider.

%description -n gda-postgres -l pl.UTF-8
Pakiet dostarczający dane z PostgreSQL dla GDA.

%package -n gda-sqlite
Summary:	GDA SQLite provider
Summary(pl.UTF-8):	Źródło danych SQLite dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-sqlite
This package contains the GDA SQLite provider.

%description -n gda-sqlite -l pl.UTF-8
Pakiet dostarczający dane z SQLite dla GDA.

%package -n gda-sybase
Summary:	GDA Sybase provider
Summary(pl.UTF-8):	Źródło danych Sybase dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-sybase
This package contains the GDA Sybase provider.

%description -n gda-sybase -l pl.UTF-8
Pakiet dostarczający dane z Sybase dla GDA.

%package -n gda-xbase
Summary:	GDA xBase provider
Summary(pl.UTF-8):	Źródło danych xBase dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gda-xbase
This package contains the GDA xBase (dBase, Clipper, FoxPro) provider.

%description -n gda-xbase -l pl.UTF-8
Pakiet dostarczający dane z xBase (dBase, Clippera, FoxPro) dla GDA.

%prep
%setup -q
%if %{with mdb05}
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	__lib=%{_lib} \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with-firebird%{!?with_firebird:=no} \
	--with-ldap%{!?with_ldap:=no} \
	--with-mdb%{!?with_mdb:=no} \
	--with-mysql%{!?with_mysql:=no} \
	--with-odbc%{!?with_odbc:=no} \
	--with-oracle%{!?with_oci:=no} \
	--with-postgres%{!?with_pgsql:=no} \
	--with-sqlite%{!?with_sqlite:=no} \
	%{?with_sybase:--with-sybase=/usr} \
	--with-tds%{!?with_freetds:=no} \
	--with-xbase%{!?with_xbase:=no}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules dlopened by *.so through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgda/providers/*.{a,la}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@Latn,sr@latin}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post apidocs
%scrollkeeper_update_post

%postun apidocs
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-config-tool
%attr(755,root,root) %{_libdir}/libgda-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-2.so.3
%attr(755,root,root) %{_libdir}/libgda-report-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-report-2.so.3
%attr(755,root,root) %{_libdir}/libgdasql.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdasql.so.3
%dir %{_libdir}/libgda
%dir %{_libdir}/libgda/providers
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-xml.so
%{_datadir}/libgda
%dir %{_sysconfdir}/libgda
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libgda/config
%{_mandir}/man1/gda-config-tool.1*
%{_mandir}/man5/gda-config.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-report-test
%attr(755,root,root) %{_bindir}/gda-run
%attr(755,root,root) %{_bindir}/gda-test
%attr(755,root,root) %{_libdir}/libgda-2.so
%attr(755,root,root) %{_libdir}/libgda-report-2.so
%attr(755,root,root) %{_libdir}/libgdasql.so
%{_libdir}/libgda-2.la
%{_libdir}/libgda-report-2.la
%{_libdir}/libgdasql.la
%{_includedir}/libgda-1.2
%{_pkgconfigdir}/libgda.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgda-2.a
%{_libdir}/libgda-report-2.a
%{_libdir}/libgdasql.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgda
%{_omf_dest_dir}/%{name}

%files -n gda-db
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-bdb.so

%if %{with firebird}
%files -n gda-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-firebird.so
%endif

%if %{with freetds}
%files -n gda-freetds
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-freetds.so
%endif

%if %{with ldap}
%files -n gda-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-ldap.so
%endif

%if %{with mdb}
%files -n gda-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-mdb.so
%endif

%if %{with mysql}
%files -n gda-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-mysql.so
%endif

%if %{with odbc}
%files -n gda-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-odbc.so
%endif

%if %{with oci}
%files -n gda-oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-oracle.so
%endif

%if %{with pgsql}
%files -n gda-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-postgres.so
%endif

%if %{with sqlite}
%files -n gda-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-sqlite.so
%endif

%if %{with sybase}
%files -n gda-sybase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-sybase.so
%endif

%if %{with xbase}
%files -n gda-xbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-xbase.so
%endif
