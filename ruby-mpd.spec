%define rname mpd
%define name ruby-%{rname}
%define version 0.2.3
%define release %mkrel 4

Summary: Ruby bindings for libmpd
Name: %{name}
Version: %{version}
Release: %{release}
URL: https://rubyforge.org/
Source0: https://rubyforge.org/frs/download.php/8040/%{rname}-rb-%{version}.tar.gz
License: GPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.6.8
BuildRequires: ruby-devel libmpd-devel

%description
This is the libmpd API module for Ruby.

%prep
%setup -q -n %{rname}-rb-%{version}
perl -pi -e 's/555/755/' setup.rb

%build
ruby setup.rb config
ruby setup.rb setup

#%check
#ruby -Ilib test/test.rb

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot

%files
%defattr(-,root,root)
%doc COPYING INSTALL.en.txt INSTALL.ja.txt
%ruby_sitelibdir/*
