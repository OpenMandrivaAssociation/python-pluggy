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
BuildRequires:	git-core
BuildRequires:	python
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python

%description
Pluggy is the core framework used by the pytest, tox, and devpi projects.

%prep
%autosetup -n %{pypi_name}-%{version} -S git

# Tag version to fix setuptools_scm
git tag -a -m %{version} -f %{version}

%build
# For some reason, if we use py_build here, we get mismatching
# version numbers -- so use build instead
python -m build -nx -w -o ../RPMBUILD_wheels

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{pypi_name}*/
