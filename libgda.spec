# Note that this is NOT a relocatable package
# defaults for redhat
%define name	libgda
%define ver	0.1.0
%define prefix     /usr
%define sysconfdir /etc

%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Summary: GNU Data Access
Name: 		%name
Version:	%ver
Release: 	%rel
Copyright: 	GPL
Group: 		Applications/Databases
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-db/%{name}-%{ver}.tar.gz
BuildRoot: 	/var/tmp/%{name}-%{ver}-root
URL: 		http://www.gnome.org/projects/gnome-db/
DocDir: 	%{prefix}/doc

%description
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome.org/projects/gnome-db), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

%package devel
Summary: GNU Data Access Development
Group: 		Applications/Databases
Requires:	%name = %{PACKAGE_VERSION}

%description devel
GNU Data Access is an attempt to provide uniform access to
 different kinds of data sources (databases, information
 servers, mail spools, etc).
 It is a complete architecture that provides all you need to
 access your data.
 .
 libgda was part of the GNOME-DB project
 (http://www.gnome.org/projects/gnome-db), but has been
 separated from it to allow non-GNOME applications to be
 developed based on it.

%package -n gda-odbc
Summary: GDA ODBC Provider
Group:		Applications/Databases
Requires:	%name = %{PACKAGE_VERSION}

%description -n gda-odbc
GNU Data Access is an attempt to provide uniform access to
 different kinds of data sources (databases, information
 servers, mail spools, etc).
 It is a complete architecture that provides all you need to
 access your data.
 .
 libgda was part of the GNOME-DB project
 (http://www.gnome.org/projects/gnome-db), but has been
 separated from it to allow non-GNOME applications to be
 developed based on it.

 This package includes the GDA ODBC provider

%package -n gda-postgres
Summary: GDA PostgreSQL Provider
Group:		Applications/Databases
Requires:	%name = %{PACKAGE_VERSION}

%description -n gda-postgres
GNU Data Access is an attempt to provide uniform access to
 different kinds of data sources (databases, information
 servers, mail spools, etc).
 It is a complete architecture that provides all you need to
 access your data.
 .
 libgda was part of the GNOME-DB project
 (http://www.gnome.org/projects/gnome-db), but has been
 separated from it to allow non-GNOME applications to be
 developed based on it.

 This package includes the GDA PostgreSQL provider

%package -n gda-mysql
Summary: GDA MySQL Provider
Group:		Applications/Databases
Requires:	%name = %{PACKAGE_VERSION}

%description -n gda-mysql
GNU Data Access is an attempt to provide uniform access to
 different kinds of data sources (databases, information
 servers, mail spools, etc).
 It is a complete architecture that provides all you need to
 access your data.
 .
 libgda was part of the GNOME-DB project
 (http://www.gnome.org/projects/gnome-db), but has been
 separated from it to allow non-GNOME applications to be
 developed based on it.

 This package includes the GDA MySQL provider

%changelog
* Sat Sep 2 2000 Rodrigo Moya <rodrigo@linuxave.net>
- Initial spec imported from old GNOME-DB spec

%prep
%setup

%build

# libtool workaround for alphalinux
%ifarch alpha
  ARCH_FLAGS="--host=alpha-redhat-linux"
%endif

# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir} --with-odbc=/opt/unixodbc --with-postgres=yes --with-mysql=yes
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir} --with-odbc=/opt/unixodbc --with-postgres=yes --with-mysql=yes
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} \
oafinfodir=$RPM_BUILD_ROOT%{prefix}/share/oaf \
idldir=$RPM_BUILD_ROOT%{prefix}/share/idl \
install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep %{prefix}/lib /etc/ld.so.conf > /dev/null ; then
  echo "%{prefix}/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig
							  
%postun
/sbin/ldconfig
							  
%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{prefix}/lib/libgda-common.so*
%{prefix}/lib/libgda-client.so*
%{prefix}/lib/libgda-server.so*
%{prefix}/share/gda/dtd/*
%{prefix}/share/gnome/help/libgda/*

%files devel
%defattr(-, root, root)

%{prefix}/bin/gda-build*
%{prefix}/bin/gda-run
%{prefix}/bin/gda-config
%{prefix}/lib/libgda-common.*a
%{prefix}/lib/libgda-client.*a
%{prefix}/lib/libgda-server.*a
%{prefix}/include/gda/*
%{prefix}/share/idl/*

%files -n gda-odbc
%defattr(-, root, root)

%{prefix}/bin/gda-odbc-srv
%{prefix}/lib/libgda-odbc.so*
%{prefix}/share/oaf/gda-odbc.oafinfo

%files -n gda-postgres
%defattr(-, root, root)

%{prefix}/bin/gda-postgres-srv
%{prefix}/lib/libgda-postgres.so*
%{prefix}/share/oaf/gda-postgres.oafinfo

%files -n gda-mysql
%defattr(-, root, root)

%{prefix}/bin/gda-mysql-srv
%{prefix}/lib/libgda-mysql.so*
%{prefix}/share/oaf/gda-mysql.oafinfo
