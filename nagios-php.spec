Summary:	Alternative Nagios Interface written in PHP
Summary(pl):	Alternatywny interfejs Nagiosa napisany w PHP
Name:		nagios-php
Version:	0.5.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/nagios-php/%{name}-%{version}.tar.bz2
# Source0-md5:	ad4c00b51d3fe2f66c964843769756a2
URL:		http://nagios-php.sourceforge.net/
Requires:	Smarty
Requires:	nagios >= 1.0
Requires:	nagios < 2.0
Requires:	php
Requires:	php-pear-Auth >= 1.2.3
Requires:	php-pear-Files_Passwd >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}
%define		_sysconfdir /etc/%{name}

%description
Alternative Nagios Interface written in PHP.

%description -l pl
Alternatywny interface Nagiosa napisany w PHP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_appdir}/{html,inc,templates},%{_sysconfdir}}
cp -a php/html/* $RPM_BUILD_ROOT%{_appdir}/html
cp -a php/inc/*  $RPM_BUILD_ROOT%{_appdir}/inc
cp -a smarty/*.tpl $RPM_BUILD_ROOT%{_appdir}/templates

sed -i -e '
s;%%config_dir%%;%{_sysconfdir}/;g
s;%%php_dir%%;%{_appdir}/;g
' $RPM_BUILD_ROOT%{_appdir}/inc/{nagios,blacksmith}.inc.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README TODO
%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_appdir}
