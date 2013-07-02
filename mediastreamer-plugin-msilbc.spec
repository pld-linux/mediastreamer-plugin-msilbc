Summary:	iLBC audio codec for mediastreamer
Summary(pl.UTF-8):	Kodek dźwięku iLBC dla mediastreamera
Name:		mediastreamer-plugin-msilbc
Version:	2.0.3
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://download-mirror.savannah.gnu.org/releases/linphone/plugins/sources/msilbc-%{version}.tar.gz
# Source0-md5:	9c8740345dd8ee9732604a8f6a4329e6
Patch0:		msilbc-webrtc-libilbc.patch
URL:		http://git.exherbo.org/summer/packages/media-plugins/msilbc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	ortp-devel >= 0.16.0
BuildRequires:	webrtc-libilbc-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	mediastreamer-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	mediastreamer >= 2.0.0
Obsoletes:	msilbc
Obsoletes:	msilbc-devel
Obsoletes:	msilbc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin for the iLBC audio
codec, which is necessary to use the codec with Linphone.

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do kodeka dźwięku iLBC,
niezbędną do używania tego kodeka w programie Linphone.

%prep
%setup -q -n msilbc-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmsilbc.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsilbc.so*