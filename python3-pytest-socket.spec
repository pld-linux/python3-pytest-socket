#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pytest Plugin to disable socket calls during tests
Summary(pl.UTF-8):	Wtyczka pytesta blokująca odwołania do gniazd w trakcie testów
Name:		python3-pytest-socket
Version:	0.7.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-socket/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-socket/pytest_socket-%{version}.tar.gz
# Source0-md5:	a0d2be06ec38c479a0731b79512ad61d
URL:		https://pypi.org/project/pytest-socket/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with pytest}
BuildRequires:	python3-pytest >= 6.2.5
BuildRequires:	python3-pytest-httpbin >= 2.0.0
BuildRequires:	python3-pytest-randomly >= 3.15.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin to use with Pytest to disable or restrict socket calls during
tests to ensure network calls are prevented.

%description -l pl.UTF-8
Wtyczka dla pytesta blokująca lub ograniczająca odwołania do gniazd
podczas testów, aby zapobiec odwołaniom do sieci.

%prep
%setup -q -n pytest_socket-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_httpbin.plugin,pytest_socket \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pytest_socket.py
%{py3_sitescriptdir}/__pycache__/pytest_socket.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_socket-%{version}.dist-info
