
Name:       check
Summary:    A unit test framework for C
Version:    0.9.8
Release:    1
Group:      Development/Tools
License:    LGPLv2+
URL:        http://check.sourceforge.net/
Source0:    http://download.sourceforge.net/check/%{name}-%{version}.tar.gz
Source100:  check.yaml
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Check is a unit test framework for C. It features a simple interface for 
defining unit tests, putting little in the way of the developer. Tests 
are run in a separate address space, so Check can catch both assertion 
failures and code errors that cause segmentation faults or other signals. 
The output from unit tests can be used within source code editors and IDEs.



%package devel
Summary:    Libraries and headers for developing programs with check
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Libraries and headers for developing programs with check


%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc COPYING.LESSER README
%{_libdir}/libcheck.so.*
%doc %{_infodir}/check*
%doc /usr/share/doc/check


%files devel
%defattr(-,root,root,-)
%{_includedir}/check.h
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

