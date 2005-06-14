#
# Conditional build:
%bcond_with	firebird	# build without firebird plugin
%bcond_without	freetds		# build without freetds plugin
%bcond_without	ldap		# build without ldap plugin
%bcond_without	mdb		# build without MDB plugin
%bcond_without	mysql		# build without MySQL plugin
%bcond_without	odbc		# build without unixODBC
%bcond_without	pgsql		# build without PostgreSQL plugin
%bcond_without	sqlite		# build without sqlite plugin
%bcond_without	xbase		# build without xbase plugin
#
%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha ppc
%undefine	with_firebird
%endif
Summary:	GNU Data Access library
Summary(pl):	Biblioteka GNU Data Access
Name:		libgda
Version:	1.2.2
Release:	1
License:	LGPL v2/GPL v2
Group:		Applications/Databases
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgda/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	19d5ec3fe7f482fe89bcf6926cfac67e
Patch0:		%{name}-gcc34.patch
Patch1:		%{name}-freetds_buildfix.patch
Patch2:		%{name}-mdb.patch
Patch3:		%{name}-bdb.patch
Patch4:		%{name}-gcc4.patch
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
%{?with_freetds:BuildRequires:	freetds-devel >= 0.62.1}
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.30
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel >= 1.0.9
%{?with_mdb:BuildRequires:	mdbtools-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	perl-base
BuildRequires:	popt-devel
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	scrollkeeper
%{?with_sqlite:BuildRequires:	sqlite3-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xbase:BuildRequires:	xbase-devel >= 2.0.0}
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project but has been separated from it
to allow non-GNOME applications to be developed based on it.

%description -l pl
GNU Data Access to próba zapewnienia jednolitego dostêpu do ró¿nych
¼róde³ danych (bazy danych, serwery informacji, katalogi z poczt±
itp.). Jest kompletn± architektur± dostarczaj±c± wszystko, czego
potrzebujesz do dostêpu do danych.

libgda by³a czê¶ci± projektu GNOME-DB, ale zosta³a wydzielona, aby
pozwoliæ na u¿ywanie przez niegnomowe aplikacje.

%package devel
Summary:	GNU Data Access development
Summary(pl):	Dla programistów GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	gtk-doc-common
Requires:	libxml2-devel
Requires:	libxslt-devel >= 1.0.9
Obsoletes:	libgda0-devel

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data. This subpackage contains development files.

%description devel -l pl
GNU Data Access to próba zapewnienia jednolitego dostêpu do ró¿nych
¼róde³ danych (bazy danych, serwery informacji, katalogi z poczt±
itp.). Jest kompletn± architektur± dostarczaj±c± wszystko, czego
potrzebujesz do dostêpu do danych. Ten podpakiet zawiera pliki dla
programistów u¿ywaj±cych libgda.

%package static
Summary:	GNU Data Access static libraries
Summary(pl):	Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNU Data Access static libraries.

%description static -l pl
Statyczne biblioteki GNU Data Access.

%package -n gda-db
Summary:	GDA Berkeley DB provider
Summary(pl):	¬ród³o danych Berkeley DB dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-db
This package contains the GDA Berkeley DB provider.

%description -n gda-db -l pl
Pakiet dostaczaj±cy dane z Berkeley DB dla GDA.

%package -n gda-firebird
Summary:	GDA Firebird provider
Summary(pl):	¬ród³o danych Firebird dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-firebird
This package contains the GDA Firebird provider.

%description -n gda-firebird -l pl
Pakiet dostarczaj±cy dane z Firebird dla GDA.

%package -n gda-freetds
Summary:	GDA FreeTDS provider
Summary(pl):	¬ród³o danych FreeTDS dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-freetds
This package contains the GDA FreeTDS provider.

%description -n gda-freetds -l pl
Pakiet dostarczaj±cy dane z FreeTDS dla GDA.

%package -n gda-ldap
Summary:	GDA LDAP provider
Summary(pl):	¬ród³o danych LDAP dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-ldap
This package contains the GDA LDAP provider.

%description -n gda-ldap -l pl
Pakiet dostarczaj±cy dane z LDAP dla GDA

%package -n gda-mdb
Summary:	GDA MDB provider
Summary(pl):	¬ród³o danych MDB
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-mdb
This package contains the GDA MDB provider.

%description -n gda-mdb -l pl
Pakiet dostarczaj±cy dane z MDB dla GDA.

%package -n gda-mysql
Summary:	GDA MySQL provider
Summary(pl):	¬ród³o danych MySQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgda-mysql0

%description -n gda-mysql
This package contains the GDA MySQL provider.

%description -n gda-mysql -l pl
Pakiet dostarczaj±cy dane z MySQL dla GDA.

%package -n gda-odbc
Summary:	GDA ODBC provider
Summary(pl):	¬ród³o danych ODBC dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-odbc
This package contains the GDA ODBC provider.

%description -n gda-odbc -l pl
Pakiet dostarczaj±cy dane z ODBC dla GDA.

%package -n gda-postgres
Summary:	GDA PostgreSQL provider
Summary(pl):	¬ród³o danych PostgreSQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgda-postgres0

%description -n gda-postgres
This package contains the GDA PostgreSQL provider.

%description -n gda-postgres -l pl
Pakiet dostarczaj±cy dane z PostgreSQL dla GDA.

%package -n gda-sqlite
Summary:	GDA SQLite provider
Summary(pl):	¬ród³o danych SQLite dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-sqlite
This package contains the GDA SQLite provider.

%description -n gda-sqlite -l pl
Pakiet dostarczaj±cy dane z SQLite dla GDA.

%package -n gda-xbase
Summary:	GDA xBase provider
Summary(pl):	¬ród³o danych xBase dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n gda-xbase
This package contains the GDA xBase (dBase, Clipper, FoxPro) provider.

%description -n gda-xbase -l pl
Pakiet dostarczaj±cy dane z xBase (dBase, Clippera, FoxPro) dla GDA.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with%{!?with_firebird:out}-firebird \
	--with%{!?with_ldap:out}-ldap \
	--with%{!?with_mdb:out}-mdb \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_odbc:out}-odbc \
	--with%{!?with_pgsql:out}-postgres \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_freetds:out}-tds \
	--with%{!?with_xbase:out}-xbase \
	--without-oracle
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} 

# modules dlopened by *.so through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/libgda/providers/*.{a,la}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-config-tool
%attr(755,root,root) %{_libdir}/libgda-2.so.*.*
%attr(755,root,root) %{_libdir}/libgda-report-2.so.*.*
%attr(755,root,root) %{_libdir}/libgdasql.so.*.*
%dir %{_libdir}/libgda
%dir %{_libdir}/libgda/providers
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-xml.so
%{_datadir}/libgda
%{_omf_dest_dir}/%{name}
%dir %{_sysconfdir}/libgda
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/libgda/config
%{_mandir}/man1/gda-config-tool.1*
%{_mandir}/man5/*

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
%{_pkgconfigdir}/*
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

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

%if %{with xbase}
%files -n gda-xbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-xbase.so
%endif
