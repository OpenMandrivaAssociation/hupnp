%define srcname herqq

Name:           hupnp
Summary:        Qt string template engine based on the Django template system
Group:          System/Libraries
Version:        1.0.0
Release:        %mkrel 1
License:        LGPLv3+
URL:            http://www.herqq.org
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{srcname}-%{version}.zip
BuildRequires:  qt4-devel



%description
Herqq UPnP (HUPnP) is a software library for building UPnP devices and control 
points conforming to the UPnP Device Architecture version 1.1. It is designed 
to be simple to use and robust in operation. It is built using C++ and the Qt 
Framework following many of the design principles and programming practices 
used in the Qt Framework. It integrates into Qt-based software smoothly and 
enables truly rapid UPnP development.

%files
%defattr(-,root,root,-)

#--------------------------------------------------------------------
%define hupnp_major 1
%define libhupnp %mklibname hupnp %{hupnp_major}

%package -n %{libhupnp}
Summary: Library for %{name}

%description -n %{libhupnp}
Software library for building UPnP devices and control points.

%files -n %{libhupnp}
%defattr(-,root,root)
%{_libdir}/libHUpnp.so.%{hupnp_major}*

#--------------------------------------------------------------------
%define qtsolution_major 1
%define libqtsolution %mklibname libqtsolution %{qtsolution_major}

%package -n %{libqtsolution}
Summary: Library for %{name}

%description -n %{libqtsolution}
Library for %{name}

%files -n %{libqtsolution} 
%defattr(-,root,root)
%{_libdir}/libQtSolutions_SOAP-2.7.so.%{qtsolution_major}*


#--------------------------------------------------------------------

%package devel
Summary:        Development files for %{name}
Group:          Development/C++  
Requires:       %{libqtsolution} = %{version}-%{release}
Requires:       %{libhupnp} = %{version}-%{release}

%description devel
Libraries and header files to develop applications that use %{name}.

%files devel
%defattr(-,root,root,-)
%{_includedir}/HUpnpCore/
%{_libdir}/libQtSolutions_SOAP-2.7.so
%{_libdir}/libHUpnp.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}

%build
%qmake_qt4 %{srcname}.pro

%make



%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}/usr/include/HUpnpCore
pushd hupnp/bin
mv lib* %{buildroot}%{_libdir}
popd
pushd hupnp/deploy/include/HUpnpCore/
mv * %{buildroot}/usr/include/HUpnpCore/
popd


%clean
rm -rf %{buildroot}





%changelog
* Fri Sep 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2012.0
+ Revision: 697777
- import hupnp

