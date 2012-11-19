#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	msilbc
Summary(pl.UTF-8):	msilbc
Name:		msilbc
Version:	2.0.3
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://mirror.lihnidos.org/GNU/savannah/linphone/plugins/sources/%{name}-%{version}.tar.gz
# Source0-md5:	9c8740345dd8ee9732604a8f6a4329e6
Patch0:		%{name}-webrtc-libilbc.patch
URL:		http://git.exherbo.org/summer/packages/media-plugins/msilbc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	webrtc-libilbc-devel
BuildRequires:	libtool
BuildRequires:	mediastreamer-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package devel
Summary:	Header files for msilbc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki msilbc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for msilbc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki msilbc.

%package static
Summary:	Static msilbc library
Summary(pl.UTF-8):	Statyczna biblioteka msilbc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static msilbc library.

%description static -l pl.UTF-8
Statyczna biblioteka msilbc.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/mediastreamer
%dir %{_libdir}/mediastreamer/plugins
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsilbc.so.?
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsilbc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsilbc.so

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsilbc.a
