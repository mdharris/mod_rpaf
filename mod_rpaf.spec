Summary: Reverse Proxy Add Forward module for Apache
Name: mod_rpaf
Version: 0.8
Release: 1
License: Apache
Group: System Environment/Daemons
URL: https://github.com/mdharris/mod_rpaf
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: httpd-devel
Requires: httpd httpd-devel
Autoreq: 0

%description
rpaf is for backend Apache servers what mod_proxy_add_forward is for
frontend Apache servers. It does excactly the opposite of
mod_proxy_add_forward written by Ask Bjørn Hansen. It will also work
with mod_proxy in Apache starting with release 1.3.25 and mod_proxy
that is distributed with Apache2 from version 2.0.36.

%prep
%setup -q -n mod_rpaf-%{version}

%build
export JOBS=%{jobs}
apxs -i -c -n mod_rpaf-2.0.so mod_rpaf.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_libdir}/httpd/modules/ %{buildroot}/usr/local/apache/conf/
mv /usr/local/apache/modules/mod_rpaf-2.0.so %{buildroot}/%{_libdir}/httpd/modules/mod_rpaf-2.0.so
chmod 0755 %{buildroot}/%{_libdir}/httpd/modules/mod_rpaf-2.0.so
install -m0644 -D conf/rpaf.conf $RPM_BUILD_ROOT/etc/httpd/conf.d/mod_rpaf.conf


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/mod_rpaf.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_rpaf.conf

%post
/usr/sbin/apxs -e -A -n rpaf $(apxs -q LIBEXECDIR)/mod_rpaf.so

%preun
/usr/sbin/apxs -e -A -n rpaf $(apxs -q LIBEXECDIR)/mod_rpaf.so

%changelog
* Tue Jul 08 2014 Matt Harris <matt@asmallorange.com> - 0.9
- Updates to mod_rpaf with gnif's and my patches
* Mon Oct 17 2011 Ben Walton <bwalton@artsci.utoronto.ca> - 0.7
- Initial spec file creation
