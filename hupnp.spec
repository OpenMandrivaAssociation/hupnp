%define srcname herqq
%define api 2.7
%define debug_package %{nil}

Name:		hupnp
Summary:	Qt4-based software library for building UPnP devices and control points
Group:		System/Libraries
Version:	1.0.0
Release:	15
License:	LGPLv3+
URL:		https://www.herqq.org
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{srcname}-%{version}.zip
Patch0:		patch-hmulticast_socket.cpp
Patch1:		patch-hupnp__src__devicehosting__devicehost__hpresence_announcer_p.h
BuildRequires:	qt4-devel

%description
Herqq UPnP (HUPnP) is a software library for building UPnP devices and control 
points conforming to the UPnP Device Architecture version 1.1. It is designed 
to be simple to use and robust in operation. It is built using C++ and the Qt 
Framework following many of the design principles and programming practices 
used in the Qt Framework. It integrates into Qt-based software smoothly and 
enables truly rapid UPnP development.

%files

#--------------------------------------------------------------------
%define hupnp_major 1
%define libhupnp %mklibname hupnp %{hupnp_major}

%package -n %{libhupnp}
Summary:	Library for %{name}

%description -n %{libhupnp}
Software library for building UPnP devices and control points.

%files -n %{libhupnp}
%{_libdir}/libHUpnp.so.%{hupnp_major}*

#--------------------------------------------------------------------
%define qtsolution_major 1
%define libqtsolution %mklibname qtsolution %{api} %{qtsolution_major}

%package -n %{libqtsolution}
Summary:	Library for %{name}

%description -n %{libqtsolution}
Library for %{name}

%files -n %{libqtsolution}
%{_libdir}/libQtSolutions_SOAP-%{api}.so.%{qtsolution_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libqtsolution} = %{version}-%{release}
Requires:	%{libhupnp} = %{version}-%{release}

%description devel
Libraries and header files to develop applications that use %{name}.

%files devel
%{_includedir}/HUpnpCore/
%{_libdir}/libQtSolutions_SOAP-%{api}.so
%{_libdir}/libHUpnp.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}
%autopatch -p1

%build
%qmake_qt4 %{srcname}.pro CONFIG+="DISABLE_AVTESTAPP DISABLE_TESTAPP"

%make CXX=%{__cxx} CC=%{__cc} LINK=%{__cxx}

%install
%makeinstall_std
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}/usr/include/HUpnpCore
pushd hupnp/bin
mv lib* %{buildroot}%{_libdir}
popd
pushd hupnp/deploy/include/HUpnpCore/
mv * %{buildroot}/usr/include/HUpnpCore/
popd

