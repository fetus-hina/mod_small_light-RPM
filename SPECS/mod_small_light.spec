Summary: Dynamic image transformation module for Apache2.
Name: mod_small_light
Version: 1.1.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Daemons
URL: http://labs.edge.jp/smalllight/

Packager: HiNa <hina@jp3cki.jp>

Source0: http://smalllight.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel, httpd-devel, imlib2-devel, ImageMagick-devel
Requires: httpd, imlib2, ImageMagick

%description
Dynamic image transformation module for Apache2.


%prep
%setup

%{__cat} <<EOF >mod_small_light.conf
LoadModule small_light_module       modules/mod_small_light.so
EOF

%build
%configure --with-apxs=%{_sbindir}/apxs --without-Wand
make

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 .libs/mod_small_light.so %{buildroot}%{_libdir}/httpd/modules/mod_small_light.so
%{__install} -Dp -m0644 mod_small_light.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_small_light.conf
%{__install} -Dp -m0644 ChangeLog %{buildroot}%{_defaultdocdir}/%{name}-%{version}/ChangeLog
%{__install} -Dp -m0644 LICENSE %{buildroot}%{_defaultdocdir}/%{name}-%{version}/LICENSE
%{__install} -Dp -m0644 README  %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README
%{__install} -Dp -m0644 README.imlib2 %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README.imlib2
%{__install} -Dp -m0644 README.JA %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README.JA

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_defaultdocdir}/%{name}-%{version}/ChangeLog
%config(noreplace) %{_defaultdocdir}/%{name}-%{version}/LICENSE
%config(noreplace) %{_defaultdocdir}/%{name}-%{version}/README
%config(noreplace) %{_defaultdocdir}/%{name}-%{version}/README.imlib2
%config(noreplace) %{_defaultdocdir}/%{name}-%{version}/README.JA
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_small_light.conf
%{_libdir}/httpd/modules/mod_small_light.so

%changelog
* Fri Apr 27 2012 HiNa <hina@jp3cki.jp> - 1.1.1
- Initial package.
