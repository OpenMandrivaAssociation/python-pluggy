%global tarName pluggy

Name:           python-%{tarName}
Version:        0.9.0
Release:        1
Summary:         A minimalist production ready plugin system

Group:          Development/Python
License:        BSD
URL:            https://github.com/pytest-dev/pluggy
Source0:        https://github.com/untitaker/python-atomicwrites/archive/%{tarName}-%{version}.tar.gz
# Note: The above URL gets incomplete sources, get the sources from PyPi
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python-setuptools
BuildRequires:  python-setuptools_scm
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:  python2-setuptools_scm

%description
Pluggy is the core framework used by the pytest, tox, and devpi projects.

%package -n python2-%{tarName}

Summary:         A minimalist production ready plugin system
%description -n python2-%{tarName}
Pluggy is the core framework used by the pytest, tox, and devpi projects.

%prep
%setup -qn %{tarName}-%{version}

cp -a . %py2dir
%build
python setup.py build

pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%{buildroot}

pushd %py2dir
python2 setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/*/*
%doc README.rst LICENSE

%files -n python2-%{tarName}
%{py2_puresitedir}/*/*
%doc README.rst LICENSE