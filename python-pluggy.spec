%global pypi_name pluggy

Name:		python-%{pypi_name}
Version:	1.6.0
Release:	1
Summary:	A minimalist production ready plugin system

Group:		Development/Python
License:	BSD
URL:		https://github.com/pytest-dev/pluggy
Source0:	https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	git-core
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python

%description
Pluggy is the core framework used by the pytest, tox, and devpi projects.

%prep
%autosetup -n %{pypi_name}-%{version} -S git

# Tag version to fix setuptools_scm
git tag -f %{version}

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}*/
