%define		plugin	cycle
Summary:	jQuery Cycle Plugin
Name:		jquery-%{plugin}
Version:	3.0.3
Release:	1
License:	MIT/GPL
Group:		Applications/WWW
Source0:	https://github.com/malsup/cycle/archive/ac38c7b6/%{plugin}-%{version}.tar.gz
# Source0-md5:	f86c9e0c5eda6347dca18ed41742e229
URL:		http://jquery.malsup.com/cycle/
Requires:	jquery >= 1.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
The jQuery Cycle Plugin is a slideshow plugin that supports many
different types of transition effects. It supports pause-on-hover,
auto-stop, auto-fit, before/after callbacks, click triggers and much
more. It also supports, but does not require, the Easing Plugin.

The plugin provides a method called cycle which is invoked on a
container element. Each child element of the container becomes a
"slide". Options control how and when the slides are transitioned.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv cycle-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.all.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
