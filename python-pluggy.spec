%global pypi_name pluggy

%bcond_without python2

Name:		python-%{pypi_name}
Version:	0.13.1
Release:	3
Summary:	A minimalist production ready plugin system

Group:		Development/Python
License:	BSD
URL:		https://github.com/pytest-dev/pluggy
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:	python-setuptools
BuildRequires:  python-setuptools_scm

%description
Pluggy is the core framework used by the pytest, tox, and devpi projects.

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:	A minimalist production ready plugin system
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:  python2-setuptools_scm

%description -n python2-%{pypi_name}
Pluggy is the core framework used by the pytest, tox, and devpi projects.
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -S git

# Tag version to fix setuptools_scm
git tag -f %{version}

%build
%if %{with python2}
%py2_build
%endif

%py3_build

%install
%if %{with python2}
%py2_install
%endif

%py3_install

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}*/

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}*/
%endif
