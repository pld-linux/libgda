Summary:	GNU Data Access library
Summary(pl):	Biblioteka GNU Data Access
Name:		libgda
Version:	0.2.96
Release:	5
License:	LGPL
Group:		Applications/Databases
Source0:	ftp://ftp.gnome-db.org/pub/gnome-db/sources/latest/%{name}-%{version}.tar.gz
Patch0:		%{name}-GNU_GETTEXT.patch
Patch1:		%{name}-openldap.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-c++.patch
Patch4:		%{name}-omf.patch
URL:		http://www.gnome-db.org/
BuildRequires:	GConf-devel
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.0.0
BuildRequires:	gtk-doc
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxml-devel
BuildRequires:	libxslt-devel
BuildRequires:	mysql-devel
BuildRequires:	oaf-devel
BuildRequires:	openldap-devel >= 2.0.0
BuildRequires:	postgresql-devel
BuildRequires:	scrollkeeper
BuildRequires:	unixODBC-devel
Prereq:         scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgda0

%define 	_prefix		/usr/X11R6
%define         _sysconfdir     /etc/X11/GNOME
%define		_omf_dest_dir   %(scrollkeeper-config --omfdir)

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

%package clientcpp
Summary:	GNU Data Access C++ client library
Summary(pl):	Biblioteka kliecka C++ do GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description clientcpp
GNU Data Access C++ client library.

%description clientcpp -l pl
Biblioteka kliencka C++ do GNU Data Access.

%package clientcpp-devel
Summary:	GNU Data Access C++ client library development
Summary(pl):	Dla programistów biblioteki klienckiej C++ do GDA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Prereq:		%{name}-devel

%description clientcpp-devel
GNU Data Access C++ client library.

%description clientcpp-devel -l pl
Pakiet dla programistów u¿ywaj±cych biblioteki klienckiej C++ do GNU
Data Access.

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

%package -n gda-ldap
Summary:	GDA LDAP provider
Summary(pl):	¬ród³o danych LDAP dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}

%description -n gda-ldap
This package contains the GDA LDAP provider.

%description -n gda-ldap -l pl
Pakiet dostarczaj±cy dane z LDAP dla GDA.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--disable-gtk-doc \
	--with-odbc \
	--with-postgres \
	--with-mysql \
	--with-ldap

LD_LIBRARY_PATH=$(pwd)/lib/gda-common/.libs; export LD_LIBRARY_PATH
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
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

%post	clientcpp -p /sbin/ldconfig
%postun	clientcpp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-common.so.*.*
%attr(755,root,root) %{_libdir}/libgda-client.so.*.*
%attr(755,root,root) %{_libdir}/libgda-server.so.*.*
%{_datadir}/gda
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}

%files devel -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-build*
%attr(755,root,root) %{_bindir}/gda-run
%attr(755,root,root) %{_bindir}/gda-config
%attr(755,root,root) %{_libdir}/libgda-common.so
%attr(755,root,root) %{_libdir}/libgda-client.so
%attr(755,root,root) %{_libdir}/libgda-server.so
%attr(755,root,root) %{_libdir}/libgda-common.la
%attr(755,root,root) %{_libdir}/libgda-client.la
%attr(755,root,root) %{_libdir}/libgda-server.la
%dir %{_includedir}/%{name}-%{version}/
%{_includedir}/%{name}-%{version}/gda

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
%{_includedir}/%{name}-%{version}/gda++

%files -n gda-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-odbc-srv

%files -n gda-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-postgres-srv

%files -n gda-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-mysql-srv

%files -n gda-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-ldap-srv
