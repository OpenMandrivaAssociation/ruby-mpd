%define rname mpd
%define debug_package %{nil}

Summary: Ruby bindings for libmpd
Name:    ruby-%{rname}
Version: 0.2.3
Release: 7
URL: https://rubyforge.org/
Source0: https://rubyforge.org/frs/download.php/8040/%{rname}-rb-%{version}.tar.gz
License: GPL
Group: Development/Ruby
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

%install
ruby setup.rb install --prefix=%buildroot

%files
%doc COPYING INSTALL.en.txt INSTALL.ja.txt
%{ruby_sitelibdir}/*
