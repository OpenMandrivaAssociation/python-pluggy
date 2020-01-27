%global tarName pluggy

Name:           python-%{tarName}
Version:	0.13.1
Release:	2
Summary:         A minimalist production ready plugin system

Group:          Development/Python
License:        BSD
URL:            https://github.com/pytest-dev/pluggy
Source0:	https://files.pythonhosted.org/packages/f8/04/7a8542bed4b16a65c2714bf76cf5a0b026157da7f75e87cc88774aa10b14/pluggy-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  git-core
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

git config --global user.email "rpm@openmandriva.org"
git config --global user.name "mock build"

git init
git add .
git commit -am 'init'

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
