Summary:	iLBC audio codec for mediastreamer
Summary(pl.UTF-8):	Kodek dźwięku iLBC dla mediastreamera
Name:		mediastreamer-plugin-msilbc
Version:	2.1.2
Release:	5
License:	GPL v2
Group:		Libraries
Source0:	http://linphone.org/releases/old/sources/plugins/msilbc/msilbc-%{version}.tar.gz
# Source0-md5:	e9472ef8ade6b06bf9519f6638a8723f
Patch0:		msilbc-webrtc-libilbc.patch
URL:		http://git.exherbo.org/summer/packages/media-plugins/msilbc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	mediastreamer-devel >= 2.0.0
BuildRequires:	ortp-devel >= 0.16.0
BuildRequires:	pkgconfig
BuildRequires:	webrtc-libilbc-devel
Requires:	mediastreamer >= 2.0.0
Requires:	ortp >= 0.16.0
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
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
