#
Summary:	msilbc
Summary(pl.UTF-8):	msilbc
Name:		msilbc
Version:	2.0.1
Release:	0.1
License:	GPL v2
Group:		Developement/Libraries
Source0:	http://mirror.lihnidos.org/GNU/savannah/linphone/plugins/sources/%{name}-%{version}.tar.gz
# Source0-md5:	ec2855c57b4344f14fbbc8cfd4c433fe
URL:		http://git.exherbo.org/summer/packages/media-plugins/msilbc
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package devel
Summary:	Header files for ... library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ...
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ... library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl.UTF-8):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl.UTF-8
Statyczna biblioteka ....

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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

%files devel
%defattr(644,root,root,755)

%files static
%defattr(644,root,root,755)
