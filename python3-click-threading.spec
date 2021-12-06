%define		module		click_threading
%define		pypi_name	click-threading
Summary:	Multithreaded Click apps made easy
Name:		python3-click-threading
Version:	0.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-threading/
Source0:	https://files.pythonhosted.org/packages/source/c/click-threading/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	4a6a345a3cc236fdd2b670588cc4b8a0
URL:		https://pypi.org/project/click-threading/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multithreaded Click apps made easy.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
