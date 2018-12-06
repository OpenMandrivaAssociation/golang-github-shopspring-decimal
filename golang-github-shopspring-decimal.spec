# Run tests in check section
# https://github.com/shopspring/decimal/issues/101
%ifarch aarch64
%bcond_with check
%else
%bcond_without check
%endif

# https://github.com/shopspring/decimal
%global goipath         github.com/shopspring/decimal
Version:                1.1.0

%global common_description %{expand:
Arbitrary-precision fixed-point decimal numbers in go.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Arbitrary-precision fixed-point decimal numbers in go
License:        MIT
URL:            %{gourl}
Source0:        %{gourl}/archive/%{version}/decimal-%{version}.tar.gz

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Tue Jul 17 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1
- Bump to version 1.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- First package for Fedora

