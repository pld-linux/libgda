#
# Conditional build:
# _without_freetds  - build without freetds plugin
# _without_ldap     - build without ldap plugin
# _without_mysql    - build without MySQL plugin
# _without_odbc     - build without unixODBC
# _without_pgsql    - build without PostgreSQL plugin
# _without_sqlite   - build without sqlite plugin
#
Summary:	GNU Data Access library
Summary(pl):	Biblioteka GNU Data Access
Name:		libgda
Version:	0.11.0
Release:	1
License:	LGPL
Group:		Applications/Databases
Source0:	ftp://ftp.gnome-db.org/pub/gnome-db/sources/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5: 7b51bcd5dc414fa770bc48646e497bc0
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_freetds:BuildRequires:	freetds-devel >= 0.61}
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel >= 1.0.9
%{!?_without_mysql:BuildRequires:	mysql-devel}
%{!?_without_ldap:BuildRequires:	openldap-devel}
%{!?_without_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	scrollkeeper
%{!?_without_sqlite:BuildRequires:	sqlite-devel}
%{!?_without_odbc:BuildRequires:	unixODBC-devel}
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
itp.). Jest kompletn± architektuj± dostarczaj±c± wszystko co
potrzebujesz do dostêpu do danych.

libgda by³a czê¶ci± projektu GNOME-DB, ale zosta³a wydzielona, aby
pozwoliæ na u¿ywanie przez niegnomowe aplikacje.

%package devel
Summary:	GNU Data Access development
Summary(pl):	Dla programistów GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libgda0-devel

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data. This subpackage contains development files.

%description devel -l pl
GNU Data Access to próba zapewnienia jednolitego dostêpu do ró¿nych
¼róde³ danych (bazy danych, serwery informacji, katalogi z poczt±
itp.). Jest kompletn± architektuj± dostarczaj±c± wszystko co
potrzebujesz do dostêpu do danych. Ten podpakiet zawiera pliki dla
programistów u¿ywaj±cych libgda.

%package static
Summary:	GNU Data Access static libraries
Summary(pl):	Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNU Data Access static libraries.

%description static -l pl
Statyczne biblioteki GNU Data Access.

%package -n gda-odbc
Summary:	GDA ODBC provider
Summary(pl):	¬ród³o danych ODBC dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}

%description -n gda-odbc
This package contains the GDA ODBC provider.

%description -n gda-odbc -l pl
Pakiet dostaczaj±cy dane z ODBC dla GDA.

%package -n gda-postgres
Summary:	GDA PostgreSQL provider
Summary(pl):	¬ród³o danych PostgreSQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}
Obsoletes:	libgda-postgres0

%description -n gda-postgres
This package contains the GDA PostgreSQL provider.

%description -n gda-postgres -l pl
Pakiet dostarczaj±cy dane z PostgreSQL dla GDA.

%package -n gda-mysql
Summary:	GDA MySQL provider
Summary(pl):	¬ród³o danych MySQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}
Obsoletes:	libgda-mysql0

%description -n gda-mysql
This package contains the GDA MySQL provider.

%description -n gda-mysql -l pl
Pakiet dostarczaj±cy dane z MySQL dla GDA.

%package -n gda-sqlite
Summary:	GDA SQLite provider
Summary(pl):	¬ród³o danych SQLite dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}

%description -n gda-sqlite
This package contains the GDA SQLite provider.

%description -n gda-sqlite -l pl
Pakiet dostarczaj±cy dane z SQLite dla GDA.

%package -n gda-freetds
Summary:	GDA FreeTDS provider
Summary(pl):	¬ród³o danych FreeTDS dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}

%description -n gda-freetds
This package contains the GDA FreeTDS provider.

%description -n gda-freetds -l pl
Pakiet dostarczaj±cy dane z FreeTDS dla GDA.

%package -n gda-ldap
Summary:	GDA LDAP provider
Summary(pl):	¬ród³o danych LDAP dla GDA
Group:		Applications/Database
Requires:	%{name} = %{version}

%description -n gda-ldap
This package contains the GDA LDAP provider.

%description -n gda-ldap -l pl
Pakiet dostarczaj±cy dane z LDAP dla GDA

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
			--enable-gtk-doc \
			--with-html-dir=%{_gtkdocdir} \
%{?_without_freetds:	--without-tds} \
%{!?_without_freetds:	--with-tds} \
%{?_without_odbc:	--without-odbc} \
%{!?_without_odbc:	--with-odbc} \
%{?_without_pgsql:	--without-postgres} \
%{!?_without_pgsql:	--with-postgres} \
%{?_without_mysql:	--without-mysql} \
%{!?_without_mysql:	--with-mysql} \
%{?_without_sqlite:	--without-sqlite} \
%{!?_without_sqlite:	--with-sqlite} \
%{?_without_ldap:	--without-ldap} \
%{!?_without_ldap:	--with-ldap} \
			--without-oracle

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir} \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

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
%{_sysconfdir}/libgda
%attr(755,root,root) %{_libdir}/libgda-2.so.*.*
%attr(755,root,root) %{_libdir}/libgda-report-2.so.*.*
%attr(755,root,root) %{_libdir}/libgdasql.so.*.*
%dir %{_libdir}/libgda
%dir %{_libdir}/libgda/providers
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-default.so
%{_libdir}/libgda/providers/libgda-default.la
%{_datadir}/libgda
%{_omf_dest_dir}/%{name}
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-config-tool
%attr(755,root,root) %{_bindir}/gda-run
%attr(755,root,root) %{_bindir}/gda-test
%attr(755,root,root) %{_libdir}/libgda-2.so
%attr(755,root,root) %{_libdir}/libgda-report-2.so
%attr(755,root,root) %{_libdir}/libgdasql.so
%{_libdir}/libgda-2.la
%{_libdir}/libgda-report-2.la
%{_libdir}/libgdasql.la
%{_includedir}/libgda
%{_includedir}/libgda-report
%{_pkgconfigdir}/*
%{_mandir}/man1/*
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{!?_without_odbc:1}0
%files -n gda-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-odbc.so
%{_libdir}/libgda/providers/libgda-odbc.la
%endif

%if %{!?_without_pgsql:1}0
%files -n gda-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-postgres.so
%{_libdir}/libgda/providers/libgda-postgres.la
%endif

%if %{!?_without_mysql:1}0
%files -n gda-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-mysql.so
%{_libdir}/libgda/providers/libgda-mysql.la
%endif

%if %{!?_without_sqlite:1}0
%files -n gda-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-sqlite.so
%{_libdir}/libgda/providers/libgda-sqlite.la
%endif

%if %{!?_without_freetds:1}0
%files -n gda-freetds
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-freetds.so
%{_libdir}/libgda/providers/libgda-freetds.la
%endif

%if %{!?_without_ldap:1}0
%files -n gda-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda/providers/libgda-ldap.so
%{_libdir}/libgda/providers/libgda-ldap.la
%endif
