Summary:	GNU Data Access library
Name:		libgda
Version:	0.1.0
Release:	1
License:	GPL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-db/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared_libmysqlclient.patch
PAtch1:		%{name}-DESTDIR.patch
URL:		http://www.gnome.org/projects/gnome-db/
BuildRequires:	GConf-devel
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml-devel
BuildRequires:	mysql-devel
BuildRequires:	oaf-devel
BuildRequires:	openldap-devel
BuildRequires:	postgresql-devel
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project but has been separated from it
to allow non-GNOME applications to be developed based on it.

%package devel
Summary:	GNU Data Access development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

%package static
Summary:	GNU Data Access static libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
GNU Data Access static libraries.

%package clientcpp
Summary:	GNU Data Access C++ client library
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description clientcpp
GNU Data Access C++ client library.

%package clientcpp-devel
Summary:	GNU Data Access C++ client library development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Prereq:		%{name}-devel

%description clientcpp-devel
GNU Data Access C++ client library.

%package -n gda-odbc
Summary:	GDA ODBC provider
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description -n gda-odbc
This package contains the GDA ODBC provider.

%package -n gda-postgres
Summary:	GDA PostgreSQL provider
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description -n gda-postgres
This package contains the GDA PostgreSQL provider.

%package -n gda-mysql
Summary:	GDA MySQL provider
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description -n gda-mysql
This package contains the GDA MySQL provider.

%package -n gda-ldap
Summary:	GDA LDAP provider
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description -n gda-ldap
This package contains the GDA LDAP provider.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
automake
autoconf
CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS -fno-rtti -fno-exceptions}%{?debug:-O -g}"
%configure \
	--with-odbc \
	--with-postgres \
	--with-mysql \
	--with-ldap

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n gda-odbc -p /sbin/ldconfig
%postun -n gda-odbc -p /sbin/ldconfig

%post   -n gda-postgres -p /sbin/ldconfig
%postun -n gda-postgres -p /sbin/ldconfig

%post   -n gda-mysql -p /sbin/ldconfig
%postun -n gda-mysql -p /sbin/ldconfig

%post   -n gda-ldap -p /sbin/ldconfig
%postun -n gda-ldap -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-common.so.*.*
%attr(755,root,root) %{_libdir}/libgda-client.so.*.*
%attr(755,root,root) %{_libdir}/libgda-server.so.*.*
%{_datadir}/gda

%files devel -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gda-build*
%attr(755,root,root) %{_bindir}/gda-run
%attr(755,root,root) %{_bindir}/gda-config
%attr(755,root,root) %{_libdir}/libgda-common.so
%attr(755,root,root) %{_libdir}/libgda-client.so
%attr(755,root,root) %{_libdir}/libgda-server.so
%attr(755,root,root) %{_libdir}/libgda-common.la
%attr(755,root,root) %{_libdir}/libgda-client.la
%attr(755,root,root) %{_libdir}/libgda-server.la
%dir %{_includedir}/gda/
%{_includedir}/gda/*.h
%{_datadir}/idl/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files clientcpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-clientcpp.so.*.*

%files clientcpp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-clientcpp.so
%attr(755,root,root) %{_libdir}/libgda-clientcpp.la
%{_includedir}/gda/gda++

%files -n gda-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-odbc-srv
%{_libdir}/libgda-odbc.so.*.*
%{_datadir}/oaf/gda-odbc.oafinfo

%files -n gda-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-postgres-srv
%{_libdir}/libgda-postgres.so.*.*
%{_datadir}/oaf/gda-postgres.oafinfo

%files -n gda-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-mysql-srv
%{_libdir}/libgda-mysql.so.*.*
%{_datadir}/oaf/gda-mysql.oafinfo

%files -n gda-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-ldap-srv
%{_libdir}/libgda-ldap.so.*.*
%{_datadir}/oaf/gda-ldap.oafinfo
