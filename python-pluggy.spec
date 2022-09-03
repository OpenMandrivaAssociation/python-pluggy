%global pypi_name pluggy

%bcond_with python2

Name:		python-%{pypi_name}
Version:	1.0.0
Release:	2
Summary:	A minimalist production ready plugin system

Group:		Development/Python
License:	BSD
URL:		https://github.com/pytest-dev/pluggy
Source0:	https://files.pythonhosted.org/packages/a1/16/db2d7de3474b6e37cbb9c008965ee63835bba517e22cdb8c35b5116b5ce1/pluggy-1.0.0.tar.gz

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
