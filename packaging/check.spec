Name:           check
Version:        0.9.8
Release:        1
License:        LGPL-2.0+
Summary:        A unit test framework for C
Url:            http://check.sourceforge.net/
Group:          Development/Tools
Source0:        http://download.sourceforge.net/check/%{name}-%{version}.tar.gz
Source1001:     check.manifest
BuildRequires:  texinfo
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests
are run in a separate address space, so Check can catch both assertion
failures and code errors that cause segmentation faults or other signals.
The output from unit tests can be used within source code editors and IDEs.

%package devel
Summary:        Libraries and headers for developing programs with check
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
Libraries and headers for developing programs with check

%prep
%setup -q

%build
cp %{SOURCE1001} .

%configure 

make %{?_smp_mflags}

%install
%make_install


%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%manifest check.manifest
%doc COPYING.LESSER
%{_libdir}/libcheck.so.*


%files devel
%manifest check.manifest
%{_includedir}/check.h
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

