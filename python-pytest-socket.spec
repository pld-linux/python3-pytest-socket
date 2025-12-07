#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-pytest-socket.spec)

Summary:	Pytest Plugin to disable socket calls during tests
Summary(pl.UTF-8):	Wtyczka pytesta blokująca odwołania do gniazd w trakcie testów
Name:		python-pytest-socket
# keep 0.3.3 here for python2 support
Version:	0.3.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-socket/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-socket/pytest-socket-%{version}.tar.gz
# Source0-md5:	5d3a96b1aff2d7a744ae2f002391d14c
URL:		https://pypi.org/project/pytest-socket/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin to use with Pytest to disable or restrict socket calls during
tests to ensure network calls are prevented.

%description -l pl.UTF-8
Wtyczka dla pytesta blokująca lub ograniczająca odwołania do gniazd
podczas testów, aby zapobiec odwołaniom do sieci.

%package -n python3-pytest-socket
Summary:	Pytest Plugin to disable socket calls during tests
Summary(pl.UTF-8):	Wtyczka pytesta blokująca odwołania do gniazd w trakcie testów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-socket
A plugin to use with Pytest to disable or restrict socket calls during
tests to ensure network calls are prevented.

%description -n python3-pytest-socket -l pl.UTF-8
Wtyczka dla pytesta blokująca lub ograniczająca odwołania do gniazd
podczas testów, aby zapobiec odwołaniom do sieci.

%prep
%setup -q -n pytest-socket-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/pytest_socket.py[co]
%{py_sitescriptdir}/pytest_socket-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-socket
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_socket.py
%{py3_sitescriptdir}/__pycache__/pytest_socket.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_socket-%{version}-py*.egg-info
%endif
